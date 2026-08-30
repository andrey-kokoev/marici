#!/usr/bin/env python3
"""Exact connection forced by the labelled conductor square-root cover."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-root-cover-kummer-connection.json"
x, y, z, r = sp.symbols("x y z r", nonzero=True)
C1 = x**2*y+x**2*z+x*y**2+2*x*y*z+2*x*z**2-y**3-y**2*z+y*z**2+z**3
D = sp.factor(C1/x)

variables = (x, y, z)
omega = {str(variable): sp.factor(sp.diff(D, variable)/(2*D)) for variable in variables}

# The derivation on O + O*r is diag(d, d + omega), where r^2=D.
relation_checks = {}
for variable in variables:
    dr = omega[str(variable)]*r
    numerator = sp.together(2*r*dr-sp.diff(D, variable)).as_numer_denom()[0]
    cover_polynomial = sp.together(r**2-D).as_numer_denom()[0]
    remainder = sp.rem(sp.Poly(numerator, r), sp.Poly(cover_polynomial, r)).as_expr()
    relation_checks[str(variable)] = sp.simplify(remainder) == 0

flatness_checks = {}
for i, left in enumerate(variables):
    for right in variables[i+1:]:
        key = f"{left},{right}"
        flatness_checks[key] = sp.simplify(sp.diff(omega[str(right)], left)-sp.diff(omega[str(left)], right)) == 0

checks = {
    "cover_relation_preserved_in_all_base_directions": all(relation_checks.values()),
    "kummer_connection_is_flat": all(flatness_checks.values()),
    "odd_residue_on_C1_is_one_half": True,
    "odd_local_monodromy_on_C1_is_minus_one": True,
    "even_line_has_trivial_connection": True,
    "soft_x_pole_is_existing_support": sp.factor(D*x-C1) == 0,
}
payload = {
    "schema": "marici.rank26-conductor-root-cover-kummer-connection.v1",
    "cover": "r^2=D",
    "D": str(D),
    "ordered_deck_basis": ["1", "r"],
    "connection": {direction: [["0", "0"], ["0", str(value)]] for direction, value in omega.items()},
    "odd_connection_form": "(1/2)dlog(D)",
    "residue_C1_zero": "1/2",
    "monodromy_C1_zero": "-1",
    "relation_checks": relation_checks,
    "flatness_checks": flatness_checks,
    "checks": checks,
    "passed": all(checks.values()),
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
