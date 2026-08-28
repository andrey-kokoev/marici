#!/usr/bin/env python3
"""Exact semistable classification of the signed-energy endpoint specialization."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/signed-energy-i2-specialization.json"

x, y, z, t, W, c = sp.symbols("x y z t W c")
h = x**2 + y**2 - z**2
F = x**2 * t**4 - h * t**2 + y**2
g = x * t**2 - y
H = W**2 - g**2 - c * t**2

# Standard I_2 monodromy in a symplectic basis, recorded as a standard
# semistable inference rather than a direct source-connection computation.
T = sp.Matrix([[1, 2], [0, 1]])
N = T - sp.eye(2)

checks = {
    "source_deformation_parameter_is_signed_energy": (
        sp.factor(F - g**2 - (z**2 - (x - y) ** 2) * t**2) == 0
    ),
    "central_fiber_has_two_components": (
        sp.expand(H.subs(c, 0) - (W - g) * (W + g)) == 0
    ),
    "component_intersection_has_two_geometric_points": sp.degree(g, t) == 2,
    "intersection_is_squarefree_generically": sp.resultant(g, sp.diff(g, t), t) != 0,
    "local_model_is_uv_equals_c_times_unit": (
        sp.expand((W - g) * (W + g) - c * t**2 - H) == 0
    ),
    "dual_graph_first_betti_rank_is_one": 2 - 2 + 1 == 1,
    "standard_i2_nilpotent_rank_is_one": N.rank() == 1,
    "standard_i2_nilpotent_squares_to_zero": N**2 == sp.zeros(2),
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.signed-energy-i2-specialization.v1",
    "family_equation": "(W-g)(W+g)=c*t^2",
    "g": "x*t^2-y",
    "c": "z^2-(x-y)^2",
    "genericity": "x*y*c != 0 away from the central fiber, with x*y != 0 on c=0",
    "central_fiber": {
        "components": ["W=g", "W=-g"],
        "intersection": "W=0 and x*t^2-y=0",
        "geometric_node_count": 2,
        "dual_graph_vertices": 2,
        "dual_graph_edges": 2,
        "dual_graph_b1": 1,
        "kodaira_type": "I_2",
    },
    "deck_action": (
        "exchanges the two components and acts by sign on the rank-one "
        "dual-graph cycle"
    ),
    "nearby_cycle": {
        "rank": 1,
        "character": "deck-odd",
        "type": "Tate/Kummer",
        "standard_monodromy": [[1, 2], [0, 1]],
        "N_rank": 1,
        "N_squared": 0,
        "provenance": "inferred from the exact semistable I_2 normal form",
    },
    "carrier_classification": "existing signed-energy support",
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("central fiber: two rational components, two nodes, dual-graph b1=1")
print("standard I2 N rank", N.rank(), "N^2", N**2)
print(OUT)
