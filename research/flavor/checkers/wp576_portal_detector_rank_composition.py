"""Exact WP576 conditional portal-to-completed-detector rank theorem."""

import json
from pathlib import Path

import sympy as sp


z, lambda_s, lambda_h = sp.symbols("z lambda_s lambda_H", positive=True, real=True)
source_coordinates = sp.Matrix([z, lambda_s])
invariant_readouts = sp.Matrix([z, lambda_s * z**2 / lambda_h])
source_jacobian = invariant_readouts.jacobian(source_coordinates)

detector_response = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
composed_response = sp.simplify(detector_response * source_jacobian)
composed_gram = sp.simplify(composed_response.T * composed_response)
composed_gram_determinant = sp.factor(composed_gram.det())

zero_mixing_jacobian = source_jacobian.subs(z, 0)
zero_mixing_response = composed_response.subs(z, 0)

checks = {
    "source_jacobian_has_expected_form": source_jacobian == sp.Matrix(
        [[1, 0], [2 * lambda_s * z / lambda_h, z**2 / lambda_h]]
    ),
    "source_wedge_is_nonzero_off_zero_mixing": sp.factor(source_jacobian.det()) == z**2 / lambda_h,
    "completed_detector_response_preserves_probability": sp.ones(1, 3) * detector_response == sp.zeros(1, 2),
    "completed_detector_response_has_rank_two": detector_response.rank() == 2,
    "formal_composition_has_rank_two": composed_response.rank() == 2,
    "composed_gram_determinant_factorizes": composed_gram_determinant == 3 * z**4 / lambda_h**2,
    "zero_mixing_source_rank_collapses": zero_mixing_jacobian.rank() == 1,
    "zero_mixing_composed_rank_collapses": zero_mixing_response.rank() == 1,
    "zero_mixing_quartic_column_vanishes": zero_mixing_response[:, 1] == sp.zeros(3, 1),
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP576",
    "classification": "rank-two invariant portal entrance plus conditional rank-two completed detector composition; common-frame physical interface absent",
    "source_domain": "z>0, lambda_H>0, lambda_s>0",
    "source_coordinates": ["z", "lambda_s"],
    "invariant_readouts": ["r=z", "q=lambda_s*z^2/lambda_H"],
    "source_jacobian": encode_matrix(source_jacobian),
    "source_wedge": str(sp.factor(source_jacobian.det())),
    "detector_response": encode_matrix(detector_response),
    "composed_response": encode_matrix(composed_response),
    "composed_gram": encode_matrix(composed_gram),
    "composed_gram_determinant": str(composed_gram_determinant),
    "smallest_exact_falsifier": "z=0 makes the quartic source column vanish and collapses both entrance and composed rank to one",
    "authority_boundary": "D may be composed with A only after a publication-bound calibrated interface identifies the detector input frame with invariant (r,q)",
    "selector_status": "separator, not selector or rigidifier",
    "remaining_gate": "portal-complete common-frame detector transport with completed null or calibrated exposure record and uncertainty-stable rank",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp576_portal_detector_rank_composition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
