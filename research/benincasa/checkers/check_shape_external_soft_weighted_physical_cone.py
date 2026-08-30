#!/usr/bin/env python3
"""Compute the source-derived weighted physical cone near P2=0 A3 points."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-weighted-physical-cone.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K
u, r, z = sp.symbols("u r z")

substitution = {
    t: 1-u,
    a: u*(r+z/2),
    c: u*(r-z/2),
}

records = {}
checks = {}
for b0 in (1, 2):
    pulled = sp.factor(K.subs(substitution).subs(b, b0))
    poly_u = sp.Poly(sp.expand(pulled), u)
    minimum_order = min(monomial[0] for monomial, coefficient in poly_u.terms())
    exceptional = sp.factor(sp.expand(pulled).coeff(u, minimum_order))
    gradient = [sp.factor(sp.diff(exceptional, variable)) for variable in (r, z)]
    rho, eta = sp.symbols("rho eta", nonnegative=True)
    endpoint_substitution = (
        {r: sp.Rational(1, 2)+rho, z: -1+eta}
        if b0 == 1
        else {r: sp.Rational(1, 2)+rho, z: 1-eta}
    )
    endpoint_form = sp.factor(exceptional.subs(endpoint_substitution))
    records[f"b={b0}"] = {
        "weighted_substitution": {
            "P2": "u",
            "a": "u*(r+z/2)",
            "c": "u*(r-z/2)",
        },
        "physical_exceptional_domain": ["r>=1/2", "-1<=z<=1"],
        "minimum_u_order": minimum_order,
        "exceptional_polynomial": sp.sstr(exceptional),
        "exceptional_gradient": [sp.sstr(value) for value in gradient],
        "physical_endpoint_coordinates": ["rho>=0", "eta>=0"],
        "endpoint_exceptional_form": sp.sstr(endpoint_form),
        "physical_zero_set": "rho=eta=0 only",
        "full_pullback": sp.sstr(pulled),
    }
    checks[f"b={b0}:positive_weighted_order"] = minimum_order > 0
    checks[f"b={b0}:exceptional_polynomial_nonzero"] = exceptional != 0
    checks[f"b={b0}:endpoint_form_is_positive_square"] = sp.factor(
        endpoint_form - sp.Rational(9, 4)*(2*rho+eta)**2
    ) == 0

assert all(checks.values()), {key: value for key, value in checks.items() if not value}
packet = {
    "schema": "marici.shape-external-soft-weighted-physical-cone.v1",
    "records": records,
    "negative_branch": "obtained by site exchange P1<->P2 and a<->b",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
for label, record in records.items():
    print(label, "order", record["minimum_u_order"], "exceptional", record["exceptional_polynomial"])
print(OUT)
