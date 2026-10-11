"""Fresh closure check of the implemented completion phase fragment."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
source = ROOT / 'agda/TickCompletionPhase.agda'
command = [os.environ.get('NIMA_AGDA', str(HOME / 'tools/cubical-agda/agda-2.8.0/agda.exe')),
           '--safe', '--cubical', '--guardedness', '--transliterate', '--ignore-interfaces']
for path in [ROOT / 'agda', ROOT.parent / 'voevodsky/agda',
             Path(os.environ.get('NIMA_CUBICAL', str(HOME / 'tools/cubical-agda/cubical-0.9')))]:
    command += ['-i', str(path)]
command.append(str(source))
before = hashlib.sha256(source.read_bytes()).hexdigest()
run = subprocess.run(command, capture_output=True, timeout=300)
(ROOT / 'results/agda-TickCompletionPhase.log').write_bytes(run.stdout + run.stderr)
stable = before == hashlib.sha256(source.read_bytes()).hexdigest()
result = {'status': 'pass' if run.returncode == 0 and stable else 'fail',
          'command': command, 'exit_code': run.returncode, 'fresh_dependency_check': True,
          'source_sha256': before, 'source_stable': stable,
          'proved': ['phase-start', 'phase-real', 'phase-imaginary', 'phase-finish-components'],
          'full_phase_test_outcome': '+-',
          'remaining': ['completion-valued pi with half-turn laws', 'unit norm', 'metric continuity']}
(ROOT / 'results/agda-TickCompletionPhase.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
raise SystemExit(0 if result['status'] == 'pass' else 1)
