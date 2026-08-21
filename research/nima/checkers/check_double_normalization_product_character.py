#!/usr/bin/env python3
"""Derive the product deck character from two normalization quotients."""

import json
import sympy as sp
from pathlib import Path


# Branch values ordered (++),(-+),(+-),(--), first sign scaffold c,
# second sign spin p.
dc = sp.Matrix([[-1, 1, 0, 0], [0, 0, -1, 1]])
dp = sp.Matrix([[-1, 1]])
mixed = dp * dc
expected = sp.Matrix([[1, -1, -1, 1]])
assert mixed == expected

# Deck permutations on branch values.
Pc = sp.Matrix([
    [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]
])
Pp = sp.Matrix([
    [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]
])
assert mixed * Pc == -mixed
assert mixed * Pp == -mixed
assert Pc * Pp == Pp * Pc

# Each single quotient is coker(diagonal Q -> Q^2), a primitive sign line.
diagonal = sp.Matrix([[1], [1]])
difference = sp.Matrix([[-1, 1]])
assert difference * diagonal == sp.zeros(1, 1)
assert difference.rank() == 1

def integer_rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


result = {
    "status": "PASS",
    "scaffold_difference": integer_rows(dc),
    "spin_difference": integer_rows(dp),
    "mixed_boundary": integer_rows(mixed),
    "mixed_coefficients": [1, -1, -1, 1],
    "scaffold_deck_character": -1,
    "spin_deck_character": -1,
    "derived_character": "chi_scaffold * chi_spin",
    "conclusion": "the bridge coefficient line is the tensor product of the two normalization-conductor quotient lines",
}

out = Path(__file__).resolve().parents[1] / "results" / "double_normalization_product_character.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
