"""Exact F3 audit: the C3 Tate line lies in the kernel of source sewing."""

import json
from pathlib import Path

P = 3


def rank_mod3(matrix):
    a = [[x % P for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, P)
        a[rank] = [(inv * x) % P for x in a[rank]]
        for r in range(rows):
            if r == rank:
                continue
            f = a[r][col]
            a[r] = [(a[r][c] - f * a[rank][c]) % P for c in range(cols)]
        rank += 1
    return rank


# Regular C3 occurrence module A=F3<e0,e1,e2>.
g = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
gm1 = [[(g[r][c] - identity[r][c]) % P for c in range(3)] for r in range(3)]
epsilon = [[1, 1, 1]]

# I=ker epsilon has basis (e0-e1,e1-e2).
i_basis = [[1, 0], [2, 1], [0, 2]]
assert rank_mod3(i_basis) == 2

# (g-1)I has rank one, hence H=I/(g-1)I has dimension one.
gm1_i = [
    [sum(gm1[r][k] * i_basis[k][c] for k in range(3)) % P for c in range(2)]
    for r in range(3)
]
image_rank = rank_mod3(gm1_i)
assert image_rank == 1
tate_dimension = 2 - image_rank
assert tate_dimension == 1

# Source sewing is augmentation, so it kills all of I before the Tate quotient.
epsilon_i = [
    [sum(epsilon[0][k] * i_basis[k][c] for k in range(3)) % P for c in range(2)]
    for _ in range(1)
]
assert epsilon_i == [[0, 0]]

# Negative control: a labelled occurrence readout need not kill I.
labelled_readout = [[1, 0, 0]]
labelled_on_i = [[
    sum(labelled_readout[0][k] * i_basis[k][c] for k in range(3)) % P
    for c in range(2)
]]
assert rank_mod3(labelled_on_i) == 1

result = {
    "schema": "marici.rs3.tate-line-kernel-of-source-sewing.v1",
    "field": "F3",
    "augmentation_ideal_dimension": 2,
    "gm1_image_in_augmentation_ideal_rank": image_rank,
    "tate_quotient_dimension": tate_dimension,
    "source_sewing_on_augmentation_ideal": epsilon_i,
    "all_unsplit_factorized_readouts_kill_tate_line": True,
    "negative_control_labelled_readout_rank_on_I": rank_mod3(labelled_on_i),
    "soft_gysin_control": (
        "not constrained by this no-go because the supported Gysin readout "
        "does not factor through unsplit augmentation"
    ),
    "verdict": (
        "The canonical C3 Tate line is a quotient of the kernel of source "
        "sewing. Any physical scalar readout factoring through the unsplit "
        "source annihilates it. Activation requires a supported or relative "
        "readout that does not factor solely through augmentation."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs3-tate-line-kernel-of-source-sewing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

