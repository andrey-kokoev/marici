#!/usr/bin/env python3
"""Deterministic stress test of the peel-shelling rule at ten points."""
import itertools,json,random
from collections import Counter
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];N=10;SAMPLES=5000
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
 ints=[F&G for G in prior];ridges=[q for q in ints if len(q)==len(F)-1]
 return bool(ridges) and all(any(q<=r for r in ridges) for q in ints)
def peel(F):
 rem=set(F);removed=[]
 while len(rem)>1:
  inc=Counter(frozenset(r) for q in rem for r in itertools.combinations(q,len(q)-1));cand=[]
  for q in rem:
   free=sum(inc[frozenset(r)]==1 for r in itertools.combinations(q,len(q)-1))
   if free:cand.append((free,fkey(q),q))
  if not cand:return None
  q=max(cand)[2];rem.remove(q);removed.append(q)
 return [next(iter(rem))]+list(reversed(removed))
alpha=tuple(range(1,N+1));U=set(alpha);A=[frozenset(canon(set(alpha[i:j]),U) for i,j in t) for t in rec(tuple(range(N)))];rng=random.Random(314159265);orders=set()
# Include structured extremes, then deterministic pseudorandom order orbits.
orders.add(alpha);orders.add((1,)+tuple(range(2,N+1,2))+tuple(range(3,N+1,2)))
while len(orders)<SAMPLES:
 tail=list(range(2,N+1));rng.shuffle(tail);b=(1,)+tuple(tail);r=(1,)+tuple(reversed(tail));orders.add(min(b,r))
empty=closed=cert=0;fails=[];hist=Counter()
for beta in orders:
 F={t for t in A if all(interval(s,beta) for s in t)};hist[len(F)]+=1
 if not F:empty+=1;continue
 order=peel(F)
 if order is None:
  inc=Counter(frozenset(r) for q in F for r in itertools.combinations(q,len(q)-1))
  if all(v==2 for v in inc.values()):closed+=1;continue
  fails.append({'beta':list(beta),'facets':len(F),'reason':'stuck'});continue
 bad=next((i for i in range(1,len(order)) if not admissible(order[i],order[:i])),None)
 if bad is None:cert+=1
 else:fails.append({'beta':list(beta),'facets':len(F),'reason':'reverse_not_shelling','index':bad})
checks={'five_thousand_distinct_order_orbits':len(orders)==SAMPLES,'identity_closed_case_present':closed==1,'every_sampled_proper_nonempty_certified':not fails}
out={'schema':'marici.nima.double-partial-ten-point-peel-shelling-stress.v1','n':10,'samples':len(orders),'empty':empty,'closed':closed,'proper_nonempty_certified':cert,'facet_count_histogram':dict(sorted(hist.items())),'failures':fails,'checks':checks,'passed':all(checks.values()),'scope':'Deterministic 5,000-orbit stress test, not the exhaustive 181,440-orbit census.'}
p=ROOT/'research/nima/results/double-partial-ten-point-peel-shelling-stress.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'samples':len(orders),'empty':empty,'closed':closed,'certified':cert,'failures':len(fails)},indent=2));raise SystemExit(0 if out['passed'] else 1)
