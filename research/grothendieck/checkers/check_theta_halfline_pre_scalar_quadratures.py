#!/usr/bin/env python3
"""Exact algebraic audit of the theta half-line pre-scalar lift."""

from fractions import Fraction


packets = (
    (Fraction(3, 5), Fraction(7, 11)),
    (Fraction(-2, 3), Fraction(5, 7)),
    (Fraction(0), Fraction(4, 9)),
)

for h_plus, h_minus in packets:
    even = h_plus + h_minus
    odd = h_plus - h_minus
    assert (even + odd) / 2 == h_plus
    assert (even - odd) / 2 == h_minus

# At a scalar zero, h_minus=-h_plus and the odd channel is 2*h_plus.
for h_plus in (Fraction(1), Fraction(-3, 4), Fraction(8, 5)):
    h_minus = -h_plus
    even = h_plus + h_minus
    odd = h_plus - h_minus
    assert even == 0
    assert odd == 2 * h_plus != 0

print("halfline_amplitudes=H_plus(z),H_plus(-z)")
print("even_channel=T=H_plus+H_minus=X")
print("odd_channel=A=H_plus-H_minus")
print("linear_reconstruction=faithful")
print("scalar_zero_implies=A=2*H_plus")
print("full_null_requires=H_plus(z)=H_plus(-z)=0")
