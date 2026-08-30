import json
from pathlib import Path

# A Seifert matrix for the oriented link of Z^2-U^3 (the trefoil).
V = [[1, 0], [-1, 1]]

def transpose(a):
    return [list(x) for x in zip(*a)]

def alexander_matrix(t):
    vt = transpose(V)
    return [[t*V[i][j] - vt[i][j] for j in range(2)] for i in range(2)]

def det2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

samples = {t: det2(alexander_matrix(t)) for t in (-2, -1, 0, 1, 2)}
assert samples == {-2: 7, -1: 3, 0: 1, 1: 1, 2: 3}

# At the source Kummer meridian t=-1, the Alexander presentation is invertible.
matrix_at_minus_one = alexander_matrix(-1)
assert matrix_at_minus_one == [[-2, 1], [1, -2]]
assert det2(matrix_at_minus_one) == 3

packet = {
    "schema": "marici.p6_soft_cusp_kummer.v1",
    "singularity": "A2: Z^2-U^3",
    "link": "trefoil",
    "seifert_matrix": V,
    "alexander_polynomial": "t^2-t+1",
    "source_meridian_character": -1,
    "alexander_matrix_at_character": matrix_at_minus_one,
    "determinant_at_character": 3,
    "twisted_link_cohomology_dimensions": [0, 0, 0],
    "kummer_supported_class_rank": 0,
}
Path("research/benincasa/results/p6-soft-cusp-kummer.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
