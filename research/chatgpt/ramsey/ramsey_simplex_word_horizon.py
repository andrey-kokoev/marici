"""Worst-case forward word length with no address reset, independently checked by Bellman recursion."""
from collections import Counter
from functools import lru_cache
from ramsey_39_simplex_phase_depth import layer,phase,M

@lru_cache(None)
def supports(x,k):
    if not k:return True
    for i in range(4):
        if x[i]==0:return False
        y=list(x);y[i]-=1;y[(i+1)%4]+=1
        if not supports(tuple(y),k-1):return False
    return True

if __name__=='__main__':
    assert [len({phase(x) for x in layer(r)}) for r in range(7)]==[1,4,10,18,27,33,35]
    for n in (12,16,24,32):
        best=[-1]*M
        for x in layer(n):
            h=min(x);assert supports(x,h) and not supports(x,h+1)
            best[phase(x)]=max(best[phase(x)],h)
        assert min(best)==(n-6)//4
        print(n, 'guaranteed',min(best),'phase histogram',sorted(Counter(best).items()))
