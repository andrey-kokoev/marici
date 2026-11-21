"""Construct the unrestricted-allocation core by propagation and recognize its cube."""
from itertools import combinations
from ramsey_stripped_core import seed,close,E,T
cross=sum(b for (i,j),b in E.items() if j<6 and i//2!=j//2)
y,n=close(seed,cross);assert (y|n)==sum(E.values()) and y.bit_count()==22
adj={v:set() for v in T if v not in ('ef','abcd')}
for (i,j),b in E.items():
    if y&b:adj[T[i]].add(T[j]);adj[T[j]].add(T[i])
rim={v for v in adj if len(adj[v])==4};hub=set(adj)-rim
L=['a','ae','d','df'];R=['b','cf','c','be'];assert set(L+R)==rim
opp={v:next(iter(set(R)-adj[v])) for v in L};assert all(adj[v]&rim==set(R)-{opp[v]} for v in L) and set(opp.values())==set(R)
# Place L on the even bitstrings; their antipodes are their unique missing neighbors.
coords=dict(zip(L,(0,3,5,6)));coords.update({o:coords[v]^7 for v,o in opp.items()});assert all((b in adj[a])==((coords[a]^coords[b]).bit_count()==1) for a,b in combinations(rim,2))
print('cube',sorted((format(i,'03b'),v) for v,i in coords.items()))
for h in sorted(hub):
    u,v=sorted(adj[h]&rim);assert coords[u]^coords[v]==7 and len(adj[h]&hub)==1;print(h,'bridges',u,v,'paired with',next(iter(adj[h]&hub)))
