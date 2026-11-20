"""Find largest valid circle without a seed. Uses R(3,8)=28 to bound the starting order."""
from itertools import combinations
from math import gcd

def audit(n):
    # Positive degree <=8, negative degree <=27. Thus n<=36. At 35 or 36,
    # closed-under-negation distance sets have degree 8 (no antipode at 36).
    out=[];tri=0;tested=0
    for D in combinations(range(1,(n+1)//2),4):
        tested+=1;S={s%n for d in D for s in (d,-d)}
        if any((x+y)%n in S for x in S for y in S):continue
        tri+=1
        # By translation any negative nine-set can be moved to contain 0.
        I=[1]
        for j in range(1,n):
            neigh=sum(1<<i for i in range(j) if (j-i)%n in S)
            new=[p|1<<j for p in I if not p&neigh]
            if any(p.bit_count()==9 for p in new):break
            I+=new
        else:out.append(D)
    print(n,'tested',tested,'triangle-free',tri,'valid',out);return out
if __name__=='__main__':
    assert not audit(36);sol=audit(35);d=sol[0];orbit={tuple(sorted(min(u*i%35,-u*i%35) for i in d)) for u in range(35) if gcd(u,35)==1};assert orbit==set(sol);print('one multiplier orbit')
