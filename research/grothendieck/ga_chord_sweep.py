"""All legal single-site chords; use exact witness lists, not a path capacity approximation."""
from ga_seam_local_clauses import S,graph,check,minimal,demands,combinations
from collections import Counter
from functools import lru_cache
from unittest.mock import patch

def chord_demands(c,i,j):
    a=graph(9,S,c);a[i]|=1<<j;a[j]|=1<<i
    with patch('ga_seam_residual.graph',return_value=a):return demands(S,c)

def cost(F):
    @lru_cache(None)
    def rec(F):return 0 if not F else 1+min(rec(frozenset(w for w in F if b not in w)) for b in min(F,key=len))
    return rec(frozenset(F))
if __name__=='__main__':
    stats=Counter();delta=Counter();first={}
    for c in range(1024):
        a=graph(9,S,c)
        if not check(a,16383,3,7):continue
        D=demands(S,c);F=minimal(set(D.values()));K={m for m,w in D.items() if w in F};d=cost(F)
        for i,j in combinations(range(9),2):
            if j==i+1 or a[i]&a[j]:continue
            stats['legal']+=1;H=chord_demands(c,i,j);L=minimal(set(H.values()));n=cost(L);delta[n-d]+=1
            mixed=[w for w in L if any(b>>i&1 for b in w) and any(b>>j&1 for b in w)];lost=L-{H[m] for m in K&H.keys()}
            for key,ws in [('mixed',mixed),('new probe',lost),('cost jump',L if n>d+1 else [])]:
                if not ws:continue
                stats[key]+=1;w=min(ws,key=lambda w:(len(w),sorted(w)));m=min(m for m in H if H[m]==w);first.setdefault(key,(c,(i+1,j+1),d,n,m,sorted(w),sorted(D.get(m,()))))
    print(stats,delta,first)
