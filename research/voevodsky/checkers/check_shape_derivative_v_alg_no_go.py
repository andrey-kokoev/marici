#!/usr/bin/env python3
"""Exact no-go for recovering v_alg by differentiating its canonical cancellation."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
x, y, t = sp.symbols("x y t", nonzero=True)
c = 1 / (4 * x**3 * y**3 * (x + y))
c101, c110 = -c, c
shape_sum = sp.factor((c101 + c110).subs({x: x + t, y: y - t}, simultaneous=True))
derivatives = [sp.simplify(sp.diff(shape_sum, t, n).subs(t, 0)) for n in range(7)]
N = sp.diag(1, -1)
even = sp.Matrix([1, 1])
odd = sp.Matrix([1, -1])
checks = {
    "canonical_v_alg_identity_zero": sp.simplify(c101 + c110) == 0,
    "shape_path_identity_zero": shape_sum == 0,
    "derivatives_zero_through_six": derivatives == [0] * 7,
    "simple_even_to_doubled_odd": N * even == odd,
    "simple_odd_to_doubled_even": N * odd == even,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.shape-derivative-v-alg-no-go.v1",
    "passed": True,
    "canonical_v_alg_projection": "0 identically",
    "shape_path": ["x+t", "y-t"],
    "checked_derivative_orders": list(range(7)),
    "all_checked_derivatives_zero": True,
    "all_order_reason": "the shape-pulled projection is the zero rational function",
    "parity": {"simple_even": "doubled_odd", "simple_odd": "doubled_even"},
    "disposition": "the primitive doubled odd response cannot be retyped as the simple odd v_alg detector",
    "remaining": "source an antisymmetric simple mixed observable or derive an independent doubled-pole-to-v_alg readout",
    "checks": checks,
}
p = R / "research/voevodsky/results/shape_derivative_v_alg_no_go.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "v_alg_shape_derivatives": "all zero", "shape_response_is_scalar_v_alg_detector": False}))
