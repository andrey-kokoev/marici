"""Count free orientation bits after local comparisons in four circular frames."""
from itertools import combinations
import random

def count(orders):
    parent={e:e for e in combinations(range(20),2)}
    def root(e):
        while parent[e]!=e:e=parent[e]
        return e
    out=[]
    for o in orders:
        for i in range(20):
            for d in range(1,11):
                a=tuple(sorted((o[i],o[(i-d)%20])));b=tuple(sorted((o[i],o[(i+d)%20])))
                parent[root(a)]=root(b)
        out.append(len({root(e) for e in parent}))
    return out

if __name__=='__main__':
    v=list(range(20));print('quarter-turn',count([v[5*i:]+v[:5*i] for i in range(4)]))
    # A second order-four action: one position shift in each consecutive block of four.
    print('block turns',count([[4*(i//4)+(i+j)%4 for i in v] for j in range(4)]))
    perm=v.copy();shuffled=v.copy();random.Random(37).shuffle(shuffled)
    for k in range(0,20,4):
        block=shuffled[k:k+4]
        for i,p in enumerate(block):perm[p]=block[(i+1)%4]
    orders=[v]
    for _ in range(3):orders.append([perm[i] for i in orders[-1]])
    print('shuffled block turns',count(orders))
