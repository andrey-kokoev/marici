#!/usr/bin/env python3
"""Exact homogeneity obstruction between scalar cumulants and Ward forms."""

from fractions import Fraction


ward = Fraction(1)
boundary_scalar = Fraction(1)
scale = Fraction(2)

ward_scaled = scale * scale * ward
boundary_scaled = boundary_scalar

assert ward == boundary_scalar
assert ward_scaled != boundary_scaled

print("unscaled_balance=possible")
print("scaled_balance=fails")
print("cause=quadratic_vs_scalar_degree_mismatch")
print("required_lift=operator_valued_boundary_form")

