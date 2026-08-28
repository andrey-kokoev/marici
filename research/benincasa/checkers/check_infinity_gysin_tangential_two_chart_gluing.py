#!/usr/bin/env python3
"""Verify reciprocal-chart gluing of the tangential finite-part covector."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-gysin-tangential-two-chart-gluing.json"

s = sp.symbols("s", positive=True)
x, y, z = sp.symbols("x y z", positive=True)
h = x**2+y**2-z**2

# Reciprocal chart after t=1/s and x<->y.
F_swap = y**2*s**4-h*s**2+x**2
W = sp.sqrt(F_swap)
omega2_swap = s**2/W
reciprocal_form = 1/(s**2*W)
primitive = W/s

# Exact de Rham reduction:
# x^2 ds/(s^2 W) = y^2 s^2 ds/W - d(W/s).
reduction_residual = sp.factor(
    x**2*reciprocal_form-y**2*omega2_swap+sp.diff(primitive, s)
)

# Endpoint finite parts of the exact primitive have no constant remainder.
zero_endpoint_remainder = sp.limit(primitive-x/s, s, 0, dir="+")
infinity_endpoint_remainder = sp.limit(primitive-y*s, s, sp.oo)

# The holomorphic basis form is invariant under reciprocal transport after
# orientation reversal of the path.
F_original_under_inverse = sp.factor(
    (1/s**4)
    * (x**2-h*s**2+y**2*s**4)
)
direct_inverse_relation = sp.factor(
    F_original_under_inverse-F_swap/s**4
)

transition = sp.diag(1, y**2/x**2)
reverse_transition = sp.diag(1, x**2/y**2)

checks = {
    "exact_reduction_identity": reduction_residual == 0,
    "zero_endpoint_has_no_finite_remainder": zero_endpoint_remainder == 0,
    "infinity_endpoint_has_no_finite_remainder": infinity_endpoint_remainder == 0,
    "quartic_reciprocal_identity": direct_inverse_relation == 0,
    "transition_is_invertible": sp.factor(transition.det()) != 0,
    "reciprocal_composition_is_identity": sp.simplify(
        transition*reverse_transition
    ) == sp.eye(2),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-gysin-tangential-two-chart-gluing.v1",
    "direct_chart": "t=a/b",
    "reciprocal_chart": "s=b/a=1/t",
    "source_exchange": "x<->y",
    "exact_form_identity": (
        "x^2 ds/(s^2 W_swap) = y^2 s^2 ds/W_swap - d(W_swap/s)"
    ),
    "endpoint_finite_remainders": {
        "s=0": sp.sstr(zero_endpoint_remainder),
        "s=infinity": sp.sstr(infinity_endpoint_remainder),
    },
    "finite_part_transition_basis_J0_J2": [
        [sp.sstr(value) for value in row] for row in transition.tolist()
    ],
    "transition_formula": {
        "J0_xy": "J0_yx",
        "J2_xy": "(y^2/x^2) J2_yx",
    },
    "additive_elliptic_period": "0",
    "cocycle_composition": "identity",
    "result": (
        "The source-normalized finite-part covector glues multiplicatively "
        "between reciprocal projective charts, with no arbitrary additive period."
    ),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("transition", transition)
print("additive period 0")
print(OUT)
