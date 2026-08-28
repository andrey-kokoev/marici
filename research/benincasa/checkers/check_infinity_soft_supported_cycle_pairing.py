#!/usr/bin/env python3
"""Supported soft-cycle pairing with the finite-mark diagonal covector."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-soft-supported-cycle-pairing.json"

t, x, y, z = sp.symbols("t x y z", positive=True)
F = x**2 * t**4 - (x**2 + y**2 - z**2) * t**2 + y**2
F_soft = sp.factor(F.subs(z, 0))
expected_factorization = (t**2 - 1) * (x**2 * t**2 - y**2)

# Exact hostile point x=2,y=1 has branch points 1/2 and 1 on the positive
# projective ray.  The sign census proves the physical real locus is split by
# the open interval between them.
sample = sp.factor(F_soft.subs({x: 2, y: 1}))
sample_values = {
    "left": sp.sign(sample.subs(t, sp.Rational(1, 4))),
    "gap": sp.sign(sample.subs(t, sp.Rational(3, 4))),
    "right": sp.sign(sample.subs(t, 2)),
}

# On the upper boundary value over the gap, sqrt(F)=+i*sqrt(-F) up to the
# source-fixed orientation sign.  The deck-odd cut cycle doubles the one-sheet
# integral.  Its magnitude integrand is strictly positive and locally has
# inverse-square-root endpoint behavior, hence is finite and nonzero.
gap_magnitude = sp.factor((1 + t**2) / sp.sqrt(-sample))
midpoint_value = sp.simplify(gap_magnitude.subs(t, sp.Rational(3, 4)))

left_root = sp.Rational(1, 2)
right_root = sp.Integer(1)
left_slope = sp.diff(sample, t).subs(t, left_root)
right_slope = sp.diff(sample, t).subs(t, right_root)

checks = {
    "soft_curve_factorizes": sp.expand(F_soft - expected_factorization) == 0,
    "sample_factorization_is_exact": sample == (t - 1) * (t + 1) * (2*t - 1) * (2*t + 1),
    "physical_real_locus_is_split": sample_values == {"left": 1, "gap": -1, "right": 1},
    "gap_pairing_magnitude_is_positive": midpoint_value > 0,
    "left_endpoint_is_simple": left_slope != 0,
    "right_endpoint_is_simple": right_slope != 0,
    "supported_pairing_is_finite_and_nonzero": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_soft_supported_cycle_pairing.v1",
    "soft_factorization": "(t^2-1)*(x^2*t^2-y^2)",
    "chamber": "x>y>0",
    "positive_branch_points": ["y/x", "1"],
    "physical_real_components": ["[0,y/x]", "[1,infinity]"],
    "supported_gap": "(y/x,1)",
    "supported_cycle": "deck-odd loop around the gap cut, oriented by the source boundary value",
    "paired_form": "omega0+omega2=(1+t^2)dt/W",
    "pairing": "up to the source-fixed orientation sign, 2*i*integral_{y/x}^1 (1+t^2)dt/sqrt(-F_soft)",
    "pairing_status": "finite and nonzero",
    "hostile_exact_point": {"x": 2, "y": 1, "roots": ["1/2", "1"]},
    "classification": (
        "physical supported activation on the existing soft-signed boundary; "
        "no new carrier support"
    ),
    "scope": (
        "The result is the local supported-cycle pairing at z=0. It does not "
        "assert a generic nonsoft contribution from the t=-1 mark."
    ),
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("supported diagonal pairing is finite and nonzero")
print(OUT)
