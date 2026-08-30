"""Exact WP571 Poisson rate-shape and exposure-profile rank audit."""

import json
from pathlib import Path

import sympy as sp


theta_1, theta_2, pi = sp.symbols("theta_1 theta_2 pi", real=True, nonnegative=True)
mu = sp.Matrix([1 + theta_1, 1 + theta_2])
d = mu.jacobian([theta_1, theta_2]).subs({theta_1: 0, theta_2: 0})
mu_0 = mu.subs({theta_1: 0, theta_2: 0})
poisson_metric = sp.diag(*[1 / value for value in mu_0])
poisson_gram = sp.simplify(d.T * poisson_metric * d)

total = sp.simplify(sum(mu))
probabilities = sp.simplify(mu / total)
shape_jacobian = sp.simplify(probabilities.jacobian([theta_1, theta_2]).subs({theta_1: 0, theta_2: 0}))
probabilities_0 = probabilities.subs({theta_1: 0, theta_2: 0})
shape_metric = sp.diag(*[1 / value for value in probabilities_0])
shape_gram = sp.simplify(sum(mu_0) * shape_jacobian.T * shape_metric * shape_jacobian)

rate_tangent = sp.Matrix([[1, 1]])
rate_gram = sp.simplify(rate_tangent.T * rate_tangent / sum(mu_0))

source_block = poisson_gram
source_exposure_cross = sp.Matrix([1, 1])
exposure_information = 2 + pi
profiled_gram = sp.simplify(
    source_block
    - source_exposure_cross * source_exposure_cross.T / exposure_information
)
profiled_eigenvalues = sorted(profiled_gram.eigenvals().keys(), key=str)
free_exposure_gram = sp.simplify(profiled_gram.subs(pi, 0))
unit_precision_gram = sp.simplify(profiled_gram.subs(pi, 1))

checks = {
    "poisson_response_has_rank_two": d.rank() == 2,
    "poisson_fisher_is_identity": poisson_gram == sp.eye(2),
    "normalized_shape_jacobian_has_rank_one": shape_jacobian.rank() == 1,
    "shape_gram_has_rank_one": shape_gram.rank() == 1,
    "rate_gram_has_rank_one": rate_gram.rank() == 1,
    "rate_plus_shape_equals_poisson_fisher": sp.simplify(rate_gram + shape_gram) == poisson_gram,
    "profiled_eigenvalues_match_exact_formula": set(profiled_eigenvalues) == {1, pi / (pi + 2)},
    "free_exposure_collapses_rank_to_one": free_exposure_gram.rank() == 1,
    "free_exposure_gram_determinant_vanishes": sp.det(free_exposure_gram) == 0,
    "unit_calibration_precision_restores_rank_two": unit_precision_gram.rank() == 2,
    "unit_calibration_smallest_eigenvalue_is_one_third": min(unit_precision_gram.eigenvals().keys()) == sp.Rational(1, 3),
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP571",
    "classification": "exposure-calibrated Poisson rate is a relational reference port that can restore the direction erased by selected-shape normalization",
    "poisson_response": encode_matrix(d),
    "poisson_fisher": encode_matrix(poisson_gram),
    "shape_jacobian": encode_matrix(shape_jacobian),
    "shape_gram": encode_matrix(shape_gram),
    "rate_gram": encode_matrix(rate_gram),
    "profiled_gram": encode_matrix(profiled_gram),
    "profiled_eigenvalues": [str(value) for value in profiled_eigenvalues],
    "free_exposure_profiled_gram": encode_matrix(free_exposure_gram),
    "unit_precision_profiled_gram": encode_matrix(unit_precision_gram),
    "smallest_exact_falsifier": "with zero exposure-calibration precision, profiling removes the common-rate direction and collapses rank two to one",
    "contextual_partition": "shape-only records retain the relative-bin direction; calibrated exposure adds the common-rate direction in a new relational experiment",
    "weak_basis_descent": "passes for invariant physical16 source paths and physical Poisson counts",
    "reference_port": "independently calibrated luminosity or completed-trial exposure; it changes the experiment and does not recover an absolute rate from shape alone",
    "remaining_gate": "a portal-score-conditioned public HHH rate-and-shape response with exposure calibration, correlations, nuisances, and robust profiled Gram",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp571_poisson_exposure_rank_restoration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
