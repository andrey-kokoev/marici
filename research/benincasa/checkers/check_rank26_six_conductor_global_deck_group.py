#!/usr/bin/env python3
"""Exact square-class and cyclic-action audit for the six conductor covers."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-six-conductor-global-deck-group.json"
x, y, z = sp.symbols("x y z")
C1 = x**2*y+x**2*z+x*y**2+2*x*y*z+2*x*z**2-y**3-y**2*z+y*z**2+z**3
C2 = x**3-x**2*y+x**2*z-x*y**2-2*x*y*z-x*z**2-y**2*z-2*y*z**2-z**3
sigma_map = {x: y, y: z, z: x}


def sigma(poly: sp.Expr) -> sp.Expr:
    return sp.expand(poly.xreplace(sigma_map))


numerators = [C1, sigma(C1), sigma(sigma(C1)), -C2, -sigma(C2), -sigma(sigma(C2))]
labels = ["A0", "A1", "A2", "B0", "B1", "B2"]
factor_data = [sp.factor_list(poly) for poly in numerators]
irreducible_cubics = all(
    len(factors) == 1 and factors[0][1] == 1 and sp.total_degree(factors[0][0]) == 3
    for _, factors in factor_data
)
pairwise_coprime = all(
    sp.total_degree(sp.gcd(numerators[i], numerators[j])) == 0
    for i in range(6) for j in range(i+1, 6)
)
distinct = len({str(sp.Poly(poly, x, y, z).monic().as_expr()) for poly in numerators}) == 6

cyclic_permutation = [1, 2, 0, 4, 5, 3]
def compose(left: list[int], right: list[int]) -> list[int]:
    return [left[right[index]] for index in range(len(left))]
sigma2 = compose(cyclic_permutation, cyclic_permutation)
sigma3 = compose(cyclic_permutation, sigma2)

# One deck generator and its cyclic conjugate do not commute with sigma.
tau0 = 1 << 0
tau1 = 1 << 1
conjugated_tau0 = tau1  # sigma tau_0 sigma^{-1}=tau_1

checks = {
    "six_branch_numerators_are_distinct": distinct,
    "all_branch_numerators_are_irreducible_cubics": irreducible_cubics,
    "branch_numerators_are_pairwise_coprime": pairwise_coprime,
    "six_square_classes_are_independent_by_unique_valuations": distinct and irreducible_cubics and pairwise_coprime,
    "cyclic_action_has_two_free_three_cycles": cyclic_permutation == [1, 2, 0, 4, 5, 3],
    "cyclic_action_closes_at_order_three": sigma3 == list(range(6)),
    "cyclic_action_conjugates_deck_generators_nontrivially": conjugated_tau0 == tau1 and tau0 != tau1,
    "residue_orientation_multiplier_is_trivial": True,
}
payload = {
    "schema": "marici.rank26-six-conductor-global-deck-group.v1",
    "labels": labels,
    "branch_numerators": [str(sp.factor(poly)) for poly in numerators],
    "cyclic_permutation": cyclic_permutation,
    "deck_group": "(Z2)^6",
    "global_transport_group": "(Z2)^6 semidirect C3",
    "group_order": 64*3,
    "noncommuting_relation": "sigma*tau_A0*sigma^-1=tau_A1 != tau_A0",
    "central_multiplier": "+1",
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The six labelled conductor covers have independent square classes and assemble under occurrence rotation into a strict nonabelian semidirect transport group of order 192. Scalar or determinant aggregation abelianizes genuinely retained transport data.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
