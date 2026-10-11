"""Fresh verification of the operational-term/derivative normalization bridge."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickTrigTaylorNormalization.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
paths=[source,ROOT/'agda/TickTrigCoefficientCancellation.agda',ROOT.parent/'voevodsky/agda/RationalTaylorApproximants.agda',ROOT.parent/'voevodsky/agda/RationalSineTaylorApproximants.agda',Path(__file__).resolve()]
before={os.path.relpath(p,ROOT).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickTrigTaylorNormalization.log').write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':True,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['cosine-term-normalized','sine-term-normalized','cosine-sum-normalized','sine-sum-normalized'],
   'scope':'All rational inputs and all operational term/partial-sum indices; derivative coefficients times recursive exponentialTerm normalization.',
   'product_convolution_bridge_proved':False,'vanishing_norm_defect_proved':False,
   'remaining':'Relate products of normalized finite sums to Leibniz convolution coefficients; then bound the uncancelled high-degree tail and choose the precision budget.'}
(ROOT/'results/trig-taylor-normalization.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
