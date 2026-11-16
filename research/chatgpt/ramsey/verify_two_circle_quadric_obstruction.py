"""Exact obstruction to splitting a FIXED 17-point quaternion realization
into two equal-energy circular factors by any invertible 4D basis change.

No external dependencies. Reads existing integer certificate:
ramsey36_natural_half_quaternions.csv
"""
from pathlib import Path
from itertools import combinations_with_replacement

P = 1_000_000_007
path = Path(__file__).with_name('ramsey36_natural_half_quaternions.csv')
Q = [list(map(int, row.split(','))) for row in path.read_text().splitlines()[1:]]
assert len(Q) == 17 and all(len(q) == 4 for q in Q)


def quadratic_rows(points):
    pairs = list(combinations_with_replacement(range(4), 2))
    return [[q[i] * q[j] * (1 if i == j else 2) for i, j in pairs]
            for q in points]


def rank_mod(rows, mod=P):
    x = [[z % mod for z in row] for row in rows]
    m, n = len(x), len(x[0])
    row = 0
    for col in range(n):
        pivot = next((r for r in range(row, m) if x[r][col]), None)
        if pivot is None:
            continue
        x[row], x[pivot] = x[pivot], x[row]
        inv = pow(x[row][col], -1, mod)
        x[row] = [v * inv % mod for v in x[row]]
        for r in range(row + 1, m):
            mult = x[r][col]
            if mult:
                x[r] = [(a - mult * b) % mod for a, b in zip(x[r], x[row])]
        row += 1
        if row == m:
            break
    return row

M = quadratic_rows(Q)
assert rank_mod(M[:10]) == 10
assert rank_mod(M) == 10
print('FIXED 17 quaternion points: quadratic evaluation rank = 10 (mod', P, ')')
print('Therefore no nonzero homogeneous quadratic vanishes on all 17 points.')

# Also check the 16-point two-circle construction: by definition it lies on
# x1^2+x2^2-x3^2-x4^2 = 0, so quadratic rank <= 9.
S = 1_000_000
T1 = [-2285936, 863234, -599810, 168418, 872786, -15116831,
      31410691, 21937442, 1095935, -484056, -102848, -154188,
      -786293, 323549, -15813583, 2037981]
T2 = [694747, -294333, -139724, 630411, 2381420, -1146721,
      431377, -476715, 877691, 213913, -538742, 2850188,
      -2110553, 6693725, 6123880, -1433097]


def rational_circle(t):
    return (S*S-t*t, 2*S*t, S*S+t*t)

C16 = []
for t, s in zip(T1, T2):
    a, b = rational_circle(t), rational_circle(s)
    q = [a[0]*b[2], a[1]*b[2], b[0]*a[2], b[1]*a[2]]
    assert q[0]*q[0]+q[1]*q[1] == q[2]*q[2]+q[3]*q[3]
    C16.append(q)
assert rank_mod(quadratic_rows(C16)) == 9
print('16 two-circle points: quadratic evaluation rank = 9.')
print('Required shared quadratic relation verified exactly.')
