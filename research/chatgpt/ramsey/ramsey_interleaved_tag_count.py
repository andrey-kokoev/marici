"""Enumerate loop-free relations invariant under S_l x S_k and a common copy flip.
No witness data. Count free tag bits needed to distinguish the existing addresses.
"""
from itertools import combinations
from collections import Counter


def audit(l,k):
    vertices=[(g,i,c) for g,n in enumerate((l,k)) for i in range(n) for c in (0,1)]
    types={}
    for a,b in combinations(range(len(vertices)),2):
        g,i,c=vertices[a];h,j,d=vertices[b]
        key=(g,h,g==h and i==j,c^d)
        types.setdefault(key,[]).append((a,b))
    hist=Counter()
    for mask in range(1<<len(types)):
        rows=[0]*len(vertices)
        for t,edges in enumerate(types.values()):
            if mask>>t&1:
                for a,b in edges:rows[a]|=1<<b;rows[b]|=1<<a
        m=max(Counter(rows).values());hist[(m-1).bit_length()]+=1
        # The k plain B labels already induce a constant off-diagonal relation.
        B=[a for a,(g,i,c) in enumerate(vertices) if g==1 and c==0]
        assert len({rows[a]>>b&1 for a,b in combinations(B,2)})==1
    return dict(sorted(hist.items()))
if __name__=='__main__':
    for k in (7,8,9):print(3,k,audit(3,k))
