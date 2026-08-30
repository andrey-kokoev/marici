"""Exact equivariant soft-star specialization of the RS-3 Tate quotient."""

import json
from pathlib import Path

P = 3


def mat_vec(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(len(v))) % P for i in range(len(m)))


def rank_mod3(columns):
    if not columns:
        return 0
    a = [[columns[c][r] % P for c in range(len(columns))] for r in range(len(columns[0]))]
    row = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, P)
        a[row] = [(inv * x) % P for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                f = a[i][col]
                a[i] = [(x - f * y) % P for x, y in zip(a[i], a[row])]
        row += 1
    return row


# Three cyclic softening arms: gamma_i(eta) has Xi=eta and the other two
# energies equal to one. Rotation permutes arms regularly.
sigma = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
augmentation = (1, 1, 1)

e0, e1, e2 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
t = tuple((x - y) % P for x, y in zip(e1, e0))
sigma_t = mat_vec(sigma, t)
t2 = tuple((x - y) % P for x, y in zip(sigma_t, t))
oriented = tuple((x - y) % P for x, y in zip(e1, e2))

assert rank_mod3([t, t2]) == 2              # augmentation ideal I
assert rank_mod3([t2]) == 1                 # (g-1)I
assert rank_mod3([t, t2]) - rank_mod3([t2]) == 1
assert sum(oriented) % P == 0

# Each normalized endpoint has soft Gysin multiplicity one, so the total
# supported readout is the identity from arm labels to endpoint labels.
gysin = identity
for e in (e0, e1, e2):
    assert mat_vec(gysin, mat_vec(sigma, e)) == mat_vec(sigma, mat_vec(gysin, e))
assert mat_vec(gysin, oriented) == oriented

# The induced map on I/(g-1)I is nonzero; equivalently the image is not in
# <t2>. The scalar unsplit readout remains zero on I.
assert rank_mod3([t2, mat_vec(gysin, oriented)]) == 2
assert sum(mat_vec(gysin, oriented)) % P == 0

# Negative control: retaining one chosen endpoint is not C3-equivariant.
single_arm = ((1, 0, 0), (0, 0, 0), (0, 0, 0))
assert mat_vec(single_arm, mat_vec(sigma, e0)) != mat_vec(sigma, mat_vec(single_arm, e0))

result = {
    "schema": "marici.rs3.cyclic-soft-star-tate-specialization.v1",
    "status": "passed",
    "carrier": "three cyclic softening arms joined at the equal-energy point",
    "arm_module": "F3[C3]",
    "endpoint_gysin_matrix": [list(row) for row in gysin],
    "each_endpoint_multiplicity": 1,
    "tate_quotient_dimension": 1,
    "induced_supported_map_rank": 1,
    "unsplit_scalar_on_tate": 0,
    "negative_control": "a single-arm endpoint projection is not C3-equivariant",
    "verdict": (
        "The cyclically saturated soft star supplies a canonical supported "
        "specialization of the Tate line. Its vector-valued endpoint Gysin is "
        "nonzero on the Tate quotient, while the unsplit scalar augmentation "
        "still annihilates it."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs3-cyclic-soft-star-tate-specialization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
