"""Test a necessary cut subset shared by all repairs using a given matching."""
from itertools import combinations
from r312_exact_triangle_cuts import adj,n,cover,mutual

def witness(g,p,k):
    if k==0:return ()
    while p.bit_count()>=k:
        b=p&-p;p^=b;v=b.bit_length()-1
        r=witness(g,p&~g[v],k-1)
        if r is not None:return (v,)+r
    return None

def run():
    base=adj.copy()
    for a,b in cover:base[a]|=1<<b;base[b]|=1<<a
    assert (0,3) in cover and base[24]&1 and base[24]&(1<<3)
    for w,rest in [(0,(2,4,5,7,9,12,17,19,22,39)),(3,(2,4,5,7,12,17,22,34,39,44))]:
        S=(24,w)+rest
        assert len(set(S))==12 and [(a,b) for a,b in combinations(S,2) if base[a]>>b&1]==[(24,w)]
    total=blocked=0
    for M in combinations(mutual,6):
        if len(set(sum((list(e) for e in M),[])))!=12:continue
        total+=1;g=base.copy()
        for a,b in M:g[a]&=~(1<<b);g[b]&=~(1<<a)
        r=witness(g,(1<<n)-1,12)
        if r:
            assert all(not(g[a]>>b&1) for a,b in combinations(r,2));blocked+=1
        print('M',M,'independent certificate',r)
    print('blocked',blocked,'of',total)
if __name__=='__main__':run()
