"""Exact seed-cycle retention and reversible two-presentation trial.

Scalar additive edge data only: not noncommutative transport or path history.
No external dependencies and no generated artifacts.
"""
from fractions import Fraction as Q


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in tr(b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(a, k):
    return [[k*x for x in row] for row in a]


def rank(a):
    a = [list(map(Q, row)) for row in a]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        v = a[r][c]
        a[r] = [x/v for x in a[r]]
        for i in range(len(a)):
            if i != r:
                v = a[i][c]
                a[i] = [x-v*y for x, y in zip(a[i], a[r])]
        r += 1
    return r


# Arrow order AB, BC, CA, AD, DB, BA.
# Record order AB, BC, AD, sum(ABC), sum(ADB), sum(AB,BA).
D = [[1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,0,1,0,0],
     [1,1,1,0,0,0], [0,0,0,1,1,1], [1,0,0,0,0,1]]
R = [[1,0,0,0,0,0], [0,1,0,0,0,0], [-1,-1,0,1,0,0],
     [0,0,1,0,0,0], [1,0,-1,0,1,-1], [-1,0,0,0,0,1]]
I = eye(6)
assert mm(D, R) == I == mm(R, D)
# Incidence: target minus source; distinct reverse arrows are independent.
arrows = [(0,1),(1,2),(2,0),(0,3),(3,1),(1,0)]
inc = [[int(j == k)-int(i == k) for i,j in arrows] for k in range(4)]
cycles = D[3:]
assert rank(inc) == 3 and rank(cycles) == 3
assert mm(inc, tr(cycles)) == [[0]*3 for _ in range(4)]
assert 6-rank(inc) == 3
for k in range(6):
    assert rank(D[:k]+D[k+1:]) == 5
# Same tree records, different cycle record: a counterexample to tree-only recovery.
z = [[0],[0],[0],[1],[0],[0]]
x = mm(R, z)
assert mm(D[:3], x) == [[0],[0],[0]] and x != [[0]]*6
# A declared reversible dynamics: circulate the three cycle records.
# This is a chosen test operator, NOT derived from a seed automorphism.
T = eye(6)
for i in range(3,6):
    T[i] = [Q(j == 3+(i-3+1)%3) for j in range(6)]
A = mm(mm(R, T), D)
assert mm(mm(T, T), T) == I
assert mm(mm(A, A), A) == I
assert mm(D, A) == mm(T, D)
# Distinct typed ports x and z, synchronized by z=Dx.
# Swap/update U(x,z)=(R T z, D x). U^2 updates both presentations.
zero = [[Q(0)]*6 for _ in range(6)]
RT = mm(R, T)
U = [a+b for a,b in zip(zero, RT)] + [a+b for a,b in zip(D, zero)]
assert mm(mm(mm(mm(mm(U,U),U),U),U),U) == eye(12)
H = mm(tr(D), D)
W = [a+b for a,b in zip(H, zero)] + [a+b for a,b in zip(zero, I)]
assert mm(mm(tr(U), W), U) == W
# Update generally leaves synchronized states: an explicit one-step witness.
xx = mm(R,z)
y = mm(U, xx+z)
assert mm(D, y[:6]) != y[6:]
# Yet two steps preserve synchronization and implement the conjugate dynamics.
y2 = mm(mm(U,U), xx+z)
assert mm(D,y2[:6]) == y2[6:]
B = [a+[-v for v in b] for a,b in zip(D,I)]
assert 12-rank(B) == 6
E = R + I  # Embed record states as synchronized pairs (Rz,z).
assert mm(mm(U,U), E) == mm(E,T)
assert mm(B,E) == [[0]*6 for _ in range(6)]
assert mm(tr(A), A) != I  # Euclidean unitarity is not automatic.
print('PASS: seed incidence rank 3; three independent additive cycle records.')
print('PASS: six-record descent/reconstruction are exact two-sided inverses.')
print('PASS: every record deletion loses rank; tree-only descent loses cycle data.')
print('PASS: declared cycle dynamics conjugates exactly; A^3=I.')
print('PASS: two-support update U^6=I and U^T W U=W; synchronization returns after two steps.')
print('CONTROL: synchronized pair has six free modes; no compression or particle identity derived.')
