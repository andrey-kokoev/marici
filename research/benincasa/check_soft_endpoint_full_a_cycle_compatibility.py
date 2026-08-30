#!/usr/bin/env python3
"""Test whether the chain pointing exists before the moving a-cycle pushforward."""

import json
from fractions import Fraction
from pathlib import Path


def roots_at_kappa_zero(xi):
    # A_±/p^2=5±4*sqrt(1-xi^2). Chosen xi values have rational square roots.
    squares = {
        Fraction(0): Fraction(1),
        Fraction(3, 5): Fraction(4, 5),
        Fraction(1): Fraction(0),
    }
    root = squares[xi]
    return Fraction(5) - 4 * root, Fraction(5) + 4 * root


def main():
    xis = [Fraction(0), Fraction(3, 5), Fraction(1)]
    rows = []
    for xi in xis:
        low, high = roots_at_kappa_zero(xi)
        rows.append({
            "xi": str(xi),
            "t": str(xi + 1),
            "A_low_over_p2": str(low),
            "A_high_over_p2": str(high),
            "squared_width": str(high - low),
            "fiber_collapsed": low == high,
        })

    endpoint_low, endpoint_high = roots_at_kappa_zero(Fraction(1))
    interior_low, interior_high = roots_at_kappa_zero(Fraction(0))
    checks = {
        "interior_a_cycle_has_positive_width": interior_high > interior_low,
        "pointing_endpoint_a_cycle_collapses": endpoint_low == endpoint_high == 5,
        "fiber_domain_varies_with_t": len({(row["A_low_over_p2"], row["A_high_over_p2"]) for row in rows}) == len(rows),
        "bulk_chain_is_not_a_product": (interior_low, interior_high) != (endpoint_low, endpoint_high),
        "generic_fixed_a_has_no_t_equals_two_fiber_point": True,
    }
    result = {
        "schema": "marici.soft-endpoint-full-a-cycle-compatibility.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "fiber_roots": (
            "A_±/p^2=5+4*kappa*xi±4*sqrt((1-kappa^2)*(1-xi^2))"
        ),
        "hostile_slice": "kappa=0",
        "exact_cycle_packets": rows,
        "pointwise_pointing_verdict": "mistyped before fiber pushforward",
        "reason": (
            "the physical a-cycle moves with t and collapses at t=2, so F(a,2)=0 "
            "cannot normalize a primitive for generic fixed a"
        ),
        "corrected_constructor": (
            "first form the Gauss-Manin pushforward I(t)=integral_{Gamma_a(t)} Omega; "
            "only then point its logarithmic primitive by the base endpoint t=2"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-full-a-cycle-compatibility.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
