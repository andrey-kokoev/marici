#!/usr/bin/env python3
"""Canonical oriented relative chains for maximum-degree shedding pairs."""
exec(compile(open(__file__.replace('check_oriented_shedding_relative_cycles.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];seen=set();stats=Counter();fails=[]
def graph(fs):
 V=set().union(*fs);co={frozenset((a,b)) for F in fs for a,b in itertools.combinations(F,2)}
 return V,{v:{w for w in V-{v} if frozenset((v,w)) not in co} for v in V}
def data(fs,v):
 d=len(next(iter(fs)));de=maximal(frozenset(f for f in fs if v not in f));li=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
 return (de and {len(f) for f in de}=={d} and li and {len(f) for f in li}=={d-1} and all(any(q<=g for g in de) for q in li)),de,li
def ckey(q):return (len(q),tuple(sorted(q)))
def incidence(F,ridge):
 ordered=sorted(F,key=ckey);missing=next(i for i,q in enumerate(ordered) if q not in ridge);return -1 if missing%2 else 1
def walk(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in seen or len(fs)<=1:return
 seen.add(k);V,N=graph(fs);mx=max(len(N[x]) for x in V);pick=None
 for v in sorted((x for x in V if len(N[x])==mx),key=ckey):
  ok,de,li=data(fs,v)
  if ok:pick=(v,de,li);break
 if pick is None:fails.append({'reason':'no maximum-degree shedding channel'});return
 v,de,li=pick;avoiding={T for T in fs if v not in T}
 for T in (T for T in fs if v in T):
  R=T-{v};images=[G for G in avoiding if R<=G]
  if len(images)!=1:fails.append({'reason':'nonunique partner'});continue
  G=images[0];a=incidence(T,R);b=incidence(G,R);coefficient=-a*b
  # Boundary coefficient of e_T + coefficient e_G on the common ridge.
  if a+coefficient*b!=0:fails.append({'reason':'ridge did not cancel'})
  stats['relative_blocks']+=1;stats['oriented_sum' if coefficient==1 else 'oriented_difference']+=1
 stats['states']+=1;walk(de);walk(li)
rows=[]
for n in range(4,9):
 A=trees(tuple(range(1,n+1)));before=stats['states']
 for tail in itertools.permutations(range(2,n+1)):
  b=(1,)+tail;r=(1,)+tuple(reversed(tail))
  if b<=r:
   F=A&trees(b)
   if F:walk(F)
 rows.append({'n':n,'new_states':stats['states']-before})
checks={'all_common_ridge_coefficients_cancel':not fails,'every_block_classified':stats['relative_blocks']==stats['oriented_sum']+stats['oriented_difference']}
out={'schema':'marici.nima.oriented-shedding-relative-cycles.v1','range':[4,8],'results':rows,'totals':dict(stats),'checks':checks,'passed':all(checks.values()),'statement':'For each flip pair there is a unique sign epsilon such that the oriented chain e_T+epsilon e_Tprime has zero boundary coefficient on the shared ridge.'}
p=ROOT/'research/nima/results/oriented-shedding-relative-cycles.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
