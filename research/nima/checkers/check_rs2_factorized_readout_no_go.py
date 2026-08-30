"""Exact tensor no-go for factorized scalar readouts of the C3 syndrome."""

import json
from pathlib import Path


P = 3


def kron(a, b):
    return [[(x * y) % P for x in ar for y in br] for ar in a for br in b]


R6 = [[1, 1, 1, 1, 1, 1]]

# Two independent norm-homology representatives in source occurrence order.
h_left = [[1], [0], [-1], [0], [0], [0]]
h_right = [[0], [1], [0], [-1], [0], [0]]
homology_representatives = [h_left, h_right]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


assert all(multiply(R6, h) == [[0]] for h in homology_representatives)

coefficient_dimension = 4
coefficient_basis = [
    [[1 if i == j else 0] for i in range(coefficient_dimension)]
    for j in range(coefficient_dimension)
]
syndrome_tensor_basis = [
    kron(h, v) for h in homology_representatives for v in coefficient_basis
]
assert len(syndrome_tensor_basis) == 8

# Test a basis of all coefficient covectors. Linearity then proves the result
# for every ell in V*.
dual_basis = [[[1 if i == j else 0 for i in range(coefficient_dimension)]]
              for j in range(coefficient_dimension)]
for ell in dual_basis:
    factorized = kron(R6, ell)
    assert all(multiply(factorized, h) == [[0]] for h in syndrome_tensor_basis)

result = {
    "schema": "marici.rs2.factorized-readout-no-go.v1",
    "occurrence_homology_dimension": 2,
    "coefficient_dimension": coefficient_dimension,
    "syndrome_tensor_dimension": len(syndrome_tensor_basis),
    "factorized_readout_family": "R_occurrence tensor ell, for arbitrary ell in V*",
    "rank_on_syndrome": 0,
    "required_shape_of_nonzero_activation": (
        "an occurrence-labelled/nonfactorizable kernel mixing label and coefficient data"
    ),
    "verdict": (
        "No global all-positive occurrence sum followed by any coefficient "
        "covector can detect the mod-three syndrome."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs2-factorized-readout-no-go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
