#!/usr/bin/env python3
"""Exact finite gates for transport of a two-dimensional seam boundary pair."""

import json
from fractions import Fraction
from pathlib import Path


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def multiply(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


symplectic_transport = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
anomalous_transport = ((Fraction(2), Fraction(0)), (Fraction(0), Fraction(1)))
reflection = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)))

assert determinant(symplectic_transport) == 1
assert determinant(anomalous_transport) == 2
assert determinant(reflection) == -1

# In dimension two, the alternating boundary form scales exactly by det(S).
x = (Fraction(1), Fraction(3))
y = (Fraction(2), Fraction(5))


def act(matrix, vector):
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def omega(left, right):
    return left[0] * right[1] - left[1] * right[0]


for transport in (symplectic_transport, anomalous_transport, reflection):
    assert omega(act(transport, x), act(transport, y)) == determinant(transport) * omega(x, y)

# Multiplicativity makes determinant transport a one-dimensional coherence record.
composite = multiply(anomalous_transport, symplectic_transport)
assert determinant(composite) == determinant(anomalous_transport) * determinant(symplectic_transport)

result = {
    "symplectic_transport_determinant": str(determinant(symplectic_transport)),
    "anomalous_transport_determinant": str(determinant(anomalous_transport)),
    "reflection_determinant": str(determinant(reflection)),
    "boundary_pair_scales_by_transport_determinant": True,
    "determinant_coherence_is_multiplicative": True,
    "verdict": (
        "four boundary coordinates form a closed transported object only when cutoff maps "
        "preserve the boundary form; otherwise a determinant-line anomaly record is required"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-boundary-transport-anomaly.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
