#!/usr/bin/env python3
"""Directed finite jump tail plus Bernstein bound for the infinite remainder."""
import json,math,sys
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
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
def peval(y):
 p0=arb(1);s=v[0]*(1/(2*L)).sqrt();p1=y
 for n in range(1,149):p2=((2*n+1)*y*p1-n*p0)/(n+1);s+=v[n+1]*((2*(n+1)+1)/(2*L)).sqrt()*p2;p0,p1=p1,p2
 return s
wend=peval(arb(1));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 d=L-arb(nn).log();J=lam/arb(nn).sqrt()/2*wend;data += [(d/L,J),(-d/L,-J)]
# Direct Arb Legendre evaluation avoids long-interval recurrence wrapping.
sq=arb(0);M=50000
for n in range(1000,M):
 c=arb(0)
 for y,J in data:
  c+=J*((2*n+1)/(2*L)).sqrt()*L*(y.legendre_p(n-1)-y.legendre_p(n+1))/(2*n+1)
 sq+=c*c
# Bernstein |P_n(cos theta)| <= sqrt(2/(pi*(n+1/2)*sin theta)); simplify to a rigorous larger C/n for n>=M.
C=arb(0)
for y,J in data:
 sint=(1-y*y).sqrt();C+=abs(J)*L.sqrt()*(2/(arb.pi()*sint)).sqrt()*arb('1.01')
remainder=C/(arb(M-1).sqrt());total=(sq+remainder*remainder).sqrt();allow=arb('4.267829461527579e-9');out={'schema':'marici.voevodsky.L075-directed-jump-tail.v1','precision_bits':flint.ctx.prec,'finite_range':[1000,M],'finite_tail_squared':str(sq),'finite_tail_norm':str(sq.sqrt()),'bernstein_constant_with_1_percent_slack':str(C),'infinite_remainder_norm_bound':str(remainder),'total_jump_tail_norm_bound':str(total),'allowable_tail_norm':str(allow),'passed':total.upper()<allow.lower(),'scope':'value-jump contribution only; continuous remainder after jump subtraction remains separate','rh_proved':False};p=root/'L075_directed_jump_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
