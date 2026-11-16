"""Boundary-information theorem: exact profiles and sharp low-order countermodels.

Standard library only. Run:
    python ramsey_boundary_information_theorem.py

A is the graph edge color, B is its complement. The program:
  1. Validates R(3,t) valid/invalid pairs for t=5,6,7 with identical
     residual A graph, degree multisets and one-/two-way A-link counts.
  2. Validates parity-based examples with equal B-link counts on every
     boundary subset of size < k, and different R(3,t) admissibility.
  3. Verifies the explicit matching certificate for the valid graph,
     the B-K_t witness for the invalid graph, the residual core, and
     the exact boundary profile inequalities.
  4. Checks 2^k pairwise distinguishable context signatures for k=3,4.
No graph catalogues, optimizer, or network access.
"""
from itertools import combinations


def empty_graph(n):
    return [0] * n


def edge(A, u, v):
    assert u != v
    A[u] |= 1 << v
    A[v] |= 1 << u


def adjacent(A, u, v):
    return bool(A[u] & (1 << v))


def is_b_clique(A, xs):
    return all(not adjacent(A, u, v) for u, v in combinations(xs, 2))


def is_a_independent(A, xs):
    return is_b_clique(A, xs)


def is_triangle_free(A):
    return all(not (A[u] & A[v])
               for u in range(len(A)) for v in range(u + 1, len(A))
               if adjacent(A, u, v))


def max_independent(A, keep):
    # Exact only for deliberately small 5,6,7 examples.
    keep = list(keep)
    ans = 0
    for size in range(1, len(keep) + 1):
        if any(is_b_clique(A, subset) for subset in combinations(keep, size)):
            ans = size
    return ans


def common_b_link(A, subset, candidates):
    return sum(all(u != s and not adjacent(A, u, s) for s in subset)
               for u in candidates)


def base_small(case, t):
    assert t in (5, 6, 7)
    n = 10 + (t - 5)
    A = empty_graph(n)
    S = [1, 2, 3] + list(range(10, n))
    T = list(range(4, 10))
    for s in S:
        edge(A, 0, s)
    for i, j in ((0, 5), (1, 3), (1, 4), (2, 3), (4, 5)):
        edge(A, T[i], T[j])
    Ds = ({4, 5}, {4, 6}, {4, 7} if case == 'valid' else {5, 6})
    for s, D in zip((1, 2, 3), Ds):
        for u in D:
            edge(A, s, u)
    return A, S, T


def boundary_profile(A, v):
    S = [u for u in range(len(A)) if adjacent(A, v, u)]
    T = [u for u in range(len(A)) if u != v and not adjacent(A, v, u)]
    D = {u: frozenset(s for s in S if adjacent(A, u, s)) for u in T}
    h = {}
    for size in range(len(S)+1):
        for F in combinations(S, size):
            F = frozenset(F)
            h[F] = max_independent(A, (u for u in T if D[u] <= F))
    return S, T, h


def exact_profile_identity(A, v):
    S, T, h = boundary_profile(A, v)
    RHS = max(1 + h[frozenset(S)],
              max(len(S)-len(F)+value for F,value in h.items()))
    assert RHS == max_independent(A, range(len(A)))
    return RHS


def audit_profile_identity():
    # All labeled triangle-free graphs on five vertices, at every root.
    n = 5
    pairs = list(combinations(range(n),2))
    checks=0
    for mask in range(1<<len(pairs)):
        A=empty_graph(n)
        for j,(u,w) in enumerate(pairs):
            if mask >> j & 1: edge(A,u,w)
        if not is_triangle_free(A): continue
        for v in range(n):
            exact_profile_identity(A,v)
            checks+=1
    return checks


def test_small():
    output = []
    for t in (5, 6, 7):
        A0, S, T = base_small('valid', t)
        A1, S1, T1 = base_small('invalid', t)
        assert S == S1 and T == T1
        assert is_triangle_free(A0) and is_triangle_free(A1)
        assert all(adjacent(A0, u, w) == adjacent(A1, u, w)
                   for u, w in combinations(T, 2))
        assert sorted(r.bit_count() for r in A0) == sorted(r.bit_count() for r in A1)
        assert max_independent(A0, range(len(A0))) == t - 1
        assert max_independent(A1, range(len(A1))) == t
        assert max_independent(A0, T) == 3
        for order in (1, 2):
            a = [common_b_link(A0, C, T) for C in combinations((1, 2, 3), order)]
            b = [common_b_link(A1, C, T) for C in combinations((1, 2, 3), order)]
            assert a == b, (t, order, a, b)
            a2 = [sum(all(adjacent(A0, u, s) for s in C) for u in T)
                  for C in combinations((1, 2, 3), order)]
            b2 = [sum(all(adjacent(A1, u, s) for s in C) for u in T)
                  for C in combinations((1, 2, 3), order)]
            assert a2 == b2
        assert common_b_link(A0, (1, 2, 3), T) == 2
        assert common_b_link(A1, (1, 2, 3), T) == 3
        output.append((t, len(A0), t-1, t, 2, 3))
    return output


def parity_example(k):
    assert k >= 3
    M = 1 << (k-1)
    t = M + k + 2
    n = 2*M + k + 2
    v=0
    S=list(range(1, k+1))
    T=list(range(k+1, k+1+M))
    X=list(range(k+1+M, n))
    assert len(X) == M+1
    examples=[]
    for is_valid in (False, True):
        vectors=[x for x in range(1<<k) if x.bit_count()%2 == ((k+1)%2 if is_valid else k%2)]
        preferred=((1<<k)-2) if is_valid else ((1<<k)-1)
        assert preferred in vectors
        vectors=[preferred]+[x for x in vectors if x != preferred]
        A=empty_graph(n)
        for s in S: edge(A,v,s)
        for u,mask in zip(T,vectors):
            for i,s in enumerate(S):
                if not (mask>>i&1): edge(A,u,s)
        u0=T[0]
        for x in X:
            for u in T[1:]: edge(A,x,u)
        # Explicit disjoint A-matching covers all of the left bipartition T+v
        if is_valid:
            matched=[(u,x) for u,x in zip(T[1:],X[:M-1])]
            matched += [(u0,S[0]),(v,S[1])]
            assert len(matched)==M+1
            assert len(set(a for e in matched for a in e))==2*(M+1)
            assert all(adjacent(A,u,w) for u,w in matched)
        else:
            assert A[u0] == 0
            assert is_b_clique(A,S+X+[u0])
            assert len(S+X+[u0])==t
        assert is_triangle_free(A)
        assert max(r.bit_count() for r in A) <= t-1
        # Same residual core for the two versions: K_{M-1,M+1} + isolated u0.
        # max residual A-independent set = max(M, (M+1)+1) = M+2.
        assert M+2 <= t-2
        examples.append((A,v,S,T,X,vectors))
    bad,good=examples
    assert all((bad[0][u] & sum(1<<w for w in T+X)) ==
               (good[0][u] & sum(1<<w for w in T+X)) for u in T+X)
    # Exactly the same lower-order common B-neighbor counts on S.
    for arity in range(k):
        for C in combinations(S,arity):
            b=common_b_link(bad[0], C, T)
            g=common_b_link(good[0], C, T)
            assert b==g==(M if arity==0 else (1 << (k-arity-1))), (k,C,b,g)
    assert common_b_link(bad[0],S,T)==1
    assert common_b_link(good[0],S,T)==0
    # Exact valid chromatic-independent-set upper bound from disjoint A matching.
    # S+X is a B clique of t-1 vertices (tight).
    assert is_b_clique(good[0],S+X)
    assert len(S+X)==t-1
    return {'k':k,'t':t,'n':n,'boundary':k,
            'lower_order_links_equal':True,'bad_full_link':1,
            'good_full_link':0,'alpha_good':t-1,'alpha_bad_at_least':t}


def module_context(k):
    # One interior vertex u. All other blue edges encode membership Q.
    # A context X_i (B-clique size t-2) is B to boundary i, B to u,
    # A to other boundary vertices. It produces B-K_t iff i in Q.
    t=k+2
    S=list(range(k));u=k;X=list(range(k+1,k+1+t-2))
    n=len(S)+1+len(X)
    def gluing(Q,i):
        A=empty_graph(n)
        for s in S:
            if s not in Q: edge(A,u,s)
        for x in X:
            for s in S:
                if s!=i: edge(A,x,s)
        assert is_triangle_free(A)
        # u-X B, X-X B, S-S B
        return A
    for mask in range(1<<k):
        Q={i for i in S if mask>>i&1}
        for i in S:
            A=gluing(Q,i)
            alpha=max_independent(A,range(n))
            assert (alpha >=t)==(i in Q),(k,Q,i,alpha)
    return 1<<k


def main():
    print('EXACT BOUNDARY IDENTITY CHECKS', audit_profile_identity())
    print('SMALL EXACT GRAPHS (t,n,alpha_valid,alpha_invalid,triple_B_link_valid,triple_B_link_invalid)')
    for row in test_small(): print(*row)
    print('PARITY HIERARCHY (k,t,n,common links below k identical, full links bad/good)')
    for k in (3,4,5,6):
        r=parity_example(k)
        print(r['k'],r['t'],r['n'],r['lower_order_links_equal'],r['bad_full_link'],r['good_full_link'])
    print('DISTINGUISHABLE MODULE STATES (k, states)')
    for k in (3,4): print(k,module_context(k))
    print('ALL CHECKS PASSED')

if __name__ == '__main__':main()
