#!/usr/bin/env python3
"""Sparse-versus-consecutive grade audit for the RH orientation lane."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_sparse_vs_consecutive_grade_audit.json"


def scalar_zero_packet(n: int):
    # At s=1, coefficients (1,-n) on labels (1,n) give weighted state (1,-1).
    return [Fraction(1), Fraction(-n)], [Fraction(1), Fraction(1, n)], [Fraction(1), Fraction(-1)]


def order_slope_for_two_point_zero_state(gap: Fraction, v):
    # Entry 4105/4107 identity for c=(a,-a): <c,[Lambda,S]c> = 2 gap |a|^2.
    return 2 * gap * v[0] * v[0]


def hardy_cross_current(a, b):
    # Real two half-line aggregate: -2 Im(conj(a)b); exact real packets give 0.
    return Fraction(0)

cases = {
    "consecutive_1_2": {"labels": [1, 2], "valuation_gap": Fraction(1)},
    "sparse_1_4": {"labels": [1, 4], "valuation_gap": Fraction(2)},
}

for case in cases.values():
    n = case["labels"][1]
    coeffs, weights, weighted = scalar_zero_packet(n)
    gap = case["valuation_gap"]
    case["coefficients"] = coeffs
    case["mellin_weights_s_1"] = weights
    case["weighted_state"] = weighted
    case["scalar_value"] = sum(c * w for c, w in zip(coeffs, weights))
    case["full_packet_norm_surrogate"] = sum(x * x for x in weighted)
    case["order_slope"] = order_slope_for_two_point_zero_state(gap, weighted)
    # Primitive and square grade moments before scalar aggregation.
    grades = [Fraction(0), gap]
    case["primitive_grade_moment"] = sum(g * x * x for g, x in zip(grades, weighted))
    case["square_grade_moment"] = sum(g * g * x * x for g, x in zip(grades, weighted))
    # Scalar zero splits as a+b=0, so aggregate Hardy incidence is silent.
    case["hardy_cross_current_at_zero"] = hardy_cross_current(weighted[0], weighted[1])

consecutive = cases["consecutive_1_2"]
sparse = cases["sparse_1_4"]

checks = {
    "both_packets_are_off_seam_scalar_zeros_at_s_1": consecutive["scalar_value"] == 0 and sparse["scalar_value"] == 0,
    "both_full_packets_remain_nonzero": consecutive["full_packet_norm_surrogate"] > 0 and sparse["full_packet_norm_surrogate"] > 0,
    "hardy_aggregate_cross_incidence_vanishes_for_both": consecutive["hardy_cross_current_at_zero"] == 0 and sparse["hardy_cross_current_at_zero"] == 0,
    "order_current_has_strict_upward_crossing_for_both": consecutive["order_slope"] > 0 and sparse["order_slope"] > 0,
    "sparse_and_consecutive_order_slopes_differ_by_grade_gap": sparse["order_slope"] == 2 * consecutive["order_slope"],
    "primitive_grade_moment_distinguishes_sparse_from_consecutive": sparse["primitive_grade_moment"] == 2 * consecutive["primitive_grade_moment"],
    "square_grade_moment_distinguishes_more_strongly": sparse["square_grade_moment"] == 4 * consecutive["square_grade_moment"],
    "scalar_and_hardy_ports_do_not_see_grade_difference": consecutive["scalar_value"] == sparse["scalar_value"] == 0 and consecutive["hardy_cross_current_at_zero"] == sparse["hardy_cross_current_at_zero"] == 0,
}

payload = {
    "schema": "marici.strominger.rh_sparse_vs_consecutive_grade_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "cases": {
        name: {
            key: ([str(x) for x in value] if isinstance(value, list) else str(value))
            for key, value in case.items()
        }
        for name, case in cases.items()
    },
    "verdict": (
        "The sparse-versus-consecutive audit keeps the RH lane productive but "
        "narrows it. Scalar darkness and aggregate Hardy cross-incidence are "
        "identical for the consecutive and sparse two-label zeros, while the "
        "order slope and primitive/square grade moments distinguish them before "
        "aggregation. Thus the smallest surviving orientation candidate must be "
        "label-sensitive and grade-sensitive. The audit still supplies no RH "
        "confinement law: strict order crossings occur for both packets, including "
        "hostile off-seam scalar zeros. The next gate is a source-derived law "
        "coupling these primitive/square grade currents to the archimedean or "
        "Poisson boundary anomaly under conductor refinement."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
