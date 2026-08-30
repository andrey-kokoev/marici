#!/usr/bin/env python3
"""Check the Gaussian heat boundary finite part of the zeta Gram kernel."""

from math import exp, pi, sqrt


def direct_sum(epsilon: float) -> float:
    total = 0.0
    n = 1
    while True:
        term = exp(-pi * epsilon * n * n)
        total += term
        if term < 1.0e-16:
            return total
        n += 1


def dual_remainder(epsilon: float) -> float:
    total = 0.0
    m = 1
    while True:
        term = exp(-pi * m * m / epsilon) / sqrt(epsilon)
        total += term
        if term < 1.0e-16:
            return total
        m += 1


for epsilon in (0.2, 0.1, 0.05):
    regulated = direct_sum(epsilon)
    finite_part = regulated - 1.0 / (2.0 * sqrt(epsilon))
    expected = -0.5 + dual_remainder(epsilon)
    assert regulated > 0.0
    assert abs(finite_part - expected) < 2.0e-14
    assert finite_part < 0.0

print("regulated_kernel_diagonal=positive")
print("gaussian_boundary_subtraction=jacobi_exact")
print("boundary_finite_part=zeta(0)=-1/2")
print("finite_part_map=not_positive")
print("required_object=relative_gram_pair")
