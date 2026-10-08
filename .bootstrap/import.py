"""One-use, hash-guarded import to the authorized feature branch only."""
from pathlib import Path, PurePosixPath
import base64
import hashlib
import json
import lzma
import os
import subprocess
import tempfile

REPOSITORY = 'GoGoKo699/Quantum-Group-Memory-Laws'
BRANCH = 'initialize/qg-memory-laws'
BASE = 'd037861f4846c6168068c83aa58112e1f044e43a'
PACK_SHA = '3e059ac3f47e1725205980615a1887de77e44d24d7f1d2ba7dca445cd7c05d21'
FINAL_TREE = '1658d22e61541518da4073fe24207fcb4e0aaf33'

def git(*args, **kwargs):
    return subprocess.check_output(['git', *args], **kwargs).decode().strip()

if os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
    raise RuntimeError('Unexpected repository')
if os.environ.get('GITHUB_REF') != 'refs/heads/' + BRANCH:
    raise RuntimeError('Import is restricted to the authorized feature branch')
if git('rev-parse', 'HEAD^') != BASE:
    raise RuntimeError('The bootstrap must be directly based on the verified initial revision')
root = Path.cwd()
if git('status', '--porcelain'):
    raise RuntimeError('Unexpected checkout changes')
packed = base64.b64decode(''.join((root / '.bootstrap' / f'chunk{i:02}.txt').read_text() for i in range(8)), validate=True)
if hashlib.sha256(packed).hexdigest() != PACK_SHA:
    raise RuntimeError('Import payload hash mismatch')
files = json.loads(lzma.decompress(packed))
if not isinstance(files, dict) or len(files) != 105:
    raise RuntimeError('Unexpected payload membership')
for name, text in files.items():
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or path.parts[0] in ('.git', '.bootstrap'):
        raise RuntimeError('Unsafe payload path')
    if str(path) != name or not isinstance(text, str):
        raise RuntimeError('Noncanonical payload path or nontext file')
    if name.startswith('.github/') and name != '.github/workflows/verify.yml':
        raise RuntimeError('Unapproved workflow path')
    target = root / name
    for part in [target, *target.parents]:
        if part == root.parent:
            break
        if part.is_symlink():
            raise RuntimeError('Symlink in payload destination')
    if name in ('LICENSE', '.github/workflows/verify.yml'):
        if target.read_bytes() != text.encode('utf-8'):
            raise RuntimeError('Protected initial license or preinstalled workflow differs')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
# Independently build a temporary index containing precisely the reviewed 105 files.
with tempfile.TemporaryDirectory() as temp:
    env = dict(os.environ, GIT_INDEX_FILE=str(Path(temp) / 'index'))
    git('read-tree', '--empty', env=env)
    for name in sorted(files):
        sha = git('hash-object', '-w', '--stdin', input=(root / name).read_bytes())
        git('update-index', '--add', '--cacheinfo', f'100644,{sha},{name}', env=env)
    tree = git('write-tree', env=env)
    if tree != FINAL_TREE:
        raise RuntimeError(f'Reviewed source-tree mismatch: {tree}')
# The token never adds or changes a workflow: verify.yml was preinstalled unchanged.
subprocess.run(['git', 'add', '--', *sorted(name for name in files if not name.startswith('.github/'))], check=True)
changed = git('diff', '--cached', '--name-only').splitlines()
if any(name.startswith(('.github/', '.bootstrap/')) for name in changed):
    raise RuntimeError('Bootstrap must not mutate its own workflow or payload')
if set(changed) - set(files):
    raise RuntimeError('Unapproved staged path')
subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
subprocess.run(['git', 'commit', '-m', 'Import frozen quantum-group memory research and workspace entry points'], check=True)
subprocess.run(['git', 'push', 'origin', f'HEAD:refs/heads/{BRANCH}'], check=True)
print(json.dumps({'repository': REPOSITORY, 'branch': BRANCH, 'source_tree': tree,
                  'files': len(files), 'payload_sha256': PACK_SHA,
                  'import_commit': git('rev-parse', 'HEAD')}, indent=2))
