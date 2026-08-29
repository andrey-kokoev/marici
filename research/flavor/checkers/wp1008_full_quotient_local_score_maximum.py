import json
from pathlib import Path

import sympy as sp

z, a, t = sp.symbols("z a t", real=True)
X = sp.diag(-1, z, 1-z)
Y = sp.Matrix([[0, a, -sp.I*t], [a, 0, 1], [sp.I*t, 1, 0]])
C = X*Y - Y*X
nx = sp.trace(X.H*X)
ny = sp.trace(Y.H*Y)
K = sp.factor(sp.trace(C.H*C)/(nx*ny))
P = sp.factor(C.det()*sp.conjugate(C.det())/(nx*ny)**3)
rstar = sp.Rational(44376, 275)
S = sp.factor(K + rstar*P)
point = {z: 0, a: 1, t: sp.Rational(6, 5)}

gradient = [sp.factor(sp.diff(S, v).subs(point)) for v in (z, a, t)]
assert gradient == [0, 0, 0]

H = sp.simplify(sp.hessian(S, (z, a, t)).subs(point))
expected_H = sp.Matrix([
    [-sp.Rational(9294, 473), sp.Rational(75, 86), 0],
    [sp.Rational(75, 86), -sp.Rational(3273750, 874577),
     sp.Rational(1296000, 874577)],
    [0, sp.Rational(1296000, 874577),
     -sp.Rational(2160000, 874577)],
])
assert H == expected_H
leading_minors = [sp.factor(H[:i, :i].det()) for i in range(1, 4)]
assert leading_minors[0] < 0
assert leading_minors[1] > 0
assert leading_minors[2] < 0
assert leading_minors[2] == -sp.Rational(14458500000, 105823817)

delta = sp.symbols("delta", real=True)
Pstar = sp.factor(P.subs(point))
phase_score = rstar*Pstar*sp.cos(delta)**2
phase_curvature = sp.factor(sp.diff(phase_score, delta, 2).subs(delta, 0))
assert phase_curvature == -2*rstar*Pstar
assert phase_curvature < 0

q = sp.symbols("q", real=True)
Kstar = sp.factor(K.subs(point))
ny_star = sp.factor(ny.subs(point))
diag_score = Kstar*ny_star/(ny_star+q**2) + rstar*Pstar*ny_star**3/(ny_star+q**2)**3
diag_curvature = sp.factor(sp.diff(diag_score, q, 2).subs(q, 0))
assert diag_curvature < 0

# Deliberate-failure test: the witness is not stationary at the wrong ratio.
S_wrong = K + P
wrong_gradient = [sp.factor(sp.diff(S_wrong, v).subs(point)) for v in (z, a, t)]
assert wrong_gradient != [0, 0, 0]

result = {
    "schema": "marici.flavor.wp1008.v1",
    "status": "PASS",
    "reduced_coordinates": ["eigenvalue_shape_z", "edge_ratio_a",
                            "edge_ratio_t", "triangle_phase_delta"],
    "gradient": [str(v) for v in gradient],
    "hessian": [[str(H[i, j]) for j in range(3)] for i in range(3)],
    "leading_principal_minors": [str(v) for v in leading_minors],
    "phase_curvature": str(phase_curvature),
    "diagonal_commuting_curvature": str(diag_curvature),
    "classification": "strict local maximum on reduced generic Hermitian-pair quotient",
    "remaining_gate": "global upper-hull theorem or exact remote dominator; source ratio and instrument remain unauthorized",
}

out = Path(__file__).parents[1] / "results" / "wp1008_full_quotient_local_score_maximum.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1008 PASS: witness is a strict local maximum on the reduced Hermitian quotient")

