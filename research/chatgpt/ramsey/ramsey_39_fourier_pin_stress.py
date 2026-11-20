"""Exact tests of Walsh information in the pair-pin tensor; integer sums, no QFT."""
from itertools import product, combinations
from collections import defaultdict

def chi(s,x): return (-1)**((s & x).bit_count()%2)
def tensor(xs): return tuple(tuple(tuple(-chi(i,x)*chi(i,y) for i in (1,2,4)) for y in xs) for x in xs)
def audit(xs):
    t=tensor(xs); n=len(xs)
    for s in range(8):
        total=0
        for p,q in product(range(n),repeat=2):
            v=1
            for k in range(3):
                if s>>k&1:v*=-t[p][q][k]
            assert v==chi(s,xs[p]^xs[q]);total+=v
        assert total==sum(chi(s,x) for x in xs)**2
    return t
if __name__=='__main__':
    for xs in [list(range(8)),[*range(8),0],[0,3,5,6]*2+[0],[0]*9]:
        t=audit(xs);print('columns, profiles, pair labels:',len(xs),len(set(xs)),len({v for row in t for v in row}))
    a=[*range(8),0];b=[x^1 for x in a];assert audit(a)==audit(b);print('identical tensor, Walsh sums at mask 1:',[sum(chi(1,x) for x in z) for z in [a,b]])
    t=tensor(a);print('one flipped bit violates triangle parity:',(-t[0][1][0])*t[1][2][0]*t[2][0][0]!=-1)
    D={1,34,7,28,11,24,16,19};red=lambda a,b:(a-b)%35 in D
    pins=(0,1,2);cols=list(range(3,12));xs=[sum(red(v,p)<<k for k,p in enumerate(pins)) for v in cols];audit(xs)
    groups=defaultdict(dict)
    for i,j in combinations(range(9),2):groups[xs[i]^xs[j]].setdefault(red(cols[i],cols[j]),(cols[i],cols[j]))
    print('circle profiles',xs,'mixed labels',{k:v for k,v in groups.items() if len(v)>1})
