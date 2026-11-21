"""Can cardinality propagation alone reject each putative independent seven?"""
from collections import Counter
from itertools import combinations
from ramsey_six_point_reconstruction import edges, tri, graph

fixed = graph((1 << len(edges)) - 1)
constraints = [(sum(1 << edges.index(e) for e in combinations(t, 2)), 1) for t in tri]
constraints += [(sum(1 << k for k,e in enumerate(edges) if i in e), 2) for i in range(15)]

def propagate(yes, no=0):
    while True:
        old = yes, no
        for mask, target in constraints:
            need = target - (yes & mask).bit_count()
            free = mask & ~(yes | no)
            if not 0 <= need <= free.bit_count(): return None
            if need == 0: no |= free
            elif need == free.bit_count(): yes |= free
        if old == (yes,no): return old

if __name__ == '__main__':
    counts=Counter(); example=None
    for S in combinations(range(22),7):
        vertices=sum(1<<v for v in S)
        if any(fixed[v]&vertices for v in S): counts['fixed edge']+=1; continue
        required=sum(1<<k for k,(i,j) in enumerate(edges) if i+7 in S and j+7 in S)
        state=propagate(required)
        if state is None: counts['propagation contradiction']+=1
        else:
            counts['stalled']+=1
            if example is None: example=(S,required,state)
    print(counts);print('first stall (0=root, 1..6 points, 7..21 lexicographic pairs):',example)
