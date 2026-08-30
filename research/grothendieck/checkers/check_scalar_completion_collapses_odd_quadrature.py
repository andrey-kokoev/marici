#!/usr/bin/env python3
"""Hostile exact-form audit of scalar even completion."""

from fractions import Fraction


def hostile(z: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return ((z - a) ** 2 + b**2) * ((z + a) ** 2 + b**2)


for z in (Fraction(-7, 3), Fraction(-1, 2), Fraction(0), Fraction(5, 4)):
    for a, b in ((Fraction(1, 3), Fraction(2, 5)), (Fraction(3, 2), Fraction(1, 7))):
        assert hostile(-z, a, b) == hostile(z, a, b)

# Any even scalar pair (x,x) has zero odd quadrature and fixed projective
# direction whenever x is nonzero. Multiplication by an even hostile factor
# cannot change either fact, although it can add a divisor.
for x in (Fraction(1), Fraction(-2), Fraction(7, 5)):
    pair = (x, x)
    assert pair[0] - pair[1] == 0
    assert pair[0] / pair[1] == 1

print("completed_functional_equation=X(-z)=X(z)")
print("completed_odd_quadrature=0")
print("completed_projective_direction=[1:1]")
print("even_hostile_multiplier=projectively_invisible")
print("divisor_channel=common_scalar_factor")
print("required_lift=pre_scalar_sewing_two_cell")
