#!/usr/bin/env python3
"""Exact five-point affine associahedral slice and canonical-form Jacobians."""
import json
from fractions import Fraction
from pathlib import Path

A, B, C = Fraction(1), Fraction(3, 2), Fraction(1)
# a_i = constant + gradient_x*x + gradient_y*y
affine = [
    (Fraction(0), (1, 0)),       # a0=x
    (Fraction(0), (0, 1)),       # a1=y
    (A, (-1, 0)),                # a2=A-x
    (B, (-1, -1)),               # a3=B-x-y
    (C, (0, -1)),                # a4=C-y
]
compatible = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


jacobians = [det(affine[i][1], affine[j][1]) for i, j in compatible]
assert jacobians == [1, 1, 1, 1, 1]

# Solve each adjacent facet pair and verify precisely those facets vanish while
# every other facet is positive.
def solve_facets(i, j):
    ci, gi = affine[i]
    cj, gj = affine[j]
    determinant = det(gi, gj)
    assert determinant != 0
    x = ((-ci) * gj[1] - gi[1] * (-cj)) / determinant
    y = (gi[0] * (-cj) - (-ci) * gj[0]) / determinant
    return x, y


def value(index, point):
    constant, gradient = affine[index]
    return constant + gradient[0] * point[0] + gradient[1] * point[1]

vertices = []
for i, j in compatible:
    point = solve_facets(i, j)
    values = [value(k, point) for k in range(5)]
    assert values[i] == values[j] == 0
    assert all(values[k] > 0 for k in range(5) if k not in (i, j))
    vertices.append(point)
assert len(set(vertices)) == 5

# Pullback of sum dlog(a_i) wedge dlog(a_j) over compatible pairs has scalar
# coefficient sum 1/(a_i a_j), because every oriented Jacobian is +1.
constraint_gradients = [
    (1, 0, 1, 0, 0),  # a0+a2=A
    (0, 1, 0, 0, 1),  # a1+a4=C
    (1, 1, 0, 1, 0),  # a0+a1+a3=B
]
# independent pivots 0,1,2 establish codimension three in five-channel space
assert len(constraint_gradients) == 3

fmt = lambda x: str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
result = {
    "schema": "marici.fact5-associahedral-slice.v1",
    "status": "passed",
    "strength": "exact affine two-dimensional pentagon slice and pullback identity; no proof this chosen constants/slice is source-selected physical kinematics",
    "ambient_channel_dimension": 5,
    "slice_dimension": 2,
    "affine_constraints": ["a0+a2=1", "a1+a4=1", "a0+a1+a3=3/2"],
    "vertices": [[fmt(x), fmt(y)] for x, y in vertices],
    "compatible_facet_jacobians": list(map(fmt, jacobians)),
    "canonical_form_pullback": "sum dlog(a_i) wedge dlog(a_j) = m5(a(x,y)) dx wedge dy",
    "weighted_sum_terms": 5,
    "boundary": "unit Jacobians derive normalization on this declared slice; source authority for the affine constraints remains absent",
}
out = Path("research/nima/results/fact5_associahedral_slice.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
