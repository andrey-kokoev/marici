"""Iterate outer-cycle replacement and inspect the canonical two-edge transport through the middle layer. Do not assume it preserves cycle adjacency."""
from collections import Counter
from ramsey_all_ten_cycle_layers import cycles,N
sets={frozenset(p) for p in cycles};pairs=set();stats=Counter()
for p in cycles:
 C=set(p);M=set.union(*(N[v] for v in C))-C;D=set(range(30))-C-M;assert frozenset(D) in sets
 M2=set.union(*(N[v] for v in D))-D;assert M2==M and set(range(30))-D-M2==C;pairs.add(frozenset((frozenset(C),frozenset(D))))
 mid={v:next(iter(N[v]&M)) for v in C};trans={v:next(iter(N[mid[v]]&D)) for v in C};assert len(set(trans.values()))==10
 offset=Counter();middle=Counter()
 for i,x in enumerate(p):
    for j,y in enumerate(p):
        if trans[y] in N[trans[x]]:offset[min((j-i)%10,(i-j)%10)]+=1
        if mid[y] in N[mid[x]]:middle[min((j-i)%10,(i-j)%10)]+=1
 stats[tuple(sorted(offset.items())),tuple(sorted(middle.items()))]+=1
print('outer replacement pairs',len(pairs),'transported outer adjacency and middle matching index distances',stats)
assert len(pairs)==36
