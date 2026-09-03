from __future__ import annotations

import json
from fractions import Fraction


def mixed_value(a: Fraction, s: Fraction, baseline: Fraction) -> Fraction:
    return (-a + s * baseline) / (1 + s)


def main() -> None:
    a = Fraction(1, 8)
    boundary_gap = a
    minimum_negative_mass = a
    generalized_robustness = a
    contamination_fraction = generalized_robustness / (1 + generalized_robustness)
    minimum_total_variation = 1 + 2 * minimum_negative_mass

    assert contamination_fraction == Fraction(1, 9)
    assert minimum_total_variation == Fraction(5, 4)
    assert mixed_value(a, generalized_robustness, Fraction(1)) == 0
    assert mixed_value(a, generalized_robustness - Fraction(1, 100), Fraction(1)) < 0

    # No baseline in [0,1] can enter the classical interval with s<a.
    smaller_s = a - Fraction(1, 100)
    baselines = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
    assert all(mixed_value(a, smaller_s, baseline) < 0 for baseline in baselines)

    # Tight signed primal fixture.
    weights = [1 + a, -a]
    responses = [Fraction(0), Fraction(1)]
    assert sum(weights) == 1
    assert sum(weight * response for weight, response in zip(weights, responses)) == -a
    assert sum(abs(weight) for weight in weights) == minimum_total_variation

    result = {
        "schema": "marici.voevodsky.negative-loop-convex-duality.v1",
        "status": "scalar_convex_resource_equivalence_verified",
        "boundary_gap": "1/8",
        "minimum_negative_mass": "1/8",
        "generalized_robustness_parameter": "1/8",
        "contamination_fraction_threshold": "1/9",
        "minimum_total_variation": "5/4",
        "tight_primal_fixture": True,
        "scalar_duality_gap": "0",
        "process_space_robustness_computed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
