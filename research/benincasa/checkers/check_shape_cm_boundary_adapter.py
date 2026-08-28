#!/usr/bin/env python3
"""Test the physical Cayley-Menger boundary adapter for shape transport."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-cm-boundary-adapter.json"

a, b, c = source.a, source.b, source.c
point = {
    a: sp.Rational(5, 3),
    b: sp.Rational(7, 3),
    c: sp.Rational(8, 3),
}

K0 = source.K0
K1 = source.K1
gradient = sp.Matrix([sp.diff(K0, variable) for variable in (a, b, c)])
K0_value = sp.factor(K0.subs(point))
K1_value = sp.factor(K1.subs(point))
gradient_value = sp.simplify(gradient.subs(point))

# In the source fiber chart, a and b remain coordinates and the moving
# boundary is solved as c=c(t).  Implicit differentiation of K(t)=0 gives
# c'(0)=-K1/K_c.
Kc_value = sp.diff(K0, c).subs(point)
boundary_velocity = sp.factor(-K1_value / Kc_value)

# V is the vertical lift of that boundary motion.  The fixed-fiber
# derivative of K^(-1/2) has numerator -K1/2, while V contributes
# -V(K0)/2.  Their sum vanishes because K1+V(K0)=0.
V_K0 = sp.factor(boundary_velocity * Kc_value)
fixed_fiber_residue = sp.factor(-K1_value / 2)
boundary_adapter_residue = sp.factor(-V_K0 / 2)
total_residue = sp.factor(fixed_fiber_residue + boundary_adapter_residue)

checks = {
    "point_is_in_nonnegative_source_chamber": all(value >= 0 for value in point.values()),
    "point_lies_on_cayley_menger_boundary": K0_value == 0,
    "boundary_is_smooth_at_point": gradient_value != sp.zeros(3, 1),
    "shape_normal_symbol_is_nonzero": K1_value != 0,
    "c_is_valid_boundary_graph_coordinate": Kc_value != 0,
    "source_boundary_velocity_is_minus_one": boundary_velocity == -1,
    "vertical_lift_cancels_shape_normal_symbol": sp.factor(K1_value + V_K0) == 0,
    "fixed_fiber_residue_is_nonzero": fixed_fiber_residue == -sp.Rational(40, 3),
    "boundary_adapter_residue_is_nonzero": boundary_adapter_residue == sp.Rational(40, 3),
    "total_transported_residue_vanishes": total_residue == 0,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-cm-boundary-adapter.v1",
    "physical_boundary_point": {str(variable): str(value) for variable, value in point.items()},
    "K0_value": str(K0_value),
    "K1_value": str(K1_value),
    "gradient_K0": [str(value) for value in gradient_value],
    "boundary_graph": "hold a,b fixed and solve K(t,a,b,c(t))=0",
    "boundary_velocity_c_prime": str(boundary_velocity),
    "fixed_fiber_shape_residue": str(fixed_fiber_residue),
    "source_boundary_adapter_residue": str(boundary_adapter_residue),
    "transported_total_residue": str(total_residue),
    "classification": {
        "fixed_fiber_operation": "fails_regular_extension",
        "supported_adapter": "nonzero_and_source_derived",
        "total_source_transport": "regular_at_test_point",
    },
    "scope": "one smooth rational point of the physical Cayley-Menger boundary; local normal comparison only",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("fixed residue", fixed_fiber_residue, "adapter", boundary_adapter_residue, "total", total_residue)
print(OUT)
