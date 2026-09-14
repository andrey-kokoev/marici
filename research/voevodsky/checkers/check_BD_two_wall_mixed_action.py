#!/usr/bin/env python3
"""Compare the same-sense BD two-node loop with individual wall swaps."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
mon = json.loads((R / "research/benincasa/two-wall-conductor-monodromy.json").read_text())
bd = json.loads((R / "research/voevodsky/results/BD_quartic_collision_arcs.json").read_text())

def matrix(columns):
    return sp.Matrix.hstack(*[sp.Matrix(c) for c in columns])

T1 = matrix(mon["root_swap_1"]["matrix_columns_in_basis"])
T2 = matrix(mon["root_swap_2"]["matrix_columns_in_basis"])
Tbd = T1 * T2
splus = sp.Matrix([1, 1, 0])
sminus = sp.Matrix([1, -1, 0])
checks = {
    "BD_same_relative_orientation": "same-sense half-twist" in bd["Hurwitz_consequence"],
    "wall_swaps_commute": T1 * T2 == T2 * T1,
    "single_second_swap_reaches_odd": T2 * splus == sminus,
    "single_first_swap_reaches_opposite_odd": T1 * splus == -sminus,
    "BD_product_preserves_symmetric_line": Tbd * splus == -splus,
    "BD_product_does_not_reach_odd": Tbd * splus not in (sminus, -sminus),
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.BD-two-wall-mixed-action.v1",
    "passed": True,
    "BD_local_input": "same-sense half-twist at both nodes",
    "BD_monodromy": "T1*T2",
    "canonical_mixed_input": [1, 1, 0],
    "BD_output": [int(v) for v in Tbd * splus],
    "single_wall_outputs": {
        "T1": [int(v) for v in T1 * splus],
        "T2": [int(v) for v in T2 * splus],
    },
    "v_alg_consequence": "BD preserves the symmetric mixed line, so its opposite v_alg coefficients still cancel",
    "missing_physical_input": "a source-derived based path selecting one labelled discriminant wall with orientation and readout authority",
    "checks": checks,
}
p = R / "research/voevodsky/results/BD_two_wall_mixed_action.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "BD_output": out["BD_output"], "antisymmetric_reached": False}))
