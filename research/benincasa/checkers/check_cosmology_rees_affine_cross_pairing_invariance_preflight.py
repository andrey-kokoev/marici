#!/usr/bin/env python3
"""Modular image-membership preflight for the adjacent-target quotient relation at order four."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul,add,sc,der=h['mul'],h['add'],h['sc'],h['der'];H,Q,K,target,B=g['H'],h['Q'],h['K'],h['target'],h['B'];one={(0,0):F(1)};R=mul(H,Q);c=F(17,839808)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def M(f,z,kp):
 p=2-kp;cc=F(-1,2)-kp;Kp=K if p==1 else mul(K,K);Km=one if p==1 else K;L=add(mul(Kp,B(f,z)),sc(mul(mul(Km,Q),mul(der(K,z),f)),cc));T=mul(mul(Kp,Q),mul(f,der(R,z)));return add(mul(R,L),sc(T,-4))
def rank(rows,p):
 bs={}
 for src in rows:
  row={j:v.numerator*pow(v.denominator,-1,p)%p for j,v in src.items() if v};row={j:v for j,v in row.items() if v}
  while row:
   q=min(row)
   if q not in bs:
    iv=pow(row[q],-1,p);bs[q]={j:v*iv%p for j,v in row.items()};break
   v=row[q]
   for j,x in bs[q].items():
    y=(row.get(j,0)-v*x)%p
    if y:row[j]=y
    elif j in row:del row[j]
 return len(bs)
cols=[]
for kp,cap in ((1,33),(0,29)):
 for z in (0,1):
  for d in range(cap+1):
   for i in range(d+1):cols.append(M({(i,d-i):F(1)},z,kp))
u=mul(target,pw(R,4));v=mul(target,pw(R,5));q=add(u,sc(v,-c));mons=sorted(set(q)|{m for x in cols for m in x},key=lambda x:(sum(x),x[0]));ix={m:i for i,m in enumerate(mons)};rows=[{} for _ in mons]
for j,x in enumerate(cols):
 for m,a in x.items():rows[ix[m]][j]=a
aug=[]
for r,m in zip(rows,mons):
 a=dict(r);z=q.get(m,F(0))
 if z:a[len(cols)]=z
 aug.append(a)
p=1000003;r=rank(rows,p);ra=rank(aug,p);out={'schema':'marici.benincasa.cosmology-rees-affine-cross-pairing-invariance-preflight.v1','order':4,'coefficient':'17/839808','columns':len(cols),'equations':len(mons),'prime':p,'matrix_rank':r,'augmented_rank':ra,'relation_consistent_mod_prime':r==ra,'rational_consequence':'none without exact preimage lift or exact separating functional'};(HERE.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_invariance_preflight.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
