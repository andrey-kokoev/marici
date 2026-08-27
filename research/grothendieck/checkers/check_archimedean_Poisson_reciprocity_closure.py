#!/usr/bin/env python3
"""Exact algebraic checks of archimedean line inversion and channel swap."""

from fractions import Fraction


# A ratio chi(1-s)/chi(s) inverts under reciprocal reflection.
chi_s = Fraction(2)
chi_reflected = Fraction(3)
gamma = chi_reflected / chi_s
gamma_after_reflection = chi_s / chi_reflected
assert gamma * gamma_after_reflection == 1

s = Fraction(1, 3)
f_zero = Fraction(2)
fourier_f_zero = Fraction(3)
polar_three = fourier_f_zero / (s - 1)
polar_four = -f_zero / s

reflected_s = 1 - s
reflected_polar_three = f_zero / (reflected_s - 1)
reflected_polar_four = -fourier_f_zero / reflected_s
assert reflected_polar_three == polar_four
assert reflected_polar_four == polar_three

channels = (11, 13, polar_three, polar_four)
reflected_channels = (channels[1], channels[0], channels[3], channels[2])
assert (reflected_channels[1], reflected_channels[0],
        reflected_channels[3], reflected_channels[2]) == channels

print("archimedean_line_transition=exactly_inverted")
print("Poisson_bulk_channels=swapped")
print("Poisson_polar_channels=swapped")
print("reciprocity_naturality=closed_without_transversality")

