"""Minimum distinguishing observations, conditional on all ten positive blades."""
from r37_reconstruct_catalogue import equality_cases
from r37_reconstruct_sat import models,blades
from itertools import combinations

def hitting(F,k):
    if not F:return ()
    if not k:return None
    for q in sorted(min(F,key=len)):
        r=hitting([s for s in F if q not in s],k-1)
        if r is not None:return (q,)+r

def cost(F):
    assert all(F)
    return next(k for k in range(len(F)+1) if hitting(F,k) is not None)

for idx,order,h,B in equality_cases():
    extras=[];diff=[]
    for g in models(h,B,positive_only=True):
        extras.append({tuple(sorted(s)) for s in blades(g)-B})
        diff.append({(i,j) for i,j in combinations(range(6,22),2) if (h[i]^g[i])>>j&1})
    print(idx,order[:6],len(diff),min(map(len,extras)),cost(extras),len(set.union(*diff)),cost(diff),flush=True)
