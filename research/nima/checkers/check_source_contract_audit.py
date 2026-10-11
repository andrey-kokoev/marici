"""Fresh verification of the bounded source-contract diagnostic, not a lift proof."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickSourceContractAudit.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda', ROOT.parent/'voevodsky/agda', Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
before=hashlib.sha256(source.read_bytes()).hexdigest()
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickSourceContractAudit.log').write_bytes(output)
stable=before==hashlib.sha256(source.read_bytes()).hexdigest()
result={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
        'command':command,'fresh_dependency_check':True,'exit_code':code,
        'source_sha256':before,'source_stable':stable,
        'proved':['arbitrary-reconstruction','arbitrary-swap','recover-semantics','interpret-injective'],
        'scope':'Reconstruction and schedule-swap alone admit every external Schedule-to-X semantics.',
        'audit_stage_outcome':'+-',
        'audit_reason':'The source-derived predicate is not yet specified sufficiently to distinguish a derived lift from a supplied adapter.',
        'lift_refuted':False,'source_contract_unlocked':False}
(ROOT/'results/source-contract-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['status']=='pass' else 1)
