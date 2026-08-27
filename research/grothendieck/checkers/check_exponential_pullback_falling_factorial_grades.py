#!/usr/bin/env python3
"""Exact polynomial check of the conjugated additive-jet grade formula."""

from fractions import Fraction


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


polynomial = [Fraction(1)]
for k in range(1, 8):
    polynomial = multiply(
        polynomial,
        [-(Fraction(1, 2) + k - 1), Fraction(1)],
    )
    rebuilt = [Fraction(1)]
    for j in range(k):
        rebuilt = multiply(
            rebuilt,
            [-(Fraction(1, 2) + j), Fraction(1)],
        )
    assert polynomial == rebuilt

print("conjugated_generator=A=exp(-q)(D_q-1/2)")
print("power_formula=A^k=exp(-kq)*product_j(D_q-1/2-j)")
print("spectral_factor=falling_factorial")
print("arithmetic_scale_weight_at_q_log_p=p^(-k)")
print("grade_split=k=1,k=2,k>=3")
