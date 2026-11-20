"""Propagate degree-one matching constraints, without enumerating completions. Start with accumulated residue; then orient the remaining cycle by the literal entry flag."""
from collections import Counter
from ramsey_strip_accumulated_pair import fixed,N,common,ms
adj={i:set() for i in range(30)}
for i,js in N.items():
    for j in js:adj[i].add(j);adj[j].add(i)
def propagate(given):
    chosen=set(given);remaining=set(range(30))-{v for e in given for v in e};rounds=[]
    while remaining:
        assert all(adj[v]&remaining for v in remaining)
        forced={tuple(sorted((v,next(iter(adj[v]&remaining))))) for v in remaining if len(adj[v]&remaining)==1}
        if not forced:break
        assert len({v for e in forced for v in e})==2*len(forced)
        rounds.append(sorted(forced));chosen|=forced;remaining-={v for e in forced for v in e}
    return chosen,remaining,rounds
chosen,left,rounds=propagate(fixed);print('residue propagation rounds',rounds,'remaining vertices',len(left),'degree histogram',Counter(len(adj[v]&left) for v in left));assert chosen==set(common) and len(left)==10 and all(len(adj[v]&left)==2 for v in left)
full,rem,rounds=propagate(chosen|{(0,16)});print('after entry choice propagation rounds',rounds,'unresolved',len(rem));assert not rem and frozenset(full) in ms
