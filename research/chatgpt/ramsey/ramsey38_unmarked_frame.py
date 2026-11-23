"""Exhaust exact point automorphisms and transport previously frozen frame interface. Use ordered wiring IDs only for storage."""
from pathlib import Path
import itertools as it,json,collections
D=Path(__file__).parent;r=json.loads((D/'ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E=list(map(tuple,r['edge_order']));W=sorted(r['wirings']);P={}
for p in it.permutations(range(7)):
 T=[sum(1<<p[i] for i in range(7) if s>>i&1) for s in S];
 if set(T)!=set(S):continue
 m=list(map(S.index,T));e=[E.index(tuple(sorted((m[i],m[j])))) for i,j in E];P[p]=tuple(W.index(sum((w>>i&1)<<j for i,j in enumerate(e))) for w in W)
def gen(*swaps):
 p=list(range(7))
 for i,j in swaps:p[i],p[j]=p[j],p[i]
 return P[tuple(p)]
A=gen((0,1),(2,3));B=gen((0,1),(4,5));C=gen((2,4),(3,5));V=set(range(8));key=lambda a,b:tuple(sorted((a,b)));graph=frozenset(key(i,g[i]) for i in V for g in (A,B,C));bridge=frozenset(key(i,C[i]) for i in V);side=frozenset((0,A[0],B[0],A[B[0]]));partition=lambda s:frozenset((s,frozenset(V-s)));cut=partition(side);rows=[];example=None
for p,g in P.items():
 act=lambda X:frozenset(key(g[i],g[j]) for i,j in X);h,k,l=act(graph),act(bridge),partition(frozenset(g[i] for i in side));rows.append((h,k,l));assert k==frozenset((i,j) for i,j in h if not any(i in s and j in s for s in l));
 if k!=bridge and (example is None or sum(i!=p[i] for i in range(7))<example[0]):example=(sum(i!=p[i] for i in range(7)),p,len(k&bridge),l==cut)
stats=lambda i,obj:dict(orbit=len({v[i] for v in rows}),stabilizer=sum(v[i]==obj for v in rows));union=frozenset.union(*(r[0] for r in rows));inter=frozenset.intersection(*(r[0] for r in rows));o=dict(label_automorphisms=len(P),distinct_state_actions=len(set(P.values())),move_graph=stats(0,graph),bridges=stats(1,bridge),tag_cut=stats(2,cut),joint_orbit=len(set(rows)),union_edges=len(union),intersection_edges=len(inter),union_triangle=next((v for v in it.combinations(sorted(V),3) if all(key(*e) in union for e in it.combinations(v,2))),None),example=example);balanced={partition(frozenset(s)) for s in it.combinations(sorted(V),4)};o['invariant_balanced_partitions']=sum(all(partition(frozenset(g[i] for i in next(iter(k))))==k for g in P.values()) for k in balanced);o['union_bipartitions']=sum(all(not any(i in s and j in s for s in k) for i,j in union) for k in balanced);print(o);(D/'ramsey38_unmarked_frame.json').write_text(json.dumps(o,indent=2)+'\n')
