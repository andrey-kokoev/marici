"""Exhaust the 44 first borders. Group by first choice, preserve labelled order."""
from collections import Counter
from random import Random
from ramsey_39_pattern_three_choices import add,options

def run():
    rng=Random(39);pairs=[];ind=[0]
    for n in range(24):
        p=rng.choice(options(n,pairs,ind));pairs,ind=add(n,p,pairs,ind)
    opts=options(24,pairs,ind);original=rng.choice(opts);groups=Counter();hist=Counter();best=[]
    def tree(n,choices,fam,path,leaves):
        nonlocal best
        if not choices:
            leaves[n]+=1
            if len(path)>len(best):best=path
            return
        for p in choices:
            missed=[s for s in fam[7] if not p&s];bit=1<<n;child=[]
            for q in choices:
                if not p&q:child.append(bit|q)
                if all(s&q for s in missed):child.append(q)
            nxt=[fam[0]]+[fam[k]+[s|bit for s in fam[k-1] if not s&p] for k in range(1,8)] if child else None
            tree(n+1,child,nxt,path+[p],leaves)
    for p in opts:
        pair2,ind2=add(24,p,pairs,ind);leaves=Counter();tree(25,options(25,pair2,ind2),[[s for s in ind2 if s.bit_count()==k] for k in range(8)],[p],leaves);groups[max(leaves)]+=1;hist.update(leaves)
        if p==original:assert leaves=={27:12}
    print('first choices by maximum',groups,'terminal histories',hist)
    for n,p in enumerate(best,24):
        assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
    assert not options(24+len(best),pairs,ind)
if __name__=='__main__':run()
