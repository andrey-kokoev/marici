#!/usr/bin/env python3
"""Directly certify simultaneous non-cut selection through n=7."""
import itertools,json
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
def trees(o):
 U=set(o);return {frozenset(canon(set(o[i:j]),U) for i,j in t) for t in tri(len(o))}
def key(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def connected(V):
 if len(V)<2:return True
 unseen=set(V);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a^b)==2]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
def selected(rem):
 inc=Counter(frozenset(r) for q in rem for r in itertools.combinations(q,len(q)-1));cand=[]
 for q in rem:
  free=sum(inc[frozenset(r)]==1 for r in itertools.combinations(q,len(q)-1))
  if free:cand.append((free,key(q),q))
 return max(cand)[2] if cand else None
def faces(F):
 q=list(F);return [frozenset(s) for r in range(len(q)+1) for s in itertools.combinations(q,r)]
selections=star_tests=0;fail=[]
for n in range(4,8):
 alpha=tuple(range(1,n+1));A=trees(alpha)
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  rem=A&trees(beta)
  while len(rem)>1:
   F=selected(rem)
   if F is None:break # unique closed associahedral case
   selections+=1
   for Q in faces(F):
    star={G for G in rem if Q<=G}
    if len(star)>1:
     star_tests+=1
     if not connected(star-{F}):fail.append({'n':n,'beta':list(beta),'remaining':len(rem),'face_size':len(Q),'star_size':len(star)})
   rem=set(rem);rem.remove(F)
checks={'nonvacuous':selections>0 and star_tests>0,'every_selected_facet_simultaneously_noncut':not fail}
out={'schema':'marici.nima.selected-facet-simultaneous-noncut.v1','range':[4,7],'selected_facets_checked':selections,'face_star_noncut_tests':star_tests,'failures':fail[:20],'checks':checks,'passed':all(checks.values()),'scope':'Direct exhaustive certification of the exact pointwise lemma through n=7; not an arbitrary-n proof.'}
p=ROOT/'research/nima/results/selected-facet-simultaneous-noncut.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'selections':selections,'star_tests':star_tests,'failures':len(fail)},indent=2));raise SystemExit(0 if out['passed'] else 1)
