#!/usr/bin/env python3
"""Exact primitive middle-route difference for the four-cusp square."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
mon = json.loads((R / "research/benincasa/two-wall-conductor-monodromy.json").read_text())

def matrix(columns):
    return sp.Matrix.hstack(*[sp.Matrix(c) for c in columns])

T1 = matrix(mon["root_swap_1"]["matrix_columns_in_basis"])
T2 = matrix(mon["root_swap_2"]["matrix_columns_in_basis"])
splus = sp.Matrix([1, 1, 0])
sminus = sp.Matrix([1, -1, 0])
numerator = T2 * splus - T1 * splus
middle = numerator / 2
checks = {
    "wall_transports_commute": T1 * T2 == T2 * T1,
    "upper_path_equalizer_zero": T2 * T1 * splus - T1 * T2 * splus == sp.zeros(3, 1),
    "middle_numerator_twice_odd": numerator == 2 * sminus,
    "half_difference_integral": all(v.q == 1 for v in middle),
    "half_difference_is_primitive_odd": middle == sminus and sp.gcd(*map(abs, middle)) == 1,
    "middle_sum_zero": T2 * splus + T1 * splus == sp.zeros(3, 1),
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.four-cusp-middle-route-difference.v1",
    "passed": True,
    "critical_vertices": ["0", "2x", "2y", "2(x+y)"],
    "source_state": [1, 1, 0],
    "middle_route_values": {
        "via_2x": [int(v) for v in T1 * splus],
        "via_2y": [int(v) for v in T2 * splus],
    },
    "primitive_half_difference": [int(v) for v in middle],
    "apex_path_difference": [int(v) for v in T2 * T1 * splus - T1 * T2 * splus],
    "interpretation": "the odd detector is retained by the normalized relative middle edge and erased by endpoint equalization",
    "remaining": "construct the same half-difference in the physical relative-period/readout complex with integral normalization",
    "checks": checks,
}
p = R / "research/voevodsky/results/four_cusp_middle_route_difference.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "middle_half_difference": out["primitive_half_difference"], "apex_difference": out["apex_path_difference"]}))
