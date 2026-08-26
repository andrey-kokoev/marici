from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


TIMES = (-3, -1, 1, 3)


def record(time: int, orientation: int, base: F, half_gap: F, drift: tuple[F, F, F]) -> F:
    constant, linear, quadratic = drift
    return base + F(orientation) * half_gap + constant + linear * time + quadratic * time * time


def contrast(schedule: tuple[int, ...], base: F, half_gap: F, drift: tuple[F, F, F]) -> F:
    plus = [record(time, orientation, base, half_gap, drift) for time, orientation in zip(TIMES, schedule) if orientation == 1]
    minus = [record(time, orientation, base, half_gap, drift) for time, orientation in zip(TIMES, schedule) if orientation == -1]
    return sum(plus, F(0)) / len(plus) - sum(minus, F(0)) / len(minus)


def main() -> None:
    observed_orientation_gap = F(8019, 12500)
    half_gap = observed_orientation_gap / 2
    systematic_error = F(1, 100)
    curvature_bound = F(1, 10000)
    base = F(1, 5)
    balanced = (1, -1, -1, 1)
    consecutive = (1, 1, -1, -1)

    arbitrary_affine = (F(7, 100), F(-3, 200), F(0))
    balanced_affine_contrast = contrast(balanced, base, half_gap, arbitrary_affine)
    assert balanced_affine_contrast == observed_orientation_gap

    worst_quadratic = (F(0), F(0), -curvature_bound)
    balanced_curved_contrast = contrast(balanced, base, half_gap, worst_quadratic)
    assert balanced_curved_contrast == observed_orientation_gap - 8 * curvature_bound
    worst_case_margin = balanced_curved_contrast - 2 * systematic_error
    assert worst_case_margin == F(7759, 12500)
    assert worst_case_margin > 0

    maximum_curvature = (observed_orientation_gap - 2 * systematic_error) / 8
    assert maximum_curvature == F(7769, 100000)

    cancelling_slope = observed_orientation_gap / 4
    consecutive_cancelled = contrast(
        consecutive,
        base,
        half_gap,
        (F(0), cancelling_slope, F(0)),
    )
    assert consecutive_cancelled == 0

    result = {
        "schema": "marici.aspect.drift-balanced-phase-orientation.v1",
        "status": "pass",
        "times": list(TIMES),
        "balanced_schedule": ["XZ" if x == 1 else "ZX" for x in balanced],
        "consecutive_hostile_schedule": ["XZ" if x == 1 else "ZX" for x in consecutive],
        "affine_drift_cancelled_exactly": True,
        "quadratic_curvature_bound": str(curvature_bound),
        "worst_quadratic_contrast": str(balanced_curved_contrast),
        "systematic_error_per_orientation_mean": str(systematic_error),
        "worst_case_criticism_margin": str(worst_case_margin),
        "maximum_quadratic_curvature_for_positive_margin": str(maximum_curvature),
        "consecutive_schedule_cancelling_affine_slope": str(cancelling_slope),
        "consecutive_schedule_contrast_under_hostile": str(consecutive_cancelled),
        "verdict": "Symmetric interleaving cancels common affine drift; bounded quadratic curvature preserves a positive orientation margin.",
        "claim_boundary": "deterministic polynomial drift through degree two; no stochastic phase-noise or feedback model",
    }
    output = Path(__file__).parents[1] / "results" / "drift_balanced_phase_orientation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
