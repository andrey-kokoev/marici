#!/usr/bin/env python3
"""Exact polar-odd factorization and reciprocal antisymmetry."""

from fractions import Fraction


c = Fraction(3)
samples = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 2))

for s in samples:
    if s in (0, 1):
        continue
    direct = c / (s - 1) + c / s
    factored = c * (2 * s - 1) / (s * (s - 1))
    assert direct == factored
    reflected = c / ((1 - s) - 1) + c / (1 - s)
    assert reflected == -direct

assert c * (2 * Fraction(1, 2) - 1) == 0
assert all(c * (2 * s - 1) != 0 for s in samples if s != Fraction(1, 2))

print("polar_odd_factor=2s_minus_1_times_meromorphic_unit")
print("reciprocal_action=odd")
print("RH_charge=Real_horizontal_component")
print("missing_object=bulk_odd_Green_attachment")

