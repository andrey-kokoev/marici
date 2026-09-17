#!/usr/bin/env python3
"""Directed value jumps of the piecewise-polynomial prime action at L=.75."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
def peval(y):
 p0=arb(1);s=v[0]*(1/(2*L)).sqrt();p1=y
 for n in range(1,149):
  p2=((2*n+1)*y*p1-n*p0)/(n+1);s+=v[n+1]*((2*(n+1)+1)/(2*L)).sqrt()*p2;p0,p1=p1,p2
 return s
wend=peval(arb(1));rows=[];sumabs=arb(0)
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 a=arb(nn).log();c=lam/arb(nn).sqrt()/2;d=L-a;amp=c*wend;sumabs+=2*abs(amp);rows.append({'prime_power':nn,'locations':[str(d),str(-d)],'jumps':[str(amp),str(-amp)],'absolute_jump_pair':str(2*abs(amp))})
out={'schema':'marici.voevodsky.L075-prime-residual-value-jumps.v1','endpoint_value_wL':str(wend),'jumps':rows,'total_absolute_internal_jump':str(sumabs),'passed':True,'use':'input to directed Legendre jump-tail estimate; continuous remainder must be treated after subtracting these steps','rh_proved':False};p=root/'L075_prime_residual_value_jumps.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
