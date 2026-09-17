#!/usr/bin/env python3
"""Construct shellings for every nonempty n=9 double-partial common-tree complex."""
import itertools,json,math
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
U=set(range(1,N+1));alpha=tuple(range(1,N+1))
A=[frozenset(canon(set(alpha[i:j]),U) for i,j in t) for t in rec(tuple(range(N)))]
def interval(S,beta):
 bits=[x in S for x in beta];return sum(bits[i]!=bits[(i+1)%N] for i in range(N))==2
def key(F):return tuple(sorted((len(q),tuple(sorted(q))) for q in F))
def admissible(F,prior):
 ints=[F&G for G in prior];ridges=[q for q in ints if len(q)==len(F)-1]
 return bool(ridges) and all(any(q<=r for r in ridges) for q in ints)
def shell(F):
 rem=set(F);order=[min(rem,key=key)];rem.remove(order[0])
 while rem:
  candidates=[q for q in rem if admissible(q,order)]
  if not candidates:return None
  q=min(candidates,key=lambda f:(-sum(len(f&g)==len(f)-1 for g in order),key(f)));rem.remove(q);order.append(q)
 return order
total=empty=shelled=0;fails=[];size_hist={}
for tail in itertools.permutations(range(2,N+1)):
 beta=(1,)+tail;rev=(1,)+tuple(reversed(tail))
 if beta>rev:continue
 total+=1;F=frozenset(t for t in A if all(interval(s,beta) for s in t))
 if not F:empty+=1;continue
 size_hist[str(len(F))]=size_hist.get(str(len(F)),0)+1
 order=shell(F)
 if order is None:fails.append({'beta':list(beta),'facets':len(F)})
 else:shelled+=1
checks={'all_20160_orbits':total==math.factorial(8)//2,'expected_nonempty_count':shelled+len(fails)==4279,'every_nonempty_has_shelling':not fails}
out={'schema':'marici.nima.double-partial-nine-point-shellings.v1','n':9,'order_orbits':total,'empty':empty,'nonempty_shelling_certificates':shelled,'facet_count_histogram':size_hist,'failures':fails,'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/double-partial-nine-point-shellings.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'order_orbits':total,'empty':empty,'shellings':shelled,'failures':len(fails)},indent=2));raise SystemExit(0 if out['passed'] else 1)
