#!/usr/bin/env python3
"""Exact two-label obstruction to a Ward cell from uncoupled tail dynamics."""

from fractions import Fraction


endpoint = (Fraction(1), Fraction(-1))
scalar_output = sum(endpoint)
ward_packet = endpoint
ward_norm_squared = sum(value * value for value in ward_packet)

assert scalar_output == 0
assert ward_norm_squared == 2

# For G_j(q)=endpoint_j exp(-q), defining
# f_j=-(d/dq+s)G_j makes every labelwise tail equation exact for every s.
print("labelwise_tail_equations=exact_by_source_forcing")
print("aggregate_endpoint=zero")
print("ward_packet=nonzero")
print("required_new_cell=arithmetic_cross_label_coherence")

