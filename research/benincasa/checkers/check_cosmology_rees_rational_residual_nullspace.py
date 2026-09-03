#!/usr/bin/env python3
"""Direct rational D=26 corrected symbol quotient."""
import json,sys
from fractions import Fraction as F
from pathlib import Path
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def sc(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+u*v
 return {k:v for k,v in r.items() if v}
def pw(a,n):
 r={(0,0):F(1)}
 for _ in range(n):r=mul(r,a)
 return r
def der(a,z):return {((i-1,j) if z==0 else (i,j-1)):v*(i if z==0 else j) for (i,j),v in a.items() if (i if z==0 else j)}
X={(1,0):F(1)};Y={(0,1):F(1)};H={(2,0):F(3),(0,2):F(-6)};Q=mul(mul(pw(X,2),pw(Y,2)),add(X,Y));D=int(sys.argv[1]) if len(sys.argv)>1 else 26
def Bop(f,z):return add(mul(Q,der(f,z)),sc(mul(der(Q,z),f),-1))
def Lop(f,z,k):return add(mul(pw(H,4 if k==0 else 2),Bop(f,z)),sc(mul(mul(pw(H,3 if k==0 else 1),Q),mul(der(H,z),f)),-1 if k==0 else -3))
labels=[];cols=[]
for k,n in [(0,D-12),(1,D-8)]:
 for z in (0,1):
  for i in range(n+1):labels.append((k,z,i,n-i));cols.append(Lop({(i,n-i):F(1)},z,k))
A=[[cols[j].get((i,D-i),F(0)) for j in range(len(cols))] for i in range(D+1)];r=0;piv=[]
for c in range(len(cols)):
 q=next((i for i in range(r,len(A)) if A[i][c]),None)
 if q is None:continue
 A[r],A[q]=A[q],A[r];p=A[r][c];A[r]=[x/p for x in A[r]]
 for i in range(len(A)):
  if i!=r and A[i][c]:z=A[i][c];A[i]=[x-z*y for x,y in zip(A[i],A[r])]
 piv.append(c);r+=1
free=[c for c in range(len(cols)) if c not in piv];null=[]
for f in free:
 v={f:F(1)}
 for i,p in enumerate(piv):
  if A[i][f]:v[p]=-A[i][f]
 null.append(v)
idx={x:i for i,x in enumerate(labels)}
def vec(parts):
 r={}
 for k,z,p,c in parts:
  for (i,j),v in p.items():r[idx[(k,z,i,j)]]=r.get(idx[(k,z,i,j)],F(0))+c*v
 return {i:v for i,v in r.items() if v}
known=[]
for z in (0,1):
 for i in range(D-13):f={(i,D-14-i):F(1)};known.append(vec([(0,z,mul(H,f),1),(1,z,mul(pw(H,3),f),-1)]))
for k,hp in [(0,1),(1,3)]:
 for i in range(D-17):
  psi={(i,D-18-i):F(1)};known.append(vec([(k,0,mul(pw(H,hp),mul(Q,der(psi,1))),1),(k,1,mul(pw(H,hp),mul(Q,der(psi,0))),-1)]))
def ins(B,v):
 while v:
  p=min(v);x=v[p]
  if p not in B:B[p]={k:a/x for k,a in v.items()};return 1
  for k,a in B[p].items():v[k]=v.get(k,F(0))-x*a
  v={k:a for k,a in v.items() if a}
 return 0
EB={};kr=sum(ins(EB,dict(v)) for v in known);res=[]
for v in null:
 if ins(EB,dict(v)):res.append(v)
def fs(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
out={'schema':'marici.benincasa.cosmology-rees-rational-residual-nullspace.v1','D':D,'symbol_rank':len(piv),'nullity':len(null),'known_rank':kr,'residual_count':len(res),'representatives':[[{'input':list(labels[i]),'coefficient':fs(c)} for i,c in sorted(v.items())] for v in res]};R=Path(__file__).resolve().parents[1]/'results';(R/f'cosmology_rees_rational_residual_nullspace_D{D}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['symbol_rank','nullity','known_rank','residual_count']},indent=2))
