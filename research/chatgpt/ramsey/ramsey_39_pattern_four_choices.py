"""Replay to 25; exhaust the remaining tree, including non-leading ties."""
from collections import Counter
from random import Random
from ramsey_39_pattern_three_choices import add,options

def leaves(n,pairs,ind):
    opts=options(n,pairs,ind)
    if not opts:return Counter({n:1})
    result=Counter()
    for p in opts:result.update(leaves(n+1,*add(n,p,pairs,ind)))
    return result

if __name__=='__main__':
    rng=Random(39);pairs=[];ind=[0]
    for n in range(25):
        p=rng.choice(options(n,pairs,ind));pairs,ind=add(n,p,pairs,ind)
    opts=options(25,pairs,ind);original=rng.choice(opts)
    for p in opts:
        child=add(25,p,pairs,ind);print([i+1 for i in range(25) if p>>i&1],p==original,len(options(26,*child)),dict(leaves(26,*child)))
    u=0;c=opts[0]
    for p in opts:u|=p;c&=p
    print('common pos',[i+1 for i in range(25) if c>>i&1]);s=max((s for s in ind if not s&u),key=int.bit_count);print('common neg set',[i+1 for i in range(25) if s>>i&1])
