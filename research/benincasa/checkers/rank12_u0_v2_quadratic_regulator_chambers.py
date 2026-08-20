#!/usr/bin/env python3
"""Exact regulator-cone pullback of the exceptional quadratic collision."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/benincasa/results/rank12-u0-v2-quadratic-regulator-chambers.json"
e1, e2, e3 = sp.symbols("epsilon_1 epsilon_2 epsilon_3", positive=True)
r2 = sp.sqrt(2)

# At X=(1,0,-1), use u=E/X1 and v=(X1+X2-X3)/X1.  Independent
# source regulators Xi -> Xi-i epsilon_i give this first projective tangent.
slope = sp.cancel((-e1 + e2 - e3) / (e1 + e2 + e3))
root_near = -3 + 2 * r2
root_far = -3 - 2 * r2

assert sp.simplify(
    (slope - root_near) * (e1 + e2 + e3)
    - 2 * (r2 - 1) * (r2 * e2 - e1 - e3)
) == 0

# The positive cone maps into (-1,1), so only the near root is reachable.
assert root_near > -1 and root_near < 1
assert root_far < -1

witnesses = {
    "below": {e1: 1, e2: 1, e3: 1},
    "above": {e1: 1, e2: 2, e3: 1},
    "wall": {e1: 1, e2: r2, e3: 1},
}
evaluated = {name: sp.simplify(slope.subs(values)) for name, values in witnesses.items()}
assert evaluated["below"] < root_near
assert evaluated["above"] > root_near
assert sp.simplify(evaluated["wall"] - root_near) == 0

result = {
    "schema": "marici.benincasa.rank12_u0_v2_quadratic_regulator_chambers.v1",
    "status": "passed",
    "center": {"X1": "1", "X2": "0", "X3": "-1", "u": "0", "v": "2"},
    "regulator_convention": "Xi -> Xi - i*epsilon_i with epsilon_i>0 independently",
    "exceptional_slope": str(slope),
    "quadratic_roots": [str(root_near), str(root_far)],
    "reachable_root": str(root_near),
    "unreachable_root": str(root_far),
    "pulled_back_collision_wall": "sqrt(2)*epsilon_2 = epsilon_1 + epsilon_3",
    "factor_identity": str(
        sp.Eq(
            (slope - root_near) * (e1 + e2 + e3),
            2 * (r2 - 1) * (r2 * e2 - e1 - e3),
        )
    ),
    "positive_cone_witnesses": {
        name: {
            "epsilon": [str(values[e1]), str(values[e2]), str(values[e3])],
            "s": str(evaluated[name]),
        }
        for name, values in witnesses.items()
    },
    "conclusion": "The independent-positive regulator cone meets both chambers separated by the reachable quadratic collision. The frozen sign prescription does not select a Kummer sheet or a crossing class.",
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
