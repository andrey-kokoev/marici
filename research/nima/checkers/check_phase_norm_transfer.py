"""Fresh Agda check of the scheduled-bound-to-phase-norm transfer theorem."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
source = ROOT / 'agda/TickPhaseNormTransfer.agda'
command = [os.environ.get('NIMA_AGDA', str(HOME / 'tools/cubical-agda/agda-2.8.0/agda.exe')),
           '--safe', '--cubical', '--guardedness', '--transliterate', '--ignore-interfaces']
for directory in [ROOT / 'agda', ROOT.parent / 'voevodsky/agda',
                  Path(os.environ.get('NIMA_CUBICAL', str(HOME / 'tools/cubical-agda/cubical-0.9')))]:
    command += ['-i', str(directory)]
fresh = '--cached' not in sys.argv
if not fresh:
    command.remove('--ignore-interfaces')
command.append(str(source))
paths = ['agda/TickPhaseNormTransfer.agda', 'agda/TickCompletionPhase.agda']
before = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
try:
    run = subprocess.run(command, capture_output=True, timeout=300)
except subprocess.TimeoutExpired as error:
    (ROOT/'results/agda-TickPhaseNormTransfer.log').write_bytes((error.stdout or b'')+(error.stderr or b''))
    (ROOT/'results/agda-TickPhaseNormTransfer.json').write_text(json.dumps({
        'status':'timeout', 'command':command, 'source_sha256':before,
        'hypothesis_instantiated':False}, indent=2)+'\n', encoding='utf-8')
    raise
(ROOT/'results/agda-TickPhaseNormTransfer.log').write_bytes(run.stdout+run.stderr)
stable = all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in before.items())
result = {'status': 'pass' if run.returncode==0 and stable else 'fail',
          'command':command, 'exit_code':run.returncode, 'fresh_dependency_check':fresh,
          'source_sha256':before, 'source_stable':stable,
          'proved':['norm-representative-class', 'representative-unit-norm', 'completion-unit-norm', 'phase-norm-reduction', 'phase-unit-norm'],
          'hypothesis':'ScheduledNormBound: actual operational norm representatives are metric-equivalent to constant one',
          'hypothesis_instantiated':False}
receipt = 'agda-TickPhaseNormTransfer.json' if fresh else 'agda-TickPhaseNormTransfer-cached.json'
(ROOT/'results'/receipt).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['status']=='pass' else 1)
