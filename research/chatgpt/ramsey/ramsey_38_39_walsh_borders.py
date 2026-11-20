"""Signed border moments by polynomial reduction, cross-checked by direct core enumeration."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from ramsey_38_cube_inversion import sign

def trial(k,ids,red):
    n=len(ids);A=[sum(1<<j for j,w in enumerate(ids) if j!=i and red(v,w)) for i,v in enumerate(ids)];full=(1<<n)-1
    ss=[0]
    for i,r in enumerate(A):ss += [s|1<<i for s in ss if not s&r]
    req=[s for s in ss if s.bit_count()==k-1];assert max(map(int.bit_count,ss))==k-1
    p={0:1}
    for t in req:
        q=p.copy()
        while t and q:
            b=t&-t;t-=b;r=A[b.bit_length()-1];o=Counter()
            for s,v in q.items():
                if not s&b:
                    o[s]+=v
                    if not s&r:o[s|b]-=v
            q={s:v for s,v in o.items() if v}
        for s,v in q.items():p[s]=p.get(s,0)-v
        p={s:v for s,v in p.items() if v}
    @lru_cache(None)
    def Z(m):
        if not m:return 1
        b=m&-m;return Z(m^b)+Z(m&~(b|A[b.bit_length()-1]))
    @lru_cache(None)
    def count(s):
        m=full^s;t=s
        while t:
            b=t&-t;t-=b;r=A[b.bit_length()-1]
            if r&s:return 0
            m&=~r
        return Z(m)
    def mon(t):return sum(v*count(t|s) for s,v in p.items())
    z=mon(0);c=[mon(1<<i) for i in range(n)];free=[i for i,a in enumerate(c) if 0<a<z];g=[s for s in ss if all(s&t for t in req)];assert z==len(g) and c==[sum(s>>i&1 for s in g) for i in range(n)]
    joint=[]
    for i,j in combinations(free,2):
        both=mon(1<<i|1<<j);h=z-2*(c[i]+c[j])+4*both;assert h==sum((-1)**((s>>i^s>>j)&1) for s in g);joint.append((ids[i],ids[j],both,h))
    return z,[ids[i] for i,a in enumerate(c) if a==z],[(ids[i],c[i]) for i in free],joint
if __name__=='__main__':
    res=[trial(8,[v for v in range(27) if v!=u],sign) for u in range(27)];print('3,8 histogram',sorted(Counter(r[0] for r in res).items()),flush=True);j=max(range(27),key=lambda i:res[i][0]);print('delete',j,res[j],flush=True)
    circ=lambda v,w:(v-w)%35 in (1,34,7,28,11,24,16,19)
    for omit in [(0,), (0,1)]:print('3,9 delete',omit,trial(9,[v for v in range(35) if v not in omit],circ),flush=True)
