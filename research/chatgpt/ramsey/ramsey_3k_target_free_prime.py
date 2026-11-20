"""Maximize cyclic order, then seek least odd prime with red iff tau(d) is a nonzero square. No complement or supplied offsets."""
from itertools import count
from math import comb,isqrt
from ramsey_45_modular_rule_trial import eta_product
from ramsey_45_modular_all_primes import factors

def red_masks(n,k):
    full=(1<<n)-1
    def bad(m,left,B):
        if not left:return True
        while m.bit_count()>=left:
            b=m&-m;m^=b
            if bad(m&B[b.bit_length()-1],left-1,B):return True
        return False
    def visit(i,d,h):
        if i>n//2:
            B=[full^(1<<j)^(((d<<j)|(d>>(n-j)))&full) for j in range(n)]
            if not bad(B[0],k-1,B):yield h
            return
        yield from visit(i+1,d,h)
        t=d|(1<<i)|(1<<(n-i))
        if not any(t&((t<<j)|(t>>(n-j))) for j in range(1,n) if t>>j&1):yield from visit(i+1,t,h|1<<(i-1))
    return set(visit(1,0,0))

def run(k):
    for n in range(comb(k+1,2)-1,0,-1):
        masks=red_masks(n,k)
        if masks:break
    a=eta_product([(1,24)],n//2)[1:];assert all(a);fs=[factors(x) for x in a];base=sorted(set(sum(fs,[])));exc={p for p in base if p>2}
    signrows=[sum(1<<j for j,b in enumerate(base) if f.count(b)%2) for f in fs]
    def feasible(m):
        piv={}
        for i,x in enumerate(signrows):
            y=1^((m>>i)&1)
            while x and x.bit_length() in piv:
                t,u=piv[x.bit_length()];x^=t;y^=u
            if not x and y:return False
            if x:piv[x.bit_length()]=x,y
        return True
    def squaremask(p):return sum(1<<i for i,x in enumerate(a) if pow(x%p,(p-1)//2,p)==1)
    possible=[m for m in masks if feasible(m)];ex=[p for p in exc if squaremask(p) in masks];print('k',k,'max order',n,'valid masks',len(masks),'consistent regular masks',len(possible),'exceptional hits',ex,flush=True)
    if not(possible or ex):print('no odd prime');return
    for p in count(3,2):
        if any(p%d==0 for d in range(3,isqrt(p)+1,2)):continue
        m=squaremask(p)
        if m in masks:print('least prime',p,'distances',[i+1 for i in range(len(a)) if m>>i&1],flush=True);return
if __name__=='__main__':
    for k in (7,8,9):run(k)
