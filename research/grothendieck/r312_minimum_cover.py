"""Exact minimum additions to kill old 12-sets, before triangle repair."""
from r312_nearmiss_cover import old,n,adj
from itertools import combinations
from functools import lru_cache
edges={}
for u,v in combinations(range(n),2):
    mask=sum(1<<i for i,s in enumerate(old) if s>>u&1 and s>>v&1)
    if mask: edges[mask]=(u,v)
rows=[[m for m in edges if m>>i&1] for i in range(len(old))]
@lru_cache(None)
def solve(U,k):
    if not U:return ()
    if U.bit_count()>8*k:return None
    floor=max(1,U.bit_count()-8*(k-1))
    opts=None
    bits=U
    while bits:
        b=bits&-bits;bits^=b
        choices=[m for m in rows[b.bit_length()-1] if (m&U).bit_count()>=floor]
        # A low-gain edge may be required for this row even if other rows
        # admit larger gains, but every edge must clear the capacity floor.
        if opts is None or len(choices)<len(opts):opts=choices
        if not opts:return None
    for m in sorted(opts,key=lambda x:-(x&U).bit_count()):
        tail=solve(U&~m,k-1)
        if tail is not None:return (m,)+tail
    return None
if __name__=='__main__':
    U=(1<<len(old))-1
    for k in range(7,10):
        # Rotation sends any first edge to (0,d) for d <= 24.
        for d in range(1,25):
            m=sum(1<<i for i,s in enumerate(old) if s&1 and s>>d&1)
            if not m:continue
            tail=solve(U&~m,k-1)
            if tail is not None:
                witness=[(0,d)]+[edges[t] for t in tail]
                assert all(any(s>>a&1 and s>>b&1 for a,b in witness) for s in old)
                print('minimum',k,'cover',witness,flush=True);quit()
        print('excluded',k,flush=True)
