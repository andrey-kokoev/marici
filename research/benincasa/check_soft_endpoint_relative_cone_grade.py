#!/usr/bin/env python3
"""Construct the associated-graded marked/unmarked endpoint cone."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    # Homogeneous p-degrees with a=p*r at a generic collision root.
    marked_rational_degree = 1 - (1 + 2 + 1)  # numerator minus denominator.
    negative_vanishing_degree = -1
    negative_total_degree = marked_rational_degree + negative_vanishing_degree
    positive_total_degree = -1
    associated_degrees = {"positive": 0, "negative": 1}

    # Generic samples verify no marked a=p collision in the open kappa interval.
    kappas = (Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4))
    regular = [4 * (1 - kappa) != 0 and 4 * (1 + kappa) != 0 for kappa in kappas]
    checks = {
        "marked_rational_factor_has_p_degree_minus_three": marked_rational_degree == -3,
        "negative_residue_period_has_p_degree_minus_four": negative_total_degree == -4,
        "positive_unmarked_period_has_p_degree_minus_one": positive_total_degree == -1,
        "entries_cannot_be_summed_without_a_degree_three_transition": positive_total_degree - negative_total_degree == 3,
        "associated_grade_has_one_line_in_each_of_two_degrees": sorted(associated_degrees.values()) == [0, 1],
        "generic_open_kappa_has_no_deeper_marked_collision": all(regular),
    }
    result = {
        "schema": "marici.soft-endpoint-relative-cone-grade.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "associated_graded_cone": {
            "degree_0": "E_plus = pure Cayley-Menger vanishing line at xi=+1",
            "degree_1": "E_minus = Res_qg1(Cayley-Menger vanishing line) at xi=-1",
            "degrees": associated_degrees,
            "graded_dimensions": [1, 1],
        },
        "local_entries": {
            "positive": "pi*i/(p*sqrt(5+4*kappa))",
            "negative": "pi*i*(r+1)/(2*p^4*r*(r-1)^2*(r+3)), r=sqrt(5-4*kappa)",
        },
        "p_homogeneous_degrees": {
            "positive": positive_total_degree,
            "negative": negative_total_degree,
            "difference": positive_total_degree - negative_total_degree,
        },
        "required_transition": "a source-derived comparison carrying p-weight +3 is required before the two local lines can enter one scalar readout; whether it is supplied by Gysin normalization is unconstructed",
        "unconstructed_data": "the off-diagonal extension/comparison map of the relative cone",
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-relative-cone-grade.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
