#!/usr/bin/env python3
"""Build degree-32 robust eigenbranch interpolant and certify its stored polynomial with Arb."""
import json,sys
from pathlib import Path
try:
 import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree8_complete_lower_matrix_L0649_L065.npz')['coefficients'];tn=np.cos(np.arange(32,-1,-1)*np.pi/32);vals=[]
for t in tn:
 M=np.polynomial.chebyshev.chebval(t,C);vals.append(float(np.linalg.eigvalsh((M+M.T)/2)[1]))
coef=np.polynomial.chebyshev.chebfit(tn,np.array(vals),32);flint.ctx.prec=256;c=[arb(repr(float(x))) for x in coef]
def val(x):
 b1=arb(0);b2=arb(0)
 for a in reversed(c[1:]):b0=a+2*x*b1-b2;b2,b1=b1,b0
 return c[0]+x*b1-b2
N=65536;lows=[]
for j in range(N):
 lo=-1+2*j/N;hi=-1+2*(j+1)/N;x=arb(repr((lo+hi)/2),arb(repr((hi-lo)/2)));lows.append(float(val(x).lower()))
out={'schema':'marici.voevodsky.robust-branch-polynomial-arb-L0649-L065.v1','degree':32,'coefficients':[float(x) for x in coef],'post_degree8_l1':float(sum(abs(coef[9:]))),'interval_count':N,'minimum_interval_lower':min(lows),'passed_polynomial':min(lows)>0,'source_matrix_enclosed':False,'passed':False,'scope':'directed positivity of stored robust eigenbranch polynomial; matrix interpolation/source remainder not enclosed','rh_proved':False};p=root/'robust_branch_polynomial_arb_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='coefficients'},indent=2))
