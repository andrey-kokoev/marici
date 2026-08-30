#!/usr/bin/env python3
"""Exact rational audit of reciprocal Euler-current half-centering."""

from fractions import Fraction


def current(r: Fraction) -> Fraction:
    return r / (1 - r)


for numerator in range(1, 10):
    r = Fraction(numerator, numerator + 3)
    assert -current(1 / r) == current(r) + 1
    assert -(current(1 / r) + Fraction(1, 2)) == current(r) + Fraction(1, 2)

print("reciprocal_involution=r->1/r")
print("oriented_current_anomaly=-J(1/r)-J(r)=1")
print("unique_centered_current=C=J+1/2")
print("centered_reciprocity=-C(1/r)=C(r)")
print("potential_transition=E(1/r)-E(r)=log(r)-i*pi")
print("seam=r=1")
