#!/usr/bin/env python3
"""No-go for nonconstant CR maps to targets concentrated in degree zero."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
def row(m):
 n=m+3;boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
 ds=[(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in boundary]
 def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
 cs=sorted(tuple(sorted(c)) for c in combinations(ds,m) if all(not cross(a,b) for a,b in combinations(c,2)))
 adj=[set() for _ in cs];edges=0
 for i,a in enumerate(cs):
  for j,b in enumerate(cs[i+1:],i+1):
   if len(set(a)^set(b))==2:adj[i].add(j);adj[j].add(i);edges+=1
 seen={0};stack=[0]
 while stack:
  i=stack.pop()
  for j in adj[i]-seen:seen.add(j);stack.append(j)
 return {'m':m,'clusters':len(cs),'mutation_edges':edges,'connected_vertices':len(seen),'connected':len(seen)==len(cs),'degree_zero_cocycle_dimension':1 if len(seen)==len(cs) else None}
rows=[row(m) for m in range(1,7)]
checks={'flip_graph_connected_A1_through_A6':all(r['connected'] for r in rows),'only_constant_zero_cocycles':all(r['degree_zero_cocycle_dimension']==1 for r in rows)}
out={'schema':'marici.nima.radiative-generator-map-no-go.v1','chain_map_equation':'F0 d_CR = d_rad F1','degree_zero_target_specialization':'If the radiative target is concentrated in degree zero, d_rad=0 and therefore F0 d_CR=0.','theorem':'The type-A mutation graph is connected, so every degree-zero cocycle F0 is constant on cluster generators. A nonconstant cluster-dependent assignment cannot descend to gauge-invariant radiative observables without nonzero higher target degrees.','rows':rows,'minimal_nontrivial_target':['R0: declared radiative records or charges','R1: gauge/flux/interpolation generators','d_rad:R1->R0','F1 on mutation edges satisfying d_rad F1=F0 d_CR'],'checks':checks,'passed':all(checks.values()),'claim_boundary':'This excludes nonconstant maps to a target with zero differential. It does not exclude a radiative chain map after the target complex and its nonzero differential are source-defined.'};p=ROOT/'research/nima/results/radiative-generator-map-no-go.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
