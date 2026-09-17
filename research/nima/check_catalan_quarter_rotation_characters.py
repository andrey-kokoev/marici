#!/usr/bin/env python3
"""Character traces of quarter-polygon rotation on Catalan triangulation modules."""
import json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def tri(v):
 if len(v)<=3:return (frozenset(),)
 out=set();a,z=v[0],v[-1]
 for k in range(1,len(v)-1):
  b=v[k];L=tri(v[:k+1]) if k+1>=3 else (frozenset(),);R=tri(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
  if k>1:add.add(edge(a,b))
  if k<len(v)-2:add.add(edge(b,z))
  for l in L:
   for r in R:out.add(frozenset(set(l)|set(r)|add))
 return tuple(out)
def rotate(T,s,n):return frozenset(edge((a+s)%n,(b+s)%n) for a,b in T)
rows=[]
for n in (4,8,12):
 F=tri(tuple(range(n)));d=len(F);s=n//4;fixed=[]
 for k in range(4):fixed.append(sum(rotate(T,k*s,n)==T for T in F))
 f0,f1,f2,f3=fixed;assert f1==f3
 assert f1==0 and f2==math.comb(n-2,(n-2)//2)
 mult=[(d+2*f1+f2)//4,(d-f2)//4,(d-2*f1+f2)//4,(d-f2)//4]
 assert sum(mult)==d and all(x>=0 for x in mult)
 rows.append({'n':n,'catalan_dimension':d,'fixed_traces_q0_q1_q2_q3':fixed,'character_multiplicities':mult,'normalized_multiplicities':[x/d for x in mult],'max_distance_from_quarter':max(abs(x/d-.25) for x in mult),'normalized_nontrivial_traces':[f1/d,f2/d,f3/d]})
checks={'all_character_multiplicities_integral':all(sum(r['character_multiplicities'])==r['catalan_dimension'] for r in rows),'nontrivial_normalized_traces_decrease':all(rows[i+1]['normalized_nontrivial_traces'][0]<=rows[i]['normalized_nontrivial_traces'][0] and rows[i+1]['normalized_nontrivial_traces'][1]<rows[i]['normalized_nontrivial_traces'][1] for i in range(len(rows)-1)),'character_weights_approach_quarter':rows[-1]['max_distance_from_quarter']<.004}
out={'schema':'marici.nima.catalan-quarter-rotation-characters.v1','degrees':[4,8,12],'action':'Rotate polygon labels by n/4; this gives q^4=1 on the triangulation module.','results':rows,'checks':checks,'passed':all(checks.values()),'scope':'Tests the natural polygon quarter-rotation model. Identification with the analytic four-chart operator remains the intertwining problem.'}
p=ROOT/'research/nima/results/catalan-quarter-rotation-characters.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
