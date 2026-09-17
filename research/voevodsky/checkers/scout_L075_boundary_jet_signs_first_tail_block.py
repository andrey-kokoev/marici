#!/usr/bin/env python3
"""Determine boundary-jet orientation signs against directed modes 1000..1098."""
import itertools,json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from scipy.special import eval_legendre
root=Path(__file__).parents[1]/'results';d=json.loads((root/'L075_residual_cached_chunk_1000_1100.json').read_text());# Arb midpoints parse safely via leading center token.
def mid(s):
 try:return float(s.strip('[]').split('+/-')[0])
 except:return float(s)
r=np.array([mid(x) for x in d['components']]);v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;L=.75;nn=np.arange(150);scale=np.sqrt((2*nn+1)/(2*L));ders=[]
for k in range(4):
 vals=np.zeros(150)
 for m in range(k,150):vals[m]=math.factorial(m+k)/(2**k*math.factorial(k)*math.factorial(m-k))
 ders.append(float(np.dot(v*scale,vals)))
points=[]
for q,lam in ((2,math.log(2)),(3,math.log(3)),(4,math.log(2))):
 y=(L-math.log(q))/L;c=lam/math.sqrt(q)/2
 # parity-derived jumps for even w: k even opposite signs, k odd same signs.
 points.append((y,c));points.append((-y,c))
def integ(poly):
 out={}
 for m,c in poly.items():out[m+1]=out.get(m+1,0)+c/(2*m+1);out[m-1]=out.get(m-1,0)-c/(2*m+1)
 return out
B=np.zeros((4,len(r)))
for j,n in enumerate(d['indices']):
 A=math.sqrt(L*(2*n+1)/2)/(2*n+1);poly={n+1:-1.,n-1:1.}
 for k in range(4):
  val=0.
  for idx,(y,c) in enumerate(points):
   parity_sign=(-1 if (k%2==0 and idx%2==1) else 1);val+=c*ders[k]*parity_sign*sum(cc*eval_legendre(m,y) for m,cc in poly.items())
  B[k,j]=A*val;poly=integ(poly)
rows=[]
for signs in itertools.product((-1,1),repeat=4):rows.append((float(np.linalg.norm(r-sum(signs[k]*B[k] for k in range(4)))),signs))
rows.sort();first_two=float(np.linalg.norm(r-B[0]+B[1]));out={'schema':'marici.voevodsky.L075-boundary-jet-signs-first-tail-block.v1','best_residual_norm':rows[0][0],'best_signs_orders_0_3':rows[0][1],'next_best':rows[1][0],'orders_0_1_residual_norm':first_two,'full_block_norm':float(np.linalg.norm(r)),'individual_jet_norms':[float(np.linalg.norm(x)) for x in B],'passed_scout':first_two<1e-11,'passed':False,'scope':'floating orientation scout against directed residual centers','rh_proved':False};p=root/'L075_boundary_jet_signs_first_tail_block.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
