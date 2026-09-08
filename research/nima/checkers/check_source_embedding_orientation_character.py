#!/usr/bin/env python3
"""Exact affine and dihedral orientation character for five labelled facets."""
import json
from fractions import Fraction
from pathlib import Path

def edge_form(permutation):
    coefficients = {}
    for i in range(5):
        a, b = permutation[i], permutation[(i+1) % 5]
        key = tuple(sorted((a, b)))
        sign = 1 if a < b else -1
        coefficients[key] = coefficients.get(key, 0) + sign
    return coefficients

identity = edge_form(tuple(range(5)))
def scale_form(form, scalar):
    return {edge: scalar * value for edge, value in form.items()}

dihedral = []
for kind in ("rotation", "reflection"):
    for k in range(5):
        permutation = tuple((i+k) % 5 for i in range(5)) if kind == "rotation" else tuple((k-i) % 5 for i in range(5))
        transformed = edge_form(permutation)
        expected_sign = 1 if kind == "rotation" else -1
        assert transformed == scale_form(identity, expected_sign)
        dihedral.append({"kind": kind, "k": k, "permutation": list(permutation), "form_sign": expected_sign})

# Coordinate reflection x'=-x, y'=y has determinant -1. Gradients transform
# by M^-T; all cyclic Jacobians reverse sign, compensating the reversed volume.
gradients = [(1,0), (0,1), (-1,0), (-1,-1), (0,-1)]
transformed_gradients = [(-gx, gy) for gx, gy in gradients]
def det(u, v):
    return u[0]*v[1] - u[1]*v[0]
old_jacobians = [det(gradients[i], gradients[(i+1) % 5]) for i in range(5)]
new_jacobians = [det(transformed_gradients[i], transformed_gradients[(i+1) % 5]) for i in range(5)]
assert old_jacobians == [1] * 5
assert new_jacobians == [-1] * 5

result = {
    "schema": "marici.source-embedding-orientation-character.v1",
    "status": "passed",
    "strength": "exact full D5 label action and one orientation-reversing affine generator; generic signs follow from determinant and wedge functoriality",
    "dihedral_checks": dihedral,
    "character": {"rotation": 1, "reflection": -1},
    "coordinate_reflection": {"determinant": -1, "old_jacobians": old_jacobians, "new_jacobians": new_jacobians},
    "transport_rule": "multiply the coordinate top-form coefficient by sign(det M), and multiply a facet relabelling by its cyclic-orientation character",
    "boundary": "orientation transport compares admitted labelled embeddings; it does not authenticate a source map or permit an unlabelled quotient",
}
out = Path("research/nima/results/source_embedding_orientation_character.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
