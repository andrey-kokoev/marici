#!/usr/bin/env python3
"""Exact countermodel: scalar covariance and nullity do not equate energies."""


def swap(vector):
    return (vector[1], vector[0])


def read_plus(vector):
    return vector[1]


def read_minus(vector):
    return vector[0]


def norm_squared(vector):
    return sum(value * value for value in vector)


test_vectors = ((0, 0), (1, 2), (-3, 5))
assert all(read_minus(swap(vector)) == read_plus(vector)
           for vector in test_vectors)

state_plus = (1, 0)
state_minus = (0, 2)
assert read_plus(state_plus) == 0
assert read_minus(state_minus) == 0
assert norm_squared(state_plus) != norm_squared(state_minus)
assert state_minus != swap(state_plus)

print("scalar_functional_equation=exact")
print("both_scalar_readouts=zero")
print("state_energies=unequal")
print("missing_rungs=state_lift_and_valuation_projection_naturality")

