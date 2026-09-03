#!/usr/bin/env python3
"""Solve all scalar normal orders jointly at the natural derivative degree bounds."""
import json
from fractions import Fraction as F
from pathlib import Path
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def sc(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+u*v
 return {k:v for k,v in r.items() if v}
def der(p,z):return {((i-1,j) if z==0 else (i,j-1)):v*(i if z==0 else j) for (i,j),v in p.items() if (i if z==0 else j)}
X={(1,0):F(1)};s={(0,1):F(1)}
def pd(fs):
 r={(0,0):F(1)}
 for p in fs:r=mul(r,p)
 return r
R=pd([X,add(X,s),add(X,{(0,0):F(-6)})]);Q=mul(mul(s,s),R);H=add(sc(mul(X,X),3),sc(mul(s,s),-6),sc(s,-36));K=mul(H,H)
def L1(f,z):return add(mul(Q,der(f,z)),sc(mul(der(Q,z),f),-1))
def L0(f,z):return add(mul(K,L1(f,z)),sc(mul(mul(Q,der(K,z)),f),F(-1,2)))
cols=[];labels=[]
for block,maxd,op in [('boundary',5,L1),('lower',1,L0)]:
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(op({(i,d-i):F(1)},z));labels.append((block,z,i,d-i))
target=sc(mul(K,Q),3);mons=sorted(set(target)|{k for c in cols for k in c},key=lambda q:(sum(q),q[0]));n=len(cols)
rows=[[c.get(m,F(0)) for c in cols]+[target.get(m,F(0))] for m in mons];pr=0;piv=[]
for j in range(n):
 q=next((i for i in range(pr,len(rows)) if rows[i][j]),None)
 if q is None:continue
 rows[pr],rows[q]=rows[q],rows[pr];v=rows[pr][j];rows[pr]=[x/v for x in rows[pr]]
 for i in range(len(rows)):
  if i!=pr and rows[i][j]:
   v=rows[i][j];rows[i]=[a-v*b for a,b in zip(rows[i],rows[pr])]
 piv.append(j);pr+=1
inconsistent=any(all(not x for x in r[:-1]) and r[-1] for r in rows);sol=[F(0)]*n
if not inconsistent:
 for i,j in enumerate(piv):sol[j]=rows[i][-1]
 residual=add(target,*[sc(c,-x) for c,x in zip(cols,sol) if x]);assert not residual
nz=[{'label':repr(labels[i]),'coefficient':str(x)} for i,x in enumerate(sol) if x]
out={'schema':'marici.benincasa.cosmology-rees-scalar-joint-tail-solve.v1','boundary_degree_max':5,'lower_degree_max':1,'unknown_count':n,'equation_count':len(mons),'matrix_rank':len(piv),'consistent':not inconsistent,'nonzero_solution_count':len(nz),'solution':nz,'exact_residual_zero':not inconsistent,'governing_dpc_disposition':'scalarized tau has an exact polynomial preimage at the natural degree bounds' if not inconsistent else 'joint tail solve is inconsistent at natural bounds'};Rout=Path(__file__).resolve().parents[1]/'results';(Rout/'cosmology_rees_scalar_joint_tail_solve.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
