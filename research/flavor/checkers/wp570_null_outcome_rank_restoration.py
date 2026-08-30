"""Exact WP570 null-outcome rank-restoration theorem."""

import json
from pathlib import Path

import sympy as sp


p = sp.Matrix([sp.Rational(1, 3)] * 3)
k = sp.eye(3)
d = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
s = sp.simplify(3 * d)
transported = sp.simplify(k * sp.diag(*p) * s)

full_metric = 3 * sp.eye(3)
full_gram = sp.simplify(d.T * full_metric * d)
full_eigenvalues = sorted(full_gram.eigenvals().keys(), key=lambda value: float(value))

selected_indices = [0, 1]
selected_baseline = sp.Matrix([p[index] for index in selected_indices])
selected_total = sp.simplify(sum(selected_baseline))
conditional_baseline = sp.simplify(selected_baseline / selected_total)

conditional_columns = []
for column in range(d.cols):
    selected_tangent = sp.Matrix([d[index, column] for index in selected_indices])
    selected_tangent_total = sp.simplify(sum(selected_tangent))
    conditional_tangent = sp.simplify(
        selected_tangent / selected_total
        - selected_baseline * selected_tangent_total / selected_total**2
    )
    conditional_columns.append(conditional_tangent)

conditional_response = sp.Matrix.hstack(*conditional_columns)
conditional_metric = sp.diag(*[sp.simplify(1 / value) for value in conditional_baseline])
conditional_gram = sp.simplify(conditional_response.T * conditional_metric * conditional_response)

checks = {
    "source_scores_are_centered": sp.simplify(p.T * s) == sp.zeros(1, 2),
    "detector_channel_is_column_stochastic": all(sum(k[:, index]) == 1 for index in range(k.cols)),
    "source_channel_factorization_reproduces_response": transported == d,
    "full_response_preserves_probability": sp.simplify(sp.ones(1, 3) * d) == sp.zeros(1, 2),
    "full_three_outcome_response_has_rank_two": d.rank() == 2,
    "full_fisher_gram_eigenvalues_are_three_and_nine": full_eigenvalues == [3, 9],
    "conditional_baseline_is_binary_uniform": conditional_baseline == sp.Matrix([sp.Rational(1, 2)] * 2),
    "conditional_response_matches_exact_formula": conditional_response == sp.Matrix(
        [[sp.Rational(3, 2), sp.Rational(-3, 4)], [sp.Rational(-3, 2), sp.Rational(3, 4)]]
    ),
    "conditional_response_preserves_probability": sp.simplify(sp.ones(1, 2) * conditional_response) == sp.zeros(1, 2),
    "selected_only_response_has_rank_one": conditional_response.rank() == 1,
    "selected_only_gram_determinant_vanishes": sp.det(conditional_gram) == 0,
    "binary_probability_tangent_dimension_is_one": conditional_response.rows - 1 == 1,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP570",
    "classification": "typed null outcome restores source-derived rank two erased by selected-only conditioning",
    "general_rank_ceiling": "rank(D) <= min(number of source directions, number of normalized outcomes - 1)",
    "source_baseline": encode_matrix(p),
    "source_scores": encode_matrix(s),
    "detector_channel": encode_matrix(k),
    "full_response": encode_matrix(d),
    "full_response_rank": d.rank(),
    "full_fisher_gram": encode_matrix(full_gram),
    "full_fisher_gram_eigenvalues": [str(value) for value in full_eigenvalues],
    "conditional_baseline": encode_matrix(conditional_baseline),
    "selected_only_response": encode_matrix(conditional_response),
    "selected_only_response_rank": conditional_response.rank(),
    "selected_only_gram": encode_matrix(conditional_gram),
    "selected_only_gram_determinant": str(sp.det(conditional_gram)),
    "smallest_exact_falsifier": "discarding the third completed-trial outcome turns the exact rank-two response into two proportional conditional columns",
    "contextual_partition": "the completed three-outcome experiment separates both directions; the selected-only quotient retains one combination",
    "weak_basis_descent": "passes for invariant physical16 source scores and normalized detector probabilities",
    "remaining_gate": "an executed portal-score instrument publishing completed-trial exposure, null outcomes, source-conditioned efficiencies, covariance, and robust rank",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp570_null_outcome_rank_restoration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
