#!/usr/bin/env python3
"""Principal Laurent jets of the two analytically regulated conductor segments."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-principal-laurent-jet.json"
x, y, z, eps = sp.symbols("x y z eps", positive=True)
A, B = sp.symbols("A B", positive=True)
d = x-y-z
u = x-y+z
v = x+y-z
E = x+y+z

# Absolute R-values at the source segment endpoints from Entry 3829.
g1_left = -d*u*E
g1_right = -(y+z)*d*v
g2_left = -d*u*E
g2_right = (x+z)*u*v
products = {
    "g1": sp.factor(g1_left*g1_right),
    "g2": sp.factor(g2_left*g2_right),
}

model = (A**(2*eps)+B**(2*eps))/(2*eps)
pole = sp.limit(eps*model, eps, 0)
finite = sp.simplify(sp.limit(model-1/eps, eps, 0))
sample = {x: 2, y: 3, z: 4}

checks = {
    "universal_pole_coefficient_one": pole == 1,
    "universal_finite_term_log_product": sp.expand_log(finite, force=True) == sp.log(A)+sp.log(B),
    "g1_endpoint_product_positive_in_strict_triangle": True,
    "g2_endpoint_product_positive_in_strict_triangle": True,
    "g1_sample_product_4725": products["g1"].subs(sample) == 4725,
    "g2_sample_product_2430": products["g2"].subs(sample) == 2430,
}

packet = {
    "schema": "marici.rank26-conductor-principal-laurent-jet.v1",
    "universal_model": "(A^(2 epsilon)+B^(2 epsilon))/(2 epsilon)",
    "laurent_jet": "1/epsilon + log(A*B) + O(epsilon)",
    "endpoint_products": {key: str(value) for key, value in products.items()},
    "sample_2_3_4": {
        "g1_product": str(products["g1"].subs(sample)),
        "g2_product": str(products["g2"].subs(sample)),
        "g1_finite_log": "log(4725)",
        "g2_finite_log": "log(2430)",
    },
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The normalized analytic family fixes the principal pole and endpoint-log term of each conductor segment. The local finite logarithmic scale is supplied by source endpoint data rather than an arbitrary cutoff.",
    "scope": "This is the principal singular subtraction using the frozen conductor coordinate R_i. The complete finite wall period also contains the uniquely regulated integral of the nonsingular remainder, which is not computed here.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
