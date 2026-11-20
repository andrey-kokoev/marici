"""Exact leave-one-orbit-out trial on reflected record 174. Run with uv run --with sympy."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sympy as sp
from pauli_realization_audit import decode_graph6, triangle_free, independent_witness

@lru_cache(None)
def odd(rows):
    m=sp.Matrix(11,11,lambda i,j:((rows[2*i]>>(2*j))&1)-((rows[2*i]>>(2*j+1))&1));return 11-m.rank()

def flip(rows,edges):
    a=list(rows)
    for i,j in edges:a[i]^=1<<j;a[j]^=1<<i
    return tuple(a)

def main():
    path=Path(__file__).parent/'pauli-realization-catalogues/r37_22.g6'
    base=tuple(decode_graph6(path.read_text().splitlines()[173]));assert triangle_free(base) and independent_witness(base,7) is None
    pairs=list(combinations(range(22),2));orbits=sorted({tuple(sorted({(i,j),tuple(sorted((i^1,j^1)))})) for i,j in pairs}); assert all(len({(base[i]>>j)&1 for i,j in o})==1 for o in orbits)
    # Any new independent seven after a deletion contains a deleted edge.
    trials=Counter();outcomes=Counter();example=None
    for cut in orbits:
        if not all(base[i]>>j&1 for i,j in cut):continue
        a=flip(base,cut); dangers=set()
        for i,j in cut:
            pool=[v for v in range(22) if v not in (i,j) and not((a[i]|a[j])>>v&1)]
            for t in combinations(pool,5):
                if all(not(a[u]>>v&1) for u,v in combinations(t,2)):dangers.add(sum(1<<v for v in (i,j,*t)))
        if not dangers:trials['already valid']+=1;continue
        trials['needs repair']+=1; cand=[];start=odd(a)
        for add in orbits:
            if any(a[i]>>j&1 for i,j in add):continue
            if any(a[i]&a[j] for i,j in add):continue
            b=flip(a,add);assert triangle_free(b) # reflected edges in one orbit are disjoint
            leftover=sum(not any(mask>>i&1 and mask>>j&1 for i,j in add) for mask in dangers)
            assert (leftover==0)==(independent_witness(b,7) is None)
            delta=odd(b)-start;outcomes[delta,leftover==0]+=1;cand.append((add,delta,leftover))
        if example is None:
            for good in cand:
                for bad in cand:
                    if good[1]==bad[1] and good[2]==0 and bad[2]>0:
                        example=cut,start,len(dangers),good,bad;break
                if example:break
    print('trials',trials,'outcomes (odd nullity delta, successful)',sorted(outcomes.items()),'example',example)

if __name__=='__main__':main()
