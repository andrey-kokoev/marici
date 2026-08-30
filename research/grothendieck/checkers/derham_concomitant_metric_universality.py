import json
from fractions import Fraction


def derivative(p):
    return [Fraction(k) * p[k] for k in range(1, len(p))]


def add(a, b):
    n = max(len(a), len(b))
    return [(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0) for k in range(n)]


def multiply(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def pair(X, Q, Y):
    out = [Fraction(0)]
    for i in range(5):
        for j in range(5):
            out = add(out, [Q[i][j] * v for v in multiply(X[i], Y[j])])
    return out


Q = [[Fraction((i + 2) * (j + 3) + (j + 2) * (i + 3)) for j in range(5)] for i in range(5)]
X = [[Fraction((i + 1) * (k + 2) - 3) for k in range(4)] for i in range(5)]
Y = [[Fraction((i + 2) * (k + 1) + 1) for k in range(4)] for i in range(5)]
yX = [[Fraction(0)] + p for p in X]
yY = [[Fraction(0)] + p for p in Y]

lhs = derivative(pair(X, Q, Y))
rhs = add(pair([derivative(p) for p in X], Q, Y), pair(X, Q, [derivative(p) for p in Y]))

result = {
    "schema": "marici.grothendieck.derham_concomitant_metric_universality.v1",
    "dependency_free": True,
    "checks": {
        "leibniz_identity": lhs == rhs,
        "wall_coordinate_symmetry": pair(yX, Q, Y) == pair(X, Q, yY),
    },
    "note": "The packet proves these coefficientwise for arbitrary constant symmetric Q; this exact rational witness guards the implementation.",
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
