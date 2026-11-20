"""Hide three from the order-35 cyclic witness. Enumerate borders blind to the deleted signs."""
from itertools import product
from collections import Counter

D={1,7,11,16,19,24,28,34}
def sign(i,j):return (i-j)%35 in D

def complete(out):
    I=[0]
    for j,v in enumerate(out):
        p=sum(1<<i for i in range(j) if sign(v,out[i]));assert p in I
        I += [s|1<<j for s in I if not s&p]
    assert max(s.bit_count() for s in I)==8
    seven=[s for s in I if s.bit_count()==7];six=[s for s in I if s.bit_count()==6]
    opts=I
    for s in I:
        if s.bit_count()==8:opts=[p for p in opts if p&s]
    perm=[out.index(-v%35) for v in out]
    inv=lambda p:sum((p>>i&1)<<j for i,j in enumerate(perm));fixed=[p for p in opts if inv(p)==p];sol=set()
    for p,q in product(opts,fixed):
        r=inv(p); assert r in opts
        def pair(x,y,b):return not x&y if b else all(s&(x|y) for s in seven)
        for b,c in product((0,1),repeat=2):
            if b and c:continue
            if not(pair(p,q,b) and pair(q,r,b) and pair(p,r,c)):continue
            if not(b or c) and any(not s&(p|q|r) for s in six):continue
            sol.add((p,q,r,b,c))
    return len(opts),len(fixed),sol

if __name__=='__main__':
    counts=Counter()
    for t in range(1,18):
        out=[i for i in range(35) if i not in (t,0,35-t)];cnt,fix,sol=complete(out)
        p,q,r=[sum(int(sign(i,u))<<j for j,i in enumerate(out)) for u in (t,0,35-t)];b=int(sign(t,0));c=int(sign(t,-t));assert (p,q,r,b,c) in sol
        counts[cnt,fix,len(sol),sol=={(p,q,r,b,c),(r,q,p,b,c)}]+=1
    print(counts)
