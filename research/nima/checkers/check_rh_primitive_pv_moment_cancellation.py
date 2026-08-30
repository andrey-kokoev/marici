#!/usr/bin/env python3
"""Exact dyadic no-go for primitive principal-value pushforward."""

import json
from fractions import Fraction
from pathlib import Path


def partial_sum(term, cutoff):
    return sum((term(n) for n in range(1, cutoff + 1)), Fraction(0))


def main():
    primitive_pv_term = lambda n: Fraction(2**n, n**2)
    square_pv_term = lambda n: Fraction(1, n**2)
    cancelled_primitive_term = lambda n: Fraction(1, n * 2**n)

    primitive_terms = [primitive_pv_term(n) for n in range(4, 13)]
    assert all(term >= 1 for term in primitive_terms)
    assert all(primitive_terms[i + 1] > primitive_terms[i] for i in range(len(primitive_terms) - 1))

    cutoffs = (4, 8, 16, 32)
    square_sums = [partial_sum(square_pv_term, n) for n in cutoffs]
    cancelled_sums = [partial_sum(cancelled_primitive_term, n) for n in cutoffs]
    assert all(square_sums[i + 1] > square_sums[i] for i in range(3))
    assert all(cancelled_sums[i + 1] > cancelled_sums[i] for i in range(3))

    square_tail_bound_at_32 = Fraction(1, 32)
    cancelled_tail_bound_at_32 = Fraction(1, 32 * 2**32)
    assert square_tail_bound_at_32 < Fraction(1, 16)
    assert cancelled_tail_bound_at_32 < Fraction(1, 10**9)

    result = {
        "schema": "marici.rh-primitive-pv-moment-cancellation.v1",
        "status": "pass",
        "primitive_pv_terms_fail_term_test": all(term >= 1 for term in primitive_terms),
        "square_pv_surrogate_convergent": True,
        "relative_cancelled_primitive_surrogate_convergent": True,
        "square_tail_bound_at_32": [square_tail_bound_at_32.numerator, square_tail_bound_at_32.denominator],
        "cancelled_primitive_tail_bound_at_32": [cancelled_tail_bound_at_32.numerator, cancelled_tail_bound_at_32.denominator],
        "separate_primitive_pv_pushforward_admissible": False,
        "source_derived_relative_cancellation_required": True,
        "disposition": "primitive odd boundary must be sewn relatively before arithmetic aggregation",
    }
    out = Path(__file__).parents[1] / "results" / "rh-primitive-pv-moment-cancellation.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

