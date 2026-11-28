"""Unit propagation without search, and reconstruction from positive 4-shadow."""
from itertools import combinations
from collections import Counter
from r37_reconstruct_catalogue import equality_cases
from r37_reconstruct_sat import models,blades
X=range(6,22); E={e:i+1 for i,e in enumerate(combinations(X,2))}
for idx,order,g,B in equality_cases():
    known={-E[i,j] for i,j in E if g[i]&g[j]&63}
    known.update(-E[e] for t in B for e in combinations(sorted(t),2))
    clauses=[[-E[e] for e in combinations(t,2)] for t in combinations(X,3)]
    for t in combinations(X,6):
        if frozenset(t) not in B:clauses.append([E[e] for e in combinations(t,2)])
    for k in range(1,8):
        for t in combinations(X,k):
            u=0
            for i in t:u|=g[i]&63
            if k>u.bit_count():clauses.append([E[e] for e in combinations(t,2)])
    rounds=[len(known)]
    while True:
        new=set()
        for c in clauses:
            if not known.isdisjoint(c):continue
            rest=[v for v in c if -v not in known];assert rest
            if len(rest)==1:new.add(rest[0])
        if not new:break
        known.update(new);rounds.append(len(known))
    assert all(((v in known)==bool(g[i]>>j&1)) for (i,j),v in E.items() if v in known or -v in known)
    P={p for t in B for p in combinations(sorted(t),4)}
    cand={frozenset(t) for t in combinations(X,6) if all(p in P for p in combinations(t,4))}
    print(idx,order[:6],'forced',rounds,'shadow candidates',len(cand),'false candidates',len(cand-B),flush=True)
    # Search for sub-16 collisions inside the positive family only.
    seen={};counts=Counter()
    for h in [g,*models(g,B,positive_only=True)]:
        S=frozenset(blades(h));counts[len(S)]+=1
        if len(S)<16 and S in seen:print('labelled collision at',len(S))
        seen[S]=1
    print('sub-16 completions',{k:v for k,v in counts.items() if k<16})
