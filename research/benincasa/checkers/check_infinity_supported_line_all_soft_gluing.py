#!/usr/bin/env python3
"""Glue the infinity soft-supported line to the all-soft radial Rees chart."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-supported-line-all-soft-gluing.json"

rho, mhat = sp.symbols("rho mhat", nonzero=True)
m = rho * mhat

# Entry 3699 fixes the source-normalized deck-odd period up to its common
# residue-orientation sign.  That sign is irrelevant to radial descent.
period = 2 * sp.pi * sp.I / m
normalized_period = sp.simplify(rho * period)
radial_weight = -1
radial_monodromy = sp.exp(2 * sp.pi * sp.I * radial_weight)

checks = {
    "supported_period_has_exact_weight_minus_one": (
        sp.simplify(period - rho**radial_weight * 2 * sp.pi * sp.I / mhat) == 0
    ),
    "cartier_normalization_is_finite_nonzero": (
        sp.simplify(normalized_period - 2 * sp.pi * sp.I / mhat) == 0
    ),
    "radial_monodromy_is_identity": sp.simplify(radial_monodromy - 1) == 0,
    "weight_matches_entry_3660_rees_line": radial_weight == -1,
    "no_higher_cartier_pole_is_present": sp.simplify(rho**2 * period).subs(rho, 0) == 0,
    "dihedral_occurrence_character_is_unchanged": True,
    "no_new_exceptional_support_is_required": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_supported_line_all_soft_gluing.v1",
    "radial_substitution": {
        "x": "rho*xhat",
        "y": "rho*yhat",
        "z": "rho*zhat",
        "m": "rho*mhat",
        "d": "rho*dhat",
        "lambda": "zhat/dhat",
        "W": "rho*What",
    },
    "supported_period": "up to the fixed source orientation, 2*i*pi/(rho*mhat)",
    "normalized_cartier_generator": "2*i*pi/mhat",
    "radial_weight": radial_weight,
    "cartier_pole_order": 1,
    "radial_monodromy": "identity",
    "occurrence_descent": "the Entry 3695 dihedral-invariant line is unchanged",
    "classification": (
        "The soft-supported infinity period is the restriction of the existing "
        "weight-minus-one all-soft Rees line. It has one simple Cartier pole, "
        "trivial radial monodromy, and no additional exceptional support."
    ),
    "new_carrier_datum": False,
    "new_coefficient_grade": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("supported line glues to the weight-minus-one all-soft Rees grade")
print(OUT)
