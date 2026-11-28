"""Test fixed-record completion on every small catalogue record; check pair-shadow recovery at equality."""
from collections import Counter
from itertools import combinations
from r37_reconstruct_catalogue import equality_cases
from r37_reconstruct_sat import models,legal,blades
X=range(6,22);counts=Counter();alts=Counter();first={}
for idx,order,h,B in equality_cases(range(10,16)):
    k=len(B);counts[k]+=1
    if k==10:
        for d in (2,3):
            P={p for s in B for p in combinations(sorted(s),d)}
            cand={frozenset(t) for t in combinations(X,6) if all(p in P for p in combinations(t,d))};assert B<=cand
            print('shadow',idx,order[:6],d,'false positives',len(cand-B),flush=True)
    for g in models(h,B):
        alts[k]+=1
        if k not in first and sum(map(int.bit_count,h))!=sum(map(int.bit_count,g)):
            assert legal(h) and blades(h)==B
            first[k]=(idx,order[:6],[(order[i],order[j]) for i,j in combinations(X,2) if (h[i]^g[i])>>j&1],sum(map(int.bit_count,h))//2,sum(map(int.bit_count,g))//2)
            print('inequivalent',k,first[k],flush=True)
print('tested',sorted(counts.items()),'labelled alternatives',sorted(alts.items()))
