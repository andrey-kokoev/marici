"""Explain all 41 ambiguous deletions in the six-point pair witness."""
from itertools import combinations
from collections import Counter
from ramsey_blind_two_address import build,recover
from pauli_realization_audit import independent_witness

g=build(); mutable=[]
for i,j in combinations(range(22),2):
    if g[i]>>j&1:
        h=g.copy();h[i]^=1<<j;h[j]^=1<<i
        if independent_witness(h,7) is None:mutable.append((i,j))
assert mutable==[(0,6)]
h=g.copy();h[0]^=1<<6;h[6]^=1
hist=Counter()
for u,v in combinations(range(22),2):
    L=[i for i in range(22) if i not in (u,v)]
    proj=lambda r:sum(((r>>i)&1)<<j for j,i in enumerate(L))
    residual=lambda graph:[proj(graph[i]) for i in L]
    completion=lambda graph:(*sorted((proj(graph[u]),proj(graph[v]))),(graph[u]>>v)&1)
    old=residual(g);expected={completion(g)}
    if residual(h)==old:expected.add(completion(h))
    actual=recover(old);assert actual==expected
    hist[len(actual)]+=1
print('changeable positive link:',mutable[0],'; number of completions -> deletions:',dict(hist))
