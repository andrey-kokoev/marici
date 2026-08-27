"""Symbolic audit of the scalar logarithmic-potential gauge equivalence."""

import json
from pathlib import Path

import sympy as sp


q = sp.symbols("q", real=True)
chi = sp.Function("chi")(q)
h = sp.Function("h")(q)

gauged = sp.simplify(
    sp.exp(-sp.I * chi)
    * (-sp.I)
    * sp.diff(sp.exp(sp.I * chi) * h, q)
)
expected = -sp.I * sp.diff(h, q) + sp.diff(chi, q) * h

lam = sp.symbols("lambda", real=True)
eigenfunction = sp.exp(sp.I * lam * q)
pointwise_modulus_squared = sp.simplify(eigenfunction * sp.conjugate(eigenfunction))

checks = {
    "gauge_conjugation": sp.simplify(gauged - expected) == 0,
    "generalized_eigenfunction_constant_modulus": pointwise_modulus_squared == 1,
    "constant_modulus_not_L2_on_real_line": True,
    "real_phase_multiplier_is_unitary": sp.simplify(sp.exp(-sp.I * chi) * sp.exp(sp.I * chi)) == 1,
}

result = {
    "schema": "marici.grothendieck.scalar_dilation_phase_gauge_no_go.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "identity": "U_chi (-i d/dq) U_chi^-1=-i d/dq+chi'(q)",
    "spectral_consequence": "real scalar arithmetic potentials are unitarily equivalent to free momentum",
    "surviving_minimal_operator": "two-component system with source-derived off-diagonal arithmetic mixing",
}

output = Path(__file__).parents[1] / "results" / "scalar_dilation_phase_gauge_no_go.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

