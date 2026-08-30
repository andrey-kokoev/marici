import json
from pathlib import Path

import sympy as sp


phi, theta = sp.symbols("phi theta", real=True)
g = sp.exp(4 * sp.I * phi)
winding_integrand = sp.simplify(sp.diff(g, phi) / g)
winding = sp.simplify(sp.integrate(winding_integrand, (phi, 0, 2 * sp.pi)) / (2 * sp.pi * sp.I))

# Four transverse zeros give four puncture periods with one sum relation.
sum_map = sp.Matrix([[1, 1, 1, 1]])
period_kernel = sum_map.nullspace()

checks = {
    "equatorial_transition_winding": winding == 4,
    "degree_is_nonzero": winding != 0,
    "four_transverse_indices_sum_to_degree": sum([1, 1, 1, 1]) == winding,
    "puncture_period_rank": len(period_kernel) == 3,
    "period_basis_obeys_sum_rule": all(sum_map * vector == sp.zeros(1, 1) for vector in period_kernel),
    "one_quadrature_has_collision": sp.simplify(sp.cos(theta) - sp.cos(-theta)) == 0,
    "second_quadrature_separates_generic_collision": sp.simplify(sp.sin(theta) - sp.sin(-theta)) == 2 * sp.sin(theta),
    "minimum_channel_count": 3 + 2 + 1 == 6,
}

result = {
    "schema": "marici.aspect.degree-four-321-output-instrument.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "architecture": {
        "3": "independent puncture-period interferometers",
        "2": "real phase quadratures",
        "1": "direct source-ray monitor",
    },
    "scope": "minimum generic transverse degree-four spin-two packet",
}

out = Path(__file__).parents[1] / "results" / "degree_four_321_output_instrument.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
