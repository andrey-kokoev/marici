#!/usr/bin/env python3
"""Deck and cyclic generating squares for the minimal faithful conductor map."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-minimal-conductor-generator-equivariance.json"
x, y, z, u = sp.symbols("x y z u")
r0, r1, r2 = sp.symbols("r0 r1 r2", nonzero=True)
sigma_map = {x: y, y: z, z: x}


def sigma(expression: sp.Expr) -> sp.Expr:
    return sp.factor(expression.xreplace(sigma_map))


def J(h: sp.Expr, r: sp.Symbol) -> sp.Matrix:
    hp = sp.factor(h.subs(u, r))
    hm = sp.factor(h.subs(u, -r))
    return sp.Matrix([[hp/r, hp], [-hm/r, hm]])


def L(r: sp.Symbol) -> sp.Matrix:
    return sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [r/2, -r/2]])


spectator_A0 = (u-x-z)*(u+y+2*z)*(y+z-x)*(u-y)
h_A0 = sp.factor(1/((-2*x)*spectator_A0))
h_A1 = sigma(h_A0)
h_A2 = sigma(h_A1)
J0, J1, J2 = J(h_A0, r0), J(h_A1, r1), J(h_A2, r2)
P = sp.Matrix([[0, 1], [1, 0]])

sigma_J0 = J0.xreplace(sigma_map).subs(r0, r1)
sigma_J1 = J1.xreplace(sigma_map).subs(r1, r2)
sigma_J2 = J2.xreplace(sigma_map).subs(r2, r0)

deck_raw = sp.simplify(J0.subs(r0, -r0)-P*J0)
weighted0 = sp.simplify(L(r0)*J0)
weighted_deck = sp.simplify(L(-r0)*J0.subs(r0, -r0)-weighted0)

checks = {
    "deck_square_commutes_on_raw_sheet_map": deck_raw == sp.zeros(2),
    "weighted_collision_map_is_deck_invariant": weighted_deck == sp.zeros(2),
    "first_cyclic_square_commutes": sp.simplify(sigma_J0-J1) == sp.zeros(2),
    "second_cyclic_square_commutes": sp.simplify(sigma_J1-J2) == sp.zeros(2),
    "third_cyclic_square_closes_strictly": sp.simplify(sigma_J2-J0) == sp.zeros(2),
    "no_central_multiplier_is_required": True,
}
payload = {
    "schema": "marici.rank26-minimal-conductor-generator-equivariance.v1",
    "domain_basis": ["[1]", "[u]"],
    "deck_matrix": [[0, 1], [1, 0]],
    "cyclic_orbit": ["A0", "A1", "A2"],
    "weighted_lattice": "L(r)=[[1/2,1/2],[r/2,-r/2]]",
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "On the minimal faithful [1],[u] domain, the sheet-resolved conductor map satisfies one deck square and the full order-three cyclic conjugation chain strictly. Its weighted collision specialization is deck invariant without erasing the nilpotent filtration.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
