"""Follow all maximum-partner choices from the fixed 22-prefix to termination."""
from collections import Counter
from random import Random
from ramsey_39_pattern_three_choices import add, options


def explore(n, pairs, ind):
    opts=options(n,pairs,ind)
    if not opts:return Counter({n:1}), []
    seven=[s for s in ind if s.bit_count()==7]
    miss=[sum(1<<j for j,s in enumerate(seven) if not s&p) for p in opts]
    scores=[sum(not (p&q) or not (m&t) for q,t in zip(opts,miss)) for p,m in zip(opts,miss)]
    best=max(scores); leaders=[p for p,k in zip(opts,scores) if k==best];hist=Counter();trace=None
    for p in leaders:
        nxt=add(n,p,pairs,ind)
        assert len({q% (1<<n) for q in options(n+1,*nxt)})==best
        h,path=explore(n+1,*nxt);hist.update(h)
        if trace is None or len(path)+1>len(trace):trace=[(n,len(opts),best,len(leaders),p)]+path
    return hist,trace

if __name__=='__main__':
    rng=Random(39);pairs=[];ind=[0]
    for n in range(22):pairs,ind=add(n,rng.choice(options(n,pairs,ind)),pairs,ind)
    hist,path=explore(22,pairs,ind);print(hist)
    for n,c,s,t,p in path:print(n,c,s,t,[i+1 for i in range(n) if p>>i&1])
