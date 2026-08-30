#!/usr/bin/env python3
"""Classify native ternary circuits in the physical shape-wall arrangement."""

import json
from itertools import combinations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-wall-ternary-circuits.json"

a, b, c, t = sp.symbols("a b c t")
variables = (a, b, c)
walls = {
    "g1": b + c + 1, "g2": c + a + 1, "g3": a + b + 1,
    "B12": c + 3, "B23": a + 3, "B31": b + 3,
    "s12": a + b + 2, "s23": b + c + 2, "s31": c + a + 2,
}
P1, P2, P3 = 1 + t, 1 - t, sp.Integer(1)
cm = sp.Matrix([
    [0, 1, 1, 1, 1], [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, P2**2, P1**2], [1, a**2, P2**2, 0, P3**2],
    [1, b**2, P1**2, P3**2, 0],
])
K0 = sp.factor((-cm.det() / 2).subs(t, 0))


def affine_row(f):
    gradient = [sp.diff(f, x) for x in variables]
    constant = sp.expand(f - sum(gradient[i] * variables[i] for i in range(3)))
    return gradient, constant


records = {}
counts = {"empty": 0, "transverse_point": 0, "transverse_point_on_K0": 0, "rank_two_circuit": 0}
checks = {}
for labels in combinations(walls, 3):
    key = "__".join(labels)
    rows = [affine_row(walls[label]) for label in labels]
    G = sp.Matrix([row[0] for row in rows])
    augmented = G.row_join(sp.Matrix([[-row[1]] for row in rows]))
    rank, augmented_rank = G.rank(), augmented.rank()
    if augmented_rank > rank:
        records[key] = {"kind": "empty", "gradient_rank": rank}
        counts["empty"] += 1
        continue
    if rank == 3:
        point = G.inv() * sp.Matrix([-row[1] for row in rows])
        value = sp.factor(K0.subs(dict(zip(variables, point))))
        on_k0 = value == 0
        kind = "transverse_point_on_K0" if on_k0 else "transverse_point"
        records[key] = {
            "kind": kind,
            "point": [sp.sstr(x) for x in point],
            "K0_value": sp.sstr(value),
        }
        counts[kind] += 1
        checks[f"{key}_solves_walls"] = all(sp.expand(walls[label].subs(dict(zip(variables, point)))) == 0 for label in labels)
        continue
    if rank == 2:
        relation = G.T.nullspace()[0]
        # Normalize the circuit to primitive integers.
        denominator = sp.ilcm(*[sp.denom(x) for x in relation])
        integers = [int(x * denominator) for x in relation]
        divisor = abs(sp.igcd(*integers))
        integers = [x // divisor for x in integers]
        if next(x for x in integers if x) < 0:
            integers = [-x for x in integers]
        affine_constant = sp.expand(sum(integers[i] * rows[i][1] for i in range(3)))
        remainder = sp.groebner([walls[label] for label in labels], *variables).reduce(K0)[1]
        records[key] = {
            "kind": "rank_two_circuit",
            "circuit_coefficients": integers,
            "affine_relation_constant": sp.sstr(affine_constant),
            "K0_not_identically_zero_on_circuit": remainder != 0,
        }
        counts["rank_two_circuit"] += 1
        checks[f"{key}_affine_circuit_closes"] = affine_constant == 0
        checks[f"{key}_proper_circuit_not_in_K0"] = remainder != 0
        continue
    raise AssertionError((labels, rank, augmented_rank))

assert all(checks.values()), {k: v for k, v in checks.items() if not v}
packet = {
    "schema": "marici.shape-wall-ternary-circuits.v1",
    "triple_count": len(records),
    "counts": counts,
    "records": records,
    "all_checks_pass": True,
    "check_count": len(checks),
    "circuit_associator_maps_constructed": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(counts)
for key, record in records.items():
    if record["kind"] == "rank_two_circuit":
        print(key, record["circuit_coefficients"])
print(OUT)
