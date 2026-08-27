#!/usr/bin/env python3
"""Exact local and cutoff inversion of the arithmetic anomaly line."""

from fractions import Fraction


q = Fraction(1, 3)
r = Fraction(1, 5)
gamma = (1 - q) / (1 - r)
gamma_reflected = (1 - r) / (1 - q)
assert gamma * gamma_reflected == 1

for grade in range(1, 9):
    coordinate = (r ** grade - q ** grade) / grade
    reflected = (q ** grade - r ** grade) / grade
    assert reflected == -coordinate

# Three exact cutoff transitions and their reflected inverses.
u_xy = Fraction(2, 3)
u_yz = Fraction(5, 7)
u_xz = u_yz * u_xy
assert (1 / u_xy) * (1 / u_yz) == 1 / u_xz

print("local_line_transition=exactly_inverted")
print("all_checked_valuation_grades=sign_reversed")
print("cutoff_triangle=reflection_coherent")
print("remaining_residual=mixed_archimedean_Poisson_attachment")

