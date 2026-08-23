"""Exact occupancy test for the physical source in C3 norm homology."""

import json
from pathlib import Path


P = 3


def rank_mod(a):
    a = [[x % P for x in row] for row in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, P)
        a[row] = [(inv * x) % P for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c * y) % P for x, y in zip(a[i], a[row])]
        row += 1
    return row


def kron(a, b):
    return [[(x * y) % P for x in ar for y in br] for ar in a for br in b]


N = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
N2 = [[0] * 6 for _ in range(6)]
for c in range(2):
    for i in range(3):
        for j in range(3):
            N2[2 * i + c][2 * j + c] = 1

I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
D = kron(N2, I4)
assert rank_mod(D) == 8

# At the fixed locus, each physical C3 orbit has identical transported
# coefficient data. The two orbits may carry independent coefficient vectors.
source_columns = []
for orbit in range(2):
    for coeff in range(4):
        col = [0] * 24
        for cut in range(3):
            label = 2 * cut + orbit
            col[4 * label + coeff] = 1
        source_columns.append(col)

source_matrix = [list(row) for row in zip(*source_columns)]
assert rank_mod(source_matrix) == 8

# The invariant physical-source subspace equals the image of N2 tensor I4.
joined = [D[i] + source_matrix[i] for i in range(24)]
assert rank_mod(joined) == rank_mod(D)

result = {
    "schema": "marici.rs2.physical-source-tate-occupancy.v1",
    "ambient_label_coefficient_dimension": 24,
    "norm_differential_rank": rank_mod(D),
    "norm_homology_dimension": 24 - 2 * rank_mod(D),
    "physical_cyclic_invariant_subspace_dimension": rank_mod(source_matrix),
    "physical_subspace_contained_in_norm_image": True,
    "physical_class_in_norm_homology": "zero",
    "scope": "equal-energy C3 fixed locus with identity coefficient transport",
    "verdict": (
        "The canonical Tate bridge identifies an available coefficient line, "
        "but the frozen cyclic all-positive physical source occupies only norm "
        "boundaries and has zero class in that homology."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs2-physical-source-tate-occupancy.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
