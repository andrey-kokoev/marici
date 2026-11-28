"""Incremental update: old minimal lists, lost reasons, newly opened five-gates."""
from ga_chord_sweep import *
from ga_seam_v5 import mask,fl

def fivegate(a,g):
    f=fl[g];A=[v for v in range(14) if not (f|a[g-1]|a[g])>>v&1]
    return any(all(not a[i]>>j&1 for i,j in combinations(t,2)) for t in combinations(A,5))

def reopened_moves(a,g):
    f=fl[g];base=[v for v in range(14) if not f>>v&1];W={mask(t) for t in combinations(base,6) if all(not a[i]>>j&1 for i,j in combinations(t,2))};out=[]
    for p in range(32):
        N=f|(p<<9)
        if any(a[i]>>j&1 and mask((i,j))!=f for i,j in combinations([v for v in range(14) if N>>v&1],2)):continue
        w=frozenset(b for b in W if not b&N)
        if w:out.append(w)
    return out
if __name__=='__main__':
    st=Counter();example=None
    for c in range(1024):
        a=graph(9,S,c)
        if not check(a,16383,3,7):continue
        D=demands(S,c);F=minimal(set(D.values()));reasons={m:[v for v in F if v<=w] for m,w in D.items() if w not in F};gates=[g for g in range(1,9) if fivegate(a,g)]
        for i,j in combinations(range(9),2):
            if j==i+1 or a[i]&a[j]:continue
            h=a.copy();h[i]|=1<<j;h[j]|=1<<i;ch=mask((i,j));trim=lambda w:frozenset(b for b in w if b&ch!=ch)
            core={trim(v) for v in F}-{frozenset()};orig=core.copy();st['discarded entries']+=len(reasons)
            for m,rs in reasons.items():
                if not any(trim(v) for v in rs):
                    st['flagged']+=1;t=trim(D[m]);
                    if t:core.add(t)
            repaired=minimal(core);opened=[g for g in gates if not fivegate(h,g)]
            for g in opened:core.update(reopened_moves(h,g))
            final=minimal(core);assert final==minimal(set(chord_demands(c,i,j).values()));st['cases']+=1;st['has opened gap']+=bool(opened);st['old lists need restoration']+=repaired!=minimal(orig);st['opened gap changes result']+=final!=repaired
            if final!=repaired and example is None:example=(c,i+1,j+1,opened,sorted(map(sorted,final-repaired)))
    print(st,example)
