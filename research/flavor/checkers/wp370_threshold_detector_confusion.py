"""WP370: exact detector-confusion audit for complementary threshold channels."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta = sp.symbols("beta", real=True)
    L, omega, mu = sp.symbols("L Omega mu", positive=True)
    u1, u2, b1, b2 = sp.symbols("u1 u2 b1 b2", real=True)
    amplitude, background_delta = sp.symbols("a delta", real=True)

    contrast = 1 - 2 * beta
    confusion = sp.Matrix([[1 - beta, beta], [beta, 1 - beta]])
    threshold_determinant = -mu**4 / (4 * (L**2 + omega**2)**2)
    threshold_coordinates = sp.Matrix([
        -mu**2 * L / (2 * (L**2 + omega**2)),
        -mu**2 * omega / (2 * (L**2 + omega**2)),
    ])
    source_jacobian = threshold_coordinates.jacobian([L, omega])
    source_jacobian_determinant = sp.factor(source_jacobian.det())
    composed_determinant = sp.factor((confusion * source_jacobian).det())

    threshold_vector = sp.Matrix([u1, u2])
    background = sp.Matrix([b1, b2])
    detector_record = confusion * threshold_vector + background
    recovered = sp.simplify(confusion.inv() * (detector_record - background))

    complete_confusion = confusion.subs(beta, sp.Rational(1, 2))
    hostile_left = sp.Matrix([1, 0])
    hostile_right = sp.Matrix([0, 1])
    differential_record = contrast * amplitude + background_delta

    checks = {
        "confusion_determinant_is_contrast": confusion.det() == contrast,
        "common_channel_eigenvalue_is_one": confusion * sp.Matrix([1, 1]) == sp.Matrix([1, 1]),
        "difference_channel_eigenvalue_is_contrast": confusion * sp.Matrix([1, -1]) == contrast * sp.Matrix([1, -1]),
        "threshold_jacobian_matches_wp369_determinant": sp.simplify(
            source_jacobian_determinant - threshold_determinant
        ) == 0,
        "composed_determinant_factors_at_detector": sp.simplify(
            composed_determinant - contrast * threshold_determinant
        ) == 0,
        "calibrated_inverse_recovers_threshold_vector": recovered == threshold_vector,
        "complete_confusion_collapses_hostile_channels": (
            complete_confusion * hostile_left == complete_confusion * hostile_right
        ),
        "complete_confusion_has_rank_one": complete_confusion.rank() == 1,
        "fixed_background_does_not_change_jacobian": detector_record.jacobian([u1, u2]) == confusion,
        "unknown_differential_background_has_exact_kernel": (
            differential_record.subs({amplitude: 1, background_delta: 0})
            == differential_record.subs({amplitude: 0, background_delta: contrast})
        ),
        "inverse_difference_gain_is_one_over_contrast": sp.simplify(
            confusion.inv() * sp.Matrix([1, -1]) - sp.Matrix([1, -1]) / contrast
        ) == sp.zeros(2, 1),
        "deliberate_complete_confusion_determinant_zero": composed_determinant.subs(beta, sp.Rational(1, 2)) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP370",
        "admitted_state_domain": "local linear two-channel detector with calibrated symmetric confusion beta in [0,1/2], calibrated fixed backgrounds, and the WP369 finite-width threshold map",
        "faithful_quotient_coordinate": "the recovered dispersive/absorptive threshold pair when contrast gamma=1-2*beta is positive; full physical16 remains projected downstream",
        "source_authorized_probe_family": "WP369 complementary threshold channels composed with calibrated detector confusion and background subtraction",
        "contextual_partition": "positive calibrated contrast preserves threshold classes; complete confusion merges channel-swapped packets, and unknown differential background creates an additional kernel",
        "classification": "finite-resolution threshold identifier with exact contrast margin; neither numerical selector nor additional control direction",
        "confusion_matrix": str(confusion),
        "contrast": str(contrast),
        "threshold_jacobian_determinant": str(threshold_determinant),
        "composed_jacobian_determinant": str(composed_determinant),
        "inverse_difference_gain": str(1 / contrast),
        "smallest_exact_falsifier": "at beta=1/2 the packets (1,0) and (0,1) both produce (1/2,1/2), so the complementary threshold channel is erased",
        "remaining_physical_instrument_gate": "independently calibrate a positive contrast lower bound and differential background, then include finite-sample noise and scan support",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp370_threshold_detector_confusion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
