"""Elementary recursive edge lower bounds from triangle-free degree deficiencies.
B[k,n] bounds graphs of order n with alpha < k. None denotes impossible.
"""
from functools import lru_cache
from math import inf
@lru_cache(None)
def bound(n,k):
    if n==0:return 0
    if k<=1:return inf
    if n<k:return 0
    ds=[(d,d*d+bound(n-d-1,k-1)) for d in range(min(k-1,n-1)+1)]
    ds=[(d,c) for d,c in ds if c<inf]
    dp={0:0}
    for _ in range(n):
        nxt={}
        for s,total in dp.items():
            for d,c in ds:
                t=s+d;v=total+c
                if v<nxt.get(t,inf):nxt[t]=v
        dp=nxt
    return min((s//2 for s,v in dp.items() if s%2==0 and n*(s//2)>=v),default=inf)
if __name__=='__main__':
    print('order 39 alpha<10 lower bound:',bound(39,10));print('nonneighbor bounds:',[(d,bound(38-d,9)) for d in range(10)]);print('edge budget at depth 2 for 11 coordinates:',11**2)
