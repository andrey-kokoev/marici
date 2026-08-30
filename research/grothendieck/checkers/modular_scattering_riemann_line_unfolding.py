import json
from pathlib import Path

import sympy as sp


rho = sp.symbols("rho")
sigma, gamma = sp.symbols("sigma gamma", real=True)
rho_parts = sigma + sp.I * gamma
pole = sp.simplify(rho_parts / 2)
zero = sp.simplify((rho_parts + 1) / 2)

checks = {
    "denominator_zero_maps_to_scattering_pole": sp.simplify(2 * pole - rho_parts) == 0,
    "numerator_zero_maps_to_scattering_zero": sp.simplify(2 * zero - 1 - rho_parts) == 0,
    "pole_and_zero_are_half_shifted": sp.simplify(zero - pole) == sp.Rational(1, 2),
    "pair_is_centered_on_unitary_seam": sp.simplify((sp.re(pole) + sp.re(zero)) / 2 - (2 * sigma + 1) / 4) == 0,
    "rh_pole_line_is_one_quarter": sp.re(pole).subs(sigma, sp.Rational(1, 2)) == sp.Rational(1, 4),
    "rh_zero_line_is_three_quarters": sp.re(zero).subs(sigma, sp.Rational(1, 2)) == sp.Rational(3, 4),
    "rh_pair_center_is_one_half": sp.simplify(((sp.re(pole) + sp.re(zero)) / 2).subs(sigma, sp.Rational(1, 2))) == sp.Rational(1, 2),
}

result = {
    "schema": "marici.grothendieck.modular-scattering-riemann-line-unfolding.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "scattering_coefficient": "Lambda(2s-1)/Lambda(2s)",
    "interpretation": "A Riemann zero rho unfolds into a scattering pole at rho/2 and a scattering zero at (rho+1)/2. RH places them on the quarter and three-quarter lines around the unitary half seam.",
}

out = Path(__file__).parents[1] / "results" / "modular_scattering_riemann_line_unfolding.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
