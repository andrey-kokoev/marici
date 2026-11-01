"""Fresh native carrier check plus exact geometry and continuation diagnostics."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/su32-native-join-binding-v1'
OUT.mkdir(parents=True, exist_ok=True)
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def node(script):
    run = subprocess.run(['node', 'research/strominger/checkers/' + script], cwd=ROOT,
                         capture_output=True, text=True, timeout=120)
    (OUT / (script + '.log')).write_text(run.stdout + run.stderr, encoding='utf-8')
    assert run.returncode == 0, (run.stdout + run.stderr)[-6000:]
node('build_su32_native_join_geometry.mjs')
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
roots = {'strominger': BASE / 'agda', 'nima': ROOT / 'research/nima/agda', 'cubical': LIB, 'primitive': PRIM}
def inventory():
    return {label + '/' + p.relative_to(folder).as_posix(): sha(p)
            for label, folder in roots.items()
            for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib')
            for p in folder.rglob(pattern)}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical', '--guardedness', '--no-import-sorts',
          '-i', str(BASE / 'agda'), '-i', str(ROOT / 'research/nima/agda'), '-i', str(LIB)]
command = common + ['--ignore-interfaces', str(BASE / 'agda/Su32CoherentReferenceCarrier.agda')]
run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=200)
log = run.stdout + run.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert run.returncode == 0 and 'Unsolved' not in log, log[-6000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line for line in warnings), warnings
controls = []
for name in ('Su32JoinInconsistentConsumer', 'Su32JoinWrongFacePort'):
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(BASE / ('agda/negative/' + name + '.agda'))]
    neg = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=120)
    diagnostic = neg.stdout + neg.stderr
    (OUT / (name + '.log')).write_text(diagnostic, encoding='utf-8')
    assert neg.returncode != 0 and any(t in diagnostic for t in ('UnequalTerms', 'UnequalTypes')), diagnostic[-6000:]
    controls.append({'module': name, 'exit': neg.returncode, 'diagnostic': diagnostic})
node('check_su32_continuation_carriers.mjs')
receipts = {}
for name in ('geometry.json', 'carrier-audit.json'):
    p = OUT / name
    result = json.loads(p.read_text(encoding='utf-8'))
    assert result['passed'] and all(sha(ROOT / k) == h for k, h in result['sourceHashes'].items())
    receipts[name] = sha(p)
assert inventory() == before, 'Sources changed during fresh verification'
lock = {'scope': 'Conservative complete include-root inventory, not an exact import graph',
        'roots': {k: str(v) for k, v in roots.items()}, 'sources': before,
        'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
        'agda_executable_sha256': sha(Path(EXE)), 'implicit_libraries_disabled': True}
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
result = {'passed': True, 'fresh_agda_exit': run.returncode, 'command': command,
          'negative_controls': controls, 'dependency_warnings': warnings,
          'dependency_manifest_sha256': sha(manifest), 'checker_sha256': sha(Path(__file__)), 'receipts': receipts,
          'nativeCoherentRecordCarrierDerived': True, 'geometricFaceCertificateChecked': True,
          'nativeSignalExecuted': False, 'nativeSu32FillerSelected': False,
          'conclusion': 'Raw native Pi does not enforce common-preparation compatibility on its whole carrier. Native shared-reader joins enforce the two-record consumer overlap and full preparation agreement while retaining actual operand derivations. The finite source geometry is checked; native wire execution and filler selection remain unbound.'}
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ('passed', 'fresh_agda_exit', 'nativeCoherentRecordCarrierDerived', 'geometricFaceCertificateChecked', 'nativeSignalExecuted', 'nativeSu32FillerSelected', 'conclusion')}))
