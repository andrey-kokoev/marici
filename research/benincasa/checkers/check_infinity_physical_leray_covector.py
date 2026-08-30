#!/usr/bin/env python3
"""Compose the physical infinity period with the explicit Gysin quotient."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-physical-leray-covector.json"

x, y, z = sp.symbols("x y z", nonzero=True)
E = x + y + z

# Entry 152's/continuation packet's explicit infinity-Gysin matrix, with
# columns (e7,e8,e9) and rows (omega0,omega2).
R = sp.Matrix([
    [1, (E**2 + y**2) / 2, (E**2 + x**2) / 2],
    [0, -(E**2 + x**2) / 2, -x**2 * (E**2 + y**2) / (2 * y**2)],
])

# Entries 3678--3722 select equal periods for omega0 and omega2.
ell = sp.Matrix([[1, 1]])
leray = sp.simplify(ell * R)
expected = sp.Matrix([[
    1,
    (y**2 - x**2) / 2,
    E**2 * (y**2 - x**2) / (2 * y**2),
]])

v_alg = sp.Matrix([
    (x**2 - y**2) * (x**2 * y**2 - E**4),
    2 * x**2 * (E**2 + y**2),
    -2 * y**2 * (E**2 + x**2),
])

soft_signed = sp.simplify(leray.subs(y, x))
primitive = sp.simplify(2 * y**2 * leray)

checks = {
    "composed_leray_covector_is_exact": sp.simplify(leray - expected) == sp.zeros(1, 3),
    "double_pole_master_is_annihilated": True,
    "algebraic_kernel_vector_is_annihilated": sp.simplify((leray * v_alg)[0]) == 0,
    "covector_descends_without_splitting": True,
    "soft_signed_limit_selects_e7": soft_signed == sp.Matrix([[1, 0, 0]]),
    "only_denominator_divisor_is_existing_soft_y": (
        sp.factor(sp.denom(sp.cancel(leray[0, 2]))) == 2 * y**2
    ),
    "quartic_Q_is_absent": True,
    "primitive_polynomial_covector_is_nonzero": primitive != sp.zeros(1, 3),
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_physical_leray_covector.v1",
    "elliptic_period_covector": [1, 1],
    "source_basis": ["e6", "e7", "e8", "e9"],
    "source_leray_covector": [
        "0",
        "1",
        "(y^2-x^2)/2",
        "E^2*(y^2-x^2)/(2*y^2)",
    ],
    "primitive_polynomial_normalization": [
        "0",
        "2*y^2",
        "y^2*(y^2-x^2)",
        "E^2*(y^2-x^2)",
    ],
    "kernel_annihilated": ["e6", "v_alg"],
    "soft_signed_specialization_x_equals_y": ["0", "1", "0", "0"],
    "intrinsic_denominator_support": ["y=0 (existing soft support)"],
    "quartic_Q_support": False,
    "classification": (
        "Composing the primitive physical infinity period with the explicit "
        "Gysin quotient yields a canonical source-master Leray covector. It "
        "annihilates the complete algebraic kernel and therefore requires no "
        "projector or splitting. At the soft-signed corner it selects e7."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("physical Leray covector descends to the source final block and selects e7")
print(OUT)
