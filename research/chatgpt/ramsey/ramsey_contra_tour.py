"""Second pass with inverse sector steps: literal retrace, same order, or one route exchange."""
from collections import Counter
from functools import lru_cache
from math import factorial
from ramsey_twelve_sector_return import moves,mul

def inv(q):return q if abs(q)==1 else -q
@lru_cache(None)
def pairs(mask):
    if not mask:return Counter({(1,1):1})
    r=Counter()
    for i,s in enumerate(moves):
        if mask>>i&1:
            for (p,q),cnt in pairs(mask^(1<<i)).items():r[mul(p,s),mul(q,inv(s))]+=cnt
    return r

def prod(ms):
    p=1
    for s in ms:p=mul(p,s)
    return p

if __name__=='__main__':
    ps=pairs((1<<12)-1);out=Counter()
    for (p,q),c in ps.items():out[mul(p,q)]+=c;assert mul(p,inv(p))==1
    assert out=={1:factorial(12)};print('same sector order, inverse steps:',dict(out))
    ns=Counter()
    for i,a in enumerate(moves):
        for j,b in enumerate(moves[i+1:],i+1):
            path=[a,b]+[x for k,x in enumerate(moves) if k not in (i,j)];back=list(map(inv,reversed(path)));back[-2:]=back[-2:][::-1];z=mul(prod(path),prod(back));assert z==(1 if abs(a)==abs(b) else -1);ns[z]+=1
    print('one exchanged neighboring pair in the retrace (sector pairs):',dict(ns))
