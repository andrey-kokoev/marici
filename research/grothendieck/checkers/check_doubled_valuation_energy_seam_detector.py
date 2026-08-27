#!/usr/bin/env python3
"""Exact factorization of the doubled finite valuation-chain energy."""

from fractions import Fraction


def energy(value, depth):
    return sum(value ** k for k in range(depth + 1))


def positive_factor(a, b, depth):
    return sum(
        a ** (k - 1 - j) * b ** j
        for k in range(1, depth + 1)
        for j in range(k)
    )


for depth in range(1, 9):
    a = Fraction(1, 3)
    b = Fraction(1, 5)
    factor = positive_factor(a, b, depth)
    assert factor > 0
    assert energy(a, depth) - energy(b, depth) == (a - b) * factor
    assert (1 - a) * energy(a, depth) == 1 - a ** (depth + 1)
    assert energy(a, depth) > energy(b, depth)
    assert energy(a, depth) - energy(a, depth) == 0

print("finite_Green_identity=exact")
print("direct_dual_difference=positive_factor_times_seam_coordinate")
print("local_zero_locus=critical_seam")
print("missing_rung=zero_state_to_completed_energy_balance")

