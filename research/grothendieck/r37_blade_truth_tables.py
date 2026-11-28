"""Truth functions of newly appearing blades, labelled in original catalogue order."""
from r37_reconstruct_catalogue import equality_cases
from r37_reconstruct_sat import models,blades
from itertools import combinations
from collections import Counter
for idx,order,h,B in equality_cases():
    G=[h,*models(h,B,positive_only=True)]
    E=[(i,j) for i,j in combinations(range(6,22),2) if any((g[i]^h[i])>>j&1 for g in G)]
    print('record',idx,'roots',order[:6],'ambiguous (catalogue labels, original red?)',[(order[i],order[j],h[i]>>j&1) for i,j in E])
    supports=[blades(g) for g in G]; extra=set.union(*supports)-B
    hist=Counter();patterns=Counter()
    for s in extra:
        mask=sum(1<<k for k,(i,j) in enumerate(E) if i in s and j in s)
        pred=[all(not(g[i]>>j&1) for k,(i,j) in enumerate(E) if mask>>k&1) for g in G]
        assert pred==[s in t for t in supports]; hist[mask.bit_count()]+=1
        patterns[mask]+=1
    print('new-blade counts by number of tested edges',sorted(hist.items()),'patterns',sorted(patterns.items()))
    collisions=[(len(supports[i]),i,j) for i,j in combinations(range(len(G)),2) if supports[i]==supports[j] and sum(map(int.bit_count,G[i]))!=sum(map(int.bit_count,G[j]))]
    if collisions:
        size,i,j=min(collisions); print('edge-count-separated collision',size,[(sum(map(int.bit_count,G[t]))//2,[k for k,(u,v) in enumerate(E) if (h[u]^G[t][u])>>v&1]) for t in (i,j)])
    print('distinct complete support records',len(set(map(frozenset,supports))),'of',len(G))
