"""Fresh native closure check, using the repository's Python Agda-checker entrypoint pattern."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/native-shared-reader-join-v1'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir(), 'Agda and cubical-0.9 are required'
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
roots = {'strominger': BASE / 'agda', 'nima': ROOT / 'research/nima/agda', 'cubical': LIB, 'primitive': PRIM}
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():
    return {label + '/' + p.relative_to(folder).as_posix(): sha(p)
            for label, folder in roots.items()
            for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib')
            for p in folder.rglob(pattern)}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical', '--guardedness', '--no-import-sorts',
          '-i', str(BASE / 'agda'), '-i', str(ROOT / 'research/nima/agda'), '-i', str(LIB)]
command = common + ['--ignore-interfaces', str(BASE / 'agda/NativeSharedReaderJoin.agda')]
start = time.monotonic()
run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=200)
log = run.stdout + run.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert run.returncode == 0 and 'Unsolved' not in log, log[-7000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line for line in warnings), warnings
controls = []
for name in ('SharedJoinBadAgreement', 'SharedJoinMissingOperand', 'SharedJoinWrongReference'):
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(BASE / ('agda/negative/' + name + '.agda'))]
    neg = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120)
    diagnostic = neg.stdout + neg.stderr
    (OUT / (name + '.log')).write_text(diagnostic, encoding='utf-8')
    assert neg.returncode != 0 and any(t in diagnostic for t in ('UnequalTerms', 'UnequalTypes')), diagnostic[-6000:]
    controls.append({'module': name, 'exit': neg.returncode, 'diagnostic': diagnostic})
finite = subprocess.run(['node', 'research/strominger/checkers/check_su32_join_type_boundary.mjs'],
                        cwd=ROOT, capture_output=True, text=True, timeout=120)
(OUT / 'finite-source.log').write_text(finite.stdout + finite.stderr, encoding='utf-8')
assert finite.returncode == 0, (finite.stdout + finite.stderr)[-6000:]
finite_path = BASE / 'results/su32-join-type-boundary-v1/verification.json'
finite_result = json.loads(finite_path.read_text(encoding='utf-8'))
assert finite_result['passed']
assert all(sha(ROOT / p) == h for p, h in finite_result['sourceHashes'].items())
assert inventory() == before, 'Source inputs changed during fresh closure verification'
lock = {'scope': 'Conservative complete include-root source inventory, not an exact import graph',
        'roots': {k: str(v) for k, v in roots.items()}, 'sources': before,
        'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
        'agda_executable': EXE, 'agda_executable_sha256': sha(Path(EXE)), 'implicit_libraries_disabled': True}
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
result = {'passed': True, 'fresh_agda_exit': run.returncode, 'command': command,
          'elapsed_seconds': round(time.monotonic() - start, 3), 'negative_controls': controls,
          'dependency_warnings': warnings, 'dependency_manifest': manifest.relative_to(ROOT).as_posix(),
          'dependency_manifest_sha256': sha(manifest), 'checker_sha256': sha(Path(__file__)),
          'native_join_derived': True, 'su32_geometric_native_binding': False,
          'finite_source_checks': {'receipt': finite_path.relative_to(ROOT).as_posix(), 'sha256': sha(finite_path), 'counts': finite_result['counts']},
          'native_enriched_exchange_derived': True,
          'conclusion': 'Existing native reflexivity, Pi and E rules derive a retained shared-reader join from both actual operand derivations and shared-reader agreement. No operand equivalence is assumed. The enriched joins admit a derived exchange.',
          'formal_results': ['Whole-carrier shared-reader agreement', 'Exact recovery of both Resolve histories through native premise ports',
                             'Native closure of the join and its enriched exchange', 'Only four tagged input records admitted in the prepared instance',
                             'Unused fourth record retained in full preparation', 'Left projection provably noninjective in the Boolean instance'],
          'limits': ['The shared reader and its selected-value path remain explicit interface data.',
                     'Generic input loops are retained, not assumed contractible or proof irrelevant.',
                     'The prepared record-interface instance is not yet a Su-32 occurrence/port binding or a physical interaction law.',
                     'No raw path equality or period-return relation is derived.']}
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ('passed', 'fresh_agda_exit', 'native_join_derived', 'su32_geometric_native_binding', 'conclusion')}))
