"""Fresh check of Taylor weights, reusing existing factorial-splitting machinery."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickTaylorBinomialWeights.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
fresh='--cached' not in sys.argv
if not fresh:
    command.remove('--ignore-interfaces')
command.append(str(source))
name='taylor-binomial-weights' if fresh else 'taylor-binomial-weights-cached'
paths=[source,ROOT/'agda/TickTaylorDegreeRegrouping.agda',ROOT.parent/'voevodsky/agda/AbsoluteTaylorSeriesMultiplication.agda',Path(__file__).resolve()]
before={os.path.relpath(p,ROOT).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results'/('agda-'+name+'.log')).write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':fresh,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['power-add','exponential-binomial-split','exponential-product-weight','normalized-product-weight','cosine-product-weight','sine-product-weight','degree-contributions-weighted'],
   'reused':'AbsoluteTaylorSeriesMultiplication.reciprocal-factorial-split and exponential-convolution-summand-from-factorial-split',
   'scope':'Exact binomial normalization for all rational inputs and indices, lifted to every actual grouped degree contribution.',
   'leibniz_coefficient_sum_identification_proved':False,'vanishing_norm_defect_proved':False,
   'remaining':'Identify the finite parity-filtered binomial sum with the truncated Leibniz derivative, apply cancellation, and instantiate the existing residual/tail machinery.'}
if code != 0:
    r['declared_theorems']=r.pop('proved')
(ROOT/'results'/(name+'.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
