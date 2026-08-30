"""Exact audit of the minimal single-spurion Wilson-coefficient basis."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
c_plus, c_minus, q2, g2, v2 = sp.symbols(
    "c_plus c_minus q_squared g_squared v_squared", positive=True
)
c_average = sp.factor((c_plus + c_minus) / 2)
c_difference = sp.factor((c_plus - c_minus) / 2)
soft_matrix_heavy_light = sp.Matrix(
    [[c_average, c_difference], [c_difference, c_average]]
) * g2 * v2

vector_mass2 = 2 * q2 * g2 * v2
heavy_basis_vector = sp.Matrix([1, 0])
heavy_image = sp.simplify(soft_matrix_heavy_light * heavy_basis_vector)
misalignment_residual = sp.factor(heavy_image[1])

c = sp.symbols("c", positive=True)
exchange_soft_mass2 = sp.factor(c_average.subs({c_plus: c, c_minus: c}) * g2 * v2)
exchange_epsilon = sp.cancel(
    exchange_soft_mass2 / (vector_mass2 + exchange_soft_mass2)
)
exchange_contrast = sp.factor(g2 * exchange_epsilon / 2)

witness_c1 = sp.factor(exchange_contrast.subs({q2: 1, c: 1}))
witness_c3 = sp.factor(exchange_contrast.subs({q2: 1, c: 3}))
wilson_residual = sp.factor(witness_c3 - witness_c1)

checks = {
    "two_independent_diagonal_spurion_coefficients_exist": (
        sp.diff(soft_matrix_heavy_light, c_plus) != sp.zeros(2)
        and sp.diff(soft_matrix_heavy_light, c_minus) != sp.zeros(2)
    ),
    "heavy_light_offdiagonal_is_coefficient_difference": (
        sp.simplify(
            soft_matrix_heavy_light[0, 1]
            - g2 * v2 * (c_plus - c_minus) / 2
        ) == 0
    ),
    "generic_spurion_map_misaligns_heavy_direction": misalignment_residual != 0,
    "exchange_symmetry_removes_misalignment": (
        misalignment_residual.subs({c_plus: c, c_minus: c}) == 0
    ),
    "exchange_soft_mass_has_common_clock": exchange_soft_mass2 == c * g2 * v2,
    "exchange_threshold_cancels_common_clock": sp.diff(exchange_epsilon, v2) == 0,
    "exchange_threshold_retains_wilson_coefficient": sp.diff(exchange_epsilon, c) != 0,
    "exchange_portal_retains_wilson_coefficient": sp.diff(exchange_contrast, c) != 0,
    "positive_coefficient_preserves_ordered_sign": exchange_contrast.is_positive is True,
    "unit_coefficient_witness": witness_c1 == g2 / 6,
    "triple_coefficient_witness": witness_c3 == 3 * g2 / 10,
    "hostile_wilson_pair_has_exact_residual": wilson_residual == 2 * g2 / 15,
    "deliberate_failure_residual_is_nonzero": wilson_residual != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP750",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "two oppositely charged link multiplets with equal vevs, one supersymmetry-breaking spurion X, and all diagonal gauge-invariant dimension-six Kahler couplings of X to the links",
    "operator_basis": "c_plus X^dagger X Phi_plus^dagger exp(2qV) Phi_plus plus c_minus X^dagger X Phi_minus^dagger exp(-2qV) Phi_minus",
    "generic_classification": "one spurion with unrestricted Wilson coefficients is neither a threshold-channel rigidifier nor a numerical selector",
    "generic_obstruction": "the heavy-light soft mixing is g^2 v^2(c_plus-c_minus)/2",
    "exchange_classification": "an exchange symmetry rigidifies the heavy-light presentation but does not select the magnitude",
    "exchange_threshold_factor": "epsilon=c/(2q^2+c)",
    "exchange_portal_contrast": "Delta=g^2 c/(2(2q^2+c))",
    "smallest_exact_falsifier": "for q^2=1 at identical g and v, c=1 gives Delta=g^2/6 while c=3 gives Delta=3g^2/10; residual 2g^2/15",
    "deutschian_status": "not a hard-to-vary explanation because the Wilson coefficient changes the prediction without changing the field content, symmetry, spurion, or mechanism",
    "claim_boundary": "minimal diagonal Kahler basis; a UV completion may calculate c, but that calculation and its uniqueness must be independently derived",
    "next_source_gate": "a principle stronger than common spurion identity must eliminate the antisymmetric operator and normalize the surviving symmetric operator",
    "candidate_stronger_principles": "extended supersymmetry, locality plus a unique mediator, compositeness sum rules, or a quantized geometric normalization, each subject to anomaly, RG, threshold, and instrument audits",
    "remaining_physical_gate": "no physical16 descent or calibrated detector-response map is constructed",
}
(ROOT / "results" / "wp750_single_spurion_wilson_coefficient_dichotomy.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
