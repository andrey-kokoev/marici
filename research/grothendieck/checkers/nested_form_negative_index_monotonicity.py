"""Exact finite-dimensional fixture for monotonicity of negative index."""

import json
from pathlib import Path

import sympy as sp

# Each matrix is the leading principal restriction of the next one.
matrices = [
    sp.diag(2, 3),
    sp.diag(2, 3, -1),
    sp.diag(2, 3, -1, -2, 5),
]


def negative_index(matrix):
    eigenvalues = matrix.eigenvals()
    return sum(multiplicity for value, multiplicity in eigenvalues.items() if value < 0)


indices = [negative_index(matrix) for matrix in matrices]
checks = {
    "expected_indices": indices == [0, 1, 2],
    "negative_index_monotone": all(a <= b for a, b in zip(indices, indices[1:])),
    "restrictions_are_leading_principal": all(
        matrices[j + 1][: matrices[j].rows, : matrices[j].cols] == matrices[j]
        for j in range(len(matrices) - 1)
    ),
}
result = {
    "schema": "marici.grothendieck.nested-form-negative-index-monotonicity.v1",
    "negative_indices": indices,
    **checks,
    "all_verified": all(checks.values()),
    "claim_boundary": "Exact finite fixture; the infinite-dimensional statement uses the variational definition of negative index.",
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "nested-form-negative-index-monotonicity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
