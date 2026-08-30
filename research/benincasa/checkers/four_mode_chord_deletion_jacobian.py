"""Exact tangent audit on the pure four-mode Gaussian chord-deletion locus."""

import json
from fractions import Fraction as F
from pathlib import Path


N = 4
EDGES = [(0, 1), (1, 2), (2, 3), (3, 0)]
J = [[F(0), F(1)], [F(-1), F(0)]]


class D:
    def __init__(self, value, gradient=None):
        self.v = F(value)
        self.g = tuple(F(0) for _ in range(N)) if gradient is None else tuple(gradient)

    def __add__(self, other):
        other = dual(other)
        return D(self.v + other.v, [a + b for a, b in zip(self.g, other.g)])

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, [-x for x in self.g])

    def __sub__(self, other):
        return self + (-dual(other))

    def __rsub__(self, other):
        return dual(other) - self

    def __mul__(self, other):
        other = dual(other)
        return D(self.v * other.v, [self.g[i] * other.v + self.v * other.g[i] for i in range(N)])

    __rmul__ = __mul__

    def inv(self):
        return D(1 / self.v, [-x / self.v**2 for x in self.g])

    def __truediv__(self, other):
        return self * dual(other).inv()


def dual(x):
    return x if isinstance(x, D) else D(x)


def variable(value, index):
    g = [F(0)] * N
    g[index] = F(1)
    return D(value, g)


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), D(0)) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), D(0))


def inverse(a):
    n = len(a)
    aug = [list(a[i]) + [D(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col].v)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        inv_pivot = aug[col][col].inv()
        aug[col] = [x * inv_pivot for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col].v:
                q = aug[r][col]
                aug[r] = [aug[r][j] - q * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def rank(matrix):
    a = [list(row) for row in matrix]
    out = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(out, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[out], a[pivot] = a[pivot], a[out]
        pv = a[out][col]
        a[out] = [x / pv for x in a[out]]
        for r in range(len(a)):
            if r != out and a[r][col]:
                q = a[r][col]
                a[r] = [a[r][j] - q * a[out][j] for j in range(len(a[0]))]
        out += 1
    return out


values = [F(1, 7), F(1, 8), F(1, 9), F(1, 10)]
variables = [variable(value, i) for i, value in enumerate(values)]
x = [[D(int(i == j)) for j in range(4)] for i in range(4)]
for (i, j), value in zip(EDGES, variables):
    x[i][j] = x[j][i] = value
xi = inverse(x)


def cblock(i, j):
    return [[x[i][j] / 2, D(0)], [D(0), xi[i][j] / 2]]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


edge_dets = [det2(cblock(i, j)) for i, j in EDGES]
jac = [list(value.g) for value in edge_dets]
jac_rank = rank(jac)
assert jac_rank == 4
assert det2(cblock(0, 2)).v == 0
assert det2(cblock(1, 3)).v == 0

product = [[D(1), D(0)], [D(0), D(1)]]
for i, j in zip((0, 1, 2, 3), (1, 2, 3, 0)):
    product = mul(product, mul([[D(v) for v in row] for row in J], cblock(i, j)))
cycle = trace(product)
assert cycle.v != 0

packet = {
    "schema": "marici.four-mode-chord-deletion-jacobian.v1",
    "family": "pure block-diagonal V=1/2 diag(X,X^-1), normalized X_ii=1, X_02=X_13=0",
    "parameters": [str(x) for x in values],
    "surviving_lower_coordinates": ["detC_01", "detC_12", "detC_23", "detC_30"],
    "restricted_jacobian_rank": jac_rank,
    "support_dimension": 4,
    "four_cycle": {"value": str(cycle.v), "gradient": [str(x) for x in cycle.g]},
    "census_companion": "8344 positive exact packets; no same-lower/different-cycle collision",
    "conclusion": "on the generic Gaussian chord-deletion locus the four surviving pair determinants remain local coordinates, so the nonzero four-cycle adds no continuous supported modulus",
    "qualification": "a deeper rank-drop sublocus or global finite branch remains possible",
}

out = Path(__file__).parent / "results" / "four-mode-chord-deletion-jacobian.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
