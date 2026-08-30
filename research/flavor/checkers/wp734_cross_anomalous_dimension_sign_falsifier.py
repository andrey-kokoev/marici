"""Exact positive cross-anomalous-dimension falsifier of truncated sign robustness."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x, y = sp.symbols("x y", nonnegative=True)
yA, kA, yB, kB = sp.symbols("y_A kappa_A y_B kappa_B", real=True)

equations = [
    8 * yA + 2 * kA - 12,
    3 * yA + 9 * kA + x * kB - sp.Rational(15, 2),
    12 * yB + sp.Rational(1, 2) * kB - 12,
    3 * yB + sp.Rational(23, 4) * kB + y * kA - sp.Rational(15, 2),
]
solution = sp.solve(equations, (yA, kA, yB, kB), dict=True)[0]
qA = sp.factor(solution[yA] * solution[kA])
qB = sp.factor(solution[yB] * solution[kB])
contrast = sp.factor(-4 * qA + 3 * qB)
F = sp.factor(-contrast * (32 * x * y - 1485) ** 2 / 18)
expected_F = (
    1536 * x**2 * y - 1152 * x**2 - 512 * x * y**2 + 576 * x * y
    - 62640 * x + 64 * y**2 + 22176 * y - 33129
)

y_star = sp.Rational(759, 28) - sp.Rational(33, 56) * sp.sqrt(1493)
witness = {x: 1, y: y_star}
witness_solution = {name: sp.simplify(value.subs(witness)) for name, value in solution.items()}
witness_denominator = sp.simplify((32 * x * y - 1485).subs(witness))
witness_contrast = sp.simplify(contrast.subs(witness))

checks = {
    "deformed_nullclines_solve_exactly": all(sp.simplify(eq.subs(solution)) == 0 for eq in equations),
    "cancellation_polynomial_is_exact": sp.simplify(F - expected_F) == 0,
    "truncated_zero_cross_terms_have_positive_contrast": contrast.subs({x: 0, y: 0}) > 0,
    "hostile_x_is_strictly_positive": witness[x] > 0,
    "hostile_y_is_strictly_positive": y_star > 0,
    "hostile_nullcline_determinant_is_nonzero": witness_denominator != 0,
    "hostile_y_A_is_positive": witness_solution[yA] > 0,
    "hostile_kappa_A_is_positive": witness_solution[kA] > 0,
    "hostile_y_B_is_positive": witness_solution[yB] > 0,
    "hostile_kappa_B_is_positive": witness_solution[kB] > 0,
    "hostile_point_lies_on_exact_cancellation_surface": sp.simplify(F.subs(witness)) == 0,
    "hostile_additive_portal_contrast_vanishes": witness_contrast == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP734",
    "status": "PASS",
    "checks": checks,
    "deformation_domain": "nonnegative cross coefficients x and y in the simultaneous A/B kappa nullclines at g1=1, g2=T=0",
    "cancellation_surface": "F(x,y)=0 with the exact polynomial recorded in the packet",
    "positive_hostile_witness": {
        "x": "1",
        "y": "759/28 - 33 sqrt(1493)/56",
    },
    "classification": "exact falsifier of extending the WP733 sign theorem from separate nullclines using cross-coefficient positivity alone",
    "smallest_exact_falsifier": "the displayed positive witness has four positive Yukawa coordinates and zero additive portal contrast",
    "claim_boundary": "x and y are generic deformations, not coefficients derived from the actual simultaneous Feynman graphs",
    "remaining_source_gate": "calculate x and y from the shared Higgs and lepton anomalous dimensions and prove a nonzero signed distance from F=0",
    "remaining_physical_gate": "after full RG closure, establish threshold survival and calibrated rank-two readout",
}
(ROOT / "results" / "wp734_cross_anomalous_dimension_sign_falsifier.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
