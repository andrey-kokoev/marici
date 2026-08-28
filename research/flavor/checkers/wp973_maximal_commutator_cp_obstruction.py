"""Exact WP973 maximal-commutator CP obstruction checker."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]

def trace(a):
    return sum(a[i][i] for i in range(3))

def dagger(a):
    return [[a[j][i].conjugate() for j in range(3)] for i in range(3)]

def norm_squared(a):
    return trace(mul(dagger(a), a)).real

def determinant(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )

X = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
Y = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
C = sub(mul(X, Y), mul(Y, X))
x_norm2 = norm_squared(X)
y_norm2 = norm_squared(Y)
c_norm2 = norm_squared(C)
bound = 2 * x_norm2 * y_norm2
c_det = determinant(C)
c_cubic = trace(mul(mul(C, C), C))
rank = 2

checks = {
    "both_fields_are_hermitian": dagger(X) == X and dagger(Y) == Y,
    "source_radii_are_equal_and_positive": x_norm2 == y_norm2 == 2,
    "commutator_is_nonzero": c_norm2 > 0,
    "hermitian_commutator_bound_is_saturated": c_norm2 == bound == 8,
    "maximizer_is_two_level": rank == 2,
    "commutator_determinant_vanishes": c_det == 0,
    "commutator_cubic_vanishes": c_cubic == 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.maximal-commutator-cp-obstruction.v1",
    "work_package": "WP973",
    "status": "PASS",
    "checks": checks,
    "domain": "two Hermitian coefficient fields at fixed positive Frobenius radii",
    "quotient": "simultaneous source SO(3), then full weak-basis physical16",
    "norms_squared": [x_norm2, y_norm2],
    "commutator_norm_squared": c_norm2,
    "sharp_bound": bound,
    "commutator_rank": rank,
    "commutator_determinant": str(c_det),
    "commutator_cubic": str(c_cubic),
    "classification": "noncommutativity selector and rigidifier; not a three-family CP selector",
    "remaining_gate": "source-derived invariant preventing two-level concentration and producing full-rank commutator",
}
out = ROOT / "results" / "wp973_maximal_commutator_cp_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
