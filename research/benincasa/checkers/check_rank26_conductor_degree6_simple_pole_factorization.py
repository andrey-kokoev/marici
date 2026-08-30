#!/usr/bin/env python3
"""Factor the full degree-six simple-pole numerator tower through the root algebra."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-degree6-simple-pole-factorization.json"
PRIME = 32009
os.environ["MARICI_FIELD_PRIME"] = str(PRIME)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")


def matrix_rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for row in rows:
        base.add_pivot(dict(row), pivots)
    return len(pivots)


gamma = (-pow(2, -1, PRIME)) % PRIME
names = ("g1", "g2", "g3", "g23", "g31")
_, columns, pivots, free = base.presentation(names, gamma, 14, 7, minimum_q_level=1)
levels = (1, 1, 1, 1, 1)
monomials = [(i, j) for i in range(7) for j in range(7-i)]
quotient_columns = [
    base.quotient_coordinates((0, *levels, exponent), columns, pivots, free)
    for exponent in monomials
]
quotient_rows = [
    {column_index: quotient_columns[column_index][coordinate]
     for column_index in range(len(monomials)) if coordinate in quotient_columns[column_index]}
    for coordinate in free
]
domain_rank = matrix_rank(quotient_rows)

x, y, z = 2, 3, 4
b0 = (y+z) % PRIME
C1 = x*x*y+x*x*z+x*y*y+2*x*y*z+2*x*z*z-y**3-y*y*z+y*z*z+z**3
D = C1*pow(x, -1, PRIME) % PRIME
r = next(value for value in range(1, PRIME) if value*value % PRIME == D)

def weight(a: int) -> int:
    factors = [(-2*x*a) % PRIME, (a-x-z) % PRIME, (a+y+2*z) % PRIME,
               (y+z-x) % PRIME, (a-y) % PRIME]
    product = 1
    for factor in factors:
        if factor == 0:
            raise ValueError("sample lies on excluded support")
        product = product*factor % PRIME
    return pow(product, -1, PRIME)

w_plus, w_minus = weight(r), weight((-r) % PRIME)
j_plus: dict[int, int] = {}
j_minus: dict[int, int] = {}
for index, (i, j) in enumerate(monomials):
    j_plus[index] = w_plus*pow(r, i, PRIME)*pow(b0, j, PRIME) % PRIME
    j_minus[index] = w_minus*pow((-r) % PRIME, i, PRIME)*pow(b0, j, PRIME) % PRIME
j_rows = [j_plus, j_minus]
j_rank = matrix_rank(j_rows)
stacked_rank = matrix_rank(quotient_rows+j_rows)
j_even = {index: (j_plus[index]+j_minus[index]) % PRIME for index in range(len(monomials))}
j_odd = {index: (j_plus[index]-j_minus[index]) % PRIME for index in range(len(monomials))}
even_stacked_rank = matrix_rank(quotient_rows+[j_even])
odd_stacked_rank = matrix_rank(quotient_rows+[j_odd])

index_of = {exponent: index for index, exponent in enumerate(monomials)}
recurrence_ok = True
wall_scalar_ok = True
for i, j in monomials:
    if i+2+j <= 6:
        left, right = index_of[(i+2, j)], index_of[(i, j)]
        recurrence_ok &= all(row[left] == D*row[right] % PRIME for row in j_rows)
    if i+j+1 <= 6:
        left, right = index_of[(i, j+1)], index_of[(i, j)]
        wall_scalar_ok &= all(row[left] == b0*row[right] % PRIME for row in j_rows)

checks = {
    "physical_absolute_dimension_is_26": len(free) == 26,
    "degree6_simple_pole_domain_rank_is_26": domain_rank == 26,
    "sheet_map_rank_is_two": j_rank == 2,
    "naive_sheet_map_has_one_descent_defect": stacked_rank-domain_rank == 1,
    "quadratic_root_recurrence_holds": recurrence_ok,
    "wall_coordinate_specializes_as_scalar": wall_scalar_ok,
    "both_deck_rows_share_one_common_defect_line": even_stacked_rank-domain_rank == 1 and odd_stacked_rank-domain_rank == 1 and stacked_rank-domain_rank == 1,
}
payload = {
    "schema": "marici.rank26-conductor-degree6-simple-pole-descent-defect.v2",
    "prime": PRIME,
    "gamma_mod_prime": gamma,
    "monomial_count": len(monomials),
    "simple_pole_domain_rank": domain_rank,
    "sheet_map_rank": j_rank,
    "stacked_rank": stacked_rank,
    "descent_defect_rank": stacked_rank-domain_rank,
    "deck_even_stacked_rank": even_stacked_rank,
    "deck_odd_stacked_rank": odd_stacked_rank,
    "root_recurrence": "J(a^(i+2)b^j)=D*J(a^i b^j)",
    "wall_recurrence": "J(a^i b^(j+1))=(y+z)*J(a^i b^j)",
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The pointwise two-sheet evaluation obeys the root recurrences but does not descend through the physical-half-twist quotient. Both deck combinations fail individually yet together add only one rank, so they share one exact-descent obstruction line. A specialization-cone coherence correction is mandatory.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
