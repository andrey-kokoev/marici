"""Fresh classification of the corrected native current-value carrier."""
from pathlib import Path
import hashlib
import itertools
import json
import shutil
import subprocess
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/su32-record-reader-classification-v1'
OUT.mkdir(parents=True, exist_ok=True)
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
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
command = common + ['--ignore-interfaces', str(BASE / 'agda/Su32RecordReaderClassification.agda')]
run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=200)
log = run.stdout + run.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert run.returncode == 0 and 'Unsolved' not in log, log[-6000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line for line in warnings), warnings
negative = common + ['-i', str(BASE / 'agda/negative'), str(BASE / 'agda/negative/Su32PortEqualityIsNotValueEquality.agda')]
neg = subprocess.run(negative, cwd=ROOT, capture_output=True, text=True, timeout=120)
diag = neg.stdout + neg.stderr
(OUT / 'negative.log').write_text(diag, encoding='utf-8')
assert neg.returncode != 0 and any(t in diag for t in ('UnequalTerms', 'UnequalTypes')), diag[-6000:]
# Refresh source geometry/domain checks, including their own native tests.
prior = subprocess.run(['python', 'research/strominger/checkers/check_su32_coherent_reference_carrier.py'],
                       cwd=ROOT, capture_output=True, text=True, timeout=210)
(OUT / 'prerequisite.log').write_text(prior.stdout + prior.stderr, encoding='utf-8')
assert prior.returncode == 0, (prior.stdout + prior.stderr)[-6000:]
# A finite countercontrol, not an exhaustive enumeration of all 16! maps:
# two pointed port-preserving permutations, only one record-preserving.
values = list(itertools.product((0, 1), repeat=4))
identity = list(range(16))
swap = identity.copy()
swap[1], swap[2] = swap[2], swap[1]
for p in (identity, swap):
    assert sorted(p) == identity and p[0] == 0
    assert all(p[p[i]] == i for i in identity)
assert all(values[identity[i]] == values[i] for i in identity)
assert any(values[swap[i]] != values[i] for i in identity)
assert inventory() == before, 'Source drift during fresh verification'
lock = {'scope': 'Conservative complete include-root inventory, not an exact import graph',
        'roots': {k: str(v) for k, v in roots.items()}, 'sources': before,
        'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
        'agda_executable_sha256': sha(Path(EXE)), 'implicit_libraries_disabled': True}
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
prior_receipt = BASE / 'results/su32-native-join-binding-v1/verification.json'
result = {'passed': True, 'fresh_agda_exit': run.returncode, 'command': command,
          'negative': {'command': negative, 'exit': neg.returncode, 'diagnostic': diag},
          'dependency_warnings': warnings, 'dependency_manifest_sha256': sha(manifest),
          'checker_sha256': sha(Path(__file__)), 'prerequisite_receipt_sha256': sha(prior_receipt),
          'nativeRecordPresentationFillerDerived': True, 'nativeSignalExecuted': False,
          'originalIncidencePathsCompared': False,
          'conclusion': 'The corrected Boolean native carrier is equivalent to its four-record reader. That reader is an embedding. The computed native comparison of preparation-first and consumer-first complete context presentations is contractible under the full-record reader law.',
          'finite_controls': {'values': values, 'pointed_port_permutations': [identity, swap],
                              'scope': 'Explicit two-permutation control, not exhaustive permutation enumeration'},
          'limits': ['Uniqueness is of this current-value pointed reader-preserving filler, not of Resolve histories.',
                     'Native closure comparison is between the two complete context presentations, not the original five-cell paths.',
                     'Boolean set-valued input fragment only; higher input fibers and physical continuation are not classified.',
                     'The existing four-vertex compiler is not applied to these operands; their normalization and uniqueness are proved directly.']}
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ('passed', 'fresh_agda_exit', 'nativeRecordPresentationFillerDerived', 'nativeSignalExecuted', 'originalIncidencePathsCompared', 'conclusion')}))
