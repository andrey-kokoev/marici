#!/usr/bin/env python3
"""Dependency-free modular augmented-rank preflight for common denominator H^3Q^3."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_affine_localized_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=h['H'],h['Q'],h['K'],h['target'],h['B']
def Lnum(f,z,kp,D):
 p=2-kp;c=F(-1,2)-kp;one={(0,0):F(1)};Kp=K if p==1 else mul(K,K);Km=one if p==1 else K
 return add(mul(Kp,add(mul(D,B(f,z)),sc(mul(mul(Q,f),der(D,z)),-1))),sc(mul(mul(mul(Km,Q),mul(der(K,z),f)),D),c))
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
H3=mul(mul(H,H),H);Q3=mul(mul(Q,Q),Q);D=mul(H3,Q3);cols=[]
for kp,maxd in ((1,26),(0,22)):
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
p=1000003;r=rank(rows,p);ra=rank(aug,p);out={'schema':'marici.benincasa.cosmology-rees-affine-H3Q3-modular-preflight.v1','denominator':'H^3Q^3','numerator_caps':[26,22],'unknowns':len(cols),'equations':len(mons),'prime':p,'matrix_rank':r,'augmented_rank':ra,'consistent_mod_prime':r==ra,'rational_consequence':'none without exact certificate lift'};(HERE.parents[1]/'results'/'cosmology_rees_affine_H3Q3_modular_preflight.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
