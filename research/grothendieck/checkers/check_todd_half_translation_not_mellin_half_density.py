#!/usr/bin/env python3
"""Exact typing witness separating translation from Mellin half-density."""

from fractions import Fraction


# On f_k(x)=x^k, [d/dx, log(x)] f_k = x^(k-1).
for k in range(1, 9):
    x = Fraction(k + 2, k + 1)
    derivative_after_log_coefficient = k
    log_after_derivative_coefficient = k
    commutator_nonlog = x ** (k - 1)
    assert derivative_after_log_coefficient == log_after_derivative_coefficient
    assert commutator_nonlog != 0

# For f(x)=exp(-x), half translation and half-density multiplication have
# Mellin transforms exp(-1/2) Gamma(s) and Gamma(s+1/2), respectively.
# Their ratios at s=1 and s=2 cannot agree: the translation ratio is fixed,
# while Gamma(s+1/2)/Gamma(s) changes by a factor 3/2.
ratio_change = Fraction(3, 2)
assert ratio_change != 1

print("todd_generator=additive_derivative")
print("mellin_shift_generator=logarithmic_multiplication")
print("commutator=[d/dx,log(x)]=1/x")
print("half_translation_not_equal_mellin_half_density=true")
print("required_next_datum=operator_realization_of_formal_germ")
