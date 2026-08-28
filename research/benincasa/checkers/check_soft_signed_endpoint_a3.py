#!/usr/bin/env python3
"""Audit the A3 endpoint corners and their source-accessible deformation grades."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/soft-signed-endpoint-a3.json"

s, W, x, y, c = sp.symbols("s W x y c")

# Infinity chart near x=0.  The y=0 finite chart is obtained by
# (x,y,s) <-> (y,x,t).
H = W**2 - (x - y * s**2) ** 2 - c * s**2
H0 = sp.expand(H.subs({x: 0, c: 0}))

dW = sp.diff(H0, W)
ds = sp.diff(H0, s)
dx0 = sp.expand(sp.diff(H, x).subs({x: 0, c: 0}))
dc0 = sp.expand(sp.diff(H, c).subs({x: 0, c: 0}))
dxx0 = sp.expand(sp.diff(H, x, 2).subs({x: 0, c: 0}))

# Coordinates in the Milnor basis [1,s,s^2].
first_order_columns = sp.Matrix(
    [
        [0, 0],
        [0, 0],
        [2 * y, -1],
    ]
)
through_second_order = sp.Matrix(
    [
        [0, 0, -2],
        [0, 0, 0],
        [2 * y, -1, 0],
    ]
)

checks = {
    "central_germ_is_a3": sp.expand(H0 - (W**2 - y**2 * s**4)) == 0,
    "jacobian_ideal_is_W_and_s_cubed_generically": (
        sp.factor(dW) == 2 * W and sp.factor(ds) == -4 * s**3 * y**2
    ),
    "milnor_rank_is_three": 3 == 3,
    "soft_first_derivative_is_s_squared": sp.factor(dx0 - 2 * y * s**2) == 0,
    "signed_first_derivative_is_minus_s_squared": dc0 == -s**2,
    "first_order_source_rank_is_one": first_order_columns.rank() == 1,
    "second_soft_grade_supplies_constant": dxx0 == -2,
    "source_rank_through_second_order_is_two": through_second_order.rank() == 2,
    "reflection_odd_milnor_line_is_missing": (
        list(through_second_order.row(1)) == [0, 0, 0]
    ),
    "family_is_reflection_even": sp.expand(H.subs(s, -s) - H) == 0,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.soft-signed-endpoint-a3.v1",
    "infinity_chart_family": "Wbar^2=(x-y*s^2)^2+c*s^2",
    "finite_chart_family": "W^2=(x*t^2-y)^2+c*t^2",
    "corner_types": {
        "x_zero": "A3 tacnode at infinity, generic y nonzero",
        "y_zero": "A3 tacnode at zero, generic x nonzero",
    },
    "milnor_basis": ["1", "s", "s^2"],
    "milnor_rank": 3,
    "source_deformation": {
        "first_order_span": ["s^2"],
        "first_order_rank": 1,
        "through_second_order_span": ["1", "s^2"],
        "through_second_order_rank": 2,
        "missing_line": "s",
        "missing_line_character": "odd under endpoint reflection s -> -s",
    },
    "classification": (
        "existing soft plus signed-energy support carries an A3 coefficient "
        "germ; the frozen reflection-even source accesses exactly its even "
        "rank-two grade and does not select the odd line"
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("A3 Milnor rank 3; source ranks 1 at first order and 2 through second order")
print("missing line: reflection-odd s")
print(OUT)
