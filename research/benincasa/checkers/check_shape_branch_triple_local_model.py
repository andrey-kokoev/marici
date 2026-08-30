#!/usr/bin/env python3
"""Exact local A1 and source-order audit at a shape-wall branch triple."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-branch-triple-local-model.json"

a, b, c = source.a, source.b, source.c
x, y, z = sp.symbols("x y z")
local_solution = {
    a: -x / 2 + y / 2 + z / 2 - 1,
    b: x / 2 - y / 2 + z / 2 - 1,
    c: x / 2 + y / 2 - z / 2,
}
K_local = sp.expand(source.K0.subs(local_solution))
poly = sp.Poly(K_local, x, y, z)
K_quadratic = sp.expand(sum(
    coefficient * x**monomial[0] * y**monomial[1] * z**monomial[2]
    for monomial, coefficient in poly.terms()
    if sum(monomial) == 2
))
hessian = sp.hessian(K_quadratic, (x, y, z))

u, v, q = sp.symbols("u v q")
source_orders = {}
for name, numerator in source.numerators.items():
    translated = sp.Poly(numerator.subs({a: u - 1, b: v - 1, c: q}), u, v, q)
    source_orders[name] = min(sum(monomial) for monomial, coefficient in translated.terms() if coefficient)

triple_terms = ["G23_g12", "G31_g12"]
pair_terms = [name for name in source_orders if name not in triple_terms]
checks = {
    "adapted_coordinates_are_exact": all(sp.expand(expr.subs(local_solution) - target) == 0 for expr, target in [
        (source.g1, x), (source.g2, y), (source.s12, z)
    ]),
    "K0_has_no_constant_or_linear_term": all(sum(monomial) >= 2 for monomial, _ in poly.terms()),
    "quadratic_hessian_is_nondegenerate": hessian.det() != 0,
    "milnor_rank_is_one": hessian.rank() == 3,
    "pair_terms_have_order_six": all(source_orders[name] == 6 for name in pair_terms),
    "triple_terms_have_order_eight": all(source_orders[name] == 8 for name in triple_terms),
    "triple_terms_are_identical": sp.expand(source.numerators[triple_terms[0]] - source.numerators[triple_terms[1]]) == 0,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-branch-triple-local-model.v1",
    "representative_point": {"a": -1, "b": -1, "c": 0},
    "adapted_coordinates": {"x": "g1", "y": "g2", "z": "s12"},
    "K_local": sp.sstr(K_local),
    "K_quadratic": sp.sstr(K_quadratic),
    "quadratic_hessian": [[sp.sstr(entry) for entry in row] for row in hessian.tolist()],
    "quadratic_hessian_determinant": sp.sstr(hessian.det()),
    "singularity_type": "A1 ordinary double point",
    "milnor_rank": 1,
    "deck_character_on_vanishing_cycle": -1,
    "source_numerator_orders": source_orders,
    "native_triple_terms": triple_terms,
    "native_triple_radial_form_order": -1,
    "interpretation": "candidate logarithmic coupling; physical/Kato pairing not yet constructed",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("det(H)=", hessian.det(), "orders=", source_orders)
print(OUT)
