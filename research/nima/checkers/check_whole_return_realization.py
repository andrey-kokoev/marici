"""Fresh Agda closure check for the whole-Tick return construction."""
import hashlib
import json
from pathlib import Path
import subprocess
import os

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
compiler = Path(os.environ.get('NIMA_AGDA', HOME / 'tools/cubical-agda/agda-2.8.0/agda.exe'))
library = Path(os.environ.get('NIMA_CUBICAL', HOME / 'tools/cubical-agda/cubical-0.9'))
source = ROOT / 'agda/TickWholeReturnRealization.agda'
command = [str(compiler), '--safe', '--cubical', '--guardedness', '--transliterate', '--ignore-interfaces']
for directory in [ROOT / 'agda', ROOT.parent / 'voevodsky/agda', ROOT / 'adapters/native-application', ROOT / 'adapters/application-extension', library]:
    command += ['-i', str(directory)]
command.append(str(source))
before = hashlib.sha256(source.read_bytes()).hexdigest()
run = subprocess.run(command, capture_output=True, timeout=300)
log = ROOT / 'results/agda-TickWholeReturnRealization.log'
log.write_bytes(run.stdout + run.stderr)
stable = before == hashlib.sha256(source.read_bytes()).hexdigest()
receipt = {
    'status': 'pass' if run.returncode == 0 and stable else 'fail',
    'command': command,
    'exit_code': run.returncode,
    'source_sha256': before,
    'source_stable': stable,
    'fresh_dependency_check': True,
    'log': str(log.relative_to(ROOT)),
    'proved': ['return-start', 'return-finish', 'return-continuous', 'reconstruction-coherence', 'same-tags-coherence', 'schedule-swap'],
    'remaining': 'unitary evolution, parameter-domain metric structure, and generator compatibility',
}
(ROOT / 'results/agda-TickWholeReturnRealization.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
raise SystemExit(0 if receipt['status'] == 'pass' else 1)
