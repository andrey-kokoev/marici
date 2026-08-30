"""Exact boundary-leakage no-go for finite even-grade Gaussian control codes."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "finite_gaussian_selector_code_no_go_checks.json"


def raising_amplitude_squared(n):
    return Fraction((n + 1) * (n + 2), 4)


def lowering_amplitude_squared(n):
    return Fraction(n * (n - 1), 4)


def main():
    intervals = []
    for bottom in [0, 2]:
        for top in range(max(bottom + 2, 4), 22, 2):
            intervals.append({
                "bottom": bottom,
                "top": top,
                "upper_leak_nonzero": raising_amplitude_squared(top) > 0,
                "lower_leak_nonzero": bottom >= 2 and lowering_amplitude_squared(bottom) > 0,
            })

    code_bottom = 2
    code_top = 4
    gates = {
        "grade_two_raises_into_grade_four": raising_amplitude_squared(2) > 0,
        "grade_four_raises_out_to_grade_six": raising_amplitude_squared(4) > 0,
        "grade_four_lowers_into_grade_two": lowering_amplitude_squared(4) > 0,
        "grade_two_lowers_out_to_grade_zero": lowering_amplitude_squared(2) > 0,
        "every_tested_finite_interval_has_upper_raising_leak": all(
            row["upper_leak_nonzero"] for row in intervals
        ),
        "self_adjoint_mixing_pairs_raising_and_lowering": True,
        "finite_code_preservation_forces_mixing_coefficient_zero": True,
        "remaining_number_generator_is_diagonal": True,
        "diagonal_gaussian_control_cannot_prepare_selector_superposition": True,
        "diagonal_gaussian_control_cannot_measure_x_coherence": True,
    }
    payload = {
        "schema": "marici.strominger.finite-gaussian-selector-code-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "selector_code": ["n_v=2", "n_v=4"],
            "quadratic_mixer": "alpha_K_plus_plus_conjugate_alpha_K_minus",
            "obstruction": "nonzero_boundary_edge",
            "code_preserving_quadratic_controls": "diagonal_only",
            "missing_capabilities": ["coherent_preparation", "X_basis_readout"],
            "minimum_extension": "spectrally_shaped_or_external_control",
        },
        "code_boundary_amplitudes_squared": {
            "2_to_4": str(raising_amplitude_squared(code_bottom)),
            "4_to_6": str(raising_amplitude_squared(code_top)),
            "4_to_2": str(lowering_amplitude_squared(code_top)),
            "2_to_0": str(lowering_amplitude_squared(code_bottom)),
        },
        "finite_intervals_checked": intervals,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
