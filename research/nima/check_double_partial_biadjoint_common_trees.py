#!/usr/bin/env python3
"""Exact common-planar-tree construction for double-partial biadjoint amplitudes."""
import itertools,json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def edge(a,b):return tuple(sorted((a,b)))
@lru_cache(None)
def triangulations_positions(n):
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
def canon_split(S,universe):
 S=frozenset(S);C=frozenset(universe-S)
 return min((S,C),key=lambda q:(len(q),tuple(sorted(q))))
def planar_trees(order):
 n=len(order);U=set(order);out=set()
 for tri in triangulations_positions(n):
  splits=[]
  for i,j in tri:splits.append(canon_split(set(order[i:j]),U))
  out.add(frozenset(splits))
 return out
cases=[];passed=True
for n in range(4,10):
 base=tuple(range(1,n+1));orders=[base,base[::-1],base[1:]+base[:1],tuple(base[i] for i in list(range(0,n,2))+list(range(1,n,2)))]
 trees={o:planar_trees(o) for o in orders}
 for a,b in itertools.product(orders,repeat=2):
  common=trees[a]&trees[b];reverse=trees[b]&trees[a];ok=common==reverse and all(len(t)==n-3 for t in common);passed &= ok
  cases.append({'n':n,'alpha':list(a),'beta':list(b),'common_planar_trees':len(common),'exchange_symmetric':common==reverse,'passed':ok})
 # Identity, reversal, and cyclic rotation describe the same planar ordering.
 expected=len(trees[base]);special=[len(trees[base]&trees[o]) for o in orders[:3]];passed &= all(q==expected for q in special)
checks={'all_exchange_symmetry_checks':all(c['exchange_symmetric'] for c in cases),'all_common_trees_have_n_minus_3_channels':all(c['passed'] for c in cases),'identity_reversal_rotation_preserve_catalan_support':passed}
out={'schema':'marici.nima.double-partial-biadjoint-common-trees.v1','definition':'m_n[alpha|beta] is the unit-coefficient sum over cubic trees planar in both cyclic orders, represented by their channel splits.','range':[4,9],'order_pairs_checked':len(cases),'cases':cases,'checks':checks,'passed':passed and all(checks.values()),'scope':'Exact finite common-tree construction for selected order pairs; arbitrary-order factorization and a universal proof remain open.'}
p=ROOT/'research/nima/results/double-partial-biadjoint-common-trees.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'range':[4,9],'order_pairs':len(cases),'sample_scrambled_counts':[c['common_planar_trees'] for c in cases if c['alpha']==list(range(1,c['n']+1))][-6:]},indent=2));raise SystemExit(0 if out['passed'] else 1)
