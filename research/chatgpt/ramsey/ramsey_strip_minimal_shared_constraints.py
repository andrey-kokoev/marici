"""Find minimal row-invariant subsets of accumulated residues forcing exactly the target two matchings. Search all completions, not just strip-derived matchings. This is a conditional certificate, not a seed derivation."""
from itertools import combinations
from ramsey_strip_accumulated_pair import fixed,ms,N,turn

def allmatch(L,R):
    if not L:yield frozenset();return
    i=min(L,key=lambda i:len(N[i]&R))
    for j in N[i]&R:
        for m in allmatch(L-{i},R-{j}):yield m|{(i,j)}
allms=list(allmatch(set(range(15)),set(range(15,30))));orbits=sorted({frozenset({e})|turn({e}) for e in fixed},key=lambda s:sorted(s));cert=[]
for k in range(len(orbits)+1):
    for parts in combinations(orbits,k):
        req=frozenset().union(*parts);surv={m for m in allms if req<=m}
        if surv==set(ms):cert.append(req)
    if cert:break
print('all perfect matchings',len(allms),'minimum number of invariant orbit constraints',k,'certificates',[sorted(q) for q in cert]);assert cert
for req in cert:
    for gate in [(0,16),(0,17)]:assert sum(req|{gate}<=m for m in allms)==1
print('either entry flag resolves each two-completion certificate uniquely')
