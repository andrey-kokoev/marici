"""Exact dual-number audit of pure four-mode Gaussian cyclic invariants."""

import json
from fractions import Fraction as F
from pathlib import Path


NVAR = 6
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
J2 = [[F(0), F(1)], [F(-1), F(0)]]
I2 = [[F(1), F(0)], [F(0), F(1)]]
Z2 = [[F(1), F(0)], [F(0), F(-1)]]


class D:
    def __init__(self, v, g=None):
        self.v = F(v)
        self.g = tuple(F(0) for _ in range(NVAR)) if g is None else tuple(g)

    def __add__(self, other):
        other = dual(other)
        return D(self.v + other.v, [a + b for a, b in zip(self.g, other.g)])

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, [-a for a in self.g])

    def __sub__(self, other):
        return self + (-dual(other))

    def __rsub__(self, other):
        return dual(other) - self

    def __mul__(self, other):
        other = dual(other)
        return D(self.v * other.v, [self.g[i] * other.v + self.v * other.g[i] for i in range(NVAR)])

    __rmul__ = __mul__

    def inv(self):
        return D(1 / self.v, [-x / (self.v * self.v) for x in self.g])

    def __truediv__(self, other):
        return self * dual(other).inv()

    def __eq__(self, other):
        other = dual(other)
        return self.v == other.v and self.g == other.g


def dual(x):
    return x if isinstance(x, D) else D(x)


def variable(value, index):
    g = [F(0) for _ in range(NVAR)]
    g[index] = F(1)
    return D(value, g)


def zeros(n):
    return [[D(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    a = zeros(n)
    for i in range(n):
        a[i][i] = D(1)
    return a


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), D(0)) for j in range(len(b[0]))] for i in range(len(a))]


def scale(s, a):
    return [[dual(s) * x for x in row] for row in a]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def neg(a):
    return scale(-1, a)


def set_block(a, i, j, block):
    for r in range(2):
        for c in range(2):
            a[2 * i + r][2 * j + c] = dual(block[r][c])


def block(a, i, j):
    return [[a[2 * i + r][2 * j + c] for c in range(2)] for r in range(2)]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), D(0))


def rank_fraction(matrix):
    a = [list(row) for row in matrix]
    rank = 0
    cols = len(a[0]) if a else 0
    for col in range(cols):
        pivot = next((r for r in range(rank, len(a)) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pv = a[rank][col]
        a[rank] = [x / pv for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col] != 0:
                q = a[r][col]
                a[r] = [a[r][j] - q * a[rank][j] for j in range(cols)]
        rank += 1
    return rank


def two_mode_squeezer(i, j, t):
    den = 1 - t * t
    ch = (1 + t * t) / den
    sh = (2 * t) / den
    s = eye(8)
    set_block(s, i, i, scale(ch, I2))
    set_block(s, j, j, scale(ch, I2))
    set_block(s, i, j, scale(sh, Z2))
    set_block(s, j, i, scale(sh, Z2))
    return s


def cycle(v, order):
    product = [[D(1), D(0)], [D(0), D(1)]]
    for a, b in zip(order, order[1:] + order[:1]):
        product = mul(product, mul([[dual(x) for x in row] for row in J2], block(v, a, b)))
    return trace(product)


values = [F(1, 11), F(1, 9), F(1, 7), F(1, 6), F(1, 5), F(2, 9)]
params = [variable(values[i], i) for i in range(NVAR)]
symplectic = eye(8)
for edge, t in zip(EDGES, params):
    symplectic = mul(two_mode_squeezer(edge[0], edge[1], t), symplectic)
v = scale(F(1, 2), mul(symplectic, transpose(symplectic)))

omega = zeros(8)
for i in range(4):
    set_block(omega, i, i, J2)
assert mul(mul(v, omega), v) == scale(F(1, 4), omega)

pair_dets = [det2(block(v, i, j)) for i, j in EDGES]
pair_jacobian = [list(x.g) for x in pair_dets]
pair_rank = rank_fraction(pair_jacobian)
assert pair_rank == 6

orders = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
cycles = [cycle(v, order) for order in orders]
assert any(x.v != 0 for x in cycles)

# Three-mode-prefix elimination.  Partition V=[[P,C],[C^T,A4]].
prefix = [row[:6] for row in v[:6]]
column = [row[6:] for row in v[:6]]
last = [row[6:] for row in v[6:]]
omega3 = [row[:6] for row in omega[:6]]
j_dual = [[dual(x) for x in row] for row in J2]
prefix_defect = add(scale(F(1, 4), omega3), neg(mul(mul(prefix, omega3), prefix)))
factorized_defect = mul(mul(column, j_dual), transpose(column))
assert prefix_defect == factorized_defect
compatibility = add(mul(mul(prefix, omega3), column), mul(mul(column, j_dual), last))
assert all(x == D(0) for row in compatibility for x in row)
vertex_residual = add(add(mul(mul(transpose(column), omega3), column), mul(mul(last, j_dual), last)), scale(F(-1, 4), j_dual))
assert all(x == D(0) for row in vertex_residual for x in row)
prefix_defect_rank = rank_fraction([[x.v for x in row] for row in prefix_defect])
assert prefix_defect_rank == 2

# Backtracking closed walks reduce to products of pair determinants because
# J C_ij J C_ji = -det(C_ij) I_2.
backtrack_tests = []
for i, j in EDGES:
    cij, cji = block(v, i, j), block(v, j, i)
    lhs = mul(mul(mul([[dual(x) for x in row] for row in J2], cij), [[dual(x) for x in row] for row in J2]), cji)
    rhs = scale(-det2(cij), I2)
    assert lhs == rhs
    backtrack_tests.append(f"{i}{j}")

packet = {
    "schema": "marici.four-mode-cyclic-invariants.v1",
    "source_family": "ordered product of six labelled rational two-mode squeezers, one per K4 edge",
    "parameters": [str(x) for x in values],
    "purity_verified": True,
    "lower_invariants": {
        "coordinates": [f"detC_{i}{j}" for i, j in EDGES],
        "jacobian_rank": pair_rank,
        "quotient_dimension": 6,
    },
    "primitive_hamilton_cycles": [
        {"order": "".join(map(str, order)), "value": str(value.v), "gradient": [str(x) for x in value.g]}
        for order, value in zip(orders, cycles)
    ],
    "backtracking_reductions": backtrack_tests,
    "prefix_extension": {
        "defect_identity": "Omega3/4-P Omega3 P=C J C^T",
        "compatibility": "P Omega3 C+C J A4=0",
        "last_vertex": "C^T Omega3 C+A4 J A4=J/4",
        "prefix_defect_rank": prefix_defect_rank,
        "interpretation": "the fourth-mode cross column is a canonical rank-two factorization of the failed purity of the reduced three-mode prefix",
    },
    "conclusion": "nonzero four-cycles survive, but on the generic six-dimensional pure-state quotient the six pair determinants are local coordinates; no additional continuous cyclic modulus exists",
    "qualification": "local generic determination does not yet exclude a global finite branch ambiguity with identical lower invariants",
}

out = Path(__file__).parent / "results" / "four-mode-cyclic-invariants.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
