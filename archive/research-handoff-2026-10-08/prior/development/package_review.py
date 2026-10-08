from pathlib import Path
import hashlib, json, zipfile, re, sys, platform
import numpy, scipy
root=Path(__file__).resolve().parents[1]
source=Path('/mnt/data/qg_memory_bulk_2026-10-08.zip')
sha=lambda b:hashlib.sha256(b).hexdigest()
rows=[]
with zipfile.ZipFile(source) as z:
    assert z.testzip() is None
    names=[i.filename for i in z.infolist() if not i.is_dir()]
    assert len(names)==len(set(names))
    for n in names:
        assert not Path(n).is_absolute() and '..' not in Path(n).parts
        incoming=z.read(n); actual=(root/'prior'/n).read_bytes()
        assert incoming==actual, n
        rows.append({'path':n,'bytes':len(actual),'sha256':sha(actual)})
manifest_results=[]
for p in sorted((root/'prior').rglob('MANIFEST.json')):
    spec=json.loads(p.read_text())
    for n,item in spec.items():
        data=(p.parent/n).read_bytes()
        assert len(data)==item['bytes'] and sha(data)==item['sha256'], (str(p),n)
    manifest_results.append({'path':str(p.relative_to(root)),'members_verified':len(spec)})
assert (root/'prior/FOLLOWUP.md').read_bytes()==Path('/mnt/data/qg_memory_bulk_2026-10-08/FOLLOWUP.md').read_bytes()
new_a=(root/'review_report.json').read_bytes()
new_b=(root/'review_report_repeat.json').read_bytes()
old_a=(root/'prior_bulk_rerun.json').read_bytes()
old_b=(root/'prior/report.json').read_bytes()
assert new_a==new_b and old_a==old_b
assert json.loads(new_a)['groups_passed']==5 and json.loads(old_a)['groups_passed']==6
verification={
 'scope':'Internal contribution review; finite checks are not independent proof review or priority clearance.',
 'input_zip':{'path':str(source),'sha256':sha(source.read_bytes()),'members':len(names)},
 'original_members_unchanged':rows,
 'nested_manifests_verified':manifest_results,
 'standalone_note_matches_archived_note':True,
 'new_groups_passed_each_run':5,'new_runs':2,
 'new_report_sha256':sha(new_a),'new_reports_byte_identical':new_a==new_b,
 'immediate_bulk_suite_groups_passed':6,
 'immediate_bulk_report_byte_identical':old_a==old_b,
 'immediate_bulk_report_sha256':sha(old_a),
 'older_five_and_four_group_suites_rerun_in_full':False,
 'largest_full_spin_hilbert_space':256,
 'small_Hamiltonian_cases_are_diagnostics_not_thermodynamic_simulations':True,
 'Haar_moments_tested_by_exact_finite_designs_not_Monte_Carlo':True,
 'prior_physical_code_or_tolerances_modified':False,
 'initial_failure':'New driver called legacy fast recurrence at q=1, outside q>1 domain. Driver now uses exact 1/L at q=1; assertions and tolerance unchanged. Initial script and log retained.',
 'packaging_note':'A metadata self-link was checked before writing its file. Assembly order corrected; no scientific change.',
 'environment':{'python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__}
}
(root/'VERIFICATION.json').write_text(json.dumps(verification,indent=2,sort_keys=True)+'\n')
links=[]
for p in [root/'README.md',root/'THEOREM.md',root/'REVIEW.md',root/'PLATEAU_DICTIONARY.md']:
    for target in re.findall(r'\]\(([^)\s]+)\)',p.read_text()):
        if '://' in target or target.startswith('#'):continue
        q=p.parent/target.split('#')[0]
        assert q.exists(),(p.name,target)
        links.append({'source':p.name,'target':target})
verification['local_current_document_links']=links
(root/'VERIFICATION.json').write_text(json.dumps(verification,indent=2,sort_keys=True)+'\n')
paths=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p!=root/'MANIFEST.json']
m={str(p.relative_to(root)):{'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in paths}
(root/'MANIFEST.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
output=Path('/mnt/data/qg_memory_contribution_review.zip')
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
    for p in paths+[root/'MANIFEST.json']:z.write(p,str(p.relative_to(root)))
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    for n,item in m.items():
        data=z.read(n);assert len(data)==item['bytes'] and sha(data)==item['sha256']
print(json.dumps({'preserved_members':len(names),'nested_manifests':manifest_results,'new_reports_identical':new_a==new_b,'bulk_report_identical':old_a==old_b,'current_document_links':len(links),'package_members':len(m)+1,'output':str(output),'bytes':output.stat().st_size,'sha256':sha(output.read_bytes())},indent=2))
