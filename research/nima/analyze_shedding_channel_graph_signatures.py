#!/usr/bin/env python3
"""Classify graph-local signatures of canonical shedding choices through n=8."""
exec(compile(open(__file__.replace('analyze_shedding_channel_graph_signatures.py','check_common_tree_vertex_decomposability.py'),encoding='utf-8').read().split('rows=[]')[0], 'vd-prefix', 'exec'))
import itertools,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];seen=set();stats=Counter();examples={}
def graph(fs):
 V=set().union(*fs);co={frozenset((a,b)) for F in fs for a,b in itertools.combinations(F,2)}
 return V,{v:{w for w in V-{v} if frozenset((v,w)) not in co} for v in V}
def shedding(fs,v):
 d=len(next(iter(fs)));de=maximal(frozenset(f for f in fs if v not in f));li=maximal(frozenset(frozenset(f-{v}) for f in fs if v in f))
 ok=(de and {len(f) for f in de}=={d} and li and {len(f) for f in li}=={d-1} and all(any(q<=g for g in de) for q in li))
 return ok,de,li
def walk(fs):
 fs=maximal(fs);k=statekey(fs)
 if k in seen or len(fs)<=1:return
 seen.add(k);V,N=graph(fs);ordered=sorted(V,key=lambda q:(len(q),tuple(sorted(q))));picked=None
 for v in ordered:
  ok,de,li=shedding(fs,v)
  if ok:picked=(v,de,li);break
 if picked is None:return
 v,de,li=picked;deg=len(N[v]);degrees=[len(N[x]) for x in V]
 simplicial=all(b in N[a] for a,b in itertools.combinations(N[v],2))
 neighbor_simplicial=any(all(b in N[a] for a,b in itertools.combinations(N[u],2)) for u in N[v])
 codominated=any(N[u]|{u} <= N[v]|{v} for u in N[v])
 props={'minimum_degree':deg==min(degrees),'maximum_degree':deg==max(degrees),'simplicial':simplicial,'adjacent_to_simplicial':neighbor_simplicial,'codominated':codominated,'isolated':deg==0}
 stats['choices']+=1
 for p,val in props.items():stats[p]+=val
 sig=(len(V),len(fs),deg,tuple(sorted(len(N[u]&N[v]) for u in N[v])))
 examples.setdefault('signature',{})[str(sig)]=examples.setdefault('signature',{}).get(str(sig),0)+1
 walk(de);walk(li)
for n in range(4,9):
 A=trees(tuple(range(1,n+1)))
 for tail in itertools.permutations(range(2,n+1)):
  b=(1,)+tail;r=(1,)+tuple(reversed(tail))
  if b<=r:
   F=A&trees(b)
   if F:walk(F)
out={'schema':'marici.nima.shedding-channel-graph-signatures.v1','range':[4,8],'recursive_states_with_choices':stats['choices'],'property_counts':dict(stats),'property_rates':{k:stats[k]/stats['choices'] for k in stats if k!='choices'},'distinct_local_signatures':len(examples.get('signature',{})),'top_local_signatures':sorted(examples.get('signature',{}).items(),key=lambda q:-q[1])[:30],'interpretation':'Properties of the lexicographically first actual shedding vertex; a universal count would identify a possible local selector.'}
p=ROOT/'research/nima/results/shedding-channel-graph-signatures.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('recursive_states_with_choices','property_counts','property_rates','distinct_local_signatures')},indent=2))
