"""Split distinct B labels by cyclic adjacency. Keep prior A and cross-group rules.
Enumerate every assignment to link classes. No witness data.
"""
from itertools import combinations
from collections import Counter
from pauli_realization_audit import independent_witness, triangle_free


def audit(k):
    vs=[(g,i,c) for g,size in enumerate((3,k)) for i in range(size) for c in (0,1)]
    types={}
    for a,b in combinations(range(len(vs)),2):
        g,i,c=vs[a];h,j,d=vs[b]
        near=(g==h==1 and (i-j)%k in (1,k-1))
        key=(g,h,g==h and i==j,near,c^d)
        types.setdefault(key,[]).append((a,b))
    counts=Counter()
    for mask in range(1<<len(types)):
        rows=[0]*len(vs)
        for t,edges in enumerate(types.values()):
            if mask>>t&1:
                for a,b in edges:rows[a]|=1<<b;rows[b]|=1<<a
        counts['tested']+=1
        if triangle_free(rows):
            counts['triangle-free']+=1
            if independent_witness(rows,k) is None:counts['valid']+=1
    return tuple(counts[key] for key in ('tested','triangle-free','valid'))

if __name__=='__main__':
    for k in (7,8,9):print(k,audit(k))
