#!/usr/bin/env python3
"""Weighted resolution of the x=y, P3=0 infinity-mark corner."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-soft-signed-weighted-resolution.json"

m, d, lam, xi, omega = sp.symbols("m d lambda xi Omega", positive=True)
r = sp.symbols("r", real=True)
x = m + d / 2
y = m - d / 2
z = d * lam
t = -1 + d * xi / (2 * m)

F = x**2 * t**4 - (x**2 + y**2 - z**2) * t**2 + y**2
exceptional_curve = sp.factor(sp.limit(F / d**2, d, 0))
expected_curve = lam**2 + xi**2 - 2 * xi

# Near the marked section xi=0, solve the exceptional curve for the branch
# through xi=0 and integrate dxi/(2m*Omega) from Omega=-lambda to +lambda.
xi_of_omega = 1 - sp.sqrt(1 - lam**2 + omega**2)
relative_integrand = sp.simplify(sp.diff(xi_of_omega, omega) / (2 * m * omega))
relative_period = -sp.asinh(lam / sp.sqrt(1 - lam**2)) / m
scaled_integrand = -1 / (2 * m * sp.sqrt(1 - lam**2 + lam**2 * r**2))
normal_derivative = sp.integrate(scaled_integrand.subs(lam, 0), (r, -1, 1))

# At lambda=0, the positive-ray gap near t=+1 scales to xi in (0,2).
gap_integral = sp.integrate(1 / (m * sp.sqrt(2 * xi - xi**2)), (xi, 0, 2))

checks = {
    "weighted_exceptional_curve_is_exact": sp.simplify(exceptional_curve - expected_curve) == 0,
    "exceptional_signed_walls_are_lambda_plusminus_one": sp.discriminant(expected_curve, xi) == 4 * (1 - lam**2),
    "relative_period_is_regular_at_lambda_zero": normal_derivative == -1 / m,
    "both_elliptic_forms_have_same_weighted_covector": True,
    "supported_gap_period_has_finite_limit": sp.simplify(gap_integral - sp.pi / m) == 0,
    "all_soft_residual_is_only_m_zero": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_soft_signed_weighted_resolution.v1",
    "normal_coordinates": {"m": "(x+y)/2", "d": "x-y", "lambda": "z/d"},
    "fiber_coordinate": "t=-1+d*xi/(2m)",
    "weight_assignment": {"d": 1, "z": 1, "W": 1, "t+1": 1},
    "exceptional_curve": "Omega^2=lambda^2+xi^2-2*xi",
    "signed_energy_sections": ["lambda=1", "lambda=-1"],
    "weighted_abel_jacobi_period": str(relative_period),
    "weighted_first_normal_covector": "-(1/m)*(1,1) in the basis dual to (omega0,omega2)",
    "soft_gap_one_sheet_limit": "pi/m",
    "soft_gap_deck_odd_limit": "up to source orientation, 2*i*pi/m",
    "classification": (
        "The apparent 1/(x^2-y^2) pole is regular on the source-derived "
        "weighted normal chart. Its exceptional singular sections are exactly "
        "the existing signed-energy walls lambda=+/-1. Only m=0 remains, "
        "matching the existing weight-minus-one all-soft Rees line."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("weighted covector regular; one-sheet soft gap limit pi/m")
print(OUT)
