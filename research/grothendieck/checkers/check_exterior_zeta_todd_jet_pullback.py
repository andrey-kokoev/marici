#!/usr/bin/env python3
"""Exact Todd-germ pullback of the exterior zeta moment sequence."""

from fractions import Fraction
from math import factorial


def bernoulli_numbers(count: int) -> list[Fraction]:
    values: list[Fraction] = []
    for m in range(count):
        value = Fraction(1)
        for k in range(m):
            value -= Fraction(factorial(m), factorial(k) * factorial(m - k)) * values[k] / Fraction(m - k + 1)
        values.append(value)
    return values


# The recurrence above uses the convention B_1=+1/2, appropriate to
# t/(1-exp(-t)).  Convert the logarithmic derivative coefficients directly.
bernoulli_plus = bernoulli_numbers(12)


def todd_log_derivative_jet(n: int) -> Fraction:
    # 1/t - 1/(1-exp(-t)) has coefficient
    # -B^+_{n+1}/(n+1)!; its nth derivative is -B^+_{n+1}/(n+1).
    return -bernoulli_plus[n + 1] / Fraction(n + 1)


expected = (
    Fraction(-1, 2),
    Fraction(-1, 12),
    Fraction(0),
    Fraction(1, 120),
    Fraction(0),
    Fraction(-1, 252),
)
actual = tuple(todd_log_derivative_jet(n) for n in range(len(expected)))
assert actual == expected

matrix = tuple(tuple(actual[i + j] for j in range(3)) for i in range(3))
assert matrix == (
    (Fraction(-1, 2), Fraction(-1, 12), Fraction(0)),
    (Fraction(-1, 12), Fraction(0), Fraction(1, 120)),
    (Fraction(0), Fraction(1, 120), Fraction(0)),
)

print("boundary_germ=t/(exp(t)-1)")
print("logarithmic_tangent=1/t-1/(1-exp(-t))")
print("jet_identity=L^(n)(0)=zeta(-n)")
print("three_probe_hankel=jet_prolongation")
print("next_pullback=multiplicative_normalization_germ")
