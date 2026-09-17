#!/usr/bin/env python3
"""Exact channel-factorization test for double-partial common-tree amplitudes."""
import itertools,json
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
def side_of(split,S,U):
 # A compatible residual channel lies wholly on one side after choosing either representative.
 A=set(split);B=U-A
 if A<=S or B<=S:return 0
 if A<=(U-S) or B<=(U-S):return 1
 return -1
cases=[];passed=True
for n in range(4,10):
 base=tuple(range(1,n+1));orders=[base,base[::-1],base[1:]+base[:1],tuple(base[i] for i in list(range(0,n,2))+list(range(1,n,2)))];cache={o:trees(o) for o in orders};U=set(base)
 for a,b in itertools.combinations_with_replacement(orders,2):
  common=cache[a]&cache[b]
  for d in sorted(set().union(*common) if common else [] ,key=lambda q:(len(q),tuple(q))):
   containing=[t for t in common if d in t];S=set(d);pairs=set();well_typed=True
   for t in containing:
    left=[];right=[]
    for q in t-{d}:
     side=side_of(q,S,U);well_typed &= side>=0;(left if side==0 else right).append(q)
    pairs.add((frozenset(left),frozenset(right)))
   L={q[0] for q in pairs};R={q[1] for q in pairs};product={(l,r) for l in L for r in R};ok=well_typed and pairs==product;passed &= ok
   cases.append({'n':n,'alpha':list(a),'beta':list(b),'channel':sorted(d),'residue_terms':len(pairs),'left_terms':len(L),'right_terms':len(R),'product_terms':len(product),'passed':ok})
checks={'all_residual_channels_lie_on_one_cut_side':all(c['passed'] for c in cases),'all_residue_supports_are_cartesian_products':all(c['residue_terms']==c['left_terms']*c['right_terms'] for c in cases),'nonvacuous_channels_checked':len(cases)>0}
out={'schema':'marici.nima.double-partial-biadjoint-factorization.v1','theorem_tested':'For each common physical channel, common-tree residue support is the Cartesian product of its two side supports. Unit coefficients therefore factor multiplicatively.','range':[4,9],'channel_factorizations_checked':len(cases),'cases':cases,'checks':checks,'passed':passed and all(checks.values()),'scope':'Exact exhaustive checks for selected order pairs. Side supports are inferred by restriction of common trees; an arbitrary-order analytic proof remains to be written.'}
p=ROOT/'research/nima/results/double-partial-biadjoint-factorization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'factorizations_checked':len(cases),'checks':checks},indent=2));raise SystemExit(0 if out['passed'] else 1)
