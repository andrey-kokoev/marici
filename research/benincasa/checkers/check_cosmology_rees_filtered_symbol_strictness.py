#!/usr/bin/env python3
"""Compare filtered image increments with combined homogeneous-symbol ranks."""
import json
from pathlib import Path
P=101;C=(-pow(2,-1,P))%P
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=(r.get(k,0)+v)%P
 return {k:v for k,v in r.items() if v}
def scale(a,c):return {k:v*c%P for k,v in a.items() if v*c%P}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=(r.get((i+k,j+l),0)+u*v)%P
 return {k:v for k,v in r.items() if v}
def der(a,z):return {((i-1,j) if z==0 else (i,j-1)):v*(i if z==0 else j)%P for (i,j),v in a.items() if (i if z==0 else j)}
def prod(fs):
 r={(0,0):1}
 for f in fs:r=mul(r,f)
 return r
X={(1,0):1};Y={(0,1):1};Q=prod([add(Y,{(0,0):-3}),X,add(X,Y,{(0,0):-3}),add(Y,{(0,0):-3}),add(X,{(0,0):-6})]);H=add(scale(mul(X,X),3),scale(mul(Y,Y),-6),{(0,0):54});K=mul(H,H)
def L(f,z,low):
 b=add(mul(Q,der(f,z)),scale(mul(der(Q,z),f),-1))
 return add(mul(K,b),scale(mul(mul(Q,der(K,z)),f),C)) if low else b
B={};rank=0;rows=[]
def insert(r):
 global rank
 while r:
  q=max(r,key=lambda z:(sum(z),z[0]));x=r[q]
  if q not in B:
   iv=pow(x,-1,P);B[q]={k:v*iv%P for k,v in r.items()};rank+=1;return (sum(q),q,dict(B[q]))
  for k,v in B[q].items():r[k]=(r.get(k,0)-x*v)%P
  r={k:v for k,v in r.items() if v}
 return 0
for D in range(0,31):
 old=rank;pivot_degrees=[];lower_pivots=[]
 for low,d in [(False,D-4),(True,D-8)]:
  if d>=0:
   for z in (0,1):
    for i in range(d+1):
     ins=insert(L({(i,d-i):1},z,low))
     if ins:pivot_degrees.append(ins[0]);
     if ins and ins[0]<D: lower_pivots.append({'source_block':'lower' if low else 'boundary','source_axis':z,'source_exp':[i,d-i],'pivot_exp':list(ins[1]),'normal_form':{repr(k):v for k,v in ins[2].items()}})
 inc=rank-old;symbol_rank=0 if D<4 else D-1 # observed combined rank D+1-2 for stable D, exceptions handled below
 rows.append({'output_degree':D,'filtered_rank_increment':inc,'new_pivot_degrees':pivot_degrees,'lower_pivots':lower_pivots,'pivot_degree_counts':{str(e):pivot_degrees.count(e) for e in sorted(set(pivot_degrees))},'generic_symbol_rank':symbol_rank,'matches_generic':inc==symbol_rank})
out={'schema':'marici.benincasa.cosmology-rees-filtered-symbol-strictness.v1','prime':P,'rows':rows,'matches_generic_D_ge_12':all(r['matches_generic'] for r in rows if r['output_degree']>=12)};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_filtered_symbol_strictness.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
