from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def ceil_fraction(value: F) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def failure_bound(sample_count_per_route: int, margin: F) -> F:
    return F(1, 2 * sample_count_per_route) / (margin * margin)


def main() -> None:
    margin = F(37, 625)
    target_failure = F(1, 100)
    required_real = F(1, 2) / (target_failure * margin * margin)
    sample_count = ceil_fraction(required_real)

    certified_bound = failure_bound(sample_count, margin)
    predecessor_bound = failure_bound(sample_count - 1, margin)
    assert certified_bound <= target_failure
    assert predecessor_bound > target_failure

    total_trials = 2 * sample_count
    result = {
        "schema": "marici.aspect.robust-continuation-shot-noise.v1",
        "status": "pass",
        "systematic_reserved_margin": str(margin),
        "target_sign_error_probability": str(target_failure),
        "required_real_sample_bound": str(required_real),
        "minimum_integer_trials_per_route": sample_count,
        "total_trials_two_routes": total_trials,
        "certified_chebyshev_failure_bound": str(certified_bound),
        "predecessor_failure_bound": str(predecessor_bound),
        "predecessor_fails_target": True,
        "assumptions": [
            "independent Bernoulli trials within and between route samples",
            "fixed preregistered sample count",
            "systematic effects already bounded by the reserved margin",
        ],
        "verdict": "The robust continuation separator has a finite conservative shot-noise sample certificate.",
        "claim_boundary": "Chebyshev finite-sample sign certificate; no drift, dead-time, or multipair model",
    }
    output = Path(__file__).parents[1] / "results" / "robust_continuation_shot_noise.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
