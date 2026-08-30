#!/usr/bin/env python3
"""Smallest exact sheet-faithfulness witness inside the physical rank-26 quotient."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-two-class-sheet-faithfulness.json"
PRIME = 32009
os.environ["MARICI_FIELD_PRIME"] = str(PRIME)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")

gamma = (-pow(2, -1, PRIME)) % PRIME
names = ("g1", "g2", "g3", "g23", "g31")
low, columns, pivots, free = base.presentation(names, gamma, 14, 7, minimum_q_level=1)
levels = (1, 1, 1, 1, 1)
q0 = base.quotient_coordinates((0, *levels, (0, 0)), columns, pivots, free)
q1 = base.quotient_coordinates((0, *levels, (1, 0)), columns, pivots, free)
span: dict[int, dict[int, int]] = {}
base.add_pivot(dict(q0), span)
base.add_pivot(dict(q1), span)

x, y, z = 2, 3, 4
C1 = x*x*y+x*x*z+x*y*y+2*x*y*z+2*x*z*z-y**3-y*y*z+y*z*z+z**3
D = C1*pow(x, -1, PRIME) % PRIME
r = next(value for value in range(1, PRIME) if value*value % PRIME == D)

def weight(a: int) -> int:
    factors = [
        (-2*x*a) % PRIME,       # dR1/da
        (a-x-z) % PRIME,        # g2
        (a+y+2*z) % PRIME,      # g3 on g1
        (y+z-x) % PRIME,        # g23 on g1
        (a-y) % PRIME,          # g31
    ]
    product = 1
    for factor in factors:
        if factor == 0:
            raise ValueError("sample lies on a spectator or ramification divisor")
        product = product*factor % PRIME
    return pow(product, -1, PRIME)

w_plus = weight(r)
w_minus = weight((-r) % PRIME)
matrix = [
    [w_plus, r*w_plus % PRIME],
    [w_minus, (-r)*w_minus % PRIME],
]
determinant = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]) % PRIME

checks = {
    "physical_half_twist_encoded": (2*gamma+1) % PRIME == 0,
    "absolute_quotient_rank_is_26": len(free) == 26,
    "constant_and_linear_classes_survive_independently": len(span) == 2,
    "chosen_root_lies_on_cover": r*r % PRIME == D,
    "both_sheet_weights_nonzero": w_plus != 0 and w_minus != 0,
    "sheet_evaluation_matrix_has_rank_two": determinant != 0,
}
payload = {
    "schema": "marici.rank26-conductor-two-class-sheet-faithfulness.v1",
    "prime": PRIME,
    "gamma_mod_prime": gamma,
    "absolute_dimension": len(free),
    "domain_classes": ["[1]", "[a]"],
    "domain_span_rank": len(span),
    "root": r,
    "conjugate_root": (-r) % PRIME,
    "sheet_matrix": matrix,
    "determinant": determinant,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The predeclared quotient classes [1] and [a] already map with rank two to the two conductor sheets. Sheet resolution is necessary and generically faithful on this minimal subspace.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
