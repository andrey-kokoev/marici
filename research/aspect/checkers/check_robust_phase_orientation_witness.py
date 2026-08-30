from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def plus_port_probability(
    reference_transmission: F,
    signal_transmission: F,
    root_product: F,
    visibility: F,
    phase_cosine: F,
    orientation: int,
) -> F:
    return (
        reference_transmission
        + signal_transmission
        + F(2 * orientation) * visibility * root_product * phase_cosine
    ) / 4


def detector_click(optical_probability: F, dark_click: F) -> F:
    return dark_click + (F(1) - dark_click) * optical_probability


def orientation_gap(
    root_product: F,
    visibility: F,
    phase_cosine: F,
    dark_click: F,
) -> F:
    return (F(1) - dark_click) * visibility * root_product * phase_cosine


def main() -> None:
    reference_transmission = F(1)
    signal_transmission = F(81, 100)
    root_product = F(9, 10)
    visibility = F(9, 10)
    phase_cosine = F(4, 5)
    dark_click = F(1, 100)
    systematic_error = F(1, 100)
    assert root_product * root_product == reference_transmission * signal_transmission

    plus_xz = plus_port_probability(
        reference_transmission,
        signal_transmission,
        root_product,
        visibility,
        phase_cosine,
        1,
    )
    plus_zx = plus_port_probability(
        reference_transmission,
        signal_transmission,
        root_product,
        visibility,
        phase_cosine,
        -1,
    )
    assert F(0) <= plus_zx < plus_xz <= F(1)

    click_xz = detector_click(plus_xz, dark_click)
    click_zx = detector_click(plus_zx, dark_click)
    raw_optical_gap = plus_xz - plus_zx
    observed_gap = click_xz - click_zx
    criticism_margin = observed_gap - 2 * systematic_error
    assert raw_optical_gap == F(81, 125)
    assert observed_gap == F(8019, 12500)
    assert criticism_margin == F(7769, 12500)
    assert criticism_margin > 0

    minimum_visibility = 2 * systematic_error / (
        (F(1) - dark_click) * root_product * phase_cosine
    )
    assert minimum_visibility == F(25, 891)
    assert visibility > minimum_visibility

    zero_visibility = orientation_gap(root_product, F(0), phase_cosine, dark_click)
    quadrature_phase = orientation_gap(root_product, visibility, F(0), dark_click)
    missing_arm = orientation_gap(F(0), visibility, phase_cosine, dark_click)
    assert zero_visibility == quadrature_phase == missing_arm == 0

    result = {
        "schema": "marici.aspect.robust-phase-orientation-witness.v1",
        "status": "pass",
        "reference_arm_transmission": str(reference_transmission),
        "signal_arm_transmission": str(signal_transmission),
        "visibility": str(visibility),
        "phase_cosine_lower_bound": str(phase_cosine),
        "dark_click_probability": str(dark_click),
        "systematic_error_per_orientation_record": str(systematic_error),
        "plus_port_probability_xz": str(plus_xz),
        "plus_port_probability_zx": str(plus_zx),
        "raw_optical_orientation_gap": str(raw_optical_gap),
        "observed_orientation_gap": str(observed_gap),
        "worst_case_criticism_margin": str(criticism_margin),
        "minimum_visibility_for_positive_margin": str(minimum_visibility),
        "zero_visibility_hostile_gap": str(zero_visibility),
        "quadrature_phase_hostile_gap": str(quadrature_phase),
        "missing_arm_hostile_gap": str(missing_arm),
        "verdict": "The phase-reference orientation separator survives the frozen imbalance and noise budget.",
        "claim_boundary": "finite exact static robustness margin; no temporal drift or dispersion model",
    }
    output = Path(__file__).parents[1] / "results" / "robust_phase_orientation_witness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
