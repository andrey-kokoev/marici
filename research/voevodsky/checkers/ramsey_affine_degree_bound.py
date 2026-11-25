"""First-principles scalar induction. No graph, coloring, or degree sequence generation. Exact affine lower supports (integer slopes) for d^2 + residual bound."""
from functools import cache
from math import inf

@cache
def lower(n,k):
    if n==0 or n<k:return 0
    if k<=1:return inf
    if lower(n-1,k)==inf:return inf
    costs=[(d,d*d+lower(n-1-d,k-1)) for d in range(min(n-1,k-1)+1)]
    costs=[(d,c) for d,c in costs if c!=inf]
    if not costs:return inf
    lo=lower(n-1,k); hi=n*max(d for d,_ in costs)//2
    for a in range(-2*n,2*n+1):
        b=min(c-a*d for d,c in costs);coef=n-2*a
        if coef>0:lo=max(lo,-((-n*b)//coef))
        elif coef<0:hi=min(hi,n*b//coef)
        elif b>0:return inf
    return lo if lo<=hi else inf

if __name__=='__main__':
    for k in range(3,11):
        n=next(n for n in range(k,80) if lower(n,k)==inf)
        print(k,n,lower(n-1,k))
