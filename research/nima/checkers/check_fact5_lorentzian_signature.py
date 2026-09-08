#!/usr/bin/env python3
"""Exact inertia test for the five-point quadratic separating probe."""
import json
from pathlib import Path
from sympy import Matrix, Poly, Rational, oo, symbols

adjacent = [2, 3, 5, 7, 11]
chords = [2, 3, -10, -15, -8]
s = [[Rational(0) for _ in range(5)] for _ in range(5)]
for i, value in enumerate(adjacent):
    j = (i + 1) % 5
    s[i][j] = s[j][i] = Rational(value)
for i, value in enumerate(chords):
    j = (i + 2) % 5
    s[i][j] = s[j][i] = Rational(value)
assert all(sum(row) == 0 for row in s)
assert Matrix(s).rank() == 4

# The classes of the first four standard basis vectors form a quotient basis
# modulo the all-ones radical. B=s/2 is the descended quadratic polarization.
quotient_gram = Matrix([[s[i][j] / 2 for j in range(4)] for i in range(4)])
assert quotient_gram.det() != 0
x = symbols("x")
characteristic = Poly(quotient_gram.charpoly(x).as_expr(), x, domain="QQ")
negative = int(characteristic.count_roots(-oo, 0))
positive = int(characteristic.count_roots(0, oo))
assert negative + positive == 4
lorentzian = sorted([negative, positive]) == [1, 3]

# Bounded exact search for a separating Lorentzian replacement. This search is
# a finite existence witness only; its lexicographic stopping point has no
# physical significance.
import itertools
coefficient = Matrix([[int(j == i) + int(j == (i - 2) % 5) for j in range(5)] for i in range(5)])
triangulation_pairs = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
search_values = [-3, -2, -1, 1, 2, 3]
searched = 0
replacement = None
for candidate in itertools.product(search_values, repeat=5):
    searched += 1
    products = [candidate[i] * candidate[j] for i, j in triangulation_pairs]
    if len(set(products)) != 5:
        continue
    residue_values = [
        Rational(1, candidate[(i - 1) % 5]) + Rational(1, candidate[(i + 1) % 5])
        for i in range(5)
    ]
    amplitude_value = sum(Rational(1, product) for product in products)
    if any(value == 0 for value in residue_values) or amplitude_value == 0:
        continue
    candidate_chords = list(coefficient.inv() * Matrix([
        -(candidate[(i - 1) % 5] + candidate[i]) for i in range(5)
    ]))
    candidate_s = [[Rational(0) for _ in range(5)] for _ in range(5)]
    for i, value in enumerate(candidate):
        j = (i + 1) % 5
        candidate_s[i][j] = candidate_s[j][i] = Rational(value)
    for i, value in enumerate(candidate_chords):
        j = (i + 2) % 5
        candidate_s[i][j] = candidate_s[j][i] = value
    candidate_gram = Matrix([[candidate_s[i][j] / 2 for j in range(4)] for i in range(4)])
    if candidate_gram.det() == 0:
        continue
    candidate_poly = Poly(candidate_gram.charpoly(x).as_expr(), x, domain="QQ")
    candidate_negative = int(candidate_poly.count_roots(-oo, 0))
    candidate_positive = int(candidate_poly.count_roots(0, oo))
    if sorted([candidate_negative, candidate_positive]) == [1, 3]:
        replacement_gram = candidate_gram
        replacement_s = candidate_s
        replacement = {
            "adjacent": list(candidate),
            "nonadjacent": list(map(str, candidate_chords)),
            "inertia": {"negative": candidate_negative, "positive": candidate_positive, "zero": 0},
            "triangulation_products": products,
            "amplitude_value": str(amplitude_value),
            "residue_values": list(map(str, residue_values)),
            "all_amplitude_and_residue_values_nonzero": True,
        }
        break
assert replacement is not None

# Exact congruence factorization into real Lorentzian coordinates. Rational
# Gram-Schmidt produces an orthogonal quotient basis; square roots realize its
# diagonal norms in a standard metric.
orthogonal = []
for entries in itertools.product([-1, 0, 1], repeat=4):
    if entries == (0, 0, 0, 0):
        continue
    vector = Matrix(entries)
    for prior in orthogonal:
        vector -= ((vector.T * replacement_gram * prior)[0] /
                   (prior.T * replacement_gram * prior)[0]) * prior
    norm = (vector.T * replacement_gram * vector)[0]
    if vector != Matrix.zeros(4, 1) and norm != 0:
        orthogonal.append(vector.applyfunc(Rational))
    if len(orthogonal) == 4:
        break
assert len(orthogonal) == 4
basis_change = Matrix.hstack(*orthogonal)
diagonal_form = basis_change.T * replacement_gram * basis_change
assert diagonal_form.is_diagonal()
diagonal_entries = [diagonal_form[i, i] for i in range(4)]
positive_axes = [i for i, value in enumerate(diagonal_entries) if value > 0]
assert len(positive_axes) == 1
energy_axis = positive_axes[0]

quotient_vectors = [Matrix.eye(4).col(i) for i in range(4)]
quotient_vectors.append(-sum(quotient_vectors, Matrix.zeros(4, 1)))
coordinates = []
for vector in quotient_vectors:
    coefficients = basis_change.inv() * vector
    coordinates.append([
        coefficients[i] * abs(diagonal_entries[i]) ** Rational(1, 2)
        for i in range(4)
    ])
signature = [1 if value > 0 else -1 for value in diagonal_entries]
for i in range(5):
    for j in range(5):
        recovered_inner = sum(
            signature[k] * coordinates[i][k] * coordinates[j][k]
            for k in range(4)
        )
        assert (recovered_inner - replacement_s[i][j] / 2).simplify() == 0
assert all(sum(coordinates[i][k] for i in range(5)).simplify() == 0 for k in range(4))
energy_signs = [1 if coordinate[energy_axis] > 0 else -1 for coordinate in coordinates]
assert sorted(energy_signs).count(-1) == 2 or sorted(energy_signs).count(1) == 2

result = {
    "schema": "marici.fact5-lorentzian-signature.v1",
    "status": "passed",
    "strength": "exact inertia of one finite algebraic Gram form; no energy-root, normalization, or physical-region claim",
    "quotient_gram": [[str(value) for value in row] for row in quotient_gram.tolist()],
    "determinant": str(quotient_gram.det()),
    "characteristic_polynomial": str(characteristic.as_expr()),
    "inertia": {"negative": negative, "positive": positive, "zero": 0},
    "lorentzian_up_to_sign": lorentzian,
    "explicit_realization": {
        "metric_diagonal": signature,
        "orthogonal_norms": list(map(str, diagonal_entries)),
        "momenta": [[str(value) for value in vector] for vector in coordinates],
        "energy_axis": energy_axis,
        "energy_signs": energy_signs,
        "incoming_outgoing_counts_up_to_reversal": sorted([energy_signs.count(-1), energy_signs.count(1)]),
        "gram_reconstruction_checked": True,
        "conservation_checked": True,
    },
    "bounded_search": {
        "candidate_values": search_values,
        "candidates_examined": searched,
        "first_separating_lorentzian_candidate": replacement,
        "scope": "finite rational search witness; not a preferred physical region or energy-root choice",
    },
}
out = Path("research/nima/results/fact5_lorentzian_signature.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
