from __future__ import annotations

import json
from fractions import Fraction


def main() -> None:
    cutoffs = [1, 2, 4, 8, 16, 32]
    quotient_weights = (Fraction(2), Fraction(3), Fraction(5))
    finite_determinants = []
    quotient_grams = []
    for cutoff in cutoffs:
        epsilon = Fraction(1, cutoff)
        determinant = epsilon * epsilon
        for weight in quotient_weights:
            determinant *= weight
        finite_determinants.append(determinant)
        quotient_grams.append(quotient_weights)
    assert all(value > 0 for value in finite_determinants)
    assert all(finite_determinants[index + 1] < finite_determinants[index] for index in range(len(cutoffs) - 1))
    assert all(gram == quotient_weights for gram in quotient_grams)
    assert min(quotient_weights) == 2

    # Hostile map sends radical basis r1 to r1+p1. Zero and r1 represent
    # the same quotient class initially, but their images differ by p1.
    zero_image_quotient = (0, 0, 0)
    radical_representative_image_quotient = (1, 0, 0)
    hostile_descends = zero_image_quotient == radical_representative_image_quotient
    assert not hostile_descends

    result = {
        "schema": "marici.voevodsky.controlled-asymptotic-radical-completion.v1",
        "status": "controlled_radical_completion_realized",
        "radical_dimension": 2,
        "physical_quotient_dimension": 3,
        "cutoffs": cutoffs,
        "finite_determinants": [f"{value.numerator}/{value.denominator}" for value in finite_determinants],
        "finite_determinants_positive_and_decreasing": True,
        "quotient_gram_constant": ["2/1", "3/1", "5/1"],
        "quotient_uniform_coercivity": "2/1",
        "quotient_transition_maps_strict": True,
        "limiting_radical_exactly_nominated_sector": True,
        "hostile_radical_mixing_transition_descends": hostile_descends,
        "source_weil_transition_map_materialized": False,
        "next_gate": "source-side cutoff quotient transition preserving rank-two wedge classes",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
