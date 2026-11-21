"""Exact independent-set extension formula from the antipodal cube to all 22 vertices."""
from itertools import combinations,product
from collections import Counter
from ramsey_cube_core import rim,hub,adj

def subsets(S):
    S=sorted(S)
    for k in range(len(S)+1):yield from map(frozenset,combinations(S,k))

def core_sets():
    for H in subsets(hub):
        if any(adj[h]&H for h in H):continue
        R=rim-set().union(*(adj[h] for h in H))
        for C in subsets(R):
            if not any(adj[c]&C for c in C):yield H|C

if __name__=='__main__':
    cores=list(core_sets());print('core sets',Counter(map(len,cores)))
    for second,third in product(['c','d'],['ab','cd']):
        X={'a',second,third};Y={'a','b','c','d','ab','cd'}-X;bounds=[0]*3;winners=[]
        for K in cores:
            for twins in ((),(X,),(Y,),(X,Y)):
                if any(t&K for t in twins):continue
                for anchor in ([False] if twins else [False,True]):
                    used=set(''.join(K));used.update('ef' if twins else '');used.update('abcd' if anchor else '')
                    free=set('abcdef')-used;value=len(K)+len(twins)+anchor+max(1,len(free));nt=len(twins);bounds[nt]=max(bounds[nt],value)
                    if value>=7:winners.append((sorted(K),['X' if t==X else 'Y' for t in twins],anchor,sorted(free),value))
        print('X',sorted(X),'maxima (0,1,2 twins)',bounds,'seven-producing patterns',winners)
        assert bounds==([6,6,6] if second=='c' else [6,7,6])
