"""Start with no addresses. Only target sizes, tie seed and trial budget are inputs.
Maintain the families of monochromatic sets; each new row must hit all old
negative (k-1)-sets and contain no positive (l-1)-set. Bit i means + to i.
"""
from random import Random
from collections import Counter
from itertools import combinations


def trial(l,k,seed):
    rng=Random(seed); plus=[0]; minus=[0]; rows=[]; history=[]
    while True:
        n=len(rows);full=(1<<n)-1
        forbid=[s for s in plus if s.bit_count()==l-1];hit=[s for s in minus if s.bit_count()==k-1]
        # For l=3 every permissible plus-neighborhood is already in minus.
        candidates=(minus if l==3 else (p for p in range(full+1) if all(s&p!=s for s in forbid)))
        opts=[p for p in candidates if all(p&s for s in hit)]
        if not opts:return rows,history
        p=rng.choice(opts);history.append((len(opts),p));m=full^p
        plus += [(1<<n)|s for s in plus if not s&~p];minus += [(1<<n)|s for s in minus if not s&~m]
        rows=[r|(((p>>i)&1)<<n) for i,r in enumerate(rows)]+[p]

if __name__=='__main__':
    l,k=3,5;hist=Counter();best=-1
    for seed in range(512):
        g,h=trial(l,k,seed);hist[len(g)]+=1
        if len(g)>best:best=len(g);winner=seed;example=h
    print('terminal orders',sorted(hist.items()),'best seed',winner,'history (#choices, chosen mask)',example)
    g,_=trial(l,k,winner)
    for size,color in [(l,1),(k,0)]:assert not any(all((g[i]>>j&1)==color for i,j in combinations(t,2)) for t in combinations(range(len(g)),size))
