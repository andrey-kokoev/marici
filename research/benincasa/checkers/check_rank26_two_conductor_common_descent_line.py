#!/usr/bin/env python3
"""Test whether both labelled conductor sheet maps share one quotient defect line."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
suffix = "" if P == 32009 else f"-p{P}"
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-two-conductor-common-descent-line{suffix}.json"
os.environ["MARICI_FIELD_PRIME"] = str(P)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")


def rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        base.add_pivot(dict(source), pivots)
    return len(pivots)


def root(n: int) -> int:
    return next(r for r in range(1, P) if r*r % P == n)


x, y, z = 2, 3, 4
gamma = -pow(2, -1, P) % P
names = ("g1", "g2", "g3", "g23", "g31")
_, columns, pivots, free = base.presentation(names, gamma, 14, 7, minimum_q_level=1)
levels = (1, 1, 1, 1, 1)
monomials = [(i, j) for i in range(7) for j in range(7-i)]
qcols = [base.quotient_coordinates((0, *levels, exponent), columns, pivots, free) for exponent in monomials]
qrows = [{j: qcols[j][coordinate] for j in range(len(monomials)) if coordinate in qcols[j]} for coordinate in free]

C1 = x*x*y+x*x*z+x*y*y+2*x*y*z+2*x*z*z-y**3-y*y*z+y*z*z+z**3
C2 = x**3-x*x*y+x*x*z-x*y*y-2*x*y*z-x*z*z-y*y*z-2*y*z*z-z**3
r1 = root(C1 * pow(x, -1, P) % P)
r2 = root(-C2 * pow(y, -1, P) % P)
b1 = (y + z) % P
a2 = (x + z) % P


def weight1(a: int) -> int:
    denominator = (-2*x*a) % P
    for factor in (a-x-z, a+y+2*z, y+z-x, a-y):
        denominator = denominator * factor % P
    return pow(denominator, -1, P)


def weight2(b: int) -> int:
    denominator = (2*y*b) % P
    for factor in (b-y-z, x+2*z+b, b-x, x+z-y):
        denominator = denominator * factor % P
    return (b+z-y) * pow(denominator, -1, P) % P


g1 = []
for a in (r1, -r1 % P):
    w = weight1(a)
    g1.append({j: w*pow(a, i, P)*pow(b1, k, P) % P for j, (i, k) in enumerate(monomials)})
g2 = []
for b in (r2, -r2 % P):
    w = weight2(b)
    g2.append({j: w*pow(a2, i, P)*pow(b, k, P) % P for j, (i, k) in enumerate(monomials)})

def deck_rows(rows):
    return [
        {j: (rows[0][j]+rows[1][j]) % P for j in range(len(monomials))},
        {j: (rows[0][j]-rows[1][j]) % P for j in range(len(monomials))},
    ]

g1_deck = deck_rows(g1)
g2_deck = deck_rows(g2)
base_rank = rank(qrows)
checks = {
    "absolute_rank_26": base_rank == 26,
    "first_conductor_sheet_rank_two": rank(g1) == 2,
    "second_conductor_sheet_rank_two": rank(g2) == 2,
    "first_conductor_adds_one_defect": rank(qrows+g1) == 27,
    "second_conductor_adds_one_defect": rank(qrows+g2) == 27,
    "both_conductors_share_one_defect": rank(qrows+g1+g2) == 27,
    "all_four_deck_channels_share_one_defect": rank(qrows+g1_deck+g2_deck) == 27,
}
payload = {
    "schema": "marici.rank26-two-conductor-common-descent-line.v1",
    "prime": P,
    "ranks": {
        "absolute": base_rank,
        "g1_sheet": rank(g1),
        "g2_sheet": rank(g2),
        "absolute_plus_g1": rank(qrows+g1),
        "absolute_plus_g2": rank(qrows+g2),
        "absolute_plus_both": rank(qrows+g1+g2),
        "absolute_plus_all_deck_channels": rank(qrows+g1_deck+g2_deck),
    },
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The two independently labelled conductor sheet maps and all four of their deck channels add the same single line beyond the rank-26 absolute quotient. The gamma-Bockstein therefore has one common conductor-descent target rather than one correction per branch.",
}
OUT.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
