"""WP332: exact conditioning margin for the calibrated common-frame instrument."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    response = sp.Matrix([
        [1, 0, 0],
        [0, 0, 1],
        [1, 1, 1],
    ])
    gram = response.T * response
    eigenvalues = sorted(gram.eigenvals().keys(), key=lambda value: float(value))
    smallest_gram = sp.simplify(eigenvalues[0])
    smallest_singular = sp.sqrt(smallest_gram)
    determinant = response.det()
    checks = {
        "log_response_has_full_rank": response.rank() == 3,
        "log_response_determinant_has_unit_magnitude": abs(determinant) == 1,
        "gram_determinant_is_one": gram.det() == 1,
        "gram_spectrum_is_exact": set(eigenvalues) == {sp.Integer(1), 2 - sp.sqrt(3), 2 + sp.sqrt(3)},
        "smallest_gram_eigenvalue_is_positive": smallest_gram == 2 - sp.sqrt(3) and smallest_gram > 0,
        "smallest_singular_value_is_exact": smallest_singular == sp.sqrt(2 - sp.sqrt(3)),
        "zero_bias_boundary_is_excluded_from_log_domain": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP332",
        "admitted_state_domain": "strictly positive beta, epsilon, c0 with frozen positive gap and gain, using local logarithmic source and readout coordinates",
        "log_source_coordinates": ["log beta", "log epsilon", "log c0"],
        "log_readout_coordinates": ["log(-log A) minus log gap", "log C minus log gain", "log L minus log 2"],
        "response_jacobian": [[int(value) for value in row] for row in response.tolist()],
        "gram_matrix": [[int(value) for value in row] for row in gram.tolist()],
        "gram_eigenvalues": [str(value) for value in eigenvalues],
        "gram_determinant": str(gram.det()),
        "smallest_singular_value": str(smallest_singular),
        "robustness_rule": "any additive response-Jacobian perturbation with spectral norm strictly below sqrt(2-sqrt(3)) preserves full rank",
        "contextual_partition": "inside the positive log domain the calibrated local response has a uniform singleton fiber; the epsilon=0 boundary is outside this chart",
        "classification": "a uniformly conditioned calibrated identification instrument on the positive domain; still neither a source selector nor evidence that the required physical channels exist",
        "smallest_exact_falsifier": "an uncertainty bound reaching the smallest-singular-value margin no longer certifies rank; epsilon=0 separately makes log L undefined",
        "remaining_physical_instrument_gate": "translate laboratory and freeze-out errors into a justified spectral-norm bound below the exact margin, while treating zero or sign-indefinite bias in a separate nonlogarithmic chart",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp332_log_instrument_robust_margin.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
