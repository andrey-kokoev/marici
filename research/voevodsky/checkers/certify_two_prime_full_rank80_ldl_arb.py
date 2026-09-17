#!/usr/bin/env python3
"""Assemble all directed rank-80 components and certify parity LDL pivots."""
import json,sys,hashlib
from pathlib import Path
try:
 import flint
 from flint import arb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,arb_mat
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';names=['two_prime_finite_gamma_arb.json','gamma_tail_250_arb_matrix.json','two_prime_overlap_arb.json','two_prime_endpoint_arb.json'];data=[json.loads((root/n).read_text()) for n in names];N=80
A=arb_mat(N,N)
for d in data:
 assert d['passed']
 for i in range(N):
  for j in range(N):A[i,j]+=arb(d['matrix'][i][j])
def ldl(B):
 n=B.nrows();L=arb_mat(n,n);D=[]
 for i in range(n):L[i,i]=1
 for j in range(n):
  q=B[j,j]
  for k in range(j):q-=L[j,k]*L[j,k]*D[k]
  if not q>0:return False,j,q,D
  D.append(q)
  for i in range(j+1,n):
   q=B[i,j]
   for k in range(j):q-=L[i,k]*L[j,k]*D[k]
   L[i,j]=q/D[j]
 return True,n,None,D
results={};allok=True
for parity,label in ((0,'even'),(1,'odd')):
 B=arb_mat([[A[i,j] for j in range(parity,N,2)] for i in range(parity,N,2)]);ok,idx,bad,D=ldl(B);allok&=ok
 results[label]={'passed':ok,'pivot_count':len(D),'minimum_pivot_lower':min(float(q.lower()) for q in D) if D else None,'minimum_pivot_index':min(range(len(D)),key=lambda k:float(D[k].lower())) if D else None,'failure_index':None if ok else idx,'failure_interval':None if ok else str(bad)}
maxrad=max(float(A[i,j].rad()) for i in range(N) for j in range(N));out={'schema':'marici.voevodsky.two-prime-full-rank80-ldl-arb.v1','L':'0.55','dimension':80,'maximum_assembled_entry_radius':maxrad,'parity_ldl':results,'dependencies':[{'file':n,'sha256':hashlib.sha256((root/n).read_bytes()).hexdigest()} for n in names],'passed':allok,'rh_proved':False}
p=root/'two_prime_full_rank80_ldl_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
