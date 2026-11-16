"""Exact verifier for conditional Ramsey incidence compression.

The program checks a sharp family with root degree t-1, triangle-free A,
R(3,t-1)-admissible residual T, and a first Hall failure at arity t-2.
It also calculates the full Hall deficiency by max-plus variable elimination
on a graph of interaction width at most three (four-variable factors).
Requires Python standard library only.
"""
from itertools import combinations, product

NEG=-10**9

def family(t):
    assert t>=5
    k=t-2
    F=list(range(k-1))
    a,b=k-1,k
    S=list(range(t-1))
    W=list(range(t-1,t-1+k))
    p,q=t-1+k,t+k
    T=W+[p,q]
    v=t+k+1
    assert v+1==2*t
    D={W[0]:{F[0]},W[-1]:{F[-1]}}
    for j in range(1,k-1):D[W[j]]={F[j-1],F[j]}
    D[p]={a};D[q]={b}
    E=set()
    def add(x,y):
        assert x!=y
        E.add(frozenset((x,y)))
    for s in S:add(v,s)
    for u in T:
        for s in D[u]:add(s,u)
    for w in W: add(w,p); add(w,q)
    return v,S,T,W,p,q,D,E

def truth(t):
    v,S,T,W,p,q,D,E=family(t)
    n=2*t
    edge=lambda u,w: frozenset((u,w)) in E
    assert not any(all(edge(a,b) for a,b in combinations(tr,2)) for tr in combinations(range(n),3))
    assert all(sum(edge(u,w) for w in range(n) if u!=w) <= t-1 for u in range(n))
    assert len(S)==t-1 and all(edge(v,s) for s in S)
    assert all(any(s in D[u] for u in T) for s in S)
    independent=lambda V: not any(edge(u,w) for u,w in combinations(V,2))
    assert all(not independent(U) for U in combinations(T,t-1))
    def deficit(V):return len(V)-len(set().union(*(D[u] for u in V)))
    independent_sets=[U for r in range(len(T)+1) for U in combinations(T,r) if independent(U)]
    bad=[U for U in independent_sets if deficit(U)>0]
    assert bad==[tuple(W)],bad
    assert max(deficit(U) for U in independent_sets)==1
    # Pairwise overlap identity for a running-intersection tree on W
    individual_sum=sum(1-len(D[u]) for u in W)
    pair_overlap=sum(len(D[W[i]]&D[W[i+1]]) for i in range(len(W)-1))
    assert individual_sum+pair_overlap==1
    return dict(first_failure=len(W),local_sum=individual_sum,overlap_sum=pair_overlap)

def max_plus_eliminate(factors,order):
    """Compute exact max-sum of binary factors. (-infinity represented by NEG)."""
    width=0
    for variable in order:
        related=[f for f in factors if variable in f[0]]
        factors=[f for f in factors if variable not in f[0]]
        if not related:continue
        scope=tuple(sorted(set().union(*(set(s) for s,_ in related))))
        width=max(width,len(scope)-1)
        remaining=tuple(x for x in scope if x!=variable)
        output={}
        for bits in product((0,1), repeat=len(remaining)):
            ab=dict(zip(remaining,bits))
            best=NEG
            for z in (0,1):
                ab[variable]=z
                score=0
                for ss,tab in related:
                    v=tab[tuple(ab[i] for i in ss)]
                    if v==NEG:score=NEG;break
                    score+=v
                best=max(best,score)
            output[bits]=best
        factors.append((remaining,output))
    assert all(not scope for scope,_ in factors)
    val=sum(tab[()] for scope,tab in factors)
    return val,width

def compressed_deficit(t):
    v,S,T,W,p,q,D,E=family(t)
    factors=[]
    for u in T:
        factors.append(((u,), {(0,):0,(1,):1}))
    for s in S:
        factors.append(((s,), {(0,):0,(1,):-1}))
    for u,w in combinations(T,2):
        if frozenset((u,w)) in E:
            ss=tuple(sorted((u,w)))
            factors.append((ss, {bits:(NEG if bits==(1,1) else 0) for bits in product((0,1),repeat=2)}))
    for u in T:
        for s in D[u]:
            # Pair factor is forbidden iff the T vertex is chosen but its direction isn't activated
            ss=tuple(sorted((u,s)))
            factors.append((ss,{bits:(NEG if dict(zip(ss,bits))[u] and not dict(zip(ss,bits))[s] else 0)
                                for bits in product((0,1),repeat=2)}))
    # Path vertices (support columns and direction labels) are eliminated first;
    # p,q are constant-size separator variables.
    path=[]
    for i,u in enumerate(W):
        path.append(u)
        if i<len(W)-1:path.append(i)
    order=path+[S[-2],S[-1],p,q]
    assert len(set(order))==len(T)+len(S)
    return max_plus_eliminate(factors,order)

if __name__=='__main__':
    print('t  n  first_Hall_arity  max_defect  induced_width  block_slack  overlap_bonus')
    for t in range(5,11):
        a=truth(t)
        defect,width=compressed_deficit(t)
        assert defect==1 and width<=3,(t,defect,width)
        print(t,2*t,a['first_failure'],defect,width,a['local_sum'],a['overlap_sum'])
    print('All tests passed.')
