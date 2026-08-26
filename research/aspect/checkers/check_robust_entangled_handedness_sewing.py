from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def werner_witness(p: F) -> F:
    return (F(1) - 3 * p) / 4


def threshold(error_radius: F) -> F:
    """Nominal Werner p threshold for estimate + error_radius < 0."""
    return (F(1) + 4 * error_radius) / 3


def guaranteed_threshold(error_radius: F) -> F:
    """Threshold guaranteeing certification for every allowed estimate."""
    return (F(1) + 8 * error_radius) / 3


def main() -> None:
    matrix_entry_error = F(1, 100)
    stokes_correlation_error = F(1, 100)

    # For w = (a + d - 2c)/2, independent absolute bounds epsilon on
    # a, d, and real c give |w_hat - w| <= 2 epsilon.
    matrix_witness_radius = 2 * matrix_entry_error

    # The directly measurable witness is
    # (1 - <XX> + <YY> - <ZZ>)/4. Three correlation bounds eta give
    # |w_hat - w| <= 3 eta / 4.
    stokes_witness_radius = 3 * stokes_correlation_error / 4
    assert stokes_witness_radius < matrix_witness_radius

    assert threshold(matrix_witness_radius) == F(9, 25)
    assert guaranteed_threshold(matrix_witness_radius) == F(29, 75)
    assert threshold(stokes_witness_radius) == F(103, 300)
    assert guaranteed_threshold(stokes_witness_radius) == F(53, 150)

    benchmark_p = F(1, 2)
    true_witness = werner_witness(benchmark_p)
    assert true_witness == F(-1, 8)

    # Worst allowed estimate is shifted upward by the radius. Applying the
    # certificate adds the radius once more.
    matrix_worst_certificate_upper = true_witness + 2 * matrix_witness_radius
    stokes_worst_certificate_upper = true_witness + 2 * stokes_witness_radius
    assert matrix_worst_certificate_upper == F(-17, 200)
    assert stokes_worst_certificate_upper == F(-11, 100)
    assert matrix_worst_certificate_upper < 0
    assert stokes_worst_certificate_upper < 0

    boundary_p = F(1, 3)
    assert werner_witness(boundary_p) == 0
    assert werner_witness(boundary_p) + stokes_witness_radius > 0

    result = {
        "schema": "marici.aspect.robust-entangled-handedness-sewing.v1",
        "status": "pass",
        "decision_rule": "certify handedness when measured witness plus its calibrated error radius is negative",
        "matrix_entry_error": str(matrix_entry_error),
        "matrix_witness_error_radius": str(matrix_witness_radius),
        "matrix_nominal_p_threshold": str(threshold(matrix_witness_radius)),
        "matrix_all_errors_p_threshold": str(guaranteed_threshold(matrix_witness_radius)),
        "stokes_correlation_error": str(stokes_correlation_error),
        "stokes_witness_error_radius": str(stokes_witness_radius),
        "stokes_nominal_p_threshold": str(threshold(stokes_witness_radius)),
        "stokes_all_errors_p_threshold": str(guaranteed_threshold(stokes_witness_radius)),
        "benchmark_p": str(benchmark_p),
        "benchmark_true_witness": str(true_witness),
        "benchmark_matrix_worst_certificate_upper": str(matrix_worst_certificate_upper),
        "benchmark_stokes_worst_certificate_upper": str(stokes_worst_certificate_upper),
        "preferred_instrument": "direct XX, YY, and ZZ coincidence correlations with calibrated absolute error bounds",
        "verdict": "Direct Stokes correlations give a tighter robust sewing certificate than separately bounding reconstructed matrix entries.",
        "claim_boundary": "deterministic bounded-error audit; does not derive the bounds from finite-count statistics",
    }
    output = Path(__file__).parents[1] / "results" / "robust_entangled_handedness_sewing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
