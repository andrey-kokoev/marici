"""Check the algebraic relative-derivation contract; no analytic-law promotion."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickRelativeSourceContract.agda'
contract=ROOT/'contracts/relative-source-derivation.v1.json'
c=json.loads(contract.read_text(encoding='utf-8'))
assert c['status']=='specified_relative_contract_not_full_lift_proof'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
paths=[source,contract,Path(__file__).resolve()]
before={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickRelativeSourceContract.log').write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':True,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['DerivedComponents is a type','canonical inhabits DerivedComponents','legs-agree for fixed analytic profile'],
   'full_analytic_interface_instantiated':False,'whole_path_contract_instantiated':False,
   'original_source_lift_closed':False}
(ROOT/'results/relative-source-contract.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
