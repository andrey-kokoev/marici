"""Derive each spine distance from cyclic clique constraints, not from valid masks.
Rooted patterns suffice by translation. Search short unsatisfiable clause families.
"""
from itertools import combinations
from random import Random
from ramsey_45_doubling_spine import distances

def patterns(k):
    d={}
    for t in combinations(range(1,24),k-1):
        ds=tuple(sorted(distances((0,)+t)));d.setdefault(ds,(0,)+t)
    return d

def prove():
    rng=Random(45);U=(1<<4096)-1;ones={i:sum(1<<m for m in range(4096) if m>>(i-1)&1) for i in range(1,13)}
    pats={k:patterns(k) for k in (4,5)}
    for target,pins in [(8,[]),(4,[8]),(2,[1,4,8])]:
        space=U^ones[target]
        for p in pins:space &= ones[p]
        c=[]
        for k,d in pats.items():
            for ds,t in d.items():
                m=space
                for i in ds:m &= ones[i] if k==4 else U^ones[i]
                if m:c.append((m,k,ds,t))
        c=[v for j,v in enumerate(c) if not any(v[0]&~w[0]==0 and (v[0]!=w[0] or j>i) for i,w in enumerate(c))];best=None
        for _ in range(250):
            rem=space;sel=[];rng.shuffle(c)
            while rem:
                v=max(c,key=lambda v:(rem&v[0]).bit_count());assert rem&v[0];sel.append(v);rem&=~v[0]
            for v in sel[:]:
                left=space
                for w in sel:
                    if w!=v:left&=~w[0]
                if not left:sel.remove(v)
            if best is None or len(sel)<len(best):best=sel
        print('force',target,'given',pins,'patterns',len(best));
        for _,k,ds,t in best:print(' R' if k==4 else ' B',ds,t)
if __name__=='__main__':prove()
