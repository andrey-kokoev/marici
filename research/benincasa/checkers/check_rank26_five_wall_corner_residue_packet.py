#!/usr/bin/env python3
"""Source-labelled wall and corner Poincare-residue packet for rank 26."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-five-wall-corner-residue-packet.json"

a, b, x, y, z = sp.symbols("a b x y z")
marks = {
    "g1": b - y - z,
    "g2": a - x - z,
    "g3": a + b + z,
    "g23": b - x,
    "g31": a - y,
}
order = tuple(marks)


def gradient(q):
    return sp.diff(q, a), sp.diff(q, b)


def wall_residue(label):
    """Return coefficient and tangent differential in dq wedge Res = da wedge db."""
    alpha, beta = gradient(marks[label])
    if alpha:
        return sp.simplify(1 / alpha), "db"
    return sp.simplify(-1 / beta), "da"


walls = []
for label in order:
    alpha, beta = gradient(marks[label])
    coefficient, tangent = wall_residue(label)
    reconstructed = alpha * coefficient if tangent == "db" else -beta * coefficient
    walls.append({
        "label": label,
        "equation": str(marks[label]),
        "gradient_da_db": [str(alpha), str(beta)],
        "residue_one_form": f"{coefficient}*d{tangent[-1]}",
        "orientation_check": str(sp.simplify(reconstructed)),
    })

corners = []
parallel = []
for i, left in enumerate(order):
    for right in order[i + 1:]:
        ai, bi = gradient(marks[left])
        aj, bj = gradient(marks[right])
        jacobian = sp.simplify(ai * bj - bi * aj)
        if jacobian == 0:
            parallel.append([left, right])
            continue
        solution = sp.solve((marks[left], marks[right]), (a, b), dict=True)[0]
        forward = sp.simplify(1 / jacobian)
        reverse = sp.simplify(-forward)
        corners.append({
            "ordered_pair": [left, right],
            "point": {"a": str(solution[a]), "b": str(solution[b])},
            "jacobian": str(jacobian),
            "iterated_residue_left_then_right": str(forward),
            "iterated_residue_right_then_left": str(reverse),
        })

# Oriented graph incidence of walls into pair corners.  This records the Cech
# sign convention independently of any period value.
incidence = []
for corner in corners:
    left, right = corner["ordered_pair"]
    incidence.append({"corner": [left, right], "wall_coefficients": {left: -1, right: 1}})

checks = {
    "five_wall_maps_present": len(walls) == 5,
    "every_wall_orientation_reconstructs_da_wedge_db": all(w["orientation_check"] == "1" for w in walls),
    "two_parallel_pairs": len(parallel) == 2,
    "parallel_pairs_are_source_expected": {frozenset(p) for p in parallel} == {
        frozenset(("g1", "g23")), frozenset(("g2", "g31"))
    },
    "eight_corner_maps_present": len(corners) == 8,
    "all_corner_jacobians_are_units": all(abs(int(c["jacobian"])) == 1 for c in corners),
    "iterated_residues_are_antisymmetric": all(
        sp.sympify(c["iterated_residue_left_then_right"]) == -sp.sympify(c["iterated_residue_right_then_left"])
        for c in corners
    ),
}

packet = {
    "schema": "marici.rank26-five-wall-corner-residue-packet.v1",
    "ambient_orientation": "da wedge db",
    "poincare_convention": "dq_i wedge Res_i(Omega) = Omega",
    "wall_order": list(order),
    "walls": walls,
    "parallel_pairs": parallel,
    "corners": corners,
    "cech_incidence": incidence,
    "checks": checks,
    "passed": all(checks.values()),
    "scope": "These are source-normalized local residue and orientation maps. They do not determine which wall or corner periods are selected by the physical relative cycle.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
