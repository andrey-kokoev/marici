#!/usr/bin/env python3
"""Certify partial flip matchings and common/difference ranks along max-degree shedding."""
exec(compile(open(__file__.replace('check_shedding_hadamard_pairing.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
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
def walk(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in seen or len(fs)<=1:return
 seen.add(k);V,N=graph(fs);mx=max(len(N[v]) for v in V);choices=[]
 for v in sorted((x for x in V if len(N[x])==mx),key=lambda q:(len(q),tuple(sorted(q)))):
  ok,de,li=data(fs,v)
  if ok:choices.append((v,de,li))
 if not choices:fails.append({'reason':'no max-degree shedding vertex','facets':len(fs)});return
 v,de,li=choices[0];containing=[T for T in fs if v in T];avoiding=set(T for T in fs if v not in T);pairs=[]
 for T in containing:
  ridge=T-{v};images=[G for G in avoiding if ridge<=G]
  if len(images)!=1:fails.append({'reason':'nonunique flip image','image_count':len(images),'facets':len(fs)});return
  pairs.append((T,images[0]))
 image=[b for a,b in pairs]
 if len(set(image))!=len(image):fails.append({'reason':'pairing_not_injective','facets':len(fs)});return
 stats['states']+=1;stats['paired_blocks']+=len(pairs);stats['unpaired_avoiding_facets']+=len(avoiding)-len(image);stats['difference_rank']+=len(pairs);stats['common_rank']+=len(pairs)
 walk(de);walk(li)
rows=[]
for n in range(4,9):
 A=trees(tuple(range(1,n+1)));before=stats['states'];nonempty=0
 for tail in itertools.permutations(range(2,n+1)):
  b=(1,)+tail;r=(1,)+tuple(reversed(tail))
  if b<=r:
   F=A&trees(b)
   if F:nonempty+=1;walk(F)
 rows.append({'n':n,'nonempty_complexes':nonempty,'new_recursive_pairing_states':stats['states']-before})
checks={'all_selected_channels_give_disjoint_two_facet_blocks':not fails,'difference_rank_equals_number_of_containing_facets':stats['difference_rank']==stats['paired_blocks']}
out={'schema':'marici.nima.shedding-hadamard-pairing.v1','range':[4,8],'results':rows,'totals':dict(stats),'failures':fails[:20],'checks':checks,'passed':all(checks.values()),'interpretation':'For fixed shedding v, facets containing v are injectively matched by the unique ridge flip to facets avoiding v. Each disjoint pair supports common and difference basis vectors.'}
p=ROOT/'research/nima/results/shedding-hadamard-pairing.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'results':rows,'totals':dict(stats),'failures':len(fails)},indent=2));raise SystemExit(0 if out['passed'] else 1)
