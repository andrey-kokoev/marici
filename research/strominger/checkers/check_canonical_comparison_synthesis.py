"""Fresh constructive comparison compiler closure and bounded regressions."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/canonical-comparison-synthesis'
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

contract_path = BASE / 'contracts/canonical-comparison-synthesis.v1.json'
contract = json.loads(contract_path.read_text(encoding='utf-8'))
assert all(v is False for v in contract['scope_guards'].values())
module = BASE / 'agda/CanonicalComparisonSynthesis.agda'
regression = BASE / 'agda/CanonicalComparisonSynthesisRegression.agda'
negatives = [BASE / ('agda/negative/' + name + '.agda') for name in
             ('SynthesisBadSamePoint', 'SynthesisBadSeedReset', 'SynthesisBadPreparedInput')]
sources = [module, regression, contract_path, Path(__file__).resolve(), *negatives,
           *[ROOT / p for p in contract['predecessors']]]
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical',
          '--guardedness', '--no-import-sorts']
for label, folder in roots.items():
    if label != 'agda-primitive':
        common += ['-i', str(folder)]
command = common + ['--ignore-interfaces', str(regression)]
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

# Independently calculate the finite normal-form shadow from the original
# typed incidence, not from the new compiler's decision table.
text = (BASE / 'agda/NativeExtensionFamilyAudit.agda').read_text(encoding='utf-8')
edges = re.findall(r'^  (\w+) : Edge (\w+) (\w+)$', text, re.M)
assert {e for e, _, _ in edges} == {'AB', 'BC', 'CA', 'BA', 'AD', 'DB'}
images = {'whole': set('ABCD'), **{v: {t for _, s, t in edges if s == v} for v in 'ABCD'}}
sigma = dict(zip('ABCD', 'BADC'))
rows = []
for mode in ('stay', 'exchange'):
    act = (lambda v: v) if mode == 'stay' else sigma.__getitem__
    for s, left in images.items():
        for t, right in images.items():
            mismatch = next((v for v in 'ABCD' if (v in left) != (act(v) in right)), None)
            accepted = mismatch is None
            expected = s == t if mode == 'stay' else (s == t == 'whole' or (s != 'whole' and t == sigma[s]))
            assert accepted == expected
            rows.append({'mode': mode, 'left_shape': s, 'right_shape': t,
                         'accepted': accepted, 'first_separating_vertex': mismatch})
assert len(rows) == 50 and sum(r['accepted'] for r in rows) == 10
assert sum(r['accepted'] for r in rows if r['mode'] == 'exchange') == 5
assert next(r for r in rows if (r['mode'], r['left_shape'], r['right_shape']) == ('stay', 'whole', 'C'))['first_separating_vertex'] == 'B'
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
          'normal_form_regressions': rows, 'scope_guards': contract['scope_guards'],
          'verification_boundary': 'The formal total procedure covers arbitrary Fragment syntax; the 50-case shadow is a regression, not a bound on syntax or proof histories.'}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before),
                  'normal_form_cases': len(rows), 'accepted_cases': 10}))
