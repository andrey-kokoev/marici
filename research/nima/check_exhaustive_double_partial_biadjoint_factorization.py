#!/usr/bin/env python3
"""Exhaustive low-multiplicity check of arbitrary-order double-partial factorization."""
import itertools,json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def triangulations(n):
 @lru_cache(None)
 def rec(v):
  if len(v)<=3:return (frozenset(),)
  out=set();a,z=v[0],v[-1]
  for k in range(1,len(v)-1):
   b=v[k];L=rec(v[:k+1]);R=rec(v[k:]);add=set()
   if k>1:add.add(edge(a,b))
   if k<len(v)-2:add.add(edge(b,z))
   for l in L:
    for r in R:out.add(frozenset(set(l)|set(r)|add))
  return tuple(out)
 return rec(tuple(range(n)))
def canon(S,U):
 S=frozenset(S);C=frozenset(U-S)
 return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def trees(order):
 U=set(order)
 return frozenset(frozenset(canon(set(order[i:j]),U) for i,j in t) for t in triangulations(len(order)))
def orders(n):
 # Fix label 1 to remove rotations and choose one representative modulo reversal.
 out=[]
 for tail in itertools.permutations(range(2,n+1)):
  if tail<=tail[::-1]:out.append((1,)+tail)
 return tuple(out)
def side_of(split,S,U):
 A=set(split);B=U-A
 if A<=S or B<=S:return 0
 if A<=(U-S) or B<=(U-S):return 1
 return -1
rows=[];passed=True;total_pairs=0;total_channels=0
for n in range(4,8):
 os=orders(n);cache={o:trees(o) for o in os};U=set(range(1,n+1));pairs_checked=0;channels_checked=0;failures=0
 for ia,a in enumerate(os):
  for b in os[ia:]:
   pairs_checked+=1;common=cache[a]&cache[b]
   # Exchange symmetry is exact because intersection is commutative.
   if common != cache[b]&cache[a]:failures+=1
   channels=set().union(*common) if common else set()
   for d in channels:
    channels_checked+=1;S=set(d);support=set();well_typed=True
    for t in common:
     if d not in t:continue
     left=[];right=[]
     for q in t-{d}:
      side=side_of(q,S,U);well_typed &= side>=0
      (left if side==0 else right).append(q)
     support.add((frozenset(left),frozenset(right)))
    L={x for x,_ in support};R={y for _,y in support}
    if not well_typed or support!={(x,y) for x in L for y in R}:failures+=1
 ok=failures==0;passed &= ok;total_pairs+=pairs_checked;total_channels+=channels_checked
 rows.append({'n':n,'inequivalent_cyclic_orders':len(os),'unordered_order_pairs':pairs_checked,'common_channels_checked':channels_checked,'failure_count':failures,'passed':ok})
out={'schema':'marici.nima.exhaustive-double-partial-biadjoint-factorization.v1','range':[4,7],'quotient':'cyclic orders modulo independent rotation and reversal; unordered pairs use exchange symmetry','results':rows,'total_order_pairs':total_pairs,'total_channel_factorizations':total_channels,'checks':{'all_exchange_symmetries':passed,'all_residual_channels_well_typed':passed,'all_residue_supports_cartesian':passed},'passed':passed,'scope':'Exhaustive exact common-tree support for all inequivalent cyclic-order pairs through seven points.'}
p=ROOT/'research/nima/results/exhaustive-double-partial-biadjoint-factorization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if passed else 1)
