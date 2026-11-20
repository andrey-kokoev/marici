"""3x8 torus: row shift, column shift and simultaneous reflection. A cell is
an address; the 3x8 binary input gives links by displacement, not by adjacency of cells.
Enumerate kernels and test all three-address borders jointly."""
from itertools import product,combinations_with_replacement
from collections import Counter
from functools import lru_cache


def audit():
    n=24;coords=[(i%3,i%8) for i in range(n)];stats=Counter();witness=None
    # For a translation invariant valid graph degree <=7; triangles are forbidden.
    for mask in range(1<<12):
        S={s for s in range(1,n) if mask>>(min(s,n-s)-1)&1}
        if len(S)>7 or any((a-b)%n in S for a in S for b in S):continue
        independent=[0];rows=[]
        for i in range(n):
            row=sum(1<<j for j in range(i) if (i-j)%n in S);rows.append(row);new=[s|1<<i for s in independent if not s&row]
            if any(s.bit_count()==8 for s in new):break
            independent+=new
        else:
            stats['valid24']+=1
            if stats['valid24']==1:print('example positive displacements:',sorted(coords[s] for s in S))
            L={k:[s for s in independent if s.bit_count()==k] for k in (5,6,7)};o=[p for p in independent if all(p&s for s in L[7])]
            if o:stats['reach25']+=1
            if not o:continue
            miss={k:[sum(1<<i for i,s in enumerate(L[k]) if not p&s) for p in o] for k in (5,6)}
            T=[[tuple(v for v,ok in [(1,not(p&q)),(0,not(miss[6][i]&miss[6][j]))] if ok) for j,q in enumerate(o)] for i,p in enumerate(o)]
            if any(T[i][j] for i,j in combinations_with_replacement(range(len(o)),2)):stats['reach26']+=1
            for i,j,k in combinations_with_replacement(range(len(o)),3):
                sol=next((v for v in product(T[i][j],T[i][k],T[j][k]) if sum(v)!=3 and (any(v) or not(miss[5][i]&miss[5][j]&miss[5][k]))),None)
                if sol is not None:
                    stats['reach27']+=1
                    if witness is None:witness=(S,(o[i],o[j],o[k]),sol)
                    break
    print(stats,'first witness',witness)
if __name__=='__main__':audit()
