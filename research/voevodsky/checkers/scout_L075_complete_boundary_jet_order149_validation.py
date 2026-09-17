#!/usr/bin/env python3
"""High-precision complete finite boundary-jet validation on ten tail modes."""
import json,re,sys
from pathlib import Path
try:
 import numpy as np, mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np,mpmath as mp
mp.mp.dps=60;root=Path(__file__).parents[1]/'results';vf=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vf[1::2]=0;v=[mp.mpf(repr(float(x))) for x in vf];L=mp.mpf('.75')
def der(m):
 return mp.fsum(v[n]*mp.sqrt(mp.mpf(2*n+1)/(2*L))*mp.factorial(n+m)/(mp.power(2,m)*mp.factorial(m)*mp.factorial(n-m)) for n in range(m+(m%2),150,2))
ds=[der(m) for m in range(150)];ys=[]
for nn,lam in ((2,mp.log(2)),(3,mp.log(3)),(4,mp.log(2))):ys.append(((L-mp.log(nn))/L,lam/mp.sqrt(nn)/2))
def integ(p):
 q={}
 for k,c in p.items():q[k+1]=q.get(k+1,mp.mpf(0))+c/(2*k+1);q[k-1]=q.get(k-1,mp.mpf(0))-c/(2*k+1)
 return q
def ev(y,p):return mp.fsum(c*mp.legendre(k,y) for k,c in p.items() if k>=0)
def coeffs(n,targets):
 z=mp.mpf(0);A=mp.sqrt(L*(2*n+1)/2)/(2*n+1);out={};all_y=[q for y,w in ys for q in (y,-y)];cache={(str(q),k):mp.legendre(k,q) for q in all_y for k in range(n-150,n+153)}
 def evc(q,p):return mp.fsum(c*cache[(str(q),k)] for k,c in p.items() if k>=0)
 for y,w in ys:
  J=w*ds[0];z+=J*mp.sqrt((2*n+1)/(2*L))*L*(mp.legendre(n-1,y)-mp.legendre(n+1,y))/(2*n+1);z-=J*mp.sqrt((2*n+1)/(2*L))*L*(mp.legendre(n-1,-y)-mp.legendre(n+1,-y))/(2*n+1)
 p={n+2:mp.mpf(1)/(2*n+3),n:-mp.mpf(1)/(2*n+3)-mp.mpf(1)/(2*n-1),n-2:mp.mpf(1)/(2*n-1)}
 for m in range(1,150):
  for y,w in ys:
   D=w*ds[m];z+=A*D*(evc(y,p)+(-1)**(m+1)*evc(-y,p))
  if m in targets:out[m]=z
  p=integ(p)
 return out
mode=int(sys.argv[1]) if len(sys.argv)>1 else 1000;start=1000 if mode<1100 else 1100;d=json.loads((root/f'L075_residual_cached_chunk_{start}_{start+100}.json').read_text());idx=d['indices'].index(mode);actual=[mp.mpf(re.match(r'\[?([^ ]+)',d['components'][idx]).group(1))];targets=(1,2,6,20,50,100,149);pred=[coeffs(mode,targets)];rows=[]
for K in targets:
 err=mp.sqrt(mp.fsum((a-b[K])**2 for a,b in zip(actual,pred)));rows.append({'order':K,'three_mode_difference_norm':mp.nstr(err,18)})
out={'schema':'marici.voevodsky.L075-complete-boundary-jet-order149-validation.v1','precision_digits':60,'mode':mode,'rows':rows,'passed_scout':True,'passed':False,'rh_proved':False};p=root/f'L075_complete_boundary_jet_order149_validation_mode{mode}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
