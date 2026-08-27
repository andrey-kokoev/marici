from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def linear_record(source: F, loading: F, tap: F) -> F:
    return source + loading * tap


def two_tap_intercept(tap_1: F, record_1: F, tap_2: F, record_2: F) -> F:
    return (tap_2 * record_1 - tap_1 * record_2) / (tap_2 - tap_1)


def main() -> None:
    tap_1, tap_2, tap_3 = F(1, 10), F(1, 5), F(3, 10)
    source_by_condition = {
        "none": F(1, 8), "D": F(9, 64), "E": F(7, 64), "DE": F(5, 32)
    }
    loading_by_condition = {
        "none": F(1, 4), "D": F(-1, 8), "E": F(3, 16), "DE": F(1, 16)
    }

    # One tap is non-identifying: shift the intercept and compensate the slope.
    source = source_by_condition["none"]
    loading = loading_by_condition["none"]
    one_record = linear_record(source, loading, tap_1)
    intercept_shift = F(1, 32)
    alternative_source = source + intercept_shift
    alternative_loading = loading - intercept_shift / tap_1
    assert linear_record(alternative_source, alternative_loading, tap_1) == one_record
    assert (alternative_source, alternative_loading) != (source, loading)

    recovered = {}
    for condition in source_by_condition:
        first = linear_record(source_by_condition[condition], loading_by_condition[condition], tap_1)
        second = linear_record(source_by_condition[condition], loading_by_condition[condition], tap_2)
        recovered[condition] = two_tap_intercept(tap_1, first, tap_2, second)
    assert recovered == source_by_condition

    # Quadratic loading aliases a shifted intercept under two-point linear
    # extrapolation. A third equally spaced tap detects and repairs one curvature mode.
    curvature = F(1, 8)

    def quadratic_record(tap: F) -> F:
        return source + loading * tap + curvature * tap**2

    q1, q2, q3 = quadratic_record(tap_1), quadratic_record(tap_2), quadratic_record(tap_3)
    biased_two_tap = two_tap_intercept(tap_1, q1, tap_2, q2)
    expected_bias = -curvature * tap_1 * tap_2
    assert biased_two_tap - source == expected_bias == F(-1, 400)
    second_difference = q3 - 2 * q2 + q1
    assert second_difference == F(1, 400)
    quadratic_intercept = 3 * q1 - 3 * q2 + q3
    assert quadratic_intercept == source

    result = {
        "schema": "marici.aspect.source-tap-back-action.v1",
        "status": "pass",
        "tap_strengths": [str(tap_1), str(tap_2), str(tap_3)],
        "one_tap_identifies_untapped_source": False,
        "one_tap_alias_intercept_shift": str(intercept_shift),
        "two_tap_linear_intercepts": {key: str(value) for key, value in recovered.items()},
        "two_tap_exact_under_affine_loading": True,
        "quadratic_curvature": str(curvature),
        "two_tap_quadratic_intercept_bias": str(expected_bias),
        "third_tap_second_difference": str(second_difference),
        "three_tap_quadratic_intercept": str(quadratic_intercept),
        "verdict": "A one-strength source tap cannot identify the untapped statistic; two strengths recover it under affine loading, while a third strength is required to expose and repair one quadratic back-action mode.",
        "claim_boundary": "known tap strengths and polynomial loading through degree two; no monitor detector nuisance, hysteresis, reset-tap interaction, or source drift across tap settings",
    }
    output = Path(__file__).parents[1] / "results" / "source_tap_back_action.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
