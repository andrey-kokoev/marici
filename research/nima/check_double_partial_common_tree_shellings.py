#!/usr/bin/env python3
"""Construct explicit shelling orders for double-partial common-tree complexes."""
import itertools,json,math
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def tri(n):
 @lru_cache(None)
 def rec(v):
  if len(v)<=3:return (frozenset(),)
  out=set();a,z=v[0],v[-1]
  for k in range(1,len(v)-1):
   b=v[k];L=rec(v[:k+1]) if k+1>=3 else (frozenset(),);R=rec(v[k:]) if len(v)-k>=3 else (frozenset(),);add=set()
   if k>1:add.add(edge(a,b))
   if k<len(v)-2:add.add(edge(b,z))
   for l in L:
    for r in R:out.add(frozenset(set(l)|set(r)|add))
  return tuple(out)
 return rec(tuple(range(n)))
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S);return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def trees(order):
 U=set(order);return {frozenset(canon(set(order[i:j]),U) for i,j in t) for t in tri(len(order))}
def fkey(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def admissible(F,prior):
 if not prior:return True
 ridge=len(F)-1;intersections=[F&G for G in prior]
 # Every intersection with an earlier facet must be contained in an earlier ridge intersection.
 ridges=[I for I in intersections if len(I)==ridge]
 return bool(ridges) and all(any(I<=R for R in ridges) for I in intersections)
def shelling(facets):
 if not facets:return []
 remaining=set(facets);order=[min(remaining,key=fkey)];remaining.remove(order[0])
 while remaining:
  candidates=[F for F in remaining if admissible(F,order)]
  if not candidates:return None
  # Prefer a facet sharing the most ridges with the current shell.
  F=min(candidates,key=lambda q:(-sum(len(q&G)==len(q)-1 for G in order),fkey(q)));order.append(F);remaining.remove(F)
 return order
rows=[];failed=[];total=0
for n in range(4,9):
 alpha=tuple(range(1,n+1));A=trees(alpha);shellable=empty=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1;continue
  order=shelling(F)
  if order is None:failed.append({'n':n,'beta':list(beta),'facets':len(F)})
  else:shellable+=1
 rows.append({'n':n,'order_orbits':math.factorial(n-1)//2,'empty':empty,'nonempty_shelling_certificates':shellable,'failed_nonempty':sum(q['n']==n for q in failed)})
checks={'all_2955_order_orbits_checked':total==2955,'every_nonempty_complex_has_constructed_shelling':not failed}
out={'schema':'marici.nima.double-partial-common-tree-shellings.v1','range':[4,8],'shelling_criterion':'Each new facet intersects the prior union in a nonempty pure codimension-one subcomplex, checked by containment in prior ridge intersections.','results':rows,'failures':failed,'checks':checks,'passed':all(checks.values()),'scope':'Constructive greedy shelling certificates for all tested order orbits; success is exact, but does not itself prove arbitrary-n shellability.'}
p=ROOT/'research/nima/results/double-partial-common-tree-shellings.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'failure_count':len(failed)},indent=2));raise SystemExit(0 if out['passed'] else 1)
