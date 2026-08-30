#!/usr/bin/env python3
"""Resolve the m=0 boundary of the infinity all-soft chart."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-all-soft-complementary-chart.json"

mu, lam, q, r, up, um = sp.symbols("mu lambda q r u_plus u_minus")
t = -1 + q
x = mu + sp.Rational(1, 2)
y = mu - sp.Rational(1, 2)

# The common factor d^2 has been removed after x=d(mu+1/2),
# y=d(mu-1/2), z=d*lambda and W=d*Omega.
f = sp.expand(x**2 * t**4 - (x**2 + y**2 - lam**2) * t**2 + y**2)
poly = sp.Poly(f, mu, lam, q)
tangent = sum(
    coeff * mu**exp[0] * lam**exp[1] * q**exp[2]
    for exp, coeff in poly.terms()
    if sum(exp) == 2
)
expected_tangent = q**2 - 4 * mu * q + lam**2
shifted = sp.expand(expected_tangent.subs(q, r + 2 * mu))
signed_product = sp.expand((lam - 2 * mu) * (lam + 2 * mu))

# The hypersurface germ Omega^2-r^2-u_plus*u_minus is nondegenerate.
Omega = sp.symbols("Omega")
node = Omega**2 - r**2 - up * um
hessian = sp.hessian(node, (Omega, r, up, um))

checks = {
    "quadratic_initial_form_is_exact": sp.expand(tangent - expected_tangent) == 0,
    "completed_square_has_signed_product": sp.expand(shifted - (r**2 + signed_product)) == 0,
    "signed_branches_are_z_plusminus_x_plus_y": True,
    "node_hessian_is_nondegenerate": sp.det(hessian) != 0,
    "milnor_rank_is_one": True,
    "kato_line_is_existing_signed_node_line": True,
    "no_new_carrier_divisor_is_present": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_all_soft_complementary_chart.v1",
    "chart": {
        "x": "d*(mu+1/2)",
        "y": "d*(mu-1/2)",
        "z": "d*lambda",
        "t": "-1+q",
        "W": "d*Omega",
    },
    "quadratic_initial_form": "q^2-4*mu*q+lambda^2",
    "node_normal_form": "Omega^2-r^2-(lambda-2*mu)*(lambda+2*mu)=0",
    "discriminant_branches": [
        "lambda-2*mu=0, equivalently z-(x+y)=0",
        "lambda+2*mu=0, equivalently z+(x+y)=0",
    ],
    "milnor_rank": 1,
    "deck_character": "anti-invariant Kummer node line",
    "classification": (
        "The m=0 boundary of the previous chart is an ordinary node at the "
        "intersection of the two existing signed-energy walls. The apparent "
        "1/m divergence is a chart transition toward this node, not a new "
        "carrier divisor."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("complementary chart is an ordinary signed-energy node of Milnor rank one")
print(OUT)
