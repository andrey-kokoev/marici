"""Exact WP972 coefficient-object minimality checker."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]

def scale(c, a):
    return [[c * a[i][j] for j in range(3)] for i in range(3)]

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def commutator(a, b):
    return add(mul(a, b), scale(-1, mul(b, a)))

def trace(a):
    return sum(a[i][i] for i in range(3))

def determinant(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )

zero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C = [[0, 1, -1j], [1, 0, 1], [1j, 1, 0]]
C2 = mul(C, C)
Yu_shared = add(add(I, scale(2, C)), C2)
Yd_shared = add(add(scale(3, I), scale(-1, C)), scale(4, C2))
shared_commutator = commutator(Yu_shared, Yd_shared)

A = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
B = C
two_commutator = commutator(A, B)
two_det = determinant(two_commutator)
two_cubic = trace(mul(mul(two_commutator, two_commutator), two_commutator))

checks = {
    "single_object_outputs_commute": shared_commutator == zero,
    "single_object_cp_cubic_vanishes": trace(mul(mul(shared_commutator, shared_commutator), shared_commutator)) == 0,
    "two_object_control_is_hermitian": all(B[i][j] == B[j][i].conjugate() for i in range(3) for j in range(3)),
    "two_object_control_does_not_commute": two_commutator != zero,
    "two_object_control_has_nonzero_commutator_determinant": two_det != 0,
    "two_object_control_has_nonzero_cp_cubic": two_cubic != 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.coefficient-object-minimality.v1",
    "work_package": "WP972",
    "status": "PASS",
    "checks": checks,
    "domain": "Hermitian coefficient objects with scalar-coefficient functional calculus",
    "quotient": "full weak-basis physical16 quotient",
    "one_object_commutator": [[str(x) for x in row] for row in shared_commutator],
    "two_object_commutator_determinant": str(two_det),
    "two_object_commutator_cubic": str(two_cubic),
    "classification": "at least two noncommuting coefficient objects are necessary but not sufficient",
    "remaining_gate": "source-derived SO(3)-invariant action selecting their relative vacuum and a typed instrument",
}
out = ROOT / "results" / "wp972_coefficient_object_minimality.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
