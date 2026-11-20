"""Check local forced-link closure from each minimum invariant certificate, with entry flag chosen before or after propagation."""
from ramsey_strip_minimal_shared_constraints import cert,ms
from ramsey_strip_forced_local_propagation import propagate,adj,common
from collections import Counter
for i,c in enumerate(cert,1):
    chosen,left,rounds=propagate(c);print('certificate',i,'input links',len(c),'rounds',rounds,'forced total',len(chosen),'unresolved',len(left),'degrees',dict(Counter(len(adj[v]&left) for v in left)));assert chosen==set(common)
    for gate in ((0,16),(0,17)):
        full,rem,early=propagate(c|{gate});assert not rem and frozenset(full) in ms;print('early gate',gate,'round sizes',list(map(len,early)))
