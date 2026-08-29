import json
from fractions import Fraction as F
from pathlib import Path

A = (F(2), F(0))
B = (F(2, 9), F(2, 27783))
C = (F(1), F(1, 20000))


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def winner(r, points):
    scores = [p[0] + r * p[1] for p in points]
    m = max(scores)
    return [i for i, value in enumerate(scores) if value == m]


response_det = det(sub(B, A), sub(C, A))
assert response_det != 0
assert winner(F(1), [A, C, B]) == [0]
assert winner(F(25000), [A, C, B]) == [1]
assert winner(F(100000), [A, C, B]) == [2]

# Deliberate-failure test: a distinct collinear midpoint adds no rank and no
# strict preparation region.
M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
assert det(sub(B, A), sub(M, A)) == 0
assert all(winner(r, [A, M, B]) != [1] for r in (F(1), F(24696), F(100000)))

result = {
    "schema": "marici.flavor.wp1004.v1",
    "status": "PASS",
    "certified_endpoints": [[str(x) for x in A], [str(x) for x in B]],
    "synthetic_capacity_point": [str(x) for x in C],
    "relative_response_determinant": str(response_det),
    "positive_exposure_witnesses": {"A": "R/Q=1", "C": "R/Q=25000", "B": "R/Q=100000"},
    "hostile_collinear_midpoint": [str(x) for x in M],
    "classification": "formal positive-cone instrument-design criterion; no physical instrument",
    "remaining_gate": "source-realizable third score above chord AB with global stability and calibration",
}

out = Path(__file__).parents[1] / "results" / "wp1004_positive_cone_reference_replacement_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1004 PASS: affine independence plus positive exposure exactly types a replacement reference")

