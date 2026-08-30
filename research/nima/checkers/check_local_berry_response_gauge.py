#!/usr/bin/env python3
"""Exact gauge audit for the local Bogoliubov Berry response."""

from fractions import Fraction

a = Fraction(-8, 9)

for winding in range(-5, 6):
    transformed = a - winding
    # The local coefficient changes for every nonzero periodic gauge winding.
    assert (transformed == a) == (winding == 0)
    # Closed holonomy depends only on A modulo integers.
    assert transformed.denominator == a.denominator
    assert (transformed - a).denominator == 1

print("nonzero periodic gauges shift local Berry coefficient: yes")
print("closed holonomy class A mod Z is unchanged: yes")
print("checks: 11/11 windings")
