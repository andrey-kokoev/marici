"""Fresh safe Agda check: relative algebraic locality and relabeling covariance."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickRelativeLocality.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
paths=[source,ROOT/'agda/TickRelativeSourceContract.agda',ROOT/'agda/TickPolynomialRealization.agda',Path(__file__).resolve()]
before={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickRelativeLocality.log').write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':True,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['generator and leg slice-locality on each factor',
             'classification of all injective Bool renamings',
             'basis covariance under independent factor relabelings',
             'generic generator and leg intertwiner transport',
             'generator and leg covariance under independent factor relabelings',
             'factor exchange interchanges generators and legs',
             'factor exchange interchanges an ordered two-leg composite',
             'locality and leg covariance transported to DerivedComponents'],
   'scope':'Algebraic fixed-profile construction over an arbitrary scalar ring; not a completion analytic theorem.',
   'full_analytic_interface_instantiated':False,'original_source_lift_closed':False,
   'warnings_present':b'warning:' in output}
(ROOT/'results/relative-locality.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
