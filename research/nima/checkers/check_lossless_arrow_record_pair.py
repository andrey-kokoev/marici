"""Exact lossless descent trial, standard library only; no particle claim."""
from fractions import Fraction as Q


def transpose(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in transpose(b)] for row in a]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


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


arrows = [(i, j) for i in range(4) for j in range(4) if i != j]
# Pin potential at vertex 0; arrows are target-source differences.
R = [[int(j == k)-int(i == k) for k in (1, 2, 3)] for i, j in arrows]
D = [[int(a == (0, k)) for a in arrows] for k in (1, 2, 3)]
assert mul(D, R) == eye(3)
P = mul(R, D)
assert mul(P, P) == P
assert mul(P, R) == R
assert rank(R) == 3
assert P != eye(12)
H = mul(transpose(R), R)
assert H == [[8*int(i == j)-2 for j in range(3)] for i in range(3)]
# H has eigenvalue 2 on constants and 8 on the sum-zero plane.
assert mul(H, [[1], [1], [1]]) == [[2], [2], [2]]
for v in ([[1], [-1], [0]], [[0], [1], [-1]]):
    assert mul(H, v) == [[8*x[0]] for x in v]
# Trial coexistence ports (x,q) with agreement x=Rq.
B = [row + [-v for v in rr] for row, rr in zip(eye(12), R)]
L = mul(transpose(B), B)
assert rank(B) == 12
assert 15-rank(L) == 3
for k in range(3):
    assert rank(mul(D[:k]+D[k+1:], R)) == 2
print('PASS: 12 gradient-arrow values <-> 3 records; exact reconstruction on im(R).')
print('PASS: induced metric H=8I-2J; all three records necessary for this linear objective.')
print('CONTROL: generic 12-arrow data are not reconstructed; nine dimensions are omitted.')
print('PAIR CONTROL: 15-port agreement operator has kernel dimension 3, not 1.')
