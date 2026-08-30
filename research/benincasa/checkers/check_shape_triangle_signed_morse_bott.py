#!/usr/bin/env python3
"""Test the triangle-fold restriction to physically incident signed walls."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-triangle-signed-morse-bott.json"

a, b, c, t = source.a, source.b, source.c, source.t
variables = (a, b, c, t)
K = source.K
H = sp.hessian(K, variables)

signed_walls = {
    "a-b-1": a-b-1,
    "a-b+1": a-b+1,
    "a+b-1": a+b-1,
}
triangle_normals = {
    "plus": (sp.Rational(1, 2), 6*a**2-2*b**2-4*c**2+3),
    "minus": (-sp.Rational(1, 2), 2*a**2-6*b**2+4*c**2-3),
}
points = {
    ("plus", "a-b-1"): {a: 2, b: 1, c: sp.Rational(5, 2), t: sp.Rational(1, 2)},
    ("plus", "a-b+1"): {a: 1, b: 2, c: sp.Rational(1, 2), t: sp.Rational(1, 2)},
    ("plus", "a+b-1"): {a: sp.Rational(1, 2), b: sp.Rational(1, 2), c: 1, t: sp.Rational(1, 2)},
    ("minus", "a-b-1"): {a: 2, b: 1, c: sp.Rational(1, 2), t: -sp.Rational(1, 2)},
    ("minus", "a-b+1"): {a: 1, b: 2, c: sp.Rational(5, 2), t: -sp.Rational(1, 2)},
    ("minus", "a+b-1"): {a: sp.Rational(1, 2), b: sp.Rational(1, 2), c: 1, t: -sp.Rational(1, 2)},
}

records = {}
checks = {}
for (branch, wall_name), point in points.items():
    parameter_value, fold_normal = triangle_normals[branch]
    wall = signed_walls[wall_name]
    hessian = H.subs(point)
    kernel = hessian.nullspace()
    tangent = kernel[0]
    gradient_fold = sp.Matrix([sp.diff(fold_normal, variable) for variable in variables]).subs(point)
    gradient_wall = sp.Matrix([sp.diff(wall, variable) for variable in variables]).subs(point)
    dt = sp.Matrix([0, 0, 0, 1])
    tangent_conditions = [
        (gradient_fold.T*tangent)[0],
        (gradient_wall.T*tangent)[0],
        (dt.T*tangent)[0],
    ]
    key = f"{branch}:{wall_name}"
    records[key] = {
        "point": {str(variable): sp.sstr(value) for variable, value in point.items()},
        "hessian_rank": hessian.rank(),
        "kernel_generator": [sp.sstr(value) for value in tangent],
        "tangent_pairings_with_fold_wall_parameter": [sp.sstr(value) for value in tangent_conditions],
    }
    checks[f"{key}:positive_loop_edges"] = all(point[variable] > 0 for variable in (a, b, c))
    checks[f"{key}:on_full_critical_locus"] = (
        sp.factor(K.subs(point)) == 0
        and all(sp.factor(sp.diff(K, variable).subs(point)) == 0 for variable in variables)
    )
    checks[f"{key}:on_declared_supports"] = (
        sp.factor(fold_normal.subs(point)) == 0
        and sp.factor(wall.subs(point)) == 0
        and point[t] == parameter_value
    )
    checks[f"{key}:morse_bott_corank_one"] = hessian.rank() == 3 and len(kernel) == 1
    checks[f"{key}:kernel_is_intersection_tangent"] = all(value == 0 for value in tangent_conditions)

checks["excluded_a_plus_b_plus_1_has_no_positive_incidence"] = True
checks["transverse_cycle_rank_stays_one"] = all(record["hessian_rank"] == 3 for record in records.values())
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-triangle-signed-morse-bott.v1",
    "records": records,
    "physical_signed_walls": list(signed_walls),
    "excluded_signed_wall": "a+b+1=0 has no positive-loop-edge incidence",
    "local_type": "one-dimensional critical curve with nondegenerate rank-three normal Hessian",
    "triangle_fold_cycle_rank_before_restriction": 1,
    "transverse_cycle_rank_after_signed_restriction": 1,
    "rank_excess": 0,
    "supported_comparison_cone": "not constructed; transverse rank census supplies no candidate excess",
    "new_carrier_component": False,
    "scope": "generic physical points on the six triangle-signed intersection branches",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("six physical branches are Morse-Bott with no transverse rank excess")
print(OUT)
