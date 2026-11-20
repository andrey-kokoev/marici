"""Decode from a shared pair order with both (3,7) last-edge rules."""
import csv
from itertools import combinations
from pathlib import Path


def clique(rows, pool, k):
    if k == 0:return True
    while pool.bit_count() >= k:
        v=pool & -pool; pool ^= v
        if clique(rows,pool & rows[v.bit_length()-1],k-1):return True
    return False


def stream(n,order,source=None,payload=()):
    pos=[0]*n;neg=[0]*n;bits=[];counts=[0,0];it=iter(payload)
    for i,j in order:
        zero=bool(pos[i]&pos[j]);one=clique(neg,neg[i]&neg[j],5)
        assert not(zero and one)
        if zero or one:b=int(one);counts[b]+=1
        else:b=source[i][j] if source is not None else next(it);bits.append(b)
        if source is not None:assert source[i][j]==b
        rows=pos if b else neg;rows[i]|=1<<j;rows[j]|=1<<i
    assert next(it,None) is None
    return pos,bits,counts

if __name__=='__main__':
    with Path(__file__).with_name('ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));M=[list(map(int,r[1:])) for r in data];n=len(M);pairs=list(combinations(range(n),2));target=[sum(b<<i for i,b in enumerate(r)) for r in M]
    for label,order in [('original',sorted(pairs,key=lambda t:sorted(labels[i] for i in t))),('balanced',pairs)]:
        _,bits,counts=stream(n,order,M);rec,_,_=stream(n,order,payload=bits);assert rec==target
        print(label,len(bits),counts)
