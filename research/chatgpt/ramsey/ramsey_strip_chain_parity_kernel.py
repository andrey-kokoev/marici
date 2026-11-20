"""Suppress degree-two chains while retaining endpoint-matching parity. Enumerate the smaller exact-one constraint system independently of full matchings."""
from itertools import product
from collections import Counter
from ramsey_strip_common_core_residual_graph import adj,left,solutions
N={v:adj[v]&left for v in left};branch={v for v in left if len(N[v])==3};seen=set();chains=[]
edge=lambda a,b:tuple(sorted((a,b)))
for s in sorted(branch):
    for t in sorted(N[s]):
        if edge(s,t) in seen:continue
        p=[s,t];seen.add(edge(s,t))
        while p[-1] not in branch:
            u,=N[p[-1]]-{p[-2]};seen.add(edge(p[-1],u));p.append(u)
        chains.append(p)
assert len(chains)==18 and len(seen)==28
counts=Counter(len(p)-1 for p in chains);print('kernel vertices',len(branch),'edges',len(chains),'chain edge lengths',dict(counts));print('even chains',[p for p in chains if (len(p)-1)%2==0]);hits=[]
for bits in product((0,1),repeat=len(chains)):
    degrees={v:0 for v in branch};chosen=set()
    for p,b in zip(chains,bits):
        L=len(p)-1;end=b if L%2 else 1-b;degrees[p[0]]+=b;degrees[p[-1]]+=end
        for j in range(L):
            if (b if j%2==0 else 1-b):chosen.add(edge(p[j],p[j+1]))
    if all(d==1 for d in degrees.values()):hits.append(frozenset(chosen))
expected={frozenset(e for e in m if set(e)<=left) for m in solutions};assert set(hits)==expected and len(hits)==12
print('exact-one solutions of parity kernel',len(hits),'odd chains enforce equal endpoint bits; even chains opposite bits')
