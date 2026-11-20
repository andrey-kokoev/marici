"""Order 24: both orientations of the nonzero-square rule, odd primes <=97."""
from ramsey_45_modular_rule_trial import eta_product, count
from itertools import combinations

D=set(range(1,13)); EVEN=set(range(2,13,2))
primes=[p for p in range(3,98,2) if all(p%i for i in range(2,int(p**0.5)+1))]
rows=[]; rejected=0
for name,factors in [('eta24',[(d,1) for d in (2,4,6,12)]),('Delta',[(1,24)])]:
    a=eta_product(factors,12)
    for p in primes:
        squares={j*j%p for j in range(1,p)};r={d for d in D if a[d]%p in squares}
        for label,red in [('square',r),('complement',D-r)]:
            if not red&EVEN or EVEN<=red:rejected+=1;continue
            k4,k5=count(red,4),count(D-red,5);rows.append((k4+k5,k4,k5,name,p,label,sorted(red)))
print('rules',4*len(primes),'rejected',rejected,'tested',len(rows),'distinct survivors',len({tuple(r[-1]) for r in rows}),'valid',sum(r[0]==0 for r in rows))
best=min(r[0] for r in rows)
for r in rows:
    if r[0]==best:
        print('best',r);red=set(r[-1]);dist=lambda x,y:min(y-x,24-y+x)
        for k,col,expected in [(4,True,r[1]),(5,False,r[2])]:
            total=sum(all((dist(x,y) in red)==col for x,y in combinations(t,2)) for t in combinations(range(24),k));assert total==expected
