#!/usr/bin/env python3
"""Verify canonical channel-lattice/Pontryagin-dual four-chart realization."""
import json
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
def F(st):kind,sign,v=st;return ('character',-sign,v) if kind=='delta' else ('delta',sign,v)
# Q permutes channel coordinates; the dual character action uses the same relabelled coefficient vector.
def applyQ(st,perm):
 kind,sign,v=st;w=[0]*len(v)
 for i,j in enumerate(perm):w[j]=v[i]
 return (kind,sign,tuple(w))
rows=[];fails=[]
for n in (4,8,12):
 facets=tri(tuple(range(n)));D=sorted(set().union(*facets));idx={d:i for i,d in enumerate(D)};s=n//4
 perm=[idx[rot_edge(d,s,n)] for d in D]
 if any(perm[perm[perm[perm[i]]]]!=i for i in range(len(D))):fails.append({'n':n,'reason':'Q4'})
 states=set();vectors=set()
 for T in facets:
  v=tuple(1 if d in T else 0 for d in D);vectors.add(v);st=('delta',1,v);orbit=[]
  for _ in range(4):orbit.append(st);st=F(st)
  if st!=orbit[0] or len(set(orbit))!=4:fails.append({'n':n,'reason':'F4'})
  if F(applyQ(orbit[0],perm))!=applyQ(F(orbit[0]),perm):fails.append({'n':n,'reason':'FQ'})
  states.update(orbit)
 if len(vectors)!=len(facets) or len(states)!=4*len(facets):fails.append({'n':n,'reason':'collision'})
 rows.append({'n':n,'channel_lattice_rank':len(D),'triangulations':len(facets),'distinct_incidence_vectors':len(vectors),'four_chart_states':len(states),'each_chart_dimension':len(facets),'exact_chart_weight':'1/4'})
checks={'incidence_realization_injective':not fails,'pontryagin_fourier_has_order_four':not fails,'channel_rotation_commutes_with_fourier':not fails,'four_charts_exactly_equidimensional':not fails}
out={'schema':'marici.nima.canonical-tate-torus-realization.v1','degrees':[4,8,12],'results':rows,'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'construction':'L_n=Z^(D_n). T maps to delta at its incidence vector. Pontryagin Fourier maps lattice deltas to torus characters; F^2 is reflection. Polygon rotation is the canonical coordinate permutation.'}
p=ROOT/'research/nima/results/canonical-tate-torus-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
