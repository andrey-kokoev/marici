#!/usr/bin/env python3
"""Rank logarithmic symbol towers modulo cross-level and stream families."""
import json
from pathlib import Path
P=101
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=(r.get(k,0)+v)%P
 return {k:v for k,v in r.items() if v}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=(r.get((i+k,j+l),0)+u*v)%P
 return {k:v for k,v in r.items() if v}
def pw(a,n):
 r={(0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
def comp(dst,p,c):
 for k,v in p.items():dst[(c,*k)]=v
H={(2,0):3,(0,2):-6};X={(1,0):1};Y={(0,1):1};L=add(X,Y);Q=mul(mul(pw(X,2),pw(Y,2)),L)
def ins(B,r):
 while r:
  q=min(r);x=r[q]
  if q not in B:
   z=pow(x,-1,P);B[q]={k:v*z%P for k,v in r.items()};return 1
  for k,v in B[q].items():r[k]=(r.get(k,0)-x*v)%P
  r={k:v for k,v in r.items() if v}
 return 0
rows=[]
for D in range(26,41):
 B={};d=D-14;pdeg=D-18
 # cross-level (H*f in kp0, -H^3*f in kp1), two vector components
 for c in (0,1):
  for i in range(d+1):
   f={(i,d-i):1};r={};comp(r,mul(H,f),c);comp(r,mul(pw(H,3),f),2+c)
   for k in list(r):
    if k[0]>=2:r[k]=-r[k]%P
   ins(B,r)
 # paired level stream kernels, independently at kp0 and kp1
 for level,hpow,off in [(0,1,0),(1,3,2)]:
  for i in range(pdeg+1):
   psi={(i,pdeg-i):1};gx={(i-1,pdeg-i):i%P} if i else {};gy={(i,pdeg-i-1):(pdeg-i)%P} if pdeg-i else {};r={};comp(r,mul(pw(H,hpow),mul(Q,gy)),off);comp(r,mul(pw(H,hpow),mul(Q,gx)),off+1)
   for k in list(r):
    if k[0]==off+1:r[k]=-r[k]%P
   ins(B,r)
 known=len(B);added=0
 # five homogeneous log towers per level: X r1/r2 tangent y; Y r1/r2 tangent x; L r1 tangent (1,-1)
 towers=[(X,1,1),(X,2,1),(Y,1,0),(Y,2,0),(L,1,0)]
 for hpow,off in [(1,0),(3,2)]:
  for l,rpow,c in towers:
   hd=d-(5-rpow);a=mul(mul({k:v for k,v in Q.items() if True},pw(l,hd)),{(0,0):1})
   # exact division for monomial factors; explicit Q/l^r
   if l is X:base=mul(pw(X,2-rpow),mul(pw(Y,2),L))
   elif l is Y:base=mul(pw(Y,2-rpow),mul(pw(X,2),L))
   else:base=mul(pw(X,2),pw(Y,2))
   a=mul(base,pw(l,hd));vec=mul(pw(H,hpow),a);rr={};comp(rr,vec,off+c)
   if l is L:
    comp(rr,vec,off+1);rr={k:(-v%P if k[0]==off+1 else v) for k,v in rr.items()}
   added+=ins(B,rr)
 rows.append({'D':D,'known_rank':known,'logarithmic_added_rank':added,'total_generated_rank':len(B)})
out={'schema':'marici.benincasa.cosmology-rees-logarithmic-Hilbert-rank.v1','prime':P,'rows':rows,'stable_added_ranks':sorted(set(r['logarithmic_added_rank'] for r in rows))};Rout=Path(__file__).resolve().parents[1]/'results';(Rout/'cosmology_rees_logarithmic_Hilbert_rank.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
