"""Monotone common-neighbor certificate against any border-only path to 35."""
from random import Random
from ramsey_39_disagreement import graph
from ramsey_39_fixed_seed_exact import B

def partners(A,S,v):
    mask=sum(1<<i for i in S)
    return sorted(w for w in S if w!=v and (A[v]&A[w]&mask).bit_count()>=3)

if __name__=='__main__':
    order=list(range(35));Random(2).shuffle(order);S=order[:27]
    A=graph((2,6,7,17));p=partners(A,S,18)
    limit=max(len(partners(B,range(35),v)) for v in range(35))
    print('host limit:',limit,'seed partners of 18:',p);assert len(p)>limit
