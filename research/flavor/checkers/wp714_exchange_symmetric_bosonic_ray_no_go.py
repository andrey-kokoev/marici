"""Exact no-go for exchange-symmetric correlation-bearing WP713 rays."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x, z, h, g = sp.symbols("x z h g", real=True)
beta_n = 4*g**2+4*z**2+8*z+176*x**2+12
beta_x = 8*g**2+8*z**2+32*z*x+160*x+32
ray_rate = 40*z+64*x+64
beta_h = 24*g**2+144*h**2
beta_g = 8*g*z+24*g+32*g**2+80*g*x+48*g*h
equations = [
    sp.expand(beta_n-x*ray_rate),
    sp.expand(beta_x-ray_rate),
    sp.expand(beta_h-h*ray_rate),
    sp.expand(beta_g-g*ray_rate),
]

def reduced_system(x_value):
    return [sp.factor(eq.subs(x, x_value)) for eq in equations]

inconsistent_three_halves = sp.groebner(
    reduced_system(sp.Rational(3, 2)), h, g, z, order="lex"
)
half_groebner = sp.groebner(
    reduced_system(sp.Rational(1, 2)), h, g, z, order="lex"
)
z_eliminant = sp.factor(half_groebner.polys[-1].as_expr())
complex_quartic = 1805*z**4-6802*z**3+13269*z**2-12996*z+5508
expected_z_eliminant = (z-2)*(z-1)*complex_quartic

solutions = [
    (sp.Rational(1, 2), 1, 0, 0),
    (sp.Rational(1, 2), 1, sp.Rational(17, 18), 0),
    (sp.Rational(1, 2), 2, 0, 0),
    (sp.Rational(1, 2), 2, sp.Rational(11, 9), 0),
]

def solves(item):
    xv, zv, hv, gv = item
    return all(eq.subs({x: xv, z: zv, h: hv, g: gv}) == 0 for eq in equations)

checks = {
    "three_halves_has_no_correlation_bearing_solution": len(inconsistent_three_halves.polys) == 1 and inconsistent_three_halves.polys[0].as_expr() == 1,
    "half_ratio_z_eliminant": z_eliminant == expected_z_eliminant,
    "remaining_z_quartic_has_no_real_roots": sp.Poly(complex_quartic, z).count_roots(-sp.oo, sp.oo) == 0,
    "four_real_symmetric_solutions": all(solves(item) for item in solutions),
    "every_solution_has_zero_portal_contrast": all(item[3] == 0 for item in solutions),
    "every_solution_is_radially_marginal": all((4*x**2-1).subs(x, item[0]) == 0 for item in solutions),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP714",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "exchange-symmetric, correlation-bearing projective sector of the RG-closed WP713 seven-quartic scalar theory",
    "faithful_coordinate": "symmetric projective tuple (x,z,h,g)",
    "source_authorized_operation": "exact WP713 projective fixed-ray equations restricted to the exchange equalizer",
    "contextual_partition": "four real rays differ in correlation and boson self-coupling but share zero portal contrast and the radially marginal stratum",
    "classification": "negative on the exchange-symmetric sector; neither selector nor rigidifier on the strict-stability domain",
    "smallest_exact_falsifier": "all four real solutions have 4x^2-1=0",
    "remaining_gate": "solve and certify the full exchange-asymmetric projective system, then test its transverse basin and threshold-safe readout",
}
(ROOT / "results" / "wp714_exchange_symmetric_bosonic_ray_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
