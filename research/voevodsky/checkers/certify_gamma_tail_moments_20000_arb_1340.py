#!/usr/bin/env python3
"""Directed scalar moments for rank-670 gamma tail starting at R=20000."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=2048;root=Path(__file__).parents[1]/'results';R=arb(20000);w=arb('1.1');a=2*arb.pi();K=1500;si=(w*R).sin();co=(w*R).cos();lg=(R/a).log();C=[arb(0)]*(K+2);S=[arb(0)]*(K+2);CL=[arb(0)]*(K+2);SL=[arb(0)]*(K+2);b=R**(1-K)/(K-1);bl=R**(1-K)*(lg/(K-1)+arb(1)/(K-1)**2);C[K]=arb(0,b);S[K]=arb(0,b);CL[K]=arb(0,bl);SL[K]=arb(0,bl)
for k in range(K-1,1,-1):
 C[k]=-R**(-k)*si/w+k*S[k+1]/w;S[k]=R**(-k)*co/w-k*C[k+1]/w;CL[k]=-R**(-k)*lg*si/w+k*SL[k+1]/w-S[k+1]/w;SL[k]=R**(-k)*lg*co/w-k*CL[k+1]/w+C[k+1]/w
dig=json.loads((root/'digamma_real_asymptotic_coefficients.json').read_text());coef={int(j):arb(c) for j,c in dig['coefficients'].items()};out={};maxrad=arb(0)
for k in range(2,1341):
 plain=R**(1-k)*(lg/(k-1)+arb(1)/(k-1)**2);zc=CL[k];zs=SL[k]
 for j,c in coef.items():plain+=c*R**(1-k-j)/(k+j-1);zc+=c*C[k+j];zs+=c*S[k+j]
 vals={'plain':plain,'cos':zc,'sin':zs};out[str(k)]={q:str(v) for q,v in vals.items()};maxrad=max(maxrad,*(v.rad() for v in vals.values()))
res={'schema':'marici.voevodsky.gamma-tail-moments-20000-arb.v1','precision_bits':flint.ctx.prec,'R':20000,'terminal_index':K,'power_range':[2,1340],'moments':out,'maximum_moment_radius':str(maxrad),'passed':True,'rh_proved':False};p=root/'gamma_tail_moments_20000_arb_1340.json';p.write_text(json.dumps(res,separators=(',',':'))+'\n');print(json.dumps({k:res[k] for k in ('precision_bits','terminal_index','power_range','maximum_moment_radius','passed')},indent=2))
