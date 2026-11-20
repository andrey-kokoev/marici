"""Characterize all successful nonexceptional primes by binary linear equations."""
from ramsey_45_modular_all_primes import factors
from ramsey_45_modular_rule_trial import eta_product
from math import prod,isqrt

a=eta_product([(1,24)],12)[1:];D={1,2,4,8,9};fs=list(map(factors,a));B=sorted(set(sum(fs,[])));rows=[]
for i,f in enumerate(fs,1):rows.append([sum(1<<j for j,b in enumerate(B) if f.count(b)%2),int(i not in D)])
r=0
for j in range(len(B)):
    k=next((k for k in range(r,len(rows)) if rows[k][0]>>j&1),None)
    if k is None:continue
    rows[k],rows[r]=rows[r],rows[k]
    for k in range(len(rows)):
        if k!=r and rows[k][0]>>j&1:rows[k]=[x^y for x,y in zip(rows[k],rows[r])]
    r+=1
assert all(v==0 for m,v in rows if not m)
conditions=[(prod(b for j,b in enumerate(B) if m>>j&1),(-1)**v) for m,v in rows if m];print('rank',r,'conditions',conditions)
def prime(p):return all(p%j for j in range(2,isqrt(p)+1))
hits=[];exceptional=[]
for p in range(3,100001,2):
    if not prime(p):continue
    red={i for i,x in enumerate(a,1) if pow(x,(p-1)//2,p)==1}
    if p in B:
        if red==D:exceptional.append(p)
    else:assert (red==D)==all(pow(b,(p-1)//2,p)==v%p for b,v in conditions)
    if red==D:hits.append(p)
print('exceptional hits',exceptional,'hits through 100000',len(hits),'first ten',hits[:10])
