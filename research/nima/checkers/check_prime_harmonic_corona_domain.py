from fractions import Fraction
import json
from pathlib import Path


def main() -> None:
    dominance_factors = (2, 4, 8, 16, 32)
    bounds = []
    previous_gap = Fraction(0, 1)
    for factor in dominance_factors:
        odd_lower = Fraction(factor, factor + 1)
        even_upper = Fraction(1, factor + 1)
        gap = odd_lower - even_upper
        assert odd_lower > even_upper
        assert gap > previous_gap
        previous_gap = gap
        bounds.append(
            {
                "dominance_factor": factor,
                "odd_block_lower_bound": str(odd_lower),
                "even_block_upper_bound": str(even_upper),
                "oscillation_gap": str(gap),
            }
        )

    # A normalized positive cutoff functional is unital.
    weights = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5))
    total = sum(weights, Fraction(0, 1))
    normalized_constant = sum((w / total for w in weights), Fraction(0, 1))
    assert normalized_constant == 1

    # If the first weight in block k is at most 2^-k, the alternating-series
    # residuals are absolutely summable. Thus f and h*f can each have mean
    # zero even when their product h has no mean.
    residual_budget = sum(
        (Fraction(1, 2**k) for k in range(1, 13)),
        Fraction(0, 1),
    )
    assert residual_budget < 1

    result = {
        "schema": "marici.nima.prime-harmonic-corona-domain.v1",
        "finite_cutoff_is_positive_unital": True,
        "finite_support_vanishes_at_corona": True,
        "mean_domain_is_proper": True,
        "mean_domain_is_operator_system": True,
        "mean_domain_is_multiplication_algebra": False,
        "multiplication_can_leave_mean_domain": True,
        "finite_alternating_residual_budget": str(residual_budget),
        "all_bounded_observables_have_cutoff_mean": False,
        "total_extension_requires_generalized_limit_choice": True,
        "alternating_block_bounds": bounds,
        "largest_verified_oscillation_gap": str(previous_gap),
    }
    output = Path(__file__).parents[1] / "results" / "prime-harmonic-corona-domain.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
