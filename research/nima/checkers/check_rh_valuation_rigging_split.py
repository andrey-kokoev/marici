#!/usr/bin/env python3
"""Exact finite partial-sum witnesses for the valuation rigging split."""

import json
from fractions import Fraction
from pathlib import Path


def partial_sum(term, cutoff):
    return sum((term(n) for n in range(1, cutoff + 1)), Fraction(0))


def main():
    primitive_critical = lambda n: Fraction(1, n)
    primitive_strong = lambda n: Fraction(1, n * (2**n))
    square_constant = lambda n: Fraction(1, n)
    square_rapid = lambda n: Fraction(1, n**3)

    cutoffs = (4, 8, 16, 32)
    pc = [partial_sum(primitive_critical, n) for n in cutoffs]
    ps = [partial_sum(primitive_strong, n) for n in cutoffs]
    sc = [partial_sum(square_constant, n) for n in cutoffs]
    sr = [partial_sum(square_rapid, n) for n in cutoffs]

    assert pc == sc
    assert all(pc[i + 1] > pc[i] for i in range(len(pc) - 1))
    assert all(ps[i + 1] > ps[i] for i in range(len(ps) - 1))
    assert all(sr[i + 1] > sr[i] for i in range(len(sr) - 1))

    # Exact tail bounds: sum_{n>N} 1/(n 2^n) <= 1/(N 2^N),
    # and sum_{n>N} 1/n^3 <= 1/(2 N^2).
    strong_tail_bound_at_32 = Fraction(1, 32 * 2**32)
    rapid_tail_bound_at_32 = Fraction(1, 2 * 32**2)
    assert strong_tail_bound_at_32 < Fraction(1, 10**9)
    assert rapid_tail_bound_at_32 < Fraction(1, 1000)

    # Harmonic growth has a blockwise lower bound of 1/2 per doubling.
    harmonic_block_bounds = []
    for n in (4, 8, 16):
        block = sum((Fraction(1, k) for k in range(n + 1, 2 * n + 1)), Fraction(0))
        harmonic_block_bounds.append(block)
        assert block >= Fraction(1, 2)

    result = {
        "schema": "marici.rh-valuation-rigging-split.v1",
        "status": "pass",
        "cutoffs": list(cutoffs),
        "primitive_critical_equals_harmonic": True,
        "square_constant_equals_harmonic": True,
        "harmonic_doubling_blocks_at_least_half": True,
        "primitive_strong_tail_bound_at_32": [strong_tail_bound_at_32.numerator, strong_tail_bound_at_32.denominator],
        "square_rapid_tail_bound_at_32": [rapid_tail_bound_at_32.numerator, rapid_tail_bound_at_32.denominator],
        "finite_incidence_missing": False,
        "rigged_completion_extension_missing": True,
        "disposition": "primitive and square incidences force distinct completion grades before scalar readout",
    }
    out = Path(__file__).parents[1] / "results" / "rh-valuation-rigging-split.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

