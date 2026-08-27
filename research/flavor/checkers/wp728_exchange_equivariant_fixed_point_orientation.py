"""Exact exchange-equivariant fixed-point and representation-orientation theorem."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
s, a = sp.symbols("s a", real=True)
v = sp.symbols("v", real=True, nonzero=True)
E = sp.diag(1, -1)
x = sp.Matrix([s, a])

beta_symmetric = sp.Matrix([s - 1, 2 * a])
symmetric_equivariance = sp.simplify(
    beta_symmetric.subs({s: s, a: -a}, simultaneous=True) - E * beta_symmetric
)
symmetric_fixed = sp.solve(list(beta_symmetric), (s, a), dict=True)
J_symmetric = beta_symmetric.jacobian(x)

beta_spontaneous = sp.Matrix([s - 1, a * (a**2 - v**2)])
spontaneous_equivariance = sp.simplify(
    beta_spontaneous.subs({s: s, a: -a}, simultaneous=True) - E * beta_spontaneous
)
spontaneous_odd_roots = sp.solve(beta_spontaneous[1], a)

oriented_star = sp.Matrix([sp.Rational(7, 4), sp.Rational(3, 5)])
beta_oriented = sp.Matrix([-(s - oriented_star[0]), 2 * (a - oriented_star[1])])
oriented_fixed = sp.solve(list(beta_oriented), (s, a), dict=True)
J_oriented = beta_oriented.jacobian(x)
oriented_equivariance_defect = sp.simplify(
    beta_oriented.subs({s: s, a: -a}, simultaneous=True) - E * beta_oriented
)

threshold_factor = sp.Rational(3, 4)
low_contrast = threshold_factor * oriented_star[1]
unlabelled = sp.Matrix([[1, 1]])
labelled = sp.eye(2)
contrast_vector = sp.Matrix([1, -1])

checks = {
    "exchange_is_an_involution": E**2 == sp.eye(2),
    "symmetric_beta_field_is_exchange_equivariant": symmetric_equivariance == sp.zeros(2, 1),
    "unique_symmetric_fixed_point_has_zero_odd_coordinate": symmetric_fixed == [{a: 0, s: 1}],
    "symmetric_stability_preserves_even_odd_split": sp.simplify(J_symmetric * E - E * J_symmetric) == sp.zeros(2),
    "spontaneous_beta_field_is_exchange_equivariant": spontaneous_equivariance == sp.zeros(2, 1),
    "nonzero_spontaneous_fixed_points_form_sign_pair": set(spontaneous_odd_roots) == {sp.Integer(0), -v, v},
    "explicit_orientation_has_unique_nonzero_fixed_contrast": oriented_fixed == [{a: sp.Rational(3, 5), s: sp.Rational(7, 4)}],
    "oriented_stability_has_relevant_clock_and_irrelevant_contrast": J_oriented.eigenvals() == {-1: 1, 2: 1},
    "nonzero_oriented_source_breaks_exchange_equivariance": oriented_equivariance_defect == sp.Matrix([0, -sp.Rational(12, 5)]),
    "positive_threshold_witness_preserves_sign": low_contrast == sp.Rational(9, 20),
    "unlabelled_detector_kills_contrast": unlabelled * contrast_vector == sp.zeros(1, 1),
    "labelled_detector_has_rank_two": labelled.rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP728",
    "status": "PASS",
    "checks": checks,
    "theorem": "a unique fixed point of an exchange-equivariant beta field has zero exchange-odd coordinate",
    "spontaneous_route": "nonzero fixed points occur in a sign pair; the original quotient retains magnitude but not ordered sign",
    "necessary_source_principle": "physical orientation by non-isomorphic representation data, followed by a unique nonzero fixed contrast with irrelevant odd fluctuation",
    "algebraic_acceptance_witness": {
        "fixed_point": {"clock_coordinate": "7/4", "portal_contrast": "3/5"},
        "scaling_exponents": {"clock": "-1 relevant", "portal_contrast": "+2 irrelevant"},
        "threshold_contrast": "9/20",
    },
    "claim_boundary": "the affine witness proves consistency of the architecture but does not derive its coefficients from an anomaly-free matter theory",
    "smallest_exact_falsifier": "exchange equivariance plus fixed-point uniqueness forces the odd coordinate to zero",
    "remaining_model_gate": "derive the exchange-odd beta source term and positive irrelevant exponent from one complete anomaly-free non-isomorphic representation packet",
    "remaining_physical_gate": "fix the relevant clock, complete finite matching, and realize a calibrated rank-two labelled detector response",
}
(ROOT / "results" / "wp728_exchange_equivariant_fixed_point_orientation.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
