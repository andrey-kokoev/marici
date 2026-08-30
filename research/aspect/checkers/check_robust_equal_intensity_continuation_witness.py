from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def analyzer_click(
    horizontal_population: F,
    eta_parallel: F,
    eta_perp: F,
    dark_click: F,
) -> F:
    optical_click = eta_perp + (eta_parallel - eta_perp) * horizontal_population
    return dark_click + (F(1) - dark_click) * optical_click


def depolarized_horizontal_population(original: F, depolarization: F) -> F:
    return (F(1) - depolarization) * original + depolarization * F(1, 2)


def gap(
    common_survival: F,
    eta_parallel: F,
    eta_perp: F,
    depolarization: F,
    dark_click: F,
) -> F:
    horizontal = depolarized_horizontal_population(F(1), depolarization)
    diagonal = depolarized_horizontal_population(F(1, 2), depolarization)
    return common_survival * (
        analyzer_click(horizontal, eta_parallel, eta_perp, dark_click)
        - analyzer_click(diagonal, eta_parallel, eta_perp, dark_click)
    )


def main() -> None:
    common_survival = F(1, 4)
    eta_parallel = F(9, 10)
    eta_perp = F(1, 10)
    depolarization = F(1, 5)
    dark_click = F(1, 100)
    systematic_error = F(1, 100)

    horizontal_population = depolarized_horizontal_population(F(1), depolarization)
    diagonal_population = depolarized_horizontal_population(F(1, 2), depolarization)
    assert horizontal_population == F(9, 10)
    assert diagonal_population == F(1, 2)

    horizontal_click = analyzer_click(horizontal_population, eta_parallel, eta_perp, dark_click)
    diagonal_click = analyzer_click(diagonal_population, eta_parallel, eta_perp, dark_click)
    conditional_gap = horizontal_click - diagonal_click
    absolute_gap = common_survival * conditional_gap
    criticism_margin = absolute_gap - 2 * systematic_error

    assert conditional_gap == F(198, 625)
    assert absolute_gap == F(99, 1250)
    assert criticism_margin == F(37, 625)
    assert criticism_margin > 0

    zero_contrast_gap = gap(common_survival, F(1, 2), F(1, 2), depolarization, dark_click)
    complete_depolarization_gap = gap(common_survival, eta_parallel, eta_perp, F(1), dark_click)
    always_clicking_gap = gap(common_survival, eta_parallel, eta_perp, depolarization, F(1))
    assert zero_contrast_gap == 0
    assert complete_depolarization_gap == 0
    assert always_clicking_gap == 0

    threshold_contrast = 4 * systematic_error / (
        common_survival * (F(1) - dark_click) * (F(1) - depolarization) * 2
    )
    assert eta_parallel - eta_perp > threshold_contrast

    result = {
        "schema": "marici.aspect.robust-equal-intensity-continuation-witness.v1",
        "status": "pass",
        "common_equalized_survival": str(common_survival),
        "eta_parallel": str(eta_parallel),
        "eta_perp": str(eta_perp),
        "depolarization": str(depolarization),
        "dark_click_probability": str(dark_click),
        "systematic_error_per_record": str(systematic_error),
        "horizontal_conditional_click": str(horizontal_click),
        "diagonal_conditional_click": str(diagonal_click),
        "conditional_click_gap": str(conditional_gap),
        "absolute_per_source_gap": str(absolute_gap),
        "worst_case_criticism_margin": str(criticism_margin),
        "minimum_analyzer_contrast_for_positive_margin": str(threshold_contrast),
        "zero_contrast_hostile_gap": str(zero_contrast_gap),
        "complete_depolarization_hostile_gap": str(complete_depolarization_gap),
        "always_clicking_detector_hostile_gap": str(always_clicking_gap),
        "verdict": "The downstream continuation distinction survives all frozen degradations with a positive exact margin.",
        "claim_boundary": "finite exact heralded binary-detector robustness theorem",
    }
    output = Path(__file__).parents[1] / "results" / "robust_equal_intensity_continuation_witness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
