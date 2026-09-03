from __future__ import annotations

import json
from fractions import Fraction


def observed(p: Fraction, baseline: Fraction) -> Fraction:
    return (1 - p) * Fraction(-1, 8) + p * baseline


def threshold(baseline: Fraction) -> Fraction:
    return Fraction(1, 1) / (1 + 8 * baseline)


def main() -> None:
    ideal = Fraction(-1, 8)
    additive_margin = Fraction(1, 8)
    assert ideal + Fraction(1, 9) < 0
    assert ideal + additive_margin == 0

    baselines = [Fraction(0), Fraction(1, 8), Fraction(1, 2), Fraction(1)]
    thresholds = [threshold(value) for value in baselines]
    assert thresholds == [Fraction(1), Fraction(1, 2), Fraction(1, 5), Fraction(1, 9)]

    for baseline, bound in zip(baselines, thresholds):
        below = bound / 2
        assert observed(below, baseline) < 0
        assert observed(bound, baseline) == 0
        if bound < 1:
            above = (bound + 1) / 2
            assert observed(above, baseline) > 0

    # A negative scalar does not identify the implemented route.
    scalar_negative = observed(Fraction(1, 10), Fraction(1)) < 0
    route_identity_verified = False
    assert scalar_negative is True
    assert route_identity_verified is False

    result = {
        "schema": "marici.voevodsky.negative-loop-robustness.v1",
        "status": "scalar_rival_exclusion_margin_verified",
        "ideal_value": "-1/8",
        "additive_error_margin_strict": "1/8",
        "contamination_threshold_formula": "1/(1+8b)",
        "baseline_thresholds": {str(b): str(t) for b, t in zip(baselines, thresholds)},
        "worst_case_unit_baseline_threshold_strict": "1/9",
        "negative_scalar_implies_route_identity": False,
        "statistical_confidence_certificate_supplied": False,
        "shared_control_fault_bound_supplied": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
