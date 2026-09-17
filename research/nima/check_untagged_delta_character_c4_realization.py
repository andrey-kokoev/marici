#!/usr/bin/env python3
"""Exact untagged C4 realization using delta/character Fourier orbits."""
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
def F(state):
 kind,sign,S=state
 return ('character',-sign,S) if kind=='delta' else ('delta',sign,S)
def state(T,phase,idx):
 S=sum(1<<idx[d] for d in T);cycle=[('delta',1,S),('character',-1,S),('delta',-1,S),('character',1,S)]
 return cycle[phase%4]
rows=[];fails=[]
for n in (4,8,12):
 facets=tri(tuple(range(n)));D=sorted(set().union(*facets));idx={d:i for i,d in enumerate(D)}
 allstates=set()
 for T in facets:
  orbit=[state(T,p,idx) for p in range(4)]
  if len(set(orbit))!=4:fails.append({'n':n,'reason':'short orbit'})
  if any(F(orbit[p])!=orbit[(p+1)%4] for p in range(4)):fails.append({'n':n,'reason':'Fourier mismatch'})
  allstates.update(orbit)
 if len(allstates)!=4*len(facets):fails.append({'n':n,'reason':'cross-facet collision','states':len(allstates)})
 rows.append({'n':n,'triangulations':len(facets),'channel_atoms':len(D),'distinct_analytic_states':len(allstates),'expected_states':4*len(facets),'full_c4_orbits':len(facets)})
checks={'no_tags_and_no_collisions':not fails,'physical_fourier_cycle_closes':not fails,'all_orbits_have_length_four':not fails}
out={'schema':'marici.nima.untagged-delta-character-c4-realization.v1','degrees':[4,8,12],'results':rows,'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'construction':'Channel d maps to delta at x_d=2^index(d). Convolution adds supports. Fourier alternates delta_{S}, character_{-S}, delta_{-S}, character_{S}. Binary subset sums separate triangulations.'}
p=ROOT/'research/nima/results/untagged-delta-character-c4-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
