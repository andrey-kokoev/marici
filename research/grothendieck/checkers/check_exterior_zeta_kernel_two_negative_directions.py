#!/usr/bin/env python3
"""Exact inertia witness for the continued exterior zeta Hankel kernel."""

from fractions import Fraction


# Probe parameters are 0, -1, -2.  Entries are zeta(-(i+j)).
matrix = (
    (Fraction(-1, 2), Fraction(-1, 12), Fraction(0)),
    (Fraction(-1, 12), Fraction(0), Fraction(1, 120)),
    (Fraction(0), Fraction(1, 120), Fraction(0)),
)

d1 = matrix[0][0]
d2 = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
d3 = (
    matrix[0][0]
    * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    - matrix[0][1]
    * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    + matrix[0][2]
    * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
)

pivots = (d1, d2 / d1, d3 / d2)
assert (d1, d2, d3) == (
    Fraction(-1, 2),
    Fraction(-1, 144),
    Fraction(1, 28800),
)
assert tuple(pivot < 0 for pivot in pivots) == (True, False, True)

print("probe_packet=0,-1,-2")
print("leading_minor_signs=negative,negative,positive")
print("ldl_pivot_signs=negative,positive,negative")
print("negative_index_at_least=2")
print("scalar_boundary_wall=sufficient:false")
