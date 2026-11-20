"""Uniform rule on all six-label partitions: given disjoint partitions A and Z and a block d of Z, classify the other partitions through d. No literal row or endpoint duality used."""
from itertools import combinations
from collections import Counter
P=list(combinations(range(6),2));T=[frozenset(t) for t in combinations(P,3) if len(set(sum(t,())))==6];counts=Counter();moves={}
for i,A in enumerate(T):
 for j,Z in enumerate(T):
    if A&Z:continue
    for d in Z:
        other=[k for k,B in enumerate(T) if d in B and k!=j];pattern=tuple(sorted(len(A&T[k]) for k in other));assert pattern==(0,1);counts[pattern]+=1;k,=[k for k in other if not A&T[k]];moves[i,j,d]=k;assert A.isdisjoint(T[k]) and T[k]&Z=={d}
assert len(moves)==360
assert all(moves[i,k,d]==j for (i,j,d),k in moves.items())
print('opposite partitions per source',Counter(sum(not A&B for B in T) for A in T),'local configurations',counts,'move at fixed reference and block is involutive',True)
