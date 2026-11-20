"""Audit every valid trial-2 seed and its prescribed first border (0-based positions)."""
from ramsey_39_disagreement import graph, valid, score
from random import Random
from itertools import combinations

order=list(range(35));Random(2).shuffle(order);S=order[:27];v=order[27];P=sum(1<<i for i in S)
print('next position',v)
for d in combinations(range(1,18),4):
    a=graph(d)
    if not valid(a,P):continue
    sets=[0]
    for i in S:sets += [s|1<<i for s in sets if not s&a[i]]
    pos=a[v]&P;octets=[s for s in sets if s.bit_count()==8];miss=[s for s in octets if not s&pos];tri=[(i,j) for i,j in combinations(S,2) if (pos>>i)&(pos>>j)&(a[i]>>j)&1]
    assert (not miss and not tri)==valid(a,P|1<<v)
    print(d,'scores',score(a,S),'octets,miss,triangles',len(octets),len(miss),len(tri),'valid at 35',valid(a,(1<<35)-1))
    if d==(2,6,7,17):
        print('positive neighbors',sorted(i for i in S if pos>>i&1));print('first obstruction',sorted(i for i in S if miss[0]>>i&1)+[v] if miss else tri[0]+(v,));print('arbitrary legal borders',sum(all(s&o for o in octets) for s in sets))
