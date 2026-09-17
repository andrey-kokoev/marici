#!/usr/bin/env python3
"""Directed second-derivative-jump tail after value/ramp subtraction."""
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
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75');d2=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb((n-1)*n*(n+1)*(n+2))/8 for n in range(2,150,2)),arb(0));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;H=lam/arb(nn).sqrt()/2*d2;data += [(y,H),(-y,-H)]
def I(y,k):return (y.legendre_p(k+1)-y.legendre_p(k-1))/(2*k+1)
def S(y,n):return (I(y,n+2)-I(y,n))/(2*n+3)-(I(y,n)-I(y,n-2))/(2*n-1)
M=50000;sq=arb(0)
for n in range(1000,M):
 A=(L*(2*n+1)/2).sqrt()/(2*n+1);c=sum((A*H*S(y,n) for y,H in data),arb(0));sq+=c*c
# Safe enlarged Bernstein constant for the four twice-integrated differences.
C=sum((16*(L/arb.pi()).sqrt()*abs(H)*(1-y*y)**arb('-.25') for y,H in data),arb(0));rem=C/(5*arb(M-1)**5).sqrt();total=(sq+rem*rem).sqrt();out={'schema':'marici.voevodsky.L075-directed-second-derivative-jump-tail.v1','endpoint_scaled_second_derivative':str(d2),'finite_norm':str(sq.sqrt()),'infinite_remainder_bound':str(rem),'total_bound':str(total),'passed':total.upper()<arb('1e-10'),'scope':'second-derivative jumps; thrice-continuous remainder remains','rh_proved':False};p=root/'L075_directed_second_derivative_jump_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
