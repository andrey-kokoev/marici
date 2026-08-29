import json
from pathlib import Path

import sympy as sp

i = sp.I
t = sp.Rational(1, 22)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -i*t], [1, 0, 1], [i*t, 1, 0]])
Cmat = X * Y - Y * X

nx = sp.trace(X.H * X)
ny = sp.trace(Y.H * Y)
nc = sp.trace(Cmat.H * Cmat)
Kc = sp.factor(nc / (nx * ny))
Pc = sp.factor((Cmat.det() * sp.conjugate(Cmat.det())) / (nx * ny) ** 3)

assert X.H == X and Y.H == Y
assert Kc == sp.Rational(162, 323)
assert Pc == sp.Rational(58564, 969**3)
assert Cmat.det() != 0

A = (sp.Rational(2), sp.Rational(0))
B = (sp.Rational(2, 9), sp.Rational(2, 27783))
C = (Kc, Pc)


def winner(r):
    scores = [p[0] + r * p[1] for p in (A, C, B)]
    m = max(scores)
    return [j for j, value in enumerate(scores) if value == m]


det_response = sp.det(sp.Matrix([[B[0]-A[0], B[1]-A[1]], [C[0]-A[0], C[1]-A[1]]]))
r_ac = sp.factor((A[0] - C[0]) / (C[1] - A[1]))
r_cb = sp.factor((C[0] - B[0]) / (B[1] - C[1]))

assert det_response != 0
assert 0 < Pc < B[1]
assert 0 < r_ac < r_cb
assert winner(sp.Rational(1)) == [0]
assert winner(sp.Rational(25000)) == [1]
assert winner(sp.Rational(100000)) == [2]

# Deliberate-failure deletion: remove the complex closing edge.
Y_deleted = Y.subs(t, 0)
C_deleted = X * Y_deleted - Y_deleted * X
assert C_deleted.det() == 0

result = {
    "schema": "marici.flavor.wp1005.v1",
    "status": "PASS",
    "candidate_X": [[str(v) for v in row] for row in X.tolist()],
    "candidate_Y": [[str(v) for v in row] for row in Y.tolist()],
    "candidate_scores": {"K": str(Kc), "P": str(Pc)},
    "commutator_determinant": str(sp.factor(Cmat.det())),
    "relative_response_determinant": str(sp.factor(det_response)),
    "positive_crossings": {"A_to_C": str(r_ac), "C_to_B": str(r_cb)},
    "strict_exposure_witnesses": {"A": 1, "C": 25000, "B": 100000},
    "classification": "Hermitian source-domain capacity witness; not source-selected or instrumented",
    "remaining_gate": "full-domain support theorem or source potential stabilizing the candidate orbit",
}

out = Path(__file__).parents[1] / "results" / "wp1005_positive_cone_third_configuration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1005 PASS: an exact Hermitian third configuration is positively exposed within the three-state set")

