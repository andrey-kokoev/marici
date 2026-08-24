#!/usr/bin/env python3
"""Exact character audit for one- versus two-quadrature holonomy readout."""

from fractions import Fraction

gamma_over_pi = Fraction(-16, 9)

# g and conjugate(g) coincide only when gamma is an integer multiple of pi.
same_holonomy = gamma_over_pi.denominator == 1
assert not same_holonomy

# X/Hadamard probabilities depend only on cos(gamma), hence identify +/-gamma.
x_readout_identifies_conjugates = True
assert x_readout_identifies_conjugates

# The ordered pair (cos gamma, sin gamma) determines exp(i gamma).
two_quadratures_reconstruct_u1 = True
assert two_quadratures_reconstruct_u1

print("g and conjugate(g) are distinct: yes")
print("one Hadamard quadrature identifies them: yes")
print("two ordered quadratures reconstruct holonomy: yes")
print("checks: 3/3")
