#!/usr/bin/env python3
"""Exact orientation-line coherence for five-point double residues."""
import itertools
import json
from pathlib import Path

N = 5
compatible = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]


def sign(sequence):
    inversions = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def ambient_residue(ordered):
    remainder = [i for i in range(N) if i not in ordered]
    return sign(list(ordered) + remainder)


def orientation_basis_sign(ordered):
    return sign([sorted(ordered).index(i) for i in ordered])


faces = []
for face in compatible:
    canonical_values = []
    order_data = []
    for ordered in itertools.permutations(face):
        raw = ambient_residue(ordered)
        basis = orientation_basis_sign(ordered)
        canonical = raw * basis
        canonical_values.append(canonical)
        order_data.append({"order": list(ordered), "raw_residue": raw, "orientation_basis_sign": basis, "canonical_tensor_coordinate": canonical})
    assert len(set(canonical_values)) == 1
    direct = ambient_residue(face)
    nested = canonical_values[0]
    assert direct == nested
    faces.append({"face": list(face), "orders": order_data, "direct_equals_nested_after_transport": True})

# Deliberate failure: discarding the orientation-line basis leaves opposite raw
# values for every reversed order.
untwisted_failures = sum(ambient_residue(face) != ambient_residue(tuple(reversed(face))) for face in compatible)
assert untwisted_failures == 5

result = {
    "schema": "marici.fact5-orientation-line-residue.v1",
    "status": "passed",
    "strength": "finite five-point normal-orientation coherence; no contour, normalization, or arbitrary-codimension theorem",
    "orientation_line": "det(Z^I)",
    "faces_checked": faces,
    "order_independent_twisted_residues": 5,
    "untwisted_commuting_deliberate_failure_count": untwisted_failures,
    "composition": "or(I) tensor or(J) -> or(I disjoint-union J) by wedge",
    "symmetry": "Koszul sign (-1)^(|I||J|)",
}
out = Path("research/nima/results/fact5_orientation_line_residue.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
