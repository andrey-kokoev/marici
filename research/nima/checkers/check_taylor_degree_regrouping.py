"""Fresh kernel verification of exact finite regrouping by actual total degree."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickTaylorDegreeRegrouping.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
paths=[source,ROOT/'agda/TickTaylorProductExpansion.agda',Path(__file__).resolve()]
before={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickTaylorDegreeRegrouping.log').write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':True,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['mass-total','bounded-sum-cong','regroup-grid','cos-degree-bound','sin-degree-bound','operational-norm-by-degree'],
   'scope':'All rational inputs and cutoffs: cosine square degrees 2i+2j, sine square degrees 2i+2j+2, bounded by 4N+2; original normalized weights retained.',
   'factorial_binomial_identification_proved':False,'vanishing_norm_defect_proved':False,
   'remaining':'Identify each degree contribution with the truncated Leibniz norm derivative times exponentialTerm(q,k), then transfer cancellation and bound the high-degree tail.'}
(ROOT/'results/taylor-degree-regrouping.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
