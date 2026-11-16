"""Exact check of symplectic monodromy and a cospectral Ramsey-readout obstruction."""
from itertools import combinations
from sympy import Matrix, eye, zeros, symbols, expand


def adjacency(n, edges):
    A = zeros(n)
    for i, j in edges:
        assert i != j
        A[i, j] = A[j, i] = 1
    return A


def monodromy(A):
    n = A.rows
    S = eye(2*n)
    for i in range(n):
        for j in range(n):
            S[n+i, j] = A[i,j]
    J = zeros(2*n)
    for i in range(n):
        J[i,n+i] = -1
        J[n+i,i] = 1
    return J*S, J


def alpha(A):
    n=A.rows
    best=0
    for mask in range(1 << n):
        count=mask.bit_count()
        if count<=best:continue
        vs=[i for i in range(n) if mask>>i & 1]
        if all(A[i,j] == 0 for i,j in combinations(vs,2)):
            best=count
    return best


def tri(A):
    return sum(int(A[i,j]*A[j,k]*A[i,k]) for i,j,k in combinations(range(A.rows),3))

# Exhaustive test for all graphs through n=5 (2**10=1024).
for n in range(1,6):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        A=adjacency(n,[p for i,p in enumerate(pairs) if mask>>i&1])
        M,J=monodromy(A)
        assert (M*M*M).trace() == -6*tri(A)
        assert (M*M).trace() == (A*A).trace() - 2*n
        # M is symplectic: M.T J M=J
        assert M.T*J*M==J

# Graph G = C4 + 4 isolates, H = K(1,4) + 3 isolates.
G=adjacency(8,[(0,1),(1,2),(2,3),(3,0)])
H=adjacency(8,[(0,1),(0,2),(0,3),(0,4)])
x=symbols('x')
pG=expand(G.charpoly(x).as_expr())
pH=expand(H.charpoly(x).as_expr())
assert pG == pH == expand(x**6*(x**2-4))
assert alpha(G)==6 and alpha(H)==7
assert tri(G)==tri(H)==0
MG,J=monodromy(G)
MH,_=monodromy(H)
assert MG.charpoly(x).as_expr().expand() == MH.charpoly(x).as_expr().expand()
print('Verified 1099 graphs (n<=5): tr((J S_A)^3) = -6 * triangles.')
print('Cospectral pair on 8 vertices: C4 + 4 isolates and K1,4 + 3 isolates.')
print('Both adjacency characteristic polynomials:', pG)
print('Independence numbers:', alpha(G), alpha(H), '; both triangle counts:', tri(G), tri(H))
print('Symplectic monodromy characteristic polynomials agree:', expand(MG.charpoly(x).as_expr()))
