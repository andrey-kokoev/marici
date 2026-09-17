#!/usr/bin/env python3
"""Verify hereditary face-star connectivity along deterministic peel suffixes."""
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
def trees(order):
 U=set(order);return {frozenset(canon(set(order[i:j]),U) for i,j in t) for t in tri(len(order))}
def key(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def connected(fs):
 if len(fs)<2:return True
 unseen=set(fs);stack=[unseen.pop()]
 while stack:
  a=stack.pop();near=[b for b in unseen if len(a^b)==2]
  for b in near:unseen.remove(b);stack.append(b)
 return not unseen
def peel_states(F):
 rem=set(F);states=[set(rem)]
 while len(rem)>1:
  inc=Counter(frozenset(r) for q in rem for r in itertools.combinations(q,len(q)-1));cand=[]
  for q in rem:
   free=sum(inc[frozenset(r)]==1 for r in itertools.combinations(q,len(q)-1))
   if free:cand.append((free,key(q),q))
  if not cand:return None
  q=max(cand)[2];rem.remove(q);states.append(set(rem))
 return states
orbits=suffixes=stars=0;fail=[]
for n in range(4,8):
 alpha=tuple(range(1,n+1));A=trees(alpha)
 for tail in itertools.permutations(range(2,n+1)):
  beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
  if beta>rev:continue
  F=A&trees(beta);states=peel_states(F) if F else None
  if states is None:continue # closed associahedral sphere
  orbits+=1
  for si,state in enumerate(states):
   suffixes+=1;faces=set()
   for T in state:
    for r in range(len(T)+1):faces.update(frozenset(q) for q in itertools.combinations(T,r))
   for Q in faces:
    stars+=1;star={T for T in state if Q<=T}
    if not connected(star):fail.append({'n':n,'beta':list(beta),'suffix':si,'face_size':len(Q),'star_facets':len(star)})
checks={'all_tested_suffix_face_stars_connected':not fail,'nonvacuous':stars>0}
out={'schema':'marici.nima.peel-suffix-star-connectivity.v1','range':[4,7],'proper_nonempty_order_orbits':orbits,'peel_suffixes_checked':suffixes,'face_stars_checked':stars,'failures':fail[:20],'checks':checks,'passed':all(checks.values()),'scope':'Exact exhaustive invariant check through n=7; establishes the induction target but not its arbitrary-n preservation proof.'}
p=ROOT/'research/nima/results/peel-suffix-star-connectivity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'orbits':orbits,'suffixes':suffixes,'face_stars':stars,'failures':len(fail)},indent=2));raise SystemExit(0 if out['passed'] else 1)
