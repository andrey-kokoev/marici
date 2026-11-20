"""All odd primes for the nonzero-square rule at distances 1..12 (both orientations).
Enumerate a superset of possible Legendre-sign assignments outside the divisors
of the coefficients. Handle all exceptional odd primes by direct modular powers.
For witness search or negative certification precompute forbidden clique distance masks.
"""
from itertools import combinations
from math import prod
from ramsey_45_modular_rule_trial import eta_product, count

def factors(x):
    d=2;n=abs(x);f=[]
    while d*d<=n:
        while n%d==0:f.append(d);n//=d
        d+=1
    if n>1:f.append(n)
    return ([-1] if x<0 else [])+f

def main():
    a=eta_product([(1,24)],12)[1:];fs=[factors(x) for x in a];assert [prod(f) for f in fs]==a
    base=sorted(set(sum(fs,[]))); exc=[d for d in base if d>2];full=(1<<12)-1
    def forbidden(k):
        out=set()
        for t in combinations(range(1,24),k-1):
            mask=0
            for i,j in combinations((0,)+t,2):mask|=1<<(min(j-i,24-j+i)-1)
            out.add(mask)
        return out
    red,blo=forbidden(4),forbidden(5);valid={m for m in range(full+1) if all(m&t!=t for t in red) and all(m&t for t in blo)}
    parity=[sum(1<<i for i,b in enumerate(base) if f.count(b)%2) for f in fs];possible=set()
    for s in range(1<<len(base)):
        m=sum(1<<i for i,p in enumerate(parity) if (p&s).bit_count()%2==0);possible.update([m,m^full])
    for p in exc:
        m=sum(1<<i for i,x in enumerate(a) if pow(x%p,(p-1)//2,p)==1);possible.update([m,m^full])
    print('factors',base,'exceptional primes',exc,'valid cyclic masks',len(valid),'candidate masks',len(possible),'intersection',sorted(valid&possible))
    hits=valid&possible
    if hits:
        for p in range(3,100000,2):
            if any(p%d==0 for d in range(3,int(p**0.5)+1,2)):continue
            m=sum(1<<i for i,x in enumerate(a) if pow(x%p,(p-1)//2,p)==1)
            for mode,z in [('square',m),('complement',m^full)]:
                if z in hits:
                    ds={i+1 for i in range(12) if z>>i&1};print('first actual hit',p,mode,sorted(ds),count(ds,4),count(set(range(1,13))-ds,5));return
if __name__=='__main__':main()
