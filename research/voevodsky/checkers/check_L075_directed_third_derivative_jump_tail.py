#!/usr/bin/env python3
"""Directed third-derivative-jump tail using repeated Legendre antiderivatives."""
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
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75');d3=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb((n-2)*(n-1)*n*(n+1)*(n+2)*(n+3))/48 for n in range(4,150,2)),arb(0));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;D=lam/arb(nn).sqrt()/2*d3;data += [(y,D),(-y,D)]
def integrate(poly):
 out={}
 for k,c in poly.items():
  out[k+1]=out.get(k+1,arb(0))+c/(2*k+1);out[k-1]=out.get(k-1,arb(0))-c/(2*k+1)
 return out
def evalpoly(y,p):return sum((c*y.legendre_p(k) for k,c in p.items()),arb(0))
def Rpoly(n):return {n+2:arb(1)/(2*n+3),n:-arb(1)/(2*n+3)-arb(1)/(2*n-1),n-2:arb(1)/(2*n-1)}
M=50000;sq=arb(0)
for n in range(1000,M):
 A=(L*(2*n+1)/2).sqrt()/(2*n+1);U=integrate(integrate(Rpoly(n)));c=sum((A*D*evalpoly(y,U) for y,D in data),arb(0));sq+=c*c
C=sum((64*(L/arb.pi()).sqrt()*abs(D)*(1-y*y)**arb('-.25') for y,D in data),arb(0));rem=C/(7*arb(M-1)**7).sqrt();total=(sq+rem*rem).sqrt();out={'schema':'marici.voevodsky.L075-directed-third-derivative-jump-tail.v1','endpoint_scaled_third_derivative':str(d3),'finite_norm':str(sq.sqrt()),'infinite_remainder_bound':str(rem),'total_bound':str(total),'available_smooth_reserve':4.475419590441005e-10,'passed':total.upper()<arb('4.475419590441005e-10'),'scope':'third-derivative jumps; four-times-continuous remainder and analytic rows remain','rh_proved':False};p=root/'L075_directed_third_derivative_jump_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
