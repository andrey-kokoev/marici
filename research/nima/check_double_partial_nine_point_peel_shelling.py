#!/usr/bin/env python3
"""Uniform free-ridge peeling and reverse shelling for every n=9 common-tree complex."""
import itertools,json,math
from collections import Counter
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];N=9
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
def fkey(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def interval(S,b):
 bits=[x in S for x in b];return sum(bits[i]!=bits[(i+1)%N] for i in range(N))==2
def admissible(F,prior):
 if not prior:return True
 ints=[F&G for G in prior];ridges=[q for q in ints if len(q)==len(F)-1]
 return bool(ridges) and all(any(q<=r for r in ridges) for q in ints)
def peel(F):
 rem=set(F);removed=[]
 while len(rem)>1:
  inc=Counter(frozenset(r) for q in rem for r in itertools.combinations(q,len(q)-1));candidates=[]
  for q in rem:
   free=sum(inc[frozenset(r)]==1 for r in itertools.combinations(q,len(q)-1))
   if free:candidates.append((free,fkey(q),q))
  if not candidates:return None
  q=max(candidates);rem.remove(q[2]);removed.append(q[2])
 survivor=next(iter(rem));return [survivor]+list(reversed(removed))
alpha=tuple(range(1,N+1));U=set(alpha);A=[frozenset(canon(set(alpha[i:j]),U) for i,j in t) for t in rec(tuple(range(N)))];total=empty=certified=closed=0;fails=[]
for tail in itertools.permutations(range(2,N+1)):
 beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
 if beta>rev:continue
 total+=1;F={t for t in A if all(interval(s,beta) for s in t)}
 if not F:empty+=1;continue
 order=peel(F)
 if order is None:
  inc=Counter(frozenset(r) for q in F for r in itertools.combinations(q,len(q)-1))
  if all(v==2 for v in inc.values()):closed+=1;continue
  fails.append({'beta':list(beta),'reason':'peeling_stuck','facets':len(F)});continue
 bad=next((i for i in range(1,len(order)) if not admissible(order[i],order[:i])),None)
 if bad is None:certified+=1
 else:fails.append({'beta':list(beta),'reason':'reverse_not_shelling','facets':len(F),'index':bad})
checks={'all_20160_orbits':total==math.factorial(8)//2,'expected_empty':empty==15881,'exactly_one_closed_complex':closed==1,'all_4278_proper_nonempty_have_peel_shelling':certified==4278,'no_failures':not fails}
out={'schema':'marici.nima.double-partial-nine-point-peel-shelling.v1','algorithm':'Repeatedly remove the lexicographically greatest facet among those with the most free ridges; reverse the deletion order and verify the shelling criterion.','n':9,'order_orbits':total,'empty':empty,'closed':closed,'proper_nonempty_certified':certified,'failures':fails,'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/double-partial-nine-point-peel-shelling.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'empty':empty,'closed':closed,'certified':certified,'failures':len(fails)},indent=2));raise SystemExit(0 if out['passed'] else 1)
