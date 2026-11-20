"""Optimize cyclic order first, then minimize prime. No exact Ramsey value, target order, offsets or prime supplied."""
from itertools import combinations,count
from math import comb,isqrt
from ramsey_45_modular_rule_trial import eta_product

def cyclic(n,r,s):
    h=n//2;size=1<<h;full=(1<<size)-1
    # One bit per possible red-distance mask. Column j flags masks with j red.
    cols=[(full//((1<<(2*b))-1))*(((1<<b)-1)<<b) for b in [1<<j for j in range(h)]]
    live=full
    for k,red in [(r,True),(s,False)]:
        seen=set()
        for t in combinations(range(1,n),k-1):
            ds=frozenset(min(j-i,n-j+i)-1 for i,j in combinations((0,)+t,2))
            if ds in seen:continue
            seen.add(ds);bad=live
            for j in ds:bad &= cols[j] if red else full^cols[j]
            live ^= bad
            if not live:return set()
    out=set()
    while live:
        b=live&-live;out.add(b.bit_length()-1);live^=b
    return out

def run(r,s):
    for n in range(comb(r+s-2,r-1)-1,0,-1):
        masks=cyclic(n,r,s);print(n,len(masks),flush=True)
        if masks:break
    a=eta_product([(1,24)],n//2)[1:]
    for p in count(3,2):
        if any(p%d==0 for d in range(3,isqrt(p)+1,2)):continue
        mask=sum(1<<i for i,x in enumerate(a) if pow(x,(p-1)//2,p)==1)
        if mask in masks:print('least odd prime at maximum cyclic order:',p);return
if __name__=='__main__':run(4,5)
