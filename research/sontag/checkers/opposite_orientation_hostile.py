#!/usr/bin/env python3
"""Exact hostile test: static Jordan contexts do not determine product orientation."""

import json
from pathlib import Path


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(a):
    return a[0][0] + a[1][1]


I = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Y = [[0, -1j], [1j, 0]]
Z = [[1, 0], [0, -1]]


def jordan(a, b, product=mul):
    return scale(0.5, add(product(a, b), product(b, a)))


def opposite(a, b):
    return mul(b, a)


checks = {
    "X_context_is_commutative": mul(X, X) == I,
    "Z_context_is_commutative": mul(Z, Z) == I,
    "same_Jordan_XZ": jordan(X, Z, mul) == jordan(X, Z, opposite),
    "Jordan_XZ_is_zero": jordan(X, Z, mul) == [[0, 0], [0, 0]],
    "ordered_products_differ": mul(X, Z) != opposite(X, Z),
    "order_reversal_is_exact": mul(X, Z) == scale(-1, opposite(X, Z)),
    "sequential_probe_separates": tr(mul(Y, mul(X, Z))) != tr(mul(Y, opposite(X, Z))),
    "sequential_probe_sign_flip": tr(mul(Y, mul(X, Z))) == -tr(mul(Y, opposite(X, Z))),
}

result = {
    "schema": "marici.sontag.opposite_orientation_hostile.v1",
    "claim_strength": "finite exact hostile fixture",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "ordered_probe": {
        "ordinary_product": str(tr(mul(Y, mul(X, Z)))),
        "opposite_product": str(tr(mul(Y, opposite(X, Z)))),
    },
    "interpretation": (
        "The ordinary and opposite products have identical Jordan symmetrization "
        "on the fixed observables, but an order-sensitive continuation separates them."
    ),
}

out = Path(__file__).parents[1] / "results" / "opposite_orientation_hostile.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
