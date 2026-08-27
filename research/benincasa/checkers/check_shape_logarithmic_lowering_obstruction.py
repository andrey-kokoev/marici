#!/usr/bin/env python3
"""Prove the local obstruction to a regular physical pole-lowering vector."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-logarithmic-lowering-obstruction.json"

x, y, z = sp.symbols("x y z")
variables = (x, y, z)
Q = (9*x**2 - 30*x*y + 6*x*z + 9*y**2 + 6*y*z + z**2) / 4
H = sp.hessian(Q, variables)
v1, v2, v3 = sp.symbols("v1 v2 v3")
v0 = sp.Matrix([v1, v2, v3])

# If V(K) belongs to (K) and ord_0(K)=2, its linear term must vanish.
# For K=Q+O(3), that linear term is (H*v0).(x,y,z).
linear_condition = H * v0
solution = sp.linsolve(list(linear_condition), (v1, v2, v3))

walls = {"g1_local": x, "g2_local": y, "s12_local": z}
records = {}
checks = {
    "quadratic_form_is_nondegenerate": H.det() == -72,
    "logarithmic_condition_forces_zero_constant_vector": solution == {(0, 0, 0)},
}
for label, wall in walls.items():
    gradient = sp.Matrix([sp.diff(wall, variable) for variable in variables])
    forced_normal_value = (gradient.dot(sp.zeros(3, 1)))
    records[label] = {
        "required_for_lowering": "V(wall)(0)=1",
        "forced_by_logarithmic_tangency": sp.sstr(forced_normal_value),
        "compatible": False,
    }
    checks[f"{label}_normalization_conflicts_with_log_tangency"] = forced_normal_value != 1

assert all(checks.values()), checks
packet = {
    "schema": "marici.shape-logarithmic-lowering-obstruction.v1",
    "local_branch_type": "A1",
    "hessian_determinant": sp.sstr(H.det()),
    "regular_logarithmic_vector_constant_term": [0, 0, 0],
    "wall_records": records,
    "all_checks_pass": True,
    "conclusion": "no regular vector field can both lower an incident wall pole and remain logarithmic along K0 at the A1 point",
    "singular_vector_field_completion_tested": False,
    "supported_correction_constructed": False,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("logarithmic constant-vector solution:", solution)
print(OUT)
