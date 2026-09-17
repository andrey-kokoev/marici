#!/usr/bin/env python3
"""Coefficientwise sum of boundary jets through order six (floating scout)."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre,gammaln
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import eval_legendre,gammaln
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;L=.75
def deriv(m):
 s=0.
 for n in range(m+(m%2),150,2):s+=v[n]*math.sqrt((2*n+1)/(2*L))*math.exp(gammaln(n+m+1)-gammaln(n-m+1)-m*math.log(2)-gammaln(m+1))
 return s
ds=[deriv(m) for m in range(7)];points=[]
for nn,lam in ((2,math.log(2)),(3,math.log(3)),(4,math.log(2))):
 y=(L-math.log(nn))/L
 for m in range(7):
  D=lam/math.sqrt(nn)/2*ds[m];points.extend([(m,y,D),(m,-y,(-1)**(m+1)*D)])
def integ(p):
 q={}
 for k,c in p.items():q[k+1]=q.get(k+1,0)+c/(2*k+1);q[k-1]=q.get(k-1,0)-c/(2*k+1)
 return q
def ev(y,p):return sum(c*eval_legendre(k,y) for k,c in p.items() if k>=0)
M=10000;sq=0
for n in range(1000,M):
 A=math.sqrt(L*(2*n+1)/2)/(2*n+1);c=0
 for m,y,D in points:
  if m==0:c+=D*math.sqrt((2*n+1)/(2*L))*L*(eval_legendre(n-1,y)-eval_legendre(n+1,y))/(2*n+1)
  else:
   p={n+2:1/(2*n+3),n:-1/(2*n+3)-1/(2*n-1),n-2:1/(2*n-1)}
   for _ in range(m-1):p=integ(p)
   c+=(-1)**(m+1)*A*D*ev(y,p)
 sq+=c*c
out={'schema':'marici.voevodsky.L075-complete-boundary-jet-order6-scout.v1','endpoint_scaled_derivatives_0_6':ds,'finite_range':[1000,M],'coefficientwise_combined_norm':math.sqrt(sq),'passed_scout':math.sqrt(sq)<4.3e-9,'passed':False,'remaining':'directed evaluation, analytic tail after M, and seven-times-continuous remainder','rh_proved':False};p=root/'L075_complete_boundary_jet_order6_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']
