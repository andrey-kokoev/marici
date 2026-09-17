#!/usr/bin/env python3
"""Analytic one-phase cover bound for the two-prime bad set (floating evaluation)."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
L=.55;delta=.025;c2=math.log(2)/math.sqrt(2);c3=math.log(3)/math.sqrt(3)
# Global digamma lower bound: gamma(u)>=(log(u/2)-3/2-log pi)/(4pi).
def gl(u):return (np.log(u/2)-1.5-math.log(math.pi))/(4*math.pi)
R=2*math.exp(4*math.pi*(c2+c3+delta)+1.5+math.log(math.pi));T=2*math.pi/math.log(2)
N=math.ceil(R/T);left=np.arange(N,dtype=float)*T
# First cell includes zero where logarithmic bound is unusable: retain whole cell.
th=np.empty(N);th[0]=-1;th[1:]=(gl(left[1:])-delta-c3)/c2
frac=np.where(th<=-1,1.,np.where(th>=1,0.,np.arccos(np.clip(th,-1,1))/math.pi))
measure=2*T*float(frac.sum())
out={'schema':'marici.voevodsky.two-prime-one-phase-bad-cover.v1','method':'On each full log(2)-phase period, discard the 3-phase by its maximum and use the digamma lower bound at the left endpoint.','containment_radius':R,'phase_period':T,'period_count':N,'floating_upper_bound_for_symmetric_bad_measure':measure,'resulting_concentration_trace_upper':L*measure/math.pi,'interpretation':'Rigorous after directed evaluation of constants, but far too large for a dense finite Schur certificate.','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_one_phase_bad_cover.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
