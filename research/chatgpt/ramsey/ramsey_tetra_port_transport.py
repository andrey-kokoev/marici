"""Classify reversible S4-equivariant transport between three-port fibers.
Specify a bijection on edge 0->1, extend by conjugation, reject conflicting
transports, then check inverse and compare direct vs two-step routes."""
from itertools import permutations
V=tuple(range(4)); edges=list(permutations(V,2)); G=list(permutations(V))
fiber=lambda a:tuple(i for i in V if i!=a)
success=[]
for image in permutations(fiber(1)):
    seed=dict(zip(fiber(0),image)); rules={}; consistent=True
    for g in G:
        edge=g[0],g[1]; mapping={g[i]:g[j] for i,j in seed.items()}
        if edge in rules and rules[edge]!=mapping:consistent=False;break
        rules[edge]=mapping
    if not consistent:continue
    assert all(rules[b,a][rules[a,b][i]]==i for a,b in edges for i in fiber(a))
    equal=sum(rules[b,c][rules[a,b][i]]==rules[a,c][i] for a,b,c in permutations(V,3) for i in fiber(a))
    loop={i:rules[2,0][rules[1,2][rules[0,1][i]]] for i in fiber(0)}
    success.append((seed,equal,loop));print('seed:',seed,'agree out of 72:',equal,'loop 0120:',loop)
assert sorted(n for _,n,_ in success)==[24,72]
