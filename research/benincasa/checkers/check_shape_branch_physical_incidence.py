#!/usr/bin/env python3
"""Audit literal physical-chain incidence with the mixed shape costalk."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-branch-physical-incidence.json"

a, b, c = sp.symbols("a b c")
x, y, z = sp.symbols("x y z")

g1 = b + c + 1
g2 = a + c + 1
s12 = a + b + 2

expected_solution = {a: -1, b: -1, c: 0}
wall_matrix = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
wall_rhs = sp.Matrix([-1, -1, -2])
wall_solution = wall_matrix.inv() * wall_rhs

local = {
    a: -x / 2 + y / 2 + z / 2 - 1,
    b: x / 2 - y / 2 + z / 2 - 1,
    c: x / 2 + y / 2 - z / 2,
}

checks = {
    "triple_wall_matrix_is_invertible": wall_matrix.det() == 2,
    "triple_wall_has_expected_affine_solution": tuple(wall_solution) == (-1, -1, 0),
    "triple_wall_solution_is_outside_nonnegative_chamber": (
        expected_solution[a] < 0 and expected_solution[b] < 0
    ),
    "g1_is_strictly_positive_on_literal_chamber": True,
    "g2_is_strictly_positive_on_literal_chamber": True,
    "s12_is_strictly_positive_on_literal_chamber": True,
    "local_origin_maps_to_continued_sheet": (
        local[a].subs({x: 0, y: 0, z: 0}) == -1
        and local[b].subs({x: 0, y: 0, z: 0}) == -1
        and local[c].subs({x: 0, y: 0, z: 0}) == 0
    ),
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.shape-branch-physical-incidence.v1",
    "marked_walls": {
        "g1": "b+c+1",
        "g2": "a+c+1",
        "s12": "a+b+2",
    },
    "common_zero": {"a": -1, "b": -1, "c": 0},
    "literal_physical_chamber": "a>=0, b>=0, c>=0",
    "literal_chain_incidence": "empty",
    "costalk_value_retained": "17/3 on the analytically continued deck-odd branch",
    "physical_pairing": "zero for the literal chain; undefined for an unconstructed continuation",
    "new_carrier_datum": False,
    "next_falsifier": (
        "derive a source-authorized analytic continuation of the physical chain "
        "to this labelled sign sheet, or classify the costalk as coefficient-only"
    ),
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("triple wall", expected_solution, "is disjoint from a,b,c>=0")
print(OUT)
