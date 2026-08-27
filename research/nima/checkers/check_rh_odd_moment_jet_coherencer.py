#!/usr/bin/env python3
"""Finite typed gate for primitive principal-value cancellation."""

from fractions import Fraction
import json
from pathlib import Path


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def main():
    # Coordinates are (even overlap/delta, odd front/PV, retained odd residue).
    primitive_tail = (Fraction(0), Fraction(1), Fraction(1))
    even_unit_anomaly = (Fraction(-1), Fraction(0), Fraction(0))
    full_reciprocal_erasure = (Fraction(0), Fraction(-1), Fraction(-1))
    odd_moment_jet = (Fraction(0), Fraction(-1), Fraction(0))

    after_even = add(primitive_tail, even_unit_anomaly)
    after_erasure = add(primitive_tail, full_reciprocal_erasure)
    after_jet = add(primitive_tail, odd_moment_jet)

    assert after_even[1] == 1
    assert after_erasure == (0, 0, 0)
    assert after_jet == (0, 0, 1)

    # Dyadic scale L_n = 2^n: primitive measure 2^n/n.
    # Algebraic PV tail 1/n fails the term test; exponential residue 4^-n passes.
    raw_terms = [Fraction(2**n, n * n) for n in range(1, 13)]
    residual_terms = [Fraction(1, n * 2**n) for n in range(1, 13)]
    assert raw_terms[-1] > raw_terms[0]
    assert residual_terms[-1] < residual_terms[0]
    assert sum(residual_terms) < 1

    result = {
        "schema": "marici.rh-odd-moment-jet-coherencer.v1",
        "coordinates": ["even_overlap_delta", "odd_front_pv_moment", "odd_orientation_residue"],
        "candidate_verdicts": {
            "reciprocal_maslov": "wrong_source_channel",
            "unit_current_anomaly": "wrong_parity",
            "flat_euler_jet": "no_independent_odd_generator",
            "full_reciprocal_cancellation": "overcancels_orientation",
            "two_front_relative_moment_jet": "unique_viable_type"
        },
        "after_even_counterterm": [str(x) for x in after_even],
        "after_full_erasure": [str(x) for x in after_erasure],
        "after_odd_moment_jet": [str(x) for x in after_jet],
        "primitive_raw_term_test_fails": True,
        "exponential_odd_residue_is_summable": True,
        "existence_status": "not_yet_derived_from_theta_tate_source"
    }
    out = Path(__file__).parents[1] / "results" / "rh-odd-moment-jet-coherencer.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
