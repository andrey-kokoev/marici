#!/usr/bin/env python3
"""Directed Arb evaluation of all scalar gamma-tail asymptotic moments at R=250."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb
flint.ctx.prec=1600;root=Path(__file__).parents[1]/'results';R=arb(250);w=arb('1.1');a=2*arb.pi();K=400
sin=(w*R).sin();cos=(w*R).cos();log=(R/a).log()
C=[arb(0) for _ in range(K+2)];S=[arb(0) for _ in range(K+2)];CL=[arb(0) for _ in range(K+2)];SL=[arb(0) for _ in range(K+2)]
# Absolute integral residual balls at the terminal index.
b=R**(1-K)/(K-1);bl=R**(1-K)*(log/(K-1)+arb(1)/(K-1)**2)
C[K]=arb(0,b);S[K]=arb(0,b);CL[K]=arb(0,bl);SL[K]=arb(0,bl)
for k in range(K-1,1,-1):
 C[k]=-R**(-k)*sin/w+k*S[k+1]/w
 S[k]= R**(-k)*cos/w-k*C[k+1]/w
 CL[k]=-R**(-k)*log*sin/w+k*SL[k+1]/w-S[k+1]/w
 SL[k]= R**(-k)*log*cos/w-k*CL[k+1]/w+C[k+1]/w
dig=json.loads((root/'digamma_real_asymptotic_coefficients.json').read_text());coef={int(j):arb(c) for j,c in dig['coefficients'].items()};out={};maxrad=0.;contained=True
for k in range(2,321):
 plain=R**(1-k)*(log/(k-1)+arb(1)/(k-1)**2);zc=CL[k];zs=SL[k]
 for j,c in coef.items():
  plain+=c*R**(1-k-j)/(k+j-1);zc+=c*C[k+j];zs+=c*S[k+j]
 vals={'plain':plain,'cos':zc,'sin':zs};out[str(k)]={q:str(v) for q,v in vals.items()}
 for q,v in vals.items():
  maxrad=max(maxrad,float(v.rad()))
res={'schema':'marici.voevodsky.gamma-tail-moments-250-arb.v1','precision_bits':flint.ctx.prec,'R':250,'terminal_index':K,'power_range':[2,320],'moments':out,'maximum_moment_radius':maxrad,'passed':True,'rh_proved':False}
p=root/'gamma_tail_moments_250_arb_320.json';p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:res[k] for k in ('precision_bits','terminal_index','power_range','maximum_moment_radius','passed')},indent=2));assert res['passed']
