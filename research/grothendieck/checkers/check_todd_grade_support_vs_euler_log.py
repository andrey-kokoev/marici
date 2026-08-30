#!/usr/bin/env python3
"""Exact coefficient support audit: Todd normalization versus Euler log."""

from fractions import Fraction
from math import factorial


degree = 12
denominator = [Fraction(1, factorial(n + 1)) for n in range(degree + 1)]
tau = [Fraction(0) for _ in range(degree + 1)]
tau[0] = Fraction(1)
for n in range(1, degree + 1):
    tau[n] = -sum(tau[k] * denominator[n - k] for k in range(n))

assert tau[1] == Fraction(-1, 2)
assert all(tau[k] == 0 for k in range(3, degree + 1, 2))
assert all(tau[k] != 0 for k in range(2, degree + 1, 2))

euler_log = [Fraction(0)] + [Fraction(1, k) for k in range(1, degree + 1)]
assert all(euler_log[k] != 0 for k in range(1, degree + 1))

print("todd_active_grades=k=1_and_even")
print("centered_todd_active_grades=even_only")
print("euler_log_active_grades=all_positive_k")
print("operator_power_tower=ambient_carrier_not_coefficient_selector")
print("required_comparison=todd_boundary_cocycle_to_euler_log_current")
