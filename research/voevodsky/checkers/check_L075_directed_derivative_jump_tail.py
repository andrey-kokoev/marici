#!/usr/bin/env python3
"""Directed derivative-jump contribution after value-jump subtraction."""
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
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
# endpoint derivative in scaled y coordinate via P_n'(1)=n(n+1)/2.
dwend=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb(n*(n+1))/2 for n in range(0,150,2)),arb(0));data=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;K=lam/arb(nn).sqrt()/2*dwend;data += [(y,K),(-y,K)]
M=50000;sq=arb(0)
for n in range(1000,M):
 c=arb(0);A=(L*(2*n+1)/2).sqrt()/(2*n+1)
 for y,K in data:
  R=(y.legendre_p(n+2)-y.legendre_p(n))/(2*n+3)-(y.legendre_p(n)-y.legendre_p(n-2))/(2*n-1);c+=A*K*R
 sq+=c*c
C=arb(0)
for y,K in data:C+=4*(L/arb.pi()).sqrt()*abs(K)*(1-y*y)**arb('-.25')*arb('1.01')
rem=C/(3*arb(M-1)**3).sqrt();total=(sq+rem*rem).sqrt();out={'schema':'marici.voevodsky.L075-directed-derivative-jump-tail.v1','endpoint_scaled_derivative':str(dwend),'finite_range':[1000,M],'finite_norm':str(sq.sqrt()),'infinite_remainder_bound':str(rem),'total_derivative_jump_tail_bound':str(total),'passed':total.upper()<arb('1e-9'),'scope':'derivative jumps only; twice-continuous remainder remains','rh_proved':False};p=root/'L075_directed_derivative_jump_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
