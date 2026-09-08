#!/usr/bin/env python3
"""Exact orientation census for five-point iterated channel residues."""
import json
from pathlib import Path

N = 5
compatible = {(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)}


def permutation_sign(sequence):
    inversions = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def direct_residue_sign(ordered_channels):
    remainder = [index for index in range(N) if index not in ordered_channels]
    return permutation_sign(list(ordered_channels) + remainder)


checks = []
for i, j in sorted(compatible):
    coefficient = 1  # the unique triangulation monomial 1/(a_i a_j)
    forward = direct_residue_sign((i, j)) * coefficient
    reverse = direct_residue_sign((j, i)) * coefficient
    assert forward == -reverse
    checks.append({
        "channels": [i, j],
        "coefficient_multi_residue": coefficient,
        "ordered_residue_i_then_j": forward,
        "ordered_residue_j_then_i": reverse,
        "koszul_relation": "Res_i Res_j = - Res_j Res_i",
        "lower_point_triangle_product": 1,
    })

incompatible = []
for i in range(N):
    for j in range(i + 1, N):
        if (i, j) not in compatible:
            incompatible.append([i, j])
assert len(compatible) == 5 and len(incompatible) == 5

# Deliberate failure: treating ordered residues as commuting disagrees for every
# compatible codimension-two face.
naive_commuting_failures = sum(
    direct_residue_sign((i, j)) != direct_residue_sign((j, i))
    for i, j in compatible
)
assert naive_commuting_failures == 5

result = {
    "schema": "marici.fact5-iterated-residue-orientation.v1",
    "status": "passed",
    "strength": "exact five-point orientation and formal multi-residue census; no contour or physical normalization theorem",
    "ambient_orientation": "da0 wedge da1 wedge da2 wedge da3 wedge da4",
    "direct_convention": "Omega=(da_i/a_i) wedge (da_j/a_j) wedge Res_(i,j)+regular",
    "compatible_faces": checks,
    "incompatible_channel_pairs_with_zero_double_coefficient": incompatible,
    "naive_commuting_deliberate_failure_count": naive_commuting_failures,
    "normalization_rule": "for N regular on the face, each ordered multi-residue is multiplied by N restricted to that face",
    "boundary": "reversing normal order changes orientation sign; contour and i0 data remain unsupplied",
}
out = Path("research/nima/results/fact5_iterated_residue_orientation.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
