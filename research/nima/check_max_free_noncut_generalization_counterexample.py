#!/usr/bin/env python3
"""Counterexample: maximal free-ridge count alone does not imply simultaneous non-cut."""
import itertools,json
from collections import Counter
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
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
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S);return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def key(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def connected(V):
 if len(V)<2:return True
 unseen=set(V);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a^b)==2]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
def all_stars_connected(R):
 faces=set()
 for F in R:
  for r in range(len(F)+1):faces.update(frozenset(s) for s in itertools.combinations(F,r))
 return all(connected({F for F in R if Q<=F}) for Q in faces)
def select(R):
 inc=Counter(frozenset(r) for F in R for r in itertools.combinations(F,len(F)-1));cand=[]
 for F in R:
  free=sum(inc[frozenset(r)]==1 for r in itertools.combinations(F,len(F)-1))
  if free:cand.append((free,key(F),F))
 return max(cand)[2]
U=set(range(1,7));A=[frozenset(canon(set(range(1,7))[i:j],U) for i,j in t) for t in []] # overwritten below
order=tuple(range(1,7));A=[frozenset(canon(set(order[i:j]),U) for i,j in t) for t in rec(tuple(range(6)))]
witness=None
for mask in range(1,1<<len(A)):
 R={A[i] for i in range(len(A)) if mask>>i&1}
 if len(R)<3 or not all_stars_connected(R):continue
 F=select(R)
 for r in range(len(F)+1):
  for q in itertools.combinations(F,r):
   Q=frozenset(q);star={G for G in R if Q<=G}
   if len(star)>1 and not connected(star-{F}):witness=(R,F,Q,star);break
  if witness:break
 if witness:break
R,F,Q,star=witness
def enc(T):return [sorted(q) for q in sorted(T,key=lambda q:(len(q),tuple(sorted(q))))]
checks={'ambient_subset_has_all_face_stars_connected':all_stars_connected(R),'selected_max_free_facet_cuts_a_face_star':connected(star) and not connected(star-{F})}
out={'schema':'marici.nima.max-free-noncut-generalization-counterexample.v1','ambient':'an eight-facet subcomplex of the six-point associahedral triangulation complex','facets':[enc(T) for T in sorted(R,key=key)],'selected_facet':enc(F),'cut_face':enc(Q),'cut_star_facets':len(star),'checks':checks,'passed':all(checks.values()),'consequence':'Maximal free-ridge count plus hereditary star connectivity is insufficient in arbitrary associahedral subcomplexes. Any proof must use the special common-order restriction.'}
p=ROOT/'research/nima/results/max-free-noncut-generalization-counterexample.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'facets':len(R),'cut_face':enc(Q),'cut_star_facets':len(star)},indent=2));raise SystemExit(0 if out['passed'] else 1)
