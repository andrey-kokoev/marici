#!/usr/bin/env python3
"""Exact gauge typing of a two-history relative-phase port."""

from fractions import Fraction

relative_character = (Fraction(-1), Fraction(1))
common_gauge = (Fraction(1), Fraction(1))
relative_gauge = (Fraction(0), Fraction(1))


def pairing(row, vector):
    return sum(a * b for a, b in zip(row, vector))


assert pairing(relative_character, common_gauge) == 0
assert pairing(relative_character, relative_gauge) != 0

# The character has rank one on a two-dimensional phase space, so its kernel
# is exactly the one-dimensional common-phase direction.
assert relative_character != (0, 0)

print("relative phase is invariant under common rephasing: yes")
print("relative phase changes under independent rephasing: yes")
print("kernel is the diagonal gauge line: yes")
print("checks: 3/3")
