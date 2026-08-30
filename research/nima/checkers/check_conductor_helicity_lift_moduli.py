#!/usr/bin/env python3
"""Solve the equivariant lift from a branch doublet to graviton helicities."""

import json
import sympy as sp
from pathlib import Path


a, b, c, d = sp.symbols("a b c d")
M = sp.Matrix([[a, b], [c, d]])
P = sp.Matrix([[0, 1], [1, 0]])
h = sp.diag(1, -1)

parity_equations = list(M * P - P * M)
parity_solution = sp.solve(parity_equations, [a, b, c, d], dict=True)
assert parity_solution == [{a: d, b: c}]

# Substitute M=[[a,b],[b,a]], then require the same little-group grading.
M_parity = sp.Matrix([[a, b], [b, a]])
helicity_equations = list(M_parity * h - h * M_parity)
helicity_solution = sp.solve(helicity_equations, [b], dict=True)
assert helicity_solution == [{b: 0}]

result = {
    "status": "PASS",
    "parity_equivariant_family": "[[a,b],[b,a]]",
    "parity_family_dimension": 2,
    "determinant": str(sp.factor(M_parity.det())),
    "with_little_group_intertwining": "[[a,0],[0,a]]",
    "remaining_dimension": 1,
    "primitive_integral_maps": ["+I", "-I"],
    "conclusion": "parity alone does not define the branch-to-helicity lift; a source-derived little-group grading removes the mixing modulus",
}

out = Path(__file__).resolve().parents[1] / "results" / "conductor_helicity_lift_moduli.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
