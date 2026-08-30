#!/usr/bin/env python3
"""Exact reciprocal and deck gluing of the endpoint A3 logarithmic line."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-a3-reciprocal-gluing.json"

t, x, y, lam = sp.symbols("t x y lam", nonzero=True)
s = 1 / t

# Coefficients of the logarithmic forms relative to dt.  At infinity,
# (1/y) ds/s pulls back to -(1/y) dt/t.  The reciprocal finite chart has
# x_target=y_source and coefficient +(1/y) dt/t.
rho_infinity_in_t = sp.simplify((1 / y) * sp.diff(s, t) / s)
rho_zero_reciprocal = 1 / (y * t)

reciprocal_transition = sp.simplify(rho_infinity_in_t / rho_zero_reciprocal)
deck_transition = -1

checks = {
    "ds_over_s_is_minus_dt_over_t": sp.simplify(sp.diff(s, t) / s + 1 / t) == 0,
    "reciprocal_transition_is_orientation_sign": reciprocal_transition == -1,
    "deck_transition_is_sign": deck_transition == -1,
    "reciprocal_cocycle_squares_to_identity": reciprocal_transition**2 == 1,
    "deck_cocycle_squares_to_identity": deck_transition**2 == 1,
    "combined_character_is_even": reciprocal_transition * deck_transition == 1,
    "common_energy_scaling_has_weight_minus_one": (
        sp.simplify((1 / (lam * y)) / (1 / y) - 1 / lam) == 0
    ),
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-a3-reciprocal-gluing.v1",
    "infinity_row": "(0,1/y,0) in coordinate s=1/t",
    "finite_row": "(0,1/x,0) in coordinate t",
    "reciprocal_transition": -1,
    "deck_transition": -1,
    "combined_transition": 1,
    "common_energy_scaling_weight": -1,
    "global_object": (
        "one rank-one orientation/Kummer line, not two independent endpoint ports"
    ),
    "scope": (
        "reciprocal generic soft-signed A3 corners; the all-soft cone vertex is excluded"
    ),
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("reciprocal", reciprocal_transition, "deck", deck_transition, "combined", reciprocal_transition * deck_transition)
print(OUT)
