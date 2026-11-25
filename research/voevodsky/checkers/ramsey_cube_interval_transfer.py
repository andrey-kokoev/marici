"""Exact transfer of path supports by missed-cut endpoints, last bit and cardinality."""
from collections import Counter
from itertools import product

def step(states,i):
    out=Counter()
    for (lo,hi,last,size),count in states.items():
        for odd,even in ((0,0),(1,0),(0,1)):
            if last and odd:continue
            # hi=0 means no selected odd vertex (unbounded upper endpoint).
            out[i if even else lo, (hi or i) if odd else hi, even,size+odd+even]+=count
    return out

def bounds(mask,m):
    return (max((i for i in range(1,m+1) if mask>>(2*i-1)&1),default=0),min((i for i in range(1,m+1) if mask>>(2*i-2)&1),default=0))

def profile(states,s,m):
    a,b=bounds(s,m);p=Counter()
    for (c,d,_,n),v in states.items():
        if max(a,c)>=min(b or m+1,d or m+1):p[n]+=v
    return [p[i] for i in range(m+1)]

if __name__=='__main__':
    states=Counter({(0,0,0,0):1})
    for m in range(1,8):
        states=step(states,m);domain=[t for t in range(1<<(2*m)) if not t&(t<<1)];mx=[t for t in domain if t.bit_count()==m];assert len(mx)==m+1
        assert states==Counter((*bounds(t,m),t>>(2*m-1),t.bit_count()) for t in domain)
        if m<6:continue
        for corner in [(1,6,11),(1,7,11)]:
            s=sum(1<<(v-1) for v in corner);p=profile(states,s,m);direct=Counter(t.bit_count() for t in domain if all((t|s)&u for u in mx));assert p==[direct[i] for i in range(m+1)];print(2*m,corner,p,sum(p))
