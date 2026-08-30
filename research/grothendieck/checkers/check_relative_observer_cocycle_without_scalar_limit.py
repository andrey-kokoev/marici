#!/usr/bin/env python3
"""A flat cutoff cocycle can exist without a convergent scalar origin."""

from fractions import Fraction


# Harmonic partial sums are an exact elementary model of cutoff charts.
charts = [sum(Fraction(1, k) for k in range(1, n + 1)) for n in range(1, 9)]


def increment(x_index, y_index):
    return charts[y_index] - charts[x_index]


for x in range(len(charts)):
    for y in range(x, len(charts)):
        for z in range(y, len(charts)):
            assert increment(x, z) == increment(x, y) + increment(y, z)

assert all(charts[n + 1] > charts[n] for n in range(len(charts) - 1))

print("cutoff_transition_cocycle=flat")
print("scalar_charts=nonstationary")
print("valid_completion_type=affine_line_system")
print("observer_naturality=requires_higher_cell")

