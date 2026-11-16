#!/usr/bin/env python3
"""Exact checks for the real symplectic pair-witness shear construction.

No Ramsey upper bound is claimed. The coloring is an INPUT (choice of shears).
The construction retains an n-mode real symplectic carrier and an active
2-vector primitive at each mode.
"""
from itertools import combinations, permutations


def mm(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def transpose(A):
    return list(map(list,zip(*A)))


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def omega_matrix(n):
    return [[(int(i+n==j) if i<n else -int(i-n==j))
             for j in range(2*n)] for i in range(2*n)]


def s(A):
    n=len(A)
    I=eye(n)
    return [I[i]+[0]*n for i in range(n)] + [A[i]+I[i] for i in range(n)]


def shear(u):
    # Conjugate of the primitive B shear in an additive integral frame.
    n=len(u)
    return s([[u[i]*u[j] for j in range(n)] for i in range(n)])


def inverse_shear(u):
    n=len(u)
    return s([[-u[i]*u[j] for j in range(n)] for i in range(n)])


def cross(i,j,n):
    A=[[0]*n for _ in range(n)]
    A[i][j]=A[j][i]=1
    return s(A)


def pair_evaluation(A):
    # One layer uses (e_i,0), and the other (e_j,A e_j).
    n=len(A)
    out=[[sum(omega_matrix(n)[i][k]*s(A)[k][j]
              for k in range(2*n)) for j in range(n)] for i in range(n)]
    return out


def graph_matrix(n,mask):
    A=[[0]*n for _ in range(n)]
    for k,(i,j) in enumerate(combinations(range(n),2)):
        if (mask>>k)&1:
            A[i][j]=A[j][i]=1
    return A


def embed(A,b):
    n=len(A)
    return [A[i]+[b[i]] for i in range(n)]+[list(b)+[0]]


def list_edges(A):
    return [(i,j) for i in range(len(A)) for j in range(i+1,len(A))
            if A[i][j]]


def assert_symplectic(T,n):
    O=omega_matrix(n)
    assert mm(transpose(T),mm(O,T))==O


def test():
    # One cross term is exactly additive squaring minus unary squaring.
    for n in range(2,7):
        for i,j in combinations(range(n),2):
            ui=[int(k==i) for k in range(n)]
            uj=[int(k==j) for k in range(n)]
            uij=[ui[k]+uj[k] for k in range(n)]
            T=mm(mm(shear(uij),inverse_shear(ui)),inverse_shear(uj))
            assert T==cross(i,j,n)
            assert_symplectic(T,n)

    counts={}
    for n in range(1,6):
        count=0
        for mask in range(1<<(n*(n-1)//2)):
            A=graph_matrix(n,mask)
            T=s(A)
            assert_symplectic(T,n)
            assert pair_evaluation(A)==A
            # The complete coloring equals the product of its primitive cross shears.
            P=eye(2*n)
            for i,j in list_edges(A):
                P=mm(P,cross(i,j,n))
            assert P==T
            count+=1
        counts[n]=count

    # A new mode adds only cross shears; all old pairings survive.
    for n in range(1,5):
        for mask in range(1<<(n*(n-1)//2)):
            A=graph_matrix(n,mask)
            # Build a representative extension set; exhaustive for n <= 3.
            for bm in (range(1<<n) if n<=3 else (0,1,3,5,15)):
                b=[(bm>>i)&1 for i in range(n)]
                newA=embed(A,b)
                P=s(embed(A,[0]*n))
                for i in range(n):
                    if b[i]:
                        P=mm(P,cross(i,n,n+1))
                assert P==s(newA)
                assert pair_evaluation(newA)==newA

    # Reordering sampled vertices changes presentation, not physical incidence.
    n=4
    for mask in range(1<<(n*(n-1)//2)):
        A=graph_matrix(n,mask)
        for perm in permutations(range(n)):
            Ap=[[A[perm[i]][perm[j]] for j in range(n)] for i in range(n)]
            P=[[int(perm[i]==j) for j in range(n)] for i in range(n)]
            F=[P[i]+[0]*n for i in range(n)] + [[0]*n+P[i] for i in range(n)]
            assert mm(mm(F,s(A)),transpose(F))==s(Ap)
            assert_symplectic(F,n)

    # Counterexamples to a claim that symplecticity alone prevents red triangles.
    K3=graph_matrix(3,7)
    assert sum(K3[i][j]*K3[j][k]*K3[k][i]
               for i,j,k in combinations(range(3),3))==1
    assert_symplectic(s(K3),3)
    print('EXACT PASS')
    print('all labeled graphs for n=1,...,5:',counts)
    print('pair polarization: checked for 2<=n<=6')
    print('all permutations of all 64 labeled four-vertex graphs: checked')
    print('new-vertex recurrence: checked')
    print('red K3 is symplectically realizable: yes (no Ramsey forcing from shears alone)')

if __name__=='__main__':
    test()
