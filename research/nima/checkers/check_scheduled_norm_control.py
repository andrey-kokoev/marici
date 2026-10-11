"""Verify actual sample indexing and the eventual-control-to-metric-bound bridge."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
source=ROOT/'agda/TickScheduledNormControl.agda'
command=[os.environ.get('NIMA_AGDA',str(HOME/'tools/cubical-agda/agda-2.8.0/agda.exe')),
         '--safe','--cubical','--guardedness','--transliterate','--ignore-interfaces']
for directory in (ROOT/'agda',ROOT.parent/'voevodsky/agda',Path(os.environ.get('NIMA_CUBICAL',str(HOME/'tools/cubical-agda/cubical-0.9')))):
    command+=['-i',str(directory)]
command.append(str(source))
paths=[source,ROOT/'agda/TickPhaseNormError.agda',Path(__file__).resolve()]
before={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
try:
    run=subprocess.run(command,capture_output=True,timeout=300)
    output=run.stdout+run.stderr; code=run.returncode
except subprocess.TimeoutExpired as error:
    output=(error.stdout or b'')+(error.stderr or b''); code=None
(ROOT/'results/agda-TickScheduledNormControl.log').write_bytes(output)
stable=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in before.items())
r={'status':'pass' if code==0 and stable else ('timeout' if code is None else 'fail'),
   'fresh_dependency_check':True,'exit_code':code,'command':command,'source_sha256':before,
   'proved':['actual-norm-sample','cosine-amplitude-bound','sine-amplitude-bound','common-amplitude-nonnegative','sample-control-bound','controls-to-scheduled-norm'],
   'sample_depth':'suc(d+d)+suc(n), separately for canonical cosine and sine radius exponents',
   'eventual_controls_constructed':False,'scheduled_norm_bound_instantiated':False,
   'remaining':'Construct common Taylor controls with amplitude/error bounds and cofinal depth choices meeting the budget. Uniform bounds on the actual scheduled samples are now instantiated.'}
(ROOT/'results/scheduled-norm-control.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['status']=='pass' else 1)
