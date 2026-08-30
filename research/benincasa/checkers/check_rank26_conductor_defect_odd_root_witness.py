#!/usr/bin/env python3
"""Extract the exact quotient relation detected by naive conductor evaluation."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-defect-odd-root-witness.json"
PRIME = 32009
os.environ["MARICI_FIELD_PRIME"] = str(PRIME)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")

gamma = (-pow(2, -1, PRIME)) % PRIME
names = ("g1", "g2", "g3", "g23", "g31")
_, columns, presentation_pivots, free = base.presentation(names, gamma, 14, 7, minimum_q_level=1)
levels = (1, 1, 1, 1, 1)
monomials = [(i, j) for i in range(7) for j in range(7-i)]
quotient_columns = [base.quotient_coordinates((0, *levels, exponent), columns, presentation_pivots, free) for exponent in monomials]

row_pivots: dict[int, dict[int, int]] = {}
for coordinate in free:
    row = {index: quotient_columns[index][coordinate] for index in range(len(monomials)) if coordinate in quotient_columns[index]}
    if row:
        base.add_pivot(row, row_pivots)
free_variables = [index for index in range(len(monomials)) if index not in row_pivots]

relations = []
for free_variable in free_variables:
    vector = {free_variable: 1}
    for pivot in sorted(row_pivots):
        value = sum(coefficient*vector.get(index, 0) for index, coefficient in row_pivots[pivot].items() if index != pivot) % PRIME
        if value:
            vector[pivot] = (-value) % PRIME
    relations.append(vector)

x, y, z = 2, 3, 4
b0 = (y+z) % PRIME
C1 = x*x*y+x*x*z+x*y*y+2*x*y*z+2*x*z*z-y**3-y*y*z+y*z*z+z**3
D = C1*pow(x, -1, PRIME) % PRIME

def root_remainder(vector: dict[int, int]) -> tuple[int, int]:
    even = odd = 0
    for index, coefficient in vector.items():
        i, j = monomials[index]
        scalar = coefficient*pow(b0, j, PRIME) % PRIME
        if i % 2:
            odd = (odd+scalar*pow(D, (i-1)//2, PRIME)) % PRIME
        else:
            even = (even+scalar*pow(D, i//2, PRIME)) % PRIME
    return even, odd

remainders = [root_remainder(vector) for vector in relations]
witness_index = next(index for index, remainder in enumerate(remainders) if remainder != (0, 0))
witness = relations[witness_index]
witness_remainder = remainders[witness_index]
null_relation = relations[1-witness_index]
null_remainder = remainders[1-witness_index]

def signed(value: int) -> int:
    return value if value <= PRIME//2 else value-PRIME

witness_terms = [
    {"a_degree": monomials[index][0], "b_degree": monomials[index][1], "coefficient": signed(coefficient)}
    for index, coefficient in sorted(witness.items())
]
checks = {
    "quotient_relation_space_has_dimension_two": len(relations) == 2,
    "one_relation_is_invisible_to_root_evaluation": null_remainder == (0, 0),
    "one_relation_has_nonzero_root_remainder": witness_remainder != (0, 0),
    "defect_remainder_has_zero_even_part": witness_remainder[0] == 0,
    "defect_remainder_has_nonzero_odd_part": witness_remainder[1] != 0,
}
payload = {
    "schema": "marici.rank26-conductor-defect-odd-root-witness.v1",
    "prime": PRIME,
    "gamma_mod_prime": gamma,
    "relation_space_dimension": len(relations),
    "witness_free_monomial": monomials[free_variables[witness_index]],
    "witness_terms": witness_terms,
    "witness_root_remainder": {"even": signed(witness_remainder[0]), "odd_coefficient_of_a": signed(witness_remainder[1])},
    "other_relation_root_remainder": {"even": signed(null_remainder[0]), "odd_coefficient_of_a": signed(null_remainder[1])},
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The unique naive-descent defect is represented by an exact quotient relation whose restriction to b=y+z and a^2=D is a nonzero pure-odd multiple of a. It is the root-odd/nilpotent collision direction, not an arbitrary scalar discrepancy.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
