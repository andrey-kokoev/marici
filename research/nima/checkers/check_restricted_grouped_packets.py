"""Exact K4 packet restricted inverse; standard library, no artifacts."""
from fractions import Fraction as F


def transpose(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in transpose(b)] for row in a]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def rank(a):
    a = [list(map(F,row)) for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r,len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r],a[pivot] = a[pivot],a[r]
        d = a[r][c]
        a[r] = [x/d for x in a[r]]
        for i in range(len(a)):
            if i != r:
                d = a[i][c]
                a[i] = [x-d*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


edges = [(u,v) for u in range(4) for v in range(4) if u != v]
S = [[F(i == u) for u,v in edges] for i in range(4)]
T = [[F(i == v) for u,v in edges] for i in range(4)]
alpha, beta = transpose(S), scale(T,F(1,3))
I,J = eye(4), [[F(1)]*4 for _ in range(4)]
b = mul(beta,alpha)
assert b == scale(add(J,scale(I,-1)),F(1,3))
inv = add(J,scale(I,-3))
assert mul(inv,b) == I == mul(b,inv)
gamma = mul(alpha,inv)
assert gamma == add(scale(mul(mul(alpha,beta),alpha),3),scale(alpha,-2))
assert mul(beta,gamma) == I
assert mul(mul(gamma,beta),alpha) == alpha
Pi = mul(gamma,beta)
assert mul(Pi,Pi) == Pi
assert mul(beta,Pi) == beta
assert rank(alpha) == rank(beta) == rank(Pi) == 4
K = add(eye(12),scale(Pi,-1))
assert rank(K) == 8
assert mul(beta,K) == [[0]*12 for _ in range(4)]
assert Pi != transpose(Pi)
# All-basis reconstruction tests the displayed packet formula for every input.
assert gamma == [[F(1)-3*F(j == u) for j in range(4)] for u,v in edges]
assert mul(gamma,b) == alpha
# Two packets into the same target cancel, but violate generated source equality.
k = [[F(0)] for _ in edges]
k[edges.index((0,2))][0] = 1
k[edges.index((1,2))][0] = -1
assert mul(beta,k) == [[0]]*4
assert mul(Pi,k) == [[0]]*12
assert any(x[0] for x in k)
assert any(x < 0 for row in gamma for x in row)
print('PASS: K4 incidence factorization and exact signed return expression.')
print('PASS: restricted inverse; oblique projector; packet split dimensions 4+8.')
print('PASS: explicit packet recovery and nonzero kernel control.')
print('Scope: matrix realization only; executable packet-calculus audit remains open.')
