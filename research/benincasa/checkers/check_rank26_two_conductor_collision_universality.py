#!/usr/bin/env python3
"""Independent weighted collision limits for both active G12 conductors."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-two-conductor-collision-universality.json"
x, y, z, u, r = sp.symbols("x y z u r", nonzero=True)


def collision_packet(name: str, h: sp.Expr) -> dict:
    hp = sp.factor(h.subs(u, r))
    hm = sp.factor(h.subs(u, -r))
    raw = sp.Matrix([[hp/r, hp], [-hm/r, hm]])
    lattice = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [r/2, -r/2]])
    weighted = sp.simplify(lattice*raw)
    limit = weighted.applyfunc(lambda entry: sp.factor(sp.limit(entry, r, 0)))
    h0 = sp.factor(h.subs(u, 0))
    h1 = sp.factor(sp.diff(h, u).subs(u, 0))
    expected = sp.Matrix([[h1, h0], [h0, 0]])
    determinant = sp.factor(limit.det())
    return {
        "name": name,
        "h0": str(h0),
        "limit": [[str(limit[i, j]) for j in range(2)] for i in range(2)],
        "determinant": str(determinant),
        "matches_universal_value_derivative_form": bool(sp.simplify(limit-expected) == sp.zeros(2)),
        "determinant_is_minus_h0_squared": bool(sp.simplify(determinant+h0**2) == 0),
        "generic_rank_two": bool(determinant != 0),
    }


# g1: b=y+z, conductor variable a=u, dR1/da=-2*x*u.
spectator_g1 = (u-x-z)*(u+y+2*z)*(y+z-x)*(u-y)
h_g1 = sp.factor(1/((-2*x)*spectator_g1))

# g2: a=x+z, conductor variable b=u, dR2/db=2*y*u.
spectator_g2 = (u-y-z)*(x+u+2*z)*(u-x)*(x+z-y)
h_g2 = sp.factor(1/((2*y)*spectator_g2))

packets = [collision_packet("G12:g1", h_g1), collision_packet("G12:g2", h_g2)]
checks = {
    "both_match_universal_value_derivative_form": all(p["matches_universal_value_derivative_form"] for p in packets),
    "both_determinants_are_minus_h0_squared": all(p["determinant_is_minus_h0_squared"] for p in packets),
    "both_are_generically_rank_two": all(p["generic_rank_two"] for p in packets),
    "the_two_source_formulas_are_independent": packets[0]["h0"] != packets[1]["h0"],
}
payload = {
    "schema": "marici.rank26-two-conductor-collision-universality.v1",
    "packets": packets,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "Both independently defined active G12 conductors specialize to the same rank-two value/derivative form. Together with cyclic covariance, all six labelled ports inherit the same nonreduced collision type.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
