"""Exact hostile separating scalar pairing zeros from common-state equalizers."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def matvec(matrix, vector):
    return [sum(Fraction(x) * y for x, y in zip(row, vector)) for row in matrix]


def dot(a, b):
    return sum(Fraction(x) * y for x, y in zip(a, b))


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    return [
        [sum(Fraction(a[i][k]) * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


u_plus = [Fraction(1), Fraction(0)]
u_minus = [Fraction(0), Fraction(1)]
rotation = [
    [Fraction(0), Fraction(-1)],
    [Fraction(1), Fraction(0)],
]
identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]

assert matvec(rotation, u_plus) == u_minus
assert dot(u_minus, u_plus) == 0
assert dot(u_plus, u_plus) == 1
assert dot(u_minus, u_minus) == 1
assert matmul(transpose(rotation), rotation) == identity
assert u_plus != u_minus

# Equality of t*u_plus and t*u_minus forces t=0.
equalizer_difference = [x - y for x, y in zip(u_plus, u_minus)]
assert equalizer_difference != [Fraction(0), Fraction(0)]
assert any(equalizer_difference)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "zero scalar pairing between transported nonzero sector states does not yield a common-state equalizer witness",
    "pairing": str(dot(u_minus, u_plus)),
    "plus_norm_squared": str(dot(u_plus, u_plus)),
    "minus_norm_squared": str(dot(u_minus, u_minus)),
    "transport_orthogonal": True,
    "transport_invertible": True,
    "equality_equalizer_dimension": 0,
    "verdict": "zero-to-equalizer bridge missing",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-pairing-zero-not-equalizer.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
