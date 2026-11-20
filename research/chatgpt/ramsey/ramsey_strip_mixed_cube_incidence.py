"""Construct pair-based and partition-based opposite cubes. Test direct incidence as a mixed-chart correspondence, without inserting an endpoint duality."""
from itertools import combinations
from collections import Counter
P=list(combinations(range(6),2));T=[frozenset(t) for t in combinations(P,3) if len(set(sum(t,())))==6]
hist=Counter()
for a,A in enumerate(P):
 U=[i for i,d in enumerate(P) if len(set(d)&set(A))==1]
 assert len(U)==8 and all(sum(not set(P[i])&set(P[j]) for j in U)==3 for i in U)
 for b,B in enumerate(T):
    V=[j for j,t in enumerate(T) if not B&t];degrees=tuple(sorted(Counter(sum(P[i] in T[j] for j in V) for i in U).items()));right=tuple(sorted(Counter(sum(P[i] in T[j] for i in U) for j in V).items()));assert degrees==right
    hist[A in B,degrees]+=1
    if (a,b)==(0,14):
        neighbors={i:[j+15 for j in V if P[i] in T[j]] for i in U};print('literal mixed-cube incidence',neighbors)
print('(references incident, cross-degree distribution): configurations',dict(hist))
