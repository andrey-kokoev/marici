#!/usr/bin/env python3
"""Modular search for an order-two cokernel representative detecting the order-three target."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def M(f,z,kp,n):
 p=2-kp;c=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),c))
 return add(mul(R,L),sc(mul(mul(Kp,Q),mul(f,der(R,z))),-n))
def rank(rows,p):
 basis={}
 for src in rows:
  row={j:(v.numerator*pow(v.denominator,-1,p))%p for j,v in src.items() if v};row={j:v for j,v in row.items() if v}
  while row:
   q=min(row)
   if q not in basis:
    iv=pow(row[q],-1,p);basis[q]={j:v*iv%p for j,v in row.items()};break
   v=row[q]
   for j,x in basis[q].items():
    y=(row.get(j,0)-v*x)%p
    if y:row[j]=y
    elif j in row:del row[j]
 return len(basis)
cols=[]
for kp,maxd in ((1,19),(0,15)):
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(M({(i,d-i):F(1)},z,kp,2))
t3=mul(target,pw(R,3));t4=mul(target,pw(R,4));mons=sorted(set(t3)|set(t4)|{m for c in cols for m in c},key=lambda x:(sum(x),x[0]));idx={m:i for i,m in enumerate(mons)};rows=[{} for _ in mons]
for j,c in enumerate(cols):
 for m,v in c.items():rows[idx[m]][j]=v
def augmented(t):
 out=[]
 for r,m in zip(rows,mons):
  a=dict(r);v=t.get(m,F(0))
  if v:a[len(cols)]=v
  out.append(a)
 return out
p=1000003;r=rank(rows,p);r3=rank(augmented(t3),p);r4=rank(augmented(t4),p);out={'schema':'marici.benincasa.cosmology-rees-affine-order2-representative-search.v1','prime':p,'columns':len(cols),'equations':len(mons),'matrix_rank':r,'target_R3_augmented_rank':r3,'target_R4_augmented_rank':r4,'disposition':'modular existence signal for a transportable representative' if r4>r else 'modular obstruction signal: target R4 lies in the order-two image modulo p','rational_consequence':'none without exact lift or exact image solution'};(HERE.parents[1]/'results'/'cosmology_rees_affine_order2_representative_search.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
