#!/usr/bin/env python3
"""Derive principal-divisor witnesses for the marked infinity endpoint classes."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-relative-endpoint-torsion.json"

t, u = sp.symbols("t u", positive=True)
x, y, z = sp.symbols("x y z", positive=True)
h = x**2+y**2-z**2
F = x**2*t**4-h*t**2+y**2
Wplus = sp.sqrt(F)
Wminus = -sp.sqrt(F)
g = x*t**2-y

phi_plus = (Wplus-g)/t**2
phi_minus = (Wminus+g)/t**2

# Generic local leading coefficients.  Their nonvanishing excludes only the
# already known signed-energy/soft loci.
p0_plus_pole = sp.factor(sp.limit(t**2*phi_plus, t, 0, dir="+"))
p0_minus_pole = sp.factor(sp.limit(t**2*phi_minus, t, 0, dir="+"))
pinf_plus_zero = sp.factor(sp.limit(phi_plus.subs(t, 1/u)/u**2, u, 0, dir="+"))
pinf_minus_zero = sp.factor(sp.limit(phi_minus.subs(t, 1/u)/u**2, u, 0, dir="+"))

# Algebraic product identity, equivalent to the sum of the two principal
# divisor relations and the principal divisor of t.
phi_product_algebraic = sp.factor((F-g**2)/t**4)
expected_product = sp.factor((z**2-(x-y)**2)/t**2)

checks = {
    "p0_plus_has_order_two_pole": p0_plus_pole == 2*y,
    "p0_minus_has_order_two_pole": p0_minus_pole == -2*y,
    "pinf_plus_has_order_two_zero_generically": sp.factor(
        pinf_plus_zero-(z**2-(x-y)**2)/(2*x)
    ) == 0,
    "pinf_minus_has_order_two_zero_generically": sp.factor(
        pinf_minus_zero+(z**2-(x-y)**2)/(2*x)
    ) == 0,
    "product_identity": sp.factor(phi_product_algebraic-expected_product) == 0,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-relative-endpoint-torsion.v1",
    "curve": "W^2=x^2 t^4-(x^2+y^2-z^2)t^2+y^2",
    "witnesses": {
        "phi_plus": "(W-x t^2+y)/t^2",
        "phi_minus": "(-W+x t^2-y)/t^2 on the negative sheet",
    },
    "principal_divisors": {
        "phi_plus": "2 p_infinity_plus - 2 p_0_plus",
        "phi_minus": "2 p_infinity_minus - 2 p_0_minus",
        "t": "p_0_plus+p_0_minus-p_infinity_plus-p_infinity_minus",
        "phi_plus_over_phi_minus": (
            "2[(p_infinity_plus-p_0_plus)-(p_infinity_minus-p_0_minus)]"
        ),
    },
    "generic_nonzero_coefficients": {
        "p0_plus_pole": sp.sstr(p0_plus_pole),
        "p0_minus_pole": sp.sstr(p0_minus_pole),
        "pinf_plus_zero": sp.sstr(pinf_plus_zero),
        "pinf_minus_zero": sp.sstr(pinf_minus_zero),
    },
    "excluded_existing_support": "x*y*(z^2-(x-y)^2)=0",
    "physical_odd_endpoint_divisor_order": 2,
    "rational_de_rham_normal_function": "zero",
    "intrinsic_extension_block_class": "zero up to regular triangular gauge",
    "aspect_kernel_disposition": (
        "The four representative B coordinates are not intrinsic quotient "
        "directions on the generic locus; endpoint torsion kills their rational "
        "de Rham extension class."
    ),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("p0 coefficients", p0_plus_pole, p0_minus_pole)
print("pinf coefficients", pinf_plus_zero, pinf_minus_zero)
print("physical odd endpoint divisor is 2-torsion")
print(OUT)
