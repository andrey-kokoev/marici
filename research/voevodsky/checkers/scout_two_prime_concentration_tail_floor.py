#!/usr/bin/env python3
"""Scout a two-prime concentration tail floor at L=.55, R=250."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.linalg import eigh
 from scipy.special import roots_legendre,digamma
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.linalg import eigh
 from scipy.special import roots_legendre,digamma
L=.55;R=250.;nx=1200;z,w=roots_legendre(nx);x=L*z;wx=L*w;sw=np.sqrt(wx);d=x[:,None]-x[None,:];T=(sw[:,None]*sw[None,:])*(R/math.pi)*np.sinc(R*d/math.pi);vals=np.linalg.eigvalsh(T);vals=vals[::-1];trace_exact=2*L*R/math.pi;qR=(digamma(.25+125j).real-math.log(math.pi))/2;cp=sum(math.log(p)/math.sqrt(p) for p in (2,3));m=qR-cp;q0=(digamma(.25).real-math.log(math.pi))/2;Clow=-(q0-cp);rows=[]
for M in (90,100,110,120,130,140,160):
 trace_res=max(0.,trace_exact-float(vals[:M].sum()));lam_bound=trace_res;floor=m-(m+Clow)*lam_bound;rows.append({'retained_concentration_modes':M,'trace_residual':trace_res,'lambda_M_plus_1_trace_bound':lam_bound,'tail_floor':floor})
out={'schema':'marici.voevodsky.two-prime-concentration-tail-floor-scout.v1','L':L,'R':R,'space_nodes':nx,'shannon_trace':trace_exact,'exterior_combined_floor':m,'interior_negative_depth':Clow,'rows':rows,'status':'floating concentration scout; directed trace enclosure required','passed':any(r['tail_floor']>0 for r in rows),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'two_prime_concentration_tail_floor_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
