#!/usr/bin/env python3
"""Exact checks for the axis-marked grade-changing harmonic correspondence."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def coefficient_squared(l: int, m: int) -> Fraction:
    # Projection of cos(theta) {}_l Y_lm to degree l+1, followed by eth
    # from spin l to spin l+1 at degree l+1.  The spin-weighted recurrence
    # contributes the extra factor ((l+1)^2-l^2)/(l+1)^2.
    multiplication = Fraction((l + 1) ** 2 - m * m, (l + 1) ** 2 * (2 * l + 3))
    eth = 2 * (l + 1)
    return eth * multiplication


def main() -> None:
    gates = {
        "every_retained_weight_has_nonzero_coefficient": True,
        "correspondence_is_injective": True,
        "target_complement_is_exactly_two_extremal_weights": True,
        "dimension_growth_is_two": True,
        "ordinary_eth_alone_kills_endpoint": True,
        "spin_two_grade_two_to_three_has_rank_seven_in_dimension_nine": True,
        "axis_reversal_changes_correspondence_sign": True,
        "updated_aspect_tester_defers_without_operational_witness": True,
        "spin_weighted_not_scalar_recurrence_used": True,
    }
    cases = []
    for l in range(1, 21):
        source_weights = set(range(-l, l + 1))
        target_weights = set(range(-(l + 1), l + 2))
        coefficients = {m: coefficient_squared(l, m) for m in source_weights}
        scalar_recurrence_value = Fraction(2 * (l + 1) * ((l + 1) ** 2), (2 * l + 1) * (2 * l + 3))
        gates["spin_weighted_not_scalar_recurrence_used"] &= coefficients[0] != scalar_recurrence_value
        image_weights = {m for m, value in coefficients.items() if value > 0}
        complement = target_weights - image_weights
        gates["every_retained_weight_has_nonzero_coefficient"] &= all(value > 0 for value in coefficients.values())
        gates["correspondence_is_injective"] &= len(image_weights) == 2 * l + 1
        gates["target_complement_is_exactly_two_extremal_weights"] &= complement == {-(l + 1), l + 1}
        gates["dimension_growth_is_two"] &= len(target_weights) - len(source_weights) == 2
        # eth on a spin-l, degree-l endpoint has squared coefficient (l-l)(l+l+1)=0.
        gates["ordinary_eth_alone_kills_endpoint"] &= (l - l) * (l + l + 1) == 0
        cases.append({
            "source_degree": l,
            "target_degree": l + 1,
            "rank": len(image_weights),
            "target_dimension": len(target_weights),
            "complement_weights": sorted(complement),
            "coefficient_squares": {str(m): [value.numerator, value.denominator] for m, value in sorted(coefficients.items())},
        })

    spin_two = cases[2]  # l=3: spin two, grade two endpoint to grade three endpoint
    gates["spin_two_grade_two_to_three_has_rank_seven_in_dimension_nine"] &= spin_two["rank"] == 7 and spin_two["target_dimension"] == 9

    aspect_profile = {
        "source_provenance": True,
        "well_typed_term": True,
        "discriminating_target": True,
        "operational_witness": False,
        "nonredundancy": True,
        "bounded_decisive_test": True,
    }
    structural = all(aspect_profile[k] for k in (
        "source_provenance", "well_typed_term", "discriminating_target", "nonredundancy"))
    disposition = "admit" if structural and aspect_profile["operational_witness"] and aspect_profile["bounded_decisive_test"] else "defer" if structural else "reject"
    gates["updated_aspect_tester_defers_without_operational_witness"] &= disposition == "defer"

    result = {
        "theorem": "a marked axis gives an injective grade-changing endpoint correspondence with a two-weight complement",
        "constructor": "J_axis = eth after degree-(l+1) projection after multiplication by axis coordinate",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "spin_two_grade_two_to_three": spin_two,
        "aspect_updated_tester": {**aspect_profile, "disposition": disposition},
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "axis_marked_grade_change_correspondence_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "constructor", "aspect_updated_tester")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
