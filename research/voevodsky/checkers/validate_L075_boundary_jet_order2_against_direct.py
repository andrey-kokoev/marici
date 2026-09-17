#!/usr/bin/env python3
"""Validate boundary-jet signs and normalization against directed direct coefficients."""
import json,math,re,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre,gammaln
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import eval_legendre,gammaln
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;L=.75
def der(m):return sum(v[n]*math.sqrt((2*n+1)/(2*L))*math.exp(gammaln(n+m+1)-gammaln(n-m+1)-m*math.log(2)-gammaln(m+1)) for n in range(m+(m%2),150,2))
ds=[der(m) for m in range(2+1)];pts=[]
for nn,lam in ((2,math.log(2)),(3,math.log(3)),(4,math.log(2))):
 y=(L-math.log(nn))/L
 for m in range(2+1):D=lam/math.sqrt(nn)/2*ds[m];pts.extend([(m,y,D),(m,-y,(-1)**(m+1)*D)])
def integ(p):
 q={}
 for k,c in p.items():q[k+1]=q.get(k+1,0)+c/(2*k+1);q[k-1]=q.get(k-1,0)-c/(2*k+1)
 return q
def jet(n):
 z=0
 for m,y,D in pts:
  if m==0:z+=D*math.sqrt((2*n+1)/(2*L))*L*(eval_legendre(n-1,y)-eval_legendre(n+1,y))/(2*n+1)
  else:
   p={n+2:1/(2*n+3),n:-1/(2*n+3)-1/(2*n-1),n-2:1/(2*n-1)}
   for _ in range(m-1):p=integ(p)
   z+=math.sqrt(L*(2*n+1)/2)/(2*n+1)*D*sum(c*eval_legendre(k,y) for k,c in p.items() if k>=0)
 return z
rows=[]
for a,b in ((1000,1100),(1100,1200)):
 d=json.loads((root/f'L075_residual_cached_chunk_{a}_{b}.json').read_text());actual=np.array([float(re.match(r'\[?([^ ]+)',s).group(1)) for s in d['components']]);pred=np.array([jet(n) for n in d['indices']]);err=actual-pred;rows.append({'range':[a,b],'actual_norm':float(np.linalg.norm(actual)),'jet6_norm':float(np.linalg.norm(pred)),'difference_norm':float(np.linalg.norm(err)),'maximum_abs_difference':float(max(abs(err)))})
out={'schema':'marici.voevodsky.L075-boundary-jet-order2-direct-validation.v1','rows':rows,'passed_scout':all(x['difference_norm']<2e-11 for x in rows),'passed':False,'remaining':'order-six truncation is not a valid approximation at n near 1000; higher jets/cancellation or optimal low-order truncation required','rh_proved':False};p=root/'L075_boundary_jet_order2_direct_validation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
