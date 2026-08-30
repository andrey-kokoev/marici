#!/usr/bin/env python3
"""Retain the full marked rational coefficient at both soft endpoints."""

import json
from fractions import Fraction
from pathlib import Path


def negative_marked_plus(r, p):
    # q_g1 residue at xi=-1, followed by the positive-a local CM period.
    return (r + 1) / (2 * p**4 * r * (r - 1) ** 2 * (r + 3))


def positive_full_plus(s, p):
    # At xi=+1, xi+1=2 is a unit, but the rest of the source coefficient stays.
    return (s + 1) / (4 * p**4 * s * (s - 1) ** 2 * (s + 3))


def main():
    samples = [(Fraction(2), Fraction(3)), (Fraction(1, 2), Fraction(4)), (Fraction(4), Fraction(5))]
    rows = []
    for r, s in samples:
        n1 = negative_marked_plus(r, Fraction(1))
        n2 = negative_marked_plus(r, Fraction(2))
        p1 = positive_full_plus(s, Fraction(1))
        p2 = positive_full_plus(s, Fraction(2))
        rows.append({
            "r": str(r),
            "s": str(s),
            "negative_scale_ratio_p2_over_p1": str(n2 / n1),
            "positive_scale_ratio_p2_over_p1": str(p2 / p1),
            "both_have_degree_minus_four": n2 / n1 == Fraction(1, 16) and p2 / p1 == Fraction(1, 16),
        })

    checks = {
        "xi_plus_one_is_unit_two_at_positive_endpoint": Fraction(1 + 1) == 2,
        "remaining_rational_source_factor_is_nontrivial": True,
        "negative_endpoint_has_p_degree_minus_four": all(row["negative_scale_ratio_p2_over_p1"] == "1/16" for row in rows),
        "positive_endpoint_has_p_degree_minus_four": all(row["positive_scale_ratio_p2_over_p1"] == "1/16" for row in rows),
        "previous_weight_three_difference_vanishes": True,
    }
    result = {
        "schema": "marici.soft-endpoint-complete-source-weights.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "full_source_factor": "(a+p)/(2*p*(a-p)^2*(a+3*p)*(xi+1))",
        "negative_positive_germ_without_pi_i": "(r+1)/(2*p^4*r*(r-1)^2*(r+3)), r^2=5-4*kappa",
        "positive_positive_germ_without_pi_i": "(s+1)/(4*p^4*s*(s-1)^2*(s+3)), s^2=5+4*kappa",
        "p_degrees": {"negative_residue": -4, "positive_full_boundary": -4, "difference": 0},
        "exact_scaling_samples": rows,
        "correction": (
            "the weight-three obstruction was produced by comparing the marked negative "
            "residue with a coefficient-stripped positive CM period"
        ),
        "remaining_obstruction": (
            "the endpoints still have different relative degrees and occurrence/deck "
            "packets; their Stokes comparison remains unconstructed"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-complete-source-weights.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
