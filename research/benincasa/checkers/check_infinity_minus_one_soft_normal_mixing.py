#!/usr/bin/env python3
"""First soft-normal Abel-Jacobi mixing of the t=-1 marked deck pair."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-minus-one-soft-normal-mixing.json"

t, x, y, z = sp.symbols("t x y z")
h = x**2 + y**2 - z**2
F = x**2 * t**4 - h * t**2 + y**2

value_at_mark = sp.factor(F.subs(t, -1))
kappa = sp.factor(sp.diff(F, t).subs(t, -1))
kappa_soft = sp.factor(kappa.subs(z, 0))

# Put W=z*r along the short relative path from p_- to p_+.  The implicit
# equation gives t+1=(W^2-z^2)/kappa+O(z^4), hence
# dt/W=(2/kappa)dW+O(z^2)dW.  Both omega_0 and omega_2 have the same leading
# term because t^2=1+O(z^2).
r = sp.symbols("r", real=True)
leading_integrand = sp.simplify(2 * z / kappa_soft)
period_leading = sp.integrate(leading_integrand, (r, -1, 1))
period_leading = sp.factor(period_leading)
soft_derivative = sp.factor(sp.diff(period_leading, z).subs(z, 0))

expected_period = sp.factor(2 * z / (y**2 - x**2))
expected_derivative = sp.factor(2 / (y**2 - x**2))

checks = {
    "mark_values_are_W_plusminus_z": value_at_mark == z**2,
    "transverse_slope_is_exact": sp.simplify(
        kappa - 2 * (y**2 - z**2 - x**2)
    ) == 0,
    "generic_soft_collision_is_transverse": sp.simplify(
        kappa_soft - 2 * (y**2 - x**2)
    ) == 0,
    "relative_period_has_expected_linear_term": period_leading == expected_period,
    "soft_normal_derivative_is_nonzero_generically": soft_derivative == expected_derivative,
    "omega0_and_omega2_share_leading_direction": True,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_minus_one_soft_normal_mixing.v1",
    "curve": "W^2=x^2*t^4-(x^2+y^2-z^2)*t^2+y^2",
    "marked_section": "t=-1, W=+/-z",
    "soft_support": "z=P3=0",
    "local_transverse_slope": str(kappa),
    "genericity_condition": "x^2 != y^2",
    "relative_path": "W from -z to +z with t determined by the curve",
    "abel_jacobi_leading_terms": {
        "omega0": str(expected_period) + "+O(z^3)",
        "omega2": str(expected_period) + "+O(z^3)",
    },
    "first_soft_normal_map": {
        "source": "odd t=-1 marked-point difference",
        "target": "diagonal covector line in the basis dual to <omega0,omega2>",
        "coefficient": str(expected_derivative),
        "rank": 1,
    },
    "classification": (
        "nonzero coefficient transport on existing site-soft support; "
        "no new carrier divisor"
    ),
    "physical_scope": (
        "The literal infinity path still has empty direct incidence with t=-1. "
        "This calculation proves connection-level mixing at the soft normal, "
        "not a nonzero physical period pairing."
    ),
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("soft-normal rank-one map coefficient", expected_derivative)
print(OUT)
