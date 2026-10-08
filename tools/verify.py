#!/usr/bin/env python3
"""Preserve imported evidence; run unchanged science with explicit report comparison.

Reports go to build/ or outside the source tree. This program never updates a
canonical report or scientific assertion. Numerical output comparison is distinct
from the scientific assertions inside the original checkers.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'archive/research-handoff-2026-10-08'
SUITES = (
    ('finite_memory', 'prior/prior/prior/prior/check_memory.py', 'prior/prior/prior/prior/report.json', 4),
    ('edge_asymptotics', 'prior/prior/prior/check_asymptotics.py', 'prior/prior/prior/report.json', 5),
    ('bulk', 'prior/prior/check_bulk.py', 'prior/prior/report.json', 6),
    ('plateau_review', 'prior/check_review.py', 'prior/review_report.json', 5),
    ('local_realization', 'check_final.py', 'report.json', 4),
)
# New infrastructure comparison, never used to modify a scientific assertion.
REPORT_ATOL = 2e-12
REPORT_RTOL = 2e-10
IGNORED = {'.git', '.venv', '__pycache__', 'build'}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_path(root: Path, name: str) -> Path:
    part = PurePosixPath(name)
    if not name or part.is_absolute() or '..' in part.parts or '\\' in name:
        raise ValueError(f'Unsafe relative path: {name!r}')
    path = root.joinpath(*part.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes root: {name!r}')
    return path

def source_files(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if any(p in IGNORED for p in rel.parts) or path.suffix == '.pyc':
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink not allowed in source: {rel}')
        if path.is_file():
            result[rel.as_posix()] = sha(path.read_bytes())
    return result

def verify_provenance(root: Path = ROOT) -> dict:
    info = json.loads((root/'provenance/IMPORT.json').read_text())
    assert info['repository'] == 'GoGoKo699/Quantum-Group-Memory-Laws'
    archive = safe_path(root, info['archive_root'])
    actual = {p.relative_to(archive).as_posix() for p in archive.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts}
    assert actual == set(info['archive_members']), 'Archive membership changed'
    for name, record in info['archive_members'].items():
        data = safe_path(archive, name).read_bytes()
        assert len(data) == record['bytes'] and sha(data) == record['sha256'], name
    manifests = sorted(archive.rglob('MANIFEST.json'))
    nested_entries = 0
    for manifest in manifests:
        for name, record in json.loads(manifest.read_text()).items():
            data = safe_path(manifest.parent, name).read_bytes()
            assert len(data) == record['bytes'] and sha(data) == record['sha256'], str(manifest)+':'+name
            nested_entries += 1
    assert sha((root/'LICENSE').read_bytes()) == info['owner_license_sha256']
    assert sha((root/'provenance/initial-README.md').read_bytes()) == info['initial_readme_sha256']
    for name, record in json.loads((root/'provenance/ACTIVE_EDITS.json').read_text()).items():
        text = safe_path(root, record['source']).read_text()
        for before, after in record['replacements']:
            text = text.replace(before, after)
        assert safe_path(root, name).read_text() == text, 'Undeclared active edit: '+name
    return {'archive_members': len(actual), 'nested_manifests': len(manifests),
            'nested_manifest_entries': nested_entries, 'license_unchanged': True,
            'active_derivations_verified': 3}

def verify_docs(root: Path = ROOT) -> dict:
    docs = json.loads((root/'provenance/DOCUMENTS.json').read_text())
    actual = {n:h for n,h in source_files(root).items()
              if (n.endswith('.md') or n=='llms.txt') and not n.startswith(ARCHIVE+'/')}
    assert docs == actual, 'Documentation integrity differs; review then refresh DOCUMENTS.json only'
    links = 0
    for name in actual:
        if name == 'provenance/initial-README.md':
            continue
        path = root/name
        text = path.read_text()
        # Archived mathematical delimiters are preserved; active ones use GitHub syntax.
        if name.startswith('research/') or name == 'README.md':
            assert '\\[' not in text and '\\]' not in text and '\\(' not in text and '\\)' not in text, name
            assert text.count('$$') % 2 == 0, 'Unbalanced display math: '+name
        stripped = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)', stripped):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            dest = (path.parent/unquote(parsed.path)).resolve()
            assert dest.is_relative_to(root.resolve()), 'Link escapes repository: '+target
            assert dest.exists(), name+' -> '+target
            links += 1
    return {'documents': len(actual), 'local_document_links': links}

def compare_reports(expected, actual, location='$') -> list[dict]:
    """Record every numeric difference; reject schema, discrete or large changes."""
    changes = []
    if isinstance(expected, dict):
        assert isinstance(actual, dict) and expected.keys() == actual.keys(), location
        for k in expected:
            changes.extend(compare_reports(expected[k], actual[k], location+'.'+k))
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(expected) == len(actual), location
        for j,(e,a) in enumerate(zip(expected,actual)):
            changes.extend(compare_reports(e,a,f'{location}[{j}]'))
    elif isinstance(expected, bool) or expected is None or isinstance(expected, str):
        assert type(expected) is type(actual) and expected == actual, location
    elif isinstance(expected, int):
        assert type(actual) is int and expected == actual, location
    elif isinstance(expected, float):
        assert type(actual) in (float,int) and math.isfinite(expected) and math.isfinite(actual), location
        error = abs(actual-expected)
        assert error <= REPORT_ATOL + REPORT_RTOL*abs(expected), f'{location}: {expected} != {actual}'
        if expected != actual:
            changes.append({'path':location,'reference':expected,'actual':actual,'absolute_difference':error})
    else:
        raise TypeError(location+': unsupported report type')
    return changes

def revision() -> str | None:
    p = subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True)
    return p.stdout.strip() if p.returncode == 0 else None

def output_location(value: Path) -> Path:
    target = value.resolve()
    if target.is_relative_to(ROOT.resolve()) and not target.is_relative_to((ROOT/'build').resolve()):
        raise ValueError('Output within this repository must be under build/')
    return target

def run(output: Path, infrastructure_only: bool = False) -> dict:
    output = output_location(output)
    output.mkdir(parents=True,exist_ok=True)
    before = source_files(ROOT)
    receipt = {'scope':'Reproducibility and source integrity; not independent proof review.',
               'commit':revision(),'github_sha':os.environ.get('GITHUB_SHA'),
               'event':os.environ.get('GITHUB_EVENT_NAME'),'run_id':os.environ.get('GITHUB_RUN_ID'),
               'python':sys.version,'platform':platform.platform(),
               'source_sha256':before,'report_atol':REPORT_ATOL,'report_rtol':REPORT_RTOL,
               'provenance':verify_provenance(),'documentation':verify_docs(),'suites':[]}
    if not infrastructure_only:
        import numpy, scipy
        receipt['numpy'] = numpy.__version__;receipt['scipy'] = scipy.__version__
        env = {**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1',
               'MKL_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
        for name, script, reference, groups in SUITES:
            actual = output/(name+'.json')
            if actual.exists():actual.unlink()
            cmd = [sys.executable,str(ROOT/ARCHIVE/script),'--output',str(actual)]
            with (output/(name+'.log')).open('w') as log:
                p = subprocess.run(cmd,cwd=ROOT/ARCHIVE,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=1200)
            assert p.returncode == 0, f'{name} failed; see {name}.log'
            ref_bytes = (ROOT/ARCHIVE/reference).read_bytes(); out_bytes = actual.read_bytes()
            ref = json.loads(ref_bytes);got = json.loads(out_bytes)
            assert got['groups_passed'] == groups, name
            changes = compare_reports(ref,got)
            receipt['suites'].append({'name':name,'script':script,'reference':reference,'groups':groups,
               'byte_identical':ref_bytes==out_bytes,'reference_sha256':sha(ref_bytes),'output_sha256':sha(out_bytes),
               'numeric_changes':changes,'max_absolute_difference':max((v['absolute_difference'] for v in changes),default=0)})
            print(f'{name}: {groups} groups; identical={ref_bytes==out_bytes}; changed numeric fields={len(changes)}',flush=True)
    assert source_files(ROOT) == before, 'Source changed during verification'
    verify_provenance()
    receipt['groups_passed'] = sum(s['groups'] for s in receipt['suites'])
    receipt['source_unchanged'] = True
    (output/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'groups_passed':receipt['groups_passed'],'source_files':len(before),
                      'archive_members':receipt['provenance']['archive_members'],'source_unchanged':True}))
    return receipt

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=ROOT/'build/verification')
    ap.add_argument('--infrastructure-only',action='store_true')
    args = ap.parse_args()
    run(args.output,args.infrastructure_only)
