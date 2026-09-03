from __future__ import annotations

import json
from fractions import Fraction


def negative_mass(weights: list[Fraction]) -> Fraction:
    return sum((-weight for weight in weights if weight < 0), Fraction(0))


def total_variation(weights: list[Fraction]) -> Fraction:
    return sum((abs(weight) for weight in weights), Fraction(0))


def expectation(weights: list[Fraction], responses: list[Fraction]) -> Fraction:
    return sum((weight * response for weight, response in zip(weights, responses)), Fraction(0))


def main() -> None:
    weights = [Fraction(9, 8), Fraction(-1, 8)]
    responses = [Fraction(0), Fraction(1)]
    assert sum(weights) == 1
    assert all(0 <= response <= 1 for response in responses)
    assert expectation(weights, responses) == Fraction(-1, 8)
    assert negative_mass(weights) == Fraction(1, 8)
    assert total_variation(weights) == Fraction(5, 4)
    assert total_variation(weights) == 1 + 2 * negative_mass(weights)

    # Finite exact fixtures satisfy Omega >= -N.
    fixtures = [
        ([Fraction(3, 2), Fraction(-1, 2)], [Fraction(0), Fraction(1)]),
        ([Fraction(5, 4), Fraction(-1, 4)], [Fraction(1, 2), Fraction(1)]),
        ([Fraction(2), Fraction(-1), Fraction(0)], [Fraction(0), Fraction(1), Fraction(1, 3)]),
    ]
    for fixture_weights, fixture_responses in fixtures:
        assert sum(fixture_weights) == 1
        omega = expectation(fixture_weights, fixture_responses)
        assert omega >= -negative_mass(fixture_weights)

    observed_values = [Fraction(-1, 8), Fraction(-1, 16), Fraction(-1, 100)]
    negativity_bounds = [-value for value in observed_values]
    assert negativity_bounds == [Fraction(1, 8), Fraction(1, 16), Fraction(1, 100)]

    result = {
        "schema": "marici.voevodsky.negative-loop-signed-cost.v1",
        "status": "tight_signed_factorization_cost_verified",
        "response_range": "[0,1]",
        "exact_witness_value": "-1/8",
        "minimum_negative_mass": "1/8",
        "minimum_total_variation": "5/4",
        "tight_two_state_fixture": True,
        "general_bound": "negative_mass >= -observed_value for observed_value < 0",
        "complex_quasiprobability_cost_bounded": False,
        "computational_separation_claimed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
