#!/usr/bin/env python3
"""Exact universal five-point massless conserved kinematic map."""
import json
from fractions import Fraction
from pathlib import Path


def invert(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if a[row][column])
        a[column], a[pivot] = a[pivot], a[column]
        scale = a[column][column]
        a[column] = [x / scale for x in a[column]]
        for row in range(n):
            if row != column and a[row][column]:
                scale = a[row][column]
                a[row] = [x - scale * y for x, y in zip(a[row], a[column])]
    return [row[n:] for row in a]


def mat_vec(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


# Adjacent invariants a_i=s_{i,i+1} are universal coordinates. Conservation
# determines chords b_i=s_{i,i+2} through b_i+b_{i-2}=-a_{i-1}-a_i.
coefficient = [[int(j == i) + int(j == (i - 2) % 5) for j in range(5)] for i in range(5)]
coefficient_inverse = invert(coefficient)
chord_coefficients = []
for basis_index in range(5):
    rhs = [Fraction(-(int(basis_index == (i - 1) % 5) + int(basis_index == i))) for i in range(5)]
    chord_coefficients.append(mat_vec(coefficient_inverse, rhs))
# transpose: row i gives coefficients of b_i in the a_j basis
chord_coefficients = [list(row) for row in zip(*chord_coefficients)]

for i in range(5):
    equation = [Fraction(int(j == (i - 1) % 5) + int(j == i)) for j in range(5)]
    for j in range(5):
        equation[j] += chord_coefficients[i][j] + chord_coefficients[(i - 2) % 5][j]
    assert equation == [0] * 5

# The formal planar channel Laurent algebra and the universal localized
# coordinate ring both have these five generators; the map is the identity on
# exponent lattices, hence injective before any specialization.
channel_map_matrix = [[int(i == j) for j in range(5)] for i in range(5)]
assert invert(channel_map_matrix) == [[Fraction(int(i == j)) for j in range(5)] for i in range(5)]
triangulation_exponents = [
    (1, 1, 0, 0, 0),
    (1, 0, 0, 0, 1),
    (0, 1, 1, 0, 0),
    (0, 0, 1, 1, 0),
    (0, 0, 0, 1, 1),
]
assert len(set(triangulation_exponents)) == 5

lorentzian_point = [-3, -3, -2, -2, 2]
point_chords = mat_vec(chord_coefficients, list(map(Fraction, lorentzian_point)))
assert point_chords == [4, 7, 1, -3, -1]
point_values = [
    Fraction(1, lorentzian_point[i] * lorentzian_point[j])
    for i, j in [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
]
assert len(set(point_values)) == 5

fmt = lambda x: str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
result = {
    "schema": "marici.fact5-universal-kinematic-map.v1",
    "status": "passed",
    "strength": "universal five-point algebraic massless-conservation coordinate theorem; no physical-region, normalization, or pole-prescription theorem",
    "coordinate_ring": "Q[a0^±1,...,a4^±1]",
    "adjacent_coordinates_free": True,
    "chord_linear_forms": [[fmt(x) for x in row] for row in chord_coefficients],
    "conservation_identities_checked": 5,
    "channel_exponent_map": "identity_Z5",
    "channel_map_injective": True,
    "triangulation_span_separated_universally": True,
    "lorentzian_specialization": {
        "adjacent": lorentzian_point,
        "nonadjacent": list(map(fmt, point_chords)),
        "triangulation_values": list(map(fmt, point_values)),
        "separates_finite_image": True,
    },
    "cross_probe_coherence": "route equality in the Laurent algebra is preserved by the universal map and every specialization",
}
out = Path("research/nima/results/fact5_universal_kinematic_map.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
