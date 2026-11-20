"""Classify XOR-zero quadruples for every independent normalized pair of extra Boolean functions."""
from collections import Counter
from itertools import combinations
from functools import reduce
from operator import xor
free=(3,5,6,7);hist=Counter()
for f,g in combinations(range(1,16),2):
    lift=[j|(((f>>free.index(j)&1)<<3)|((g>>free.index(j)&1)<<4) if j in free else 0) for j in range(8)]
    flats=[set(t) for t in combinations(range(8),4) if not reduce(xor,(lift[i] for i in t))]
    key=len(flats),len(set.union(*flats)),len(set.intersection(*flats)),tuple(sorted(len(x&y) for x,y in combinations(flats,2)));hist[key]+=1
assert hist=={(2,8,0,(0,)):21,(3,6,0,(2,2,2)):84};print(hist)
