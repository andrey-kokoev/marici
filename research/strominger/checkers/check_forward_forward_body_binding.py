"""Fresh closure of the actual forward/forward Body diagram and higher admission."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/forward-forward-body-binding'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
roots = {**{'repo-' + owner: ROOT / ('research/' + owner + '/agda')
            for owner in ('strominger', 'nima', 'voevodsky', 'grothendieck')},
         'cubical': LIB, 'agda-primitive': PRIM}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def inventory():
    return {label + '/' + p.relative_to(folder).as_posix(): sha(p)
            for label, folder in roots.items()
            for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib')
            for p in folder.rglob(pattern)}

contract_path = BASE / 'contracts/forward-forward-body-binding.v1.json'
contract = json.loads(contract_path.read_text(encoding='utf-8'))
assert all(v is False for v in contract['scope_guards'].values())
module = BASE / 'agda/ForwardForwardBodyBinding.agda'
higher = BASE / 'agda/ForwardForwardHigherAdmission.agda'
negatives = [BASE / ('agda/negative/' + name + '.agda') for name in
             ('ForwardBodyBadJudgmentalReset', 'ForwardBodyBadUnmovedEdge', 'ForwardBodyBadBareAdmission')]
sources = [module, higher, contract_path, Path(__file__).resolve(), *negatives,
           *[ROOT / p for p in contract['predecessors']]]
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical',
          '--guardedness', '--no-import-sorts']
for label, folder in roots.items():
    if label != 'agda-primitive':
        common += ['-i', str(folder)]
command = common + ['--ignore-interfaces', str(higher)]
start = time.monotonic()
positive = subprocess.run(command, capture_output=True, text=True, timeout=600)
log = positive.stdout + positive.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert positive.returncode == 0 and not any(s in log for s in ('Unsolved', 'error:')), log[-7000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
assert all(w.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in w
           for w in warnings), warnings
controls = []
for p in negatives:
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(p)]
    run = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    diagnostic = run.stdout + run.stderr
    (OUT / (p.stem + '.log')).write_text(diagnostic, encoding='utf-8')
    assert run.returncode != 0 and 'UnequalTerms' in diagnostic, diagnostic[-5000:]
    controls.append({'module': p.stem, 'exit': run.returncode, 'command': cmd,
                     'diagnostic': diagnostic.strip()})
assert inventory() == before, 'Declared source inventory changed during verification'
assert all(sha(ROOT / p) == h for p, h in hashes.items())
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps({'scope': 'Conservative complete include-root and primitive inventory, not exact imports',
    'implicit_libraries_disabled': True, 'roots': {k: str(v) for k, v in roots.items()},
    'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
    'agda_executable_sha256': sha(Path(EXE)), 'sources': before}, indent=2) + '\n', encoding='utf-8')
report = {'status': 'pass', 'fresh_agda_exit': positive.returncode, 'command': command,
          'elapsed_seconds': round(time.monotonic() - start, 3), 'source_hashes': hashes,
          'dependency_manifest': manifest.relative_to(ROOT).as_posix(),
          'dependency_manifest_sha256': sha(manifest), 'locked_source_files': len(before),
          'dependency_warnings': warnings, 'repository_source_warnings': [],
          'negative_controls': controls, 'formal_results': contract['formal_results'],
          'input_contract': contract['inputs'], 'scope_guards': contract['scope_guards'],
          'verification_boundary': 'Arbitrary initial proof at A, named AB/BC two-exchange diagram; generic row helper is checked, but no global Body action or triple overlap is inferred.'}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before)}))
