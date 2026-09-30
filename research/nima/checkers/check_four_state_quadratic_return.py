"""Exact checks of the uniform quadratic forward/return realization."""
from fractions import Fraction as F


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def scale(a, k):
    return [[k*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def power(a,k):
    result = eye(len(a))
    for _ in range(k):
        result = mul(result,a)
    return result


for m in range(1,7):
    n = m+1
    I = eye(n)
    J = [[F(1)]*n for _ in range(n)]
    b = scale(add(J,scale(I,-1)),F(1,m))
    inverse = add(scale(b,m),scale(I,-(m-1)))
    assert mul(b,b) == add(scale(I,F(1,m)),scale(b,F(m-1,m)))
    assert mul(b,inverse) == I == mul(inverse,b)
    P = scale(add(I,scale(b,m)),F(1,m+1))
    Q = scale(add(I,scale(b,-1)),F(m,m+1))
    zero = scale(I,0)
    assert mul(P,P) == P and mul(Q,Q) == Q
    assert mul(P,Q) == zero == mul(Q,P)
    assert add(P,Q) == I
    # Idempotents have rank equal to trace in characteristic zero.
    assert sum(P[i][i] for i in range(n)) == 1
    assert sum(Q[i][i] for i in range(n)) == m
    assert b == add(P,scale(Q,F(-1,m)))
    assert inverse == add(P,scale(Q,-m))
    for k in range(-5,6):
        t = F(-1,m)**k
        formula = add(scale(I,(1+m*t)/(m+1)),scale(b,m*(1-t)/(m+1)))
        assert formula == power(b,k) if k >= 0 else formula == power(inverse,-k)
    x = [[F(i*i-2*i+3, i+1)] for i in range(n)]
    assert mul(inverse,mul(b,x)) == x
    if m > 1:
        assert inverse[0][0] < 0
        assert mul(b,b) != I  # b is symmetric, so this also checks nonunitarity.
    if m == 3:
        assert sum(v != 0 for row in b for v in row) == 12
        assert sum(v != 0 for row in inverse for v in row) == 16
print('PASS: exact quadratic relation, inverse, projectors and ranks for m=1..6.')
print('PASS: powers k=-5..5 and forward/return recovery; m=3 supports 12 forward, 16 inverse entries.')
print('CONTROL: for m>1 the inverse is signed and the forward map is not unitary.')
