#!/usr/bin/env python3
"""Exact boundary-pair tests for the proposed value/flux seam split."""

import json
from fractions import Fraction
from pathlib import Path


omega = ((0, 1), (-1, 0))
reflection = ((1, 0), (0, -1))


def multiply(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def transpose(matrix):
    return tuple(zip(*matrix))


assert multiply(multiply(transpose(reflection), omega), reflection) == tuple(
    tuple(-entry for entry in row) for row in omega
)


def boundary_pair(x, y):
    return x[0] * y[1] - x[1] * y[0]


value_basis = (Fraction(1), Fraction(0))
flux_basis = (Fraction(0), Fraction(1))
assert boundary_pair(value_basis, flux_basis) == 1

# Any scalar graph J=L M is isotropic: two graph states have zero boundary pair.
graph_tests = {}
for slope in (Fraction(-2), Fraction(0), Fraction(3, 2)):
    x = (Fraction(2), 2 * slope)
    y = (Fraction(-3), -3 * slope)
    graph_tests[str(slope)] = str(boundary_pair(x, y))
    assert boundary_pair(x, y) == 0

# A nonzero determinant is the exact two-state independence witness.
independent_x = (Fraction(1), Fraction(2))
independent_y = (Fraction(3), Fraction(5))
independent_pair = boundary_pair(independent_x, independent_y)
assert independent_pair == -1

result = {
    "boundary_form": [[0, 1], [-1, 0]],
    "reflection_reverses_boundary_orientation": True,
    "value_flux_pairing": 1,
    "scalar_graph_restrictions_are_isotropic": graph_tests,
    "independent_trace_witness_pairing": str(independent_pair),
    "verdict": (
        "the fourth observer is genuine only if theta/Tate supplies a nondegenerate "
        "value-flux boundary pair; a graph relation J=L M is a one-port presentation"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-seam-symplectic-pair.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
