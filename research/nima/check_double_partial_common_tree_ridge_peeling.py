#!/usr/bin/env python3
"""Boundary-ridge peeling census for double-partial common-tree complexes."""
import itertools,json,math
from collections import Counter
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
def peel(facets):
 remaining=set(facets);steps=[]
 while len(remaining)>1:
  incidence=Counter()
  for F in remaining:
   for r in itertools.combinations(F,len(F)-1):incidence[frozenset(r)]+=1
  candidates=[]
  for F in remaining:
   free=[frozenset(r) for r in itertools.combinations(F,len(F)-1) if incidence[frozenset(r)]==1]
   if free:candidates.append((len(free),tuple(sorted((len(q),tuple(sorted(q))) for q in F)),F,free[0]))
  if not candidates:return None
  _,_,F,ridge=max(candidates);remaining.remove(F);steps.append((F,ridge))
 return steps
rows=[];fail=[];closed=[];total=0
for n in range(4,9):
 alpha=tuple(range(1,n+1));A=trees(alpha);empty=peeled=closed_n=0
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  total+=1;F=A&trees(beta)
  if not F:empty+=1;continue
  result=peel(F)
  if result is not None:peeled+=1
  else:
   # The full closed associahedral complex is expected to have no free ridge.
   ridges=Counter(frozenset(r) for facet in F for r in itertools.combinations(facet,len(facet)-1))
   if all(v==2 for v in ridges.values()):closed_n+=1;closed.append({'n':n,'beta':list(beta),'facets':len(F)})
   else:fail.append({'n':n,'beta':list(beta),'facets':len(F)})
 rows.append({'n':n,'order_orbits':math.factorial(n-1)//2,'empty':empty,'ridge_peeled_to_one_facet':peeled,'closed_no_free_ridge':closed_n,'failures':sum(q['n']==n for q in fail)})
checks={'all_2955_orbits_checked':total==2955,'all_proper_nonempty_complexes_peel':not fail,'exactly_one_closed_complex_per_n':all(sum(q['n']==n for q in closed)==1 for n in range(4,9))}
out={'schema':'marici.nima.double-partial-common-tree-ridge-peeling.v1','range':[4,8],'results':rows,'closed_examples':closed,'failures':fail,'checks':checks,'passed':all(checks.values()),'scope':'Greedy deletion of a maximal facet having a free codimension-one face until one facet remains. This is a strong ball diagnostic but is not, by itself, a full elementary-collapse or PL-ball proof.'}
p=ROOT/'research/nima/results/double-partial-common-tree-ridge-peeling.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'failure_count':len(fail)},indent=2));raise SystemExit(0 if out['passed'] else 1)
