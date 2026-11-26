"""Minimum shellable completion on the existing labels. No coordinates or cube template."""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter
from ramsey38_support_shell import N

P=sorted(N[1]); outside=set(N)-{1}-set(P)
rows={frozenset(N[v]&set(P)) for v in outside}
assert len(rows)==19 and set(map(len,rows))=={1,2,3,4}
tets=list(map(frozenset,combinations(P,4)))
forced={s for s in rows if len(s)==4}; pool=[s for s in tets if s not in forced]

def shelling(ts):
    @lru_cache(None)
    def peel(left):
        if len(left)==1:return tuple(left)
        for t in sorted(left,key=lambda s:tuple(sorted(s))):
            rest=left-{t}; hits=[t&u for u in rest]; facets=[h for h in hits if len(h)==3]
            # Attach along 1, 2 or 3 boundary triangles (a disk), with no stray edges or points.
            if not 1<=len(facets)<=3 or len(set(facets))!=len(facets):continue
            if not all(any(h<=f for f in facets) for h in hits):continue
            order=peel(rest)
            if order:return order+(t,)
        return ()
    return peel(frozenset(ts))

def fmt(sets):return ' '.join(str(tuple(sorted(s))) for s in sets)
if __name__=='__main__':
    for k in range(6):
        winners=[]
        for extra in combinations(pool,k):
            ts=forced.union(extra)
            if not all(any(r<=t for t in ts) for r in rows):continue
            order=shelling(ts)
            if order:winners.append((extra,order))
        print('added',k,'solutions',len(winners))
        if winners:
            sym=[]
            for perm in permutations(P):
                m=dict(zip(P,perm)); image=lambda s:frozenset(m[v] for v in s)
                if {image(r) for r in rows}==rows:sym.append(m)
            def orbit(extra):return {frozenset(frozenset(m[v] for v in t) for t in extra) for m in sym}
            print('support symmetries:',len(sym),'orbits:',len({frozenset(orbit(e)) for e,_ in winners}))
            extra,order=winners[0];print('example added:',fmt(extra),'shelling:',fmt(order));faces=Counter(f for t in order for f in combinations(sorted(t),3));bd=[f for f,n in faces.items() if n==1];print('boundary triangles:',len(bd),'boundary at 5,14:',[f for f in bd if {5,14}<=set(f)],'boundary at 11:',[f for f in bd if 11 in f]);break
