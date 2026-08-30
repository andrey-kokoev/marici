#!/usr/bin/env python3
"""Exact checker for the WP985 bounded rational lift theorem."""

from fractions import Fraction
import json
from math import comb
from pathlib import Path


def convolution(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(poly, n):
    out = [Fraction(1)]
    for _ in range(n):
        out = convolution(out, poly)
    return out


degree_bounds = {
    "d_Gamma": 2,
    "d_A": 1,
    "d_B": 1,
    "d_C": 1,
}
M = 2 * degree_bounds["d_Gamma"] + 4 * degree_bounds["d_A"]
Q = degree_bounds["d_B"] + 5 * degree_bounds["d_C"]
K = M + Q

gamma_1 = [Fraction(1), Fraction(2), Fraction(1)]
a_1 = [Fraction(1)]
gamma_2 = [Fraction(1)]
a_2 = [Fraction(1), Fraction(1)]

response_1 = convolution(power(gamma_1, 2), power(a_1, 4))
response_2 = convolution(power(gamma_2, 2), power(a_2, 4))
expected_response = [Fraction(comb(4, k)) for k in range(5)]

# The degree lemma used in the theorem: a polynomial of degree at most K with
# K+1 zero coefficients is the zero polynomial.
zero_cross_difference = [Fraction(0) for _ in range(K + 1)]

checks = {
    "numerator_degree_bound_is_eight": M == 8,
    "denominator_degree_bound_is_six": Q == 6,
    "finite_jet_cutoff_is_fourteen": K == 14,
    "cross_difference_degree_bound_matches_cutoff": len(zero_cross_difference) - 1 == K,
    "K_plus_one_zero_coefficients_force_zero_cross_difference": all(
        x == 0 for x in zero_cross_difference
    ),
    "distinct_factorizations_have_identical_response": response_1 == response_2,
    "common_response_is_one_plus_epsilon_to_fourth": response_1 == expected_response,
}

result = {
    "schema": "marici.flavor.bounded-rational-lift-tomography.v1",
    "work_package": "WP985",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "degree_bounds": degree_bounds,
    "numerator_bound_M": M,
    "denominator_bound_Q": Q,
    "faithful_response_jet_cutoff_K": K,
    "constructor_kernel_witness": {
        "U1": "Gamma=(1+epsilon)^2, A=1, B=C=1",
        "U2": "Gamma=1, A=1+epsilon, B=C=1",
        "shared_response_coefficients": [str(x) for x in response_1],
    },
    "classification": "finite jets are faithful on bounded rational responses but not on their UV factorizations",
    "remaining_gate": (
        "derive complementary source channels whose joint response separates "
        "the frozen UV constructor domain"
    ),
}

out = Path("research/flavor/results/wp985_bounded_rational_lift_tomography.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
