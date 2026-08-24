#!/usr/bin/env python3
"""Exact tangent test separating diagonal readout from framed response."""

from fractions import Fraction

psi = (Fraction(1), Fraction(1))
phase_tangent = (-psi[1], psi[0])

# R(psi)=||psi||^2, the real form of a phase-blind diagonal readout.
d_readout = 2 * sum(x * dx for x, dx in zip(psi, phase_tangent))

# A framed protocol port can inspect a coordinate relative to its frame.
d_framed_port = phase_tangent[0]

assert d_readout == 0
assert d_framed_port != 0

print("phase tangent lies in diagonal-readout kernel: yes")
print("same tangent detected by framed protocol port: yes")
print("checks: 2/2")
