"""Exact WP579 pullback cost of an invariant portal calibration design."""

import json
from pathlib import Path

import sympy as sp


z, lambda_h = sp.symbols("z lambda_H", positive=True, real=True)
lambda_s = sp.symbols("lambda_s", positive=True, real=True)

a = sp.Matrix([[1, 0], [2 * lambda_s * z / lambda_h, z**2 / lambda_h]])
a_inverse = sp.simplify(a.inv())

e_r = sp.Matrix([1, 0])
e_q = sp.Matrix([0, 1])
pullback_r = sp.simplify(a_inverse * e_r)
pullback_q = sp.simplify(a_inverse * e_q)

cost_r = sp.factor((pullback_r.T * pullback_r)[0])
cost_q = sp.factor((pullback_q.T * pullback_q)[0])

hostile = {z: sp.Rational(1, 2), lambda_h: 1, lambda_s: 1}
hostile_q_pullback = pullback_q.subs(hostile)
unit_bounded_q_reach = sp.factor(z**2 / lambda_h)

checks = {
    "portal_jacobian_inverse_is_exact": sp.simplify(a * a_inverse) == sp.eye(2),
    "unit_r_pullback_is_exact": pullback_r == sp.Matrix([1, -2 * lambda_s / z]),
    "unit_q_pullback_is_exact": pullback_q == sp.Matrix([0, lambda_h / z**2]),
    "r_cost_is_exact": sp.simplify(cost_r - (1 + 4 * lambda_s**2 / z**2)) == 0,
    "q_cost_is_exact": cost_q == lambda_h**2 / z**4,
    "q_cost_diverges_at_zero_mixing": sp.limit(cost_q, z, 0, dir="+") == sp.oo,
    "r_cost_diverges_for_nonzero_lambda_s": sp.limit(cost_r.subs(lambda_s, 1), z, 0, dir="+") == sp.oo,
    "rational_hostile_needs_lambda_s_shift_four": hostile_q_pullback == sp.Matrix([0, 4]),
    "unit_bounded_q_reach_at_hostile_is_one_quarter": unit_bounded_q_reach.subs(hostile) == sp.Rational(1, 4),
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP579",
    "classification": "the invariant portal entrance is pointwise rank two but an orthogonal unit design has unbounded physical-parameter pullback cost near zero mixing",
    "portal_jacobian": encode_matrix(a),
    "portal_jacobian_inverse": encode_matrix(a_inverse),
    "unit_r_pullback": encode_matrix(pullback_r),
    "unit_q_pullback": encode_matrix(pullback_q),
    "unit_r_squared_cost": str(cost_r),
    "unit_q_squared_cost": str(cost_q),
    "unit_bounded_pure_q_reach": str(unit_bounded_q_reach),
    "smallest_exact_falsifier": "at z=1/2 and lambda_H=1, unit q response requires delta_lambda_s=4 while a unit-bounded setting reaches only q=1/4",
    "contextual_partition": "positive-lambda_s pointwise rank-two portal; bounded-reach viable subdomain; singular zero-mixing boundary",
    "remaining_gate": "publish a compact portal calibration domain, physical setting norm and bound, induced design singular value, and finite-setting remainder",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp579_portal_design_pullback_cost.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
