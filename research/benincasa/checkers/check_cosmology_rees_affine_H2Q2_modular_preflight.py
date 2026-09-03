#!/usr/bin/env python3
"""Sparse modular augmented-rank preflight for the common H^2 Q^2 denominator."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve(); base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()): h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p-1==0 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
def mrank(rows,p,n):
 basis={}
 for src in rows:
  row={j:(v.numerator*pow(v.denominator,-1,p))%p for j,v in src.items() if v}
  row={j:v for j,v in row.items() if v}
  while row:
   q=min(row)
   if q not in basis:
    iv=pow(row[q],-1,p);basis[q]={j:(v*iv)%p for j,v in row.items()};break
   v=row[q];b=basis[q]
   for j,x in b.items():
    y=(row.get(j,0)-v*x)%p
    if y:row[j]=y
    elif j in row:del row[j]
 return len(basis)
D=mul(mul(H,H),mul(Q,Q));cols=[]
for kp,maxd in ((1,19),(0,15)):
 for z in (0,1):
  for d in range(maxd+1):
   for i in range(d+1):cols.append(Lnum({(i,d-i):F(1)},z,kp,D))
tgt=mul(target,mul(D,D));mons=sorted(set(tgt)|{m for c in cols for m in c},key=lambda x:(sum(x),x[0]));idx={m:i for i,m in enumerate(mons)};rows=[{} for _ in mons]
for j,c in enumerate(cols):
 for m,v in c.items():rows[idx[m]][j]=v
aug=[]
for r,m in zip(rows,mons):
 a=dict(r);v=tgt.get(m,F(0))
 if v:a[len(cols)]=v
 aug.append(a)
checks=[]
for p in (1000003,1000033,1000037):
 r=mrank(rows,p,len(cols));ra=mrank(aug,p,len(cols)+1);checks.append({'prime':p,'matrix_rank':r,'augmented_rank':ra,'consistent_mod_prime':r==ra})
out={'schema':'marici.benincasa.cosmology-rees-affine-H2Q2-modular-preflight.v1','denominator':'H^2Q^2','numerator_caps':[19,15],'unknowns':len(cols),'equations':len(mons),'checks':checks,'rational_consequence':'none without proving rank preservation or lifting a left-null certificate; the repeated modular gap is a preflight signal only'};path=HERE.parents[1]/'results'/'cosmology_rees_affine_H2Q2_modular_preflight.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
