#!/usr/bin/env python3
"""Verify deck and reciprocal transitions of the principal endpoint splitter."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-principal-splitting-transition.json"

x, y, z, t, W = sp.symbols("x y z t W")
h = x**2 + y**2 - z**2
F = x**2 * t**4 - h * t**2 + y**2
g = x * t**2 - y
c = z**2 - (x - y) ** 2

f = (W - g) / t
f_deck = (-W - g) / t
f_reciprocal = (W + g) / t


def on_curve(expression):
    numerator = sp.together(expression).as_numer_denom()[0]
    return sp.factor(sp.rem(sp.Poly(numerator, W), sp.Poly(W**2 - F, W)).as_expr())


checks = {
    "curve_difference_is_existing_support_unit": sp.factor(F - g**2 - c * t**2) == 0,
    "deck_product_is_minus_c": on_curve(f * f_deck + c) == 0,
    "reciprocal_product_is_c": on_curve(f * f_reciprocal - c) == 0,
    "transition_support_is_signed_energy": sp.factor(c - (z - x + y) * (z + x - y)) == 0,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-principal-splitting-transition.v1",
    "curve": "W^2=x^2*t^4-(x^2+y^2-z^2)*t^2+y^2",
    "principal_splitter": "f=(W-x*t^2+y)/t",
    "existing_support_unit": "c=z^2-(x-y)^2",
    "deck_transition": "deck(f)=-c/f",
    "reciprocal_transition": "reciprocal(f)=c/f",
    "relative_fiber_consequence": (
        "dlog(f) transforms by sign; the additive dlog(c) term is pulled back "
        "from the base"
    ),
    "support_consequence": (
        "all transition failure is confined to the existing signed-energy "
        "divisor c=0"
    ),
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("deck(f)=-c/f; reciprocal(f)=c/f")
print(OUT)
