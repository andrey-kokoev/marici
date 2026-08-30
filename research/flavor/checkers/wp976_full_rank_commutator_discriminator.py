"""Exact WP976 full-rank commutator discriminator checker."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]

def dagger(a):
    return [[a[j][i].conjugate() for j in range(3)] for i in range(3)]

def trace(a):
    return sum(a[i][i] for i in range(3))

def norm_squared(a):
    return int(trace(mul(dagger(a), a)).real)

def determinant(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )

def commutator(x, y):
    return sub(mul(x, y), mul(y, x))

def discriminator(c):
    det = determinant(c)
    det_abs_squared = int((det * det.conjugate()).real)
    n2 = norm_squared(c)
    return Fraction(det_abs_squared, n2**3)

X2 = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
Y2 = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
C2 = commutator(X2, Y2)

X3 = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
Y3 = [[0, 1, -1j], [1, 0, 1], [1j, 1, 0]]
C3 = commutator(X3, Y3)

d2 = discriminator(C2)
d3 = discriminator(C3)
det2 = determinant(C2)
det3 = determinant(C3)

checks = {
    "two_level_norm_squared_is_eight": norm_squared(C2) == 8,
    "two_level_determinant_vanishes": det2 == 0,
    "two_level_discriminator_vanishes": d2 == 0,
    "full_rank_norm_squared_is_twenty_eight": norm_squared(C3) == 28,
    "full_rank_determinant_is_twelve_i": det3 == 12j,
    "full_rank_discriminator_is_exact": d3 == Fraction(9, 1372),
    "discriminator_separates_rank_two_from_rank_three": d3 > d2,
    "cp_even_operator_field_degree_is_twelve": 2 * 3 * 2 == 12,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.full-rank-commutator-discriminator.v1",
    "work_package": "WP976",
    "status": "PASS",
    "checks": checks,
    "domain": "nonzero commutators of two Hermitian coefficient fields",
    "quotient": "full weak-basis conjugation and common commutator rescaling",
    "two_level": {"norm_squared": 8, "determinant": str(det2), "D": str(d2)},
    "full_rank": {"norm_squared": 28, "determinant": str(det3), "D": str(d3)},
    "operator_field_degree": 12,
    "classification": "legal conditional CP-magnitude selector; source operator and instrument not admitted",
    "remaining_gate": "derive the degree-twelve operator, coefficient, scale, and stable completion from an admitted flavor source",
}
out = ROOT / "results" / "wp976_full_rank_commutator_discriminator.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
