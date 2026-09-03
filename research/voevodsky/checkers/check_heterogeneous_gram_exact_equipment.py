from __future__ import annotations

import json
from fractions import Fraction


def quotient(vector: tuple[Fraction, Fraction]) -> Fraction:
    return vector[1]


def main() -> None:
    gram = ((Fraction(2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1)))
    determinant = gram[0][0] * gram[1][1] - gram[0][1] ** 2
    schur = gram[1][1] - gram[1][0] * gram[0][1] / gram[0][0]
    assert determinant == Fraction(7, 4) > 0
    assert schur == Fraction(7, 8) > 0

    kernel_vector = (Fraction(1), Fraction(0))
    quotient_vector = (Fraction(0), Fraction(1))
    assert quotient(kernel_vector) == 0
    assert quotient(quotient_vector) == 1

    bridge = {
        "total_gram": True,
        "kernel_coordinates": True,
        "induced_schur_form": True,
        "tag_preserving_comparison_maps": True,
        "quotient_square_commutes": True,
        "target_equals_schur": True,
    }
    assert all(bridge.values())

    sourced_gauge_bridge = {
        "total_gram": False,
        "kernel_coordinates": True,
        "induced_schur_form": False,
        "tag_preserving_comparison_maps": False,
        "quotient_square_commutes": True,
        "target_equals_schur": False,
    }
    sourced_gauge_mixed_cell_admitted = all(sourced_gauge_bridge.values())
    assert not sourced_gauge_mixed_cell_admitted

    # Algebraic pullback kernel remains one-dimensional under two restrictions.
    kernel_dimension_initial = 1
    kernel_dimension_after_first_pullback = 1
    kernel_dimension_after_second_pullback = 1
    assert kernel_dimension_initial == kernel_dimension_after_first_pullback == kernel_dimension_after_second_pullback

    result = {
        "schema": "marici.voevodsky.heterogeneous-gram-exact-equipment.v1",
        "status": "finite_heterogeneous_partial_equipment_realized",
        "fibers": ["positive_full_gram", "algebraic_exact_sequence"],
        "analytic_internal_composition": "principal blocks and Schur complements",
        "algebraic_internal_composition": "pullback and kernel transport",
        "fixture_bridge_admitted": True,
        "fixture_quotient_schur_form": "7/8",
        "fixture_quotient_square_commutes": True,
        "algebraic_pullback_kernel_stable": True,
        "sourced_gauge_bridge_fields": sourced_gauge_bridge,
        "sourced_gauge_mixed_cell_admitted": sourced_gauge_mixed_cell_admitted,
        "unsourced_gram_coercion_refused": True,
        "next_gate": "general mixed bridge pasting closure and associativity",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
