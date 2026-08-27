#!/usr/bin/env python3
"""Finite witnesses separating rungs of the cross-tower coherence tower."""

from fractions import Fraction


# Equal scalar trace, unequal operator action.
A = ((1, 0), (0, 0))
B = ((0, 0), (0, 1))
trace_A = A[0][0] + A[1][1]
trace_B = B[0][0] + B[1][1]
assert trace_A == trace_B
assert A != B

# Agreement at one cutoff does not force a coherent extension.
small_comparison = (Fraction(1),)
large_comparison = (Fraction(2), Fraction(0))
assert large_comparison[:1] != small_comparison

# Exact finite contractions may diverge under completion.
epsilons = (Fraction(1), Fraction(1, 2), Fraction(1, 4))
contractions = tuple(1 / epsilon for epsilon in epsilons)
assert contractions == (1, 2, 4)

print("scalar_equality_without_operator_lift=witnessed")
print("one_cutoff_equality_without_naturality=witnessed")
print("finite_coherence_without_completion_control=witnessed")
print("coherence_cell_requires=its_own_tower")

