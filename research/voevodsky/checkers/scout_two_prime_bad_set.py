#!/usr/bin/env python3
"""Nonrigorous grid scout for the exact two-prime combined symbol."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
 from scipy.special import digamma
L=.55;delta=.025;R=10000.;step=.01
x=np.arange(0,R+step/2,step)
y=(digamma(.25+.5j*x).real-math.log(math.pi))/(4*math.pi)
for p in (2,3):y-=math.log(p)/math.sqrt(p)*np.cos(x*math.log(p))
measure=2*step*np.count_nonzero(y<delta)
S=sum(math.log(p)/math.sqrt(p) for p in (2,3))
# Rigorous analytic containment radius if the registered global digamma lower bound is used.
contain=2*math.exp(4*math.pi*(S+delta)+1.5+math.log(math.pi))
out={'schema':'marici.voevodsky.two-prime-bad-set-scout.v1','declared_L':L,'active_prime_powers':[2,3],'delta':delta,'grid':{'radius':R,'step':step,'sample_count':len(x),'minimum':float(y.min()),'minimizer':float(x[y.argmin()]),'estimated_symmetric_bad_measure_inside_grid':measure},'analytic_bad_set_containment_radius':contain,'trace_scale_estimate_inside_grid':L*measure/math.pi,'status':'floating scout only; no directed enclosure, root isolation, concentration spectrum, endpoint bound, or Schur certificate','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_bad_set_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
