"""Check the rational norm perturbation bound with a fresh Agda closure."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
source = ROOT/'agda/TickPhaseNormError.agda'
command = [os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
           '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in [ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))]:
    command += ['-i',str(directory)]
command.append(str(source))
before = hashlib.sha256(source.read_bytes()).hexdigest()
try:
    run = subprocess.run(command,capture_output=True,timeout=300)
    output = run.stdout+run.stderr
    code = run.returncode
except subprocess.TimeoutExpired as error:
    output = (error.stdout or b'')+(error.stderr or b'')
    code = None
(ROOT/'results/agda-TickPhaseNormError.log').write_bytes(output)
stable = before == hashlib.sha256(source.read_bytes()).hexdigest()
result = {'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
          'command':command,'exit_code':code,'fresh_dependency_check':True,
          'source_sha256':before,'source_stable':stable,
          'proved':'norm-error-bound: amplitude bounds M, sample errors epsilon, and Taylor norm defect delta imply scheduled norm defect at most 4*M*epsilon+delta',
          'remaining':'instantiate sample bounds and errors for the operational Taylor schedules'}
(ROOT/'results/agda-TickPhaseNormError.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['status']=='pass' else 1)
