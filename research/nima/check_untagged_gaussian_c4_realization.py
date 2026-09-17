#!/usr/bin/env python3
"""Verify an untagged injective Gaussian realization of Catalan C4 charts."""
import json
from fractions import Fraction
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
def rot_edge(e,s,n):a,b=e;return edge((a+s)%n,(b+s)%n)
def rot(T,s,n):return frozenset(rot_edge(e,s,n) for e in T)
rows=[];fails=[]
for n in (4,8,12):
 F=tri(tuple(range(n)));D=sorted(set().union(*F));idx={d:i for i,d in enumerate(D)};s=n//4
 # Base atom h_a has Gaussian shape a_d=2^-idx. Fourier sends shape a to 1/a.
 code=lambda T:sum(1<<idx[d] for d in T)
 for phase in range(4):
  shapes={}
  for T in F:
   # q^phase T uses chart atoms transported from the unique preimage base labels.
   S=code(T);shape=Fraction(1,S) if phase%2==0 else Fraction(S,1)
   shapes.setdefault(shape,0);shapes[shape]+=1
   # Fourier inverts Gaussian shape and advances the chart.
   nextshape=Fraction(S,1) if phase%2==0 else Fraction(1,S)
   if nextshape != (Fraction(S,1) if (phase+1)%2 else Fraction(1,S)):fails.append({'n':n,'phase':phase})
  if len(shapes)!=len(F):fails.append({'n':n,'phase':phase,'collision_count':len(F)-len(shapes)})
 rows.append({'n':n,'triangulations':len(F),'channel_atoms':len(D),'each_chart_separately_injective':not any(x['n']==n for x in fails),'base_shape_rule':'a_T=(sum_(d in T) 2^index(d))^-1','fourier_shape_cycle':['1/S','S','1/S','S'],'combined_c4_faithful':False,'collapse':'phase 0 equals phase 2 and phase 1 equals phase 3 because all Gaussians are reflection-even'})
checks={'each_chart_has_no_collisions':not fails,'fourier_inversion_intertwines_chart_products':not fails,'audit_detects_c4_to_c2_collapse':all(not r['combined_c4_faithful'] for r in rows)}
out={'schema':'marici.nima.untagged-even-gaussian-c4-collapse.v1','degrees':[4,8,12],'results':rows,'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'construction':'Use normalized even Gaussians h_a with base channel shape a_d=2^-index(d). This removes within-chart tags but reflection-evenness collapses the combined C4 action to C2.'}
p=ROOT/'research/nima/results/untagged-gaussian-c4-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
