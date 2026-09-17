#!/usr/bin/env python3
"""Exhaust all pure induced restrictions of common-interval complexes through n=6."""
exec(compile(open(__file__.replace('check_well_covered_common_interval_restrictions.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def compatible(a,b,U):
 return not (a&b and a&(U-b) and (U-a)&b and (U-a)&(U-b))
def maximal_independent(A,U):
 faces=[];L=list(A)
 for mask in range(1<<len(L)):
  f=frozenset(L[i] for i in range(len(L)) if mask>>i&1)
  if all(compatible(a,b,U) for a,b in itertools.combinations(f,2)):faces.append(f)
 return maximal(frozenset(faces))
def facet_connected(F):
 if len(F)<2:return True
 d=len(next(iter(F)));unseen=set(F);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a&b)==d-1]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
rows=[];counter=[];seen_complexes=set()
for n in range(4,8):
 U=set(range(1,n+1));alpha=tuple(range(1,n+1));allA=set().union(*trees(alpha));orders=restrictions=pure=good=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  orders+=1;common=set().union(*(trees(alpha)&trees(beta))) if trees(alpha)&trees(beta) else set()
  ck=tuple(sorted((len(q),tuple(sorted(q))) for q in common))
  if ck in seen_complexes:continue
  seen_complexes.add(ck)
  C=list(common)
  for mask in range(1,1<<len(C)):
   restrictions+=1;A={C[i] for i in range(len(C)) if mask>>i&1};F=maximal_independent(A,U);dims={len(f) for f in F}
   if len(dims)!=1 or not facet_connected(F):continue
   pure+=1
   if vd(F):good+=1
   else:
    counter.append({'n':n,'beta':list(beta),'allowed_channels':[sorted(q) for q in A],'facet_sizes':sorted(dims),'facets':[[sorted(q) for q in T] for T in F]});break
  if counter:break
 rows.append({'n':n,'order_orbits':orders,'induced_restrictions':restrictions,'pure_facet_connected_restrictions':pure,'vertex_decomposable':good})
 if counter:break
out={'schema':'marici.nima.well-covered-common-interval-restrictions.v1','range':[4,7],'results':rows,'counterexamples':counter[:5],'passed':not counter,'scope':'All nonempty channel subsets through n=7, restricted to pure facet-connected induced complexes.'}
p=ROOT/'research/nima/results/well-covered-common-interval-restrictions.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'first_counterexample':counter[:1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
