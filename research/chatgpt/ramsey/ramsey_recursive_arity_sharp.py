"""Sharpness of Hall arity even with recursive (3,t-1) residual admissibility.
No external libraries.  A=adjacency; B=complement.  Run python script.
"""
from itertools import combinations


def example(t):
    assert t >= 5
    v=0
    S=list(range(1,t))
    F=S[:t-3]
    outside=S[t-3:]
    assert len(outside)==2
    W=list(range(t,2*t-2))
    Y=[2*t-2,2*t-1]
    assert len(W)==t-2
    n=2*t
    A=[set() for _ in range(n)]
    def edge(i,j):
        assert i!=j
        A[i].add(j);A[j].add(i)
    for s in S:edge(v,s)
    for s in F:
        for w in W:edge(s,w)
    for s,y in zip(outside,Y):edge(s,y)
    for w in W:
        for y in Y:edge(w,y)
    return A,v,S,W,Y,F,outside


def has_clique(A,c,size):
    n=len(A)
    return next((q for q in combinations(range(n),size)
                 if all((j in A[i])==c for i,j in combinations(q,2))),None)


def alpha(A,T):
    return max((len(q) for k in range(len(T)+1) for q in combinations(T,k)
                if all(j not in A[i] for i,j in combinations(q,2))),default=0)


def verify(t):
    A,v,S,W,Y,F,outside=example(t)
    T=W+Y
    D={u:frozenset(s for s in S if s in A[u]) for u in T}
    assert len(A)==2*t
    assert all(len(A[u])<=t-1 for u in range(len(A)))
    assert all(any(s in D[u] for u in T) for s in S)
    assert has_clique(A,True,3) is None
    assert alpha(A,T)==t-2
    assert has_clique(A,False,t-1) is not None
    # Hall for all A-independent U of at most t-3, not just subset of W
    for k in range(1,t-2):
        for U in combinations(T,k):
            if all(j not in A[i] for i,j in combinations(U,2)):
                assert len(set().union(*(D[u] for u in U)))>=len(U)
    assert len(set().union(*(D[u] for u in W)))==t-3
    # All proper subfamilies of W are matchable: W is a single U_(t-3,t-2) circuit
    for k in range(1,t-2):
        assert k<=len(set().union(*(D[u] for u in W[:k])))
    B_t=has_clique(A,False,t)
    assert B_t is not None
    assert set(W+outside)==set(B_t) or all(j not in A[i] for i,j in combinations(W+outside,2))
    return {'t':t,'n':len(A),'residual_n':len(T),'alpha_residual':alpha(A,T),
            'max_A_degree':max(map(len,A)),'first_Hall_failure':t-2,
            'forbidden_B_witness':tuple(W+outside)}

if __name__=='__main__':
    for t in range(5,10):
        print(verify(t))
    print('ALL TESTS PASSED')
