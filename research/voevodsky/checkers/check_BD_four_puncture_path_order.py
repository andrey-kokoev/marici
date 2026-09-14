#!/usr/bin/env python3
"""Exact chamber order of the BD path through four energy punctures."""
import json
from pathlib import Path
from fractions import Fraction as F

R = Path(__file__).resolve().parents[3]

def classify(x, y, z):
    E = x + y + z
    crit = [(F(0), "0"), (2*x, "2x"), (2*y, "2y"), (2*(x+y), "2(x+y)")]
    left = [label for value, label in sorted(crit, reverse=True) if value < E]
    right = [label for value, label in sorted(crit) if value > E]
    return E, left, right

# Two samples in the strict triangle chamber, one for each middle ordering.
E1, left1, right1 = classify(F(3), F(5), F(4))
E2, left2, right2 = classify(F(5), F(3), F(4))
checks = {
    "x_less_y_triangle_order": left1 == ["2y", "2x", "0"],
    "x_greater_y_triangle_order": left2 == ["2x", "2y", "0"],
    "top_puncture_right_first_sample": right1 == ["2(x+y)"],
    "top_puncture_right_second_sample": right2 == ["2(x+y)"],
    "basepoint_values_equal": E1 == E2 == 12,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.BD-four-puncture-path-order.v1",
    "passed": True,
    "triangle_chamber": "max(2x,2y) < E_phys < 2(x+y)",
    "lower_half_plane_routes": {
        "x<y": ["E_phys", "below 2y", "below 2x", "0"],
        "y<x": ["E_phys", "below 2x", "below 2y", "0"],
    },
    "top_vertex": "2(x+y) remains to the right of E_phys",
    "retained_data": ["middle-puncture order", "lower detour signs", "terminal BD collision orientation"],
    "missing_map": "ordered root braid -> integral Picard-Lefschetz action",
    "checks": checks,
}
p = R / "research/voevodsky/results/BD_four_puncture_path_order.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "x<y_route": out["lower_half_plane_routes"]["x<y"], "missing": out["missing_map"]}))
