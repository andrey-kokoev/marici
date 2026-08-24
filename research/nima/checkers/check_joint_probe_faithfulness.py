#!/usr/bin/env python3
"""Exact local joint-faithfulness test for diagonal and framed probes."""

from fractions import Fraction

psi = (Fraction(1), Fraction(1))
phase = (-psi[1], psi[0])

# Differentials at psi of R=x^2+y^2 and the framed port P=x.
d_r = (2 * psi[0], 2 * psi[1])
d_p = (Fraction(1), Fraction(0))


def evaluate(row, vector):
    return sum(a * b for a, b in zip(row, vector))


assert evaluate(d_r, phase) == 0
assert evaluate(d_p, phase) != 0

# The stacked probe Jacobian is invertible, hence locally jointly faithful.
det = d_r[0] * d_p[1] - d_r[1] * d_p[0]
assert det != 0

print("diagonal probe alone misses phase tangent: yes")
print("framed probe detects phase tangent: yes")
print("stacked probe family is locally faithful: yes")
print("checks: 3/3")
