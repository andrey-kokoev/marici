#!/usr/bin/env python3
"""Dependency-free exact minors for radial plus five scalar-image columns."""
import json
from pathlib import Path
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=r.get(k,0)+v
 return {k:v for k,v in r.items() if v}
def sc(a,c):return {k:c*v for k,v in a.items() if c*v}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=r.get((i+k,j+l),0)+u*v
 return r
def der(a,z):return {((i-1,j) if z==0 else (i,j-1)):v*(i if z==0 else j) for (i,j),v in a.items() if (i if z==0 else j)}
def det(A):
 A=[r[:] for r in A];n=len(A);sg=1;prev=1
 for k in range(n-1):
  q=next((i for i in range(k,n) if A[i][k]),None)
  if q is None:return 0
  if q!=k:A[k],A[q]=A[q],A[k];sg=-sg
  p=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):A[i][j]=(A[i][j]*p-A[i][k]*A[k][j])//prev
  prev=p
 return sg*A[-1][-1]
X={(1,0):1};Y={(0,1):1};H={(2,0):3,(0,2):-6};Q=mul(mul(mul(X,X),mul(Y,Y)),add(X,Y))
def T(fx,fy):
 div=add(der(fx,0),der(fy,1));bx=add(mul(H,der(Q,0)),sc(mul(Q,der(H,0)),3));by=add(mul(H,der(Q,1)),sc(mul(Q,der(H,1)),3));return mul(H,add(mul(mul(H,Q),div),sc(mul(fx,bx),-1),sc(mul(fy,by),-1)))
def mono(i,j):return {(i,j):1}
def smallfac(v):
 r={};v=abs(v)
 for p in range(2,101):
  if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
  while v%p==0:r[str(p)]=r.get(str(p),0)+1;v//=p
 return {'small_prime_factors':r,'residual':str(v)}
rows=[]
for n in range(10,31):
 cs=[]
 for i in range(n):
  g=mono(i,n-1-i);cs.append(T(mul(X,g),mul(Y,g)))
 for i in range(4):cs.append(T(mono(i,n-i),{}))
 cs.append(T({},mono(n,0)));exps=range(1,n+6);A=[[c.get((i,n+8-i),0) for c in cs] for i in exps];d=det(A);z=None if n==10 else d//((n-10)**n);rows.append({'n':n,'D':n+8,'minor':str(d),'normalized_by_radial':None if z is None else str(z),'normalized_factorization':None if z is None else smallfac(z),'closed_form_matches':d==((-1)**n)*(2**(n+12))*(3**(2*n+12))*((n-10)**n)})
out={'schema':'marici.benincasa.cosmology-rees-five-column-determinant.v1','selected_output_x_powers':'1 through n+5','rows':rows};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_five_column_determinant.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(rows,indent=2))
