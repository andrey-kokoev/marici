"""Exact WP574 combined null-deletion and exposure-profile quotient theorem."""

import json
from pathlib import Path

import sympy as sp


pi = sp.symbols("pi", real=True, nonnegative=True)
q = sp.Matrix([sp.Rational(1, 3)] * 3)
d = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
v = sp.Matrix([1, 2])
full_tangent = sp.simplify(d * v)

full_metric = 3 * sp.eye(3)
full_gram = sp.simplify(d.T * full_metric * d)
full_eigenvalues = sorted(full_gram.eigenvals().keys(), key=lambda value: float(value))

selected_q = q[:2, :]
selected_total = sp.simplify(sum(selected_q))
conditional_columns = []
for column in range(d.cols):
    selected_tangent = d[:2, column]
    selected_tangent_total = sp.simplify(sum(selected_tangent))
    conditional_columns.append(
        sp.simplify(
            selected_tangent / selected_total
            - selected_q * selected_tangent_total / selected_total**2
        )
    )
shape_response = sp.Matrix.hstack(*conditional_columns)
shape_kernel_witness = sp.simplify(shape_response * v)

count_response = d[:2, :]
count_metric = 3 * sp.eye(2)
exposure_direction = selected_q
count_tangent = sp.simplify(count_response * v)
exposure_multiple = sp.simplify(count_tangent[0] / exposure_direction[0])

source_gram = sp.simplify(count_response.T * count_metric * count_response)
source_exposure_cross = sp.simplify(count_response.T * count_metric * exposure_direction)
exposure_information = sp.simplify((exposure_direction.T * count_metric * exposure_direction)[0] + pi)
profiled_gram = sp.simplify(
    source_gram
    - source_exposure_cross * source_exposure_cross.T / exposure_information
)
profiled_determinant = sp.factor(sp.det(profiled_gram))
free_exposure_gram = sp.simplify(profiled_gram.subs(pi, 0))
free_exposure_kernel_witness = sp.simplify(free_exposure_gram * v)
calibrated_gram = sp.simplify(profiled_gram.subs(pi, 2))

checks = {
    "full_response_preserves_probability": sp.simplify(sp.ones(1, 3) * d) == sp.zeros(1, 2),
    "full_completed_record_has_rank_two": d.rank() == 2,
    "full_gram_eigenvalues_are_three_and_nine": full_eigenvalues == [3, 9],
    "hostile_source_direction_maps_to_selected_rate_vs_null": full_tangent == sp.Matrix([1, 1, -2]),
    "hostile_selected_response_is_proportional_to_baseline": count_tangent == 3 * exposure_direction,
    "selected_shape_quotient_has_rank_one": shape_response.rank() == 1,
    "selected_shape_quotient_erases_hostile_direction": shape_kernel_witness == sp.zeros(2, 1),
    "raw_selected_count_response_has_rank_two": count_response.rank() == 2,
    "free_exposure_profile_has_rank_one": free_exposure_gram.rank() == 1,
    "free_exposure_profile_erases_same_hostile_direction": free_exposure_kernel_witness == sp.zeros(2, 1),
    "profiled_determinant_matches_formula": profiled_determinant == 27 * pi / (3 * pi + 2),
    "positive_exposure_precision_restores_rank_two": calibrated_gram.rank() == 2 and sp.det(calibrated_gram) > 0,
    "exposure_multiple_is_three": exposure_multiple == 3,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP574",
    "classification": "sector-independent detector theorem: null deletion and free exposure profiling erase the same source direction through distinct nonfaithful quotients",
    "baseline": encode_matrix(q),
    "complete_response": encode_matrix(d),
    "complete_gram": encode_matrix(full_gram),
    "complete_gram_eigenvalues": [str(value) for value in full_eigenvalues],
    "hostile_source_direction": encode_matrix(v),
    "complete_detector_tangent": encode_matrix(full_tangent),
    "shape_quotient": {
        "response": encode_matrix(shape_response),
        "rank": shape_response.rank(),
        "kernel_witness": encode_matrix(shape_kernel_witness),
    },
    "count_exposure_quotient": {
        "raw_count_response": encode_matrix(count_response),
        "raw_rank": count_response.rank(),
        "exposure_direction": encode_matrix(exposure_direction),
        "source_tangent_exposure_multiple": str(exposure_multiple),
        "profiled_gram": encode_matrix(profiled_gram),
        "profiled_determinant": str(profiled_determinant),
        "free_exposure_gram": encode_matrix(free_exposure_gram),
        "free_exposure_rank": free_exposure_gram.rank(),
        "free_exposure_kernel_witness": encode_matrix(free_exposure_kernel_witness),
        "pi_two_calibrated_gram": encode_matrix(calibrated_gram),
    },
    "smallest_exact_falsifier": "v=(1,2) is visible as (1,1,-2) in the completed record, erased by selected conditioning, and erased again by free exposure profiling",
    "contextual_partition": "null retention keeps selected-rate-versus-null contrast; calibrated exposure retains the selected-rate component in a new relational experiment",
    "weak_basis_descent": "passes for an invariant source entrance; exposure calibration explicitly changes the relational stabilizer groupoid",
    "remaining_flavor_gate": "a publication-bound portal-score response joined to the completed detector or calibrated exposure experiment",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp574_detector_null_exposure_quotient_theorem.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
