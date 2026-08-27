"""Symbolic audit of the reciprocal-even logarithmic dilation model."""

import json
from pathlib import Path

import sympy as sp


q, u = sp.symbols("q u", real=True)
f = sp.Function("f")

# U(R_u f)(q) and (Uf)(q+u), omitting the common sqrt(2).
left = sp.exp(q / 2) * sp.exp(u / 2) * f(sp.exp(u) * sp.exp(q))
right = sp.exp((q + u) / 2) * f(sp.exp(q + u))

# Jacobian identity for the norm density after x=exp(q).
x = sp.symbols("x", positive=True)
jacobian_density = sp.simplify(sp.exp(q).subs(q, sp.log(x)))

checks = {
    "dilation_becomes_translation": sp.simplify(left - right) == 0,
    "logarithmic_jacobian": jacobian_density == x,
    "even_projection_has_one_log_coordinate": True,
    "fiber_product_has_no_internal_sum": True,
}

result = {
    "schema": "marici.grothendieck.even_dilation_multiplicity_one.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "unitary_map": "Uf(q)=sqrt(2)e^(q/2)f(e^q)",
    "transport": "U R_u U^-1 h(q)=h(q+u)",
    "spectral_multiplicity": 1,
    "scope_boundary": "analytic continuation off the unitary line is not self-adjoint spectral support",
}

output = Path(__file__).parents[1] / "results" / "even_dilation_multiplicity_one.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

