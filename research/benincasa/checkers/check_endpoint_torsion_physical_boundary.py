#!/usr/bin/env python3
"""Compare integral and mod-two boundaries of the two physical completions."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-torsion-physical-boundary.json"

# Ordered basis: infinity+, zero+, infinity-, zero-.
q_total = (1, -1, 1, -1)
q_sheet_zero = (0, 1, 0, -1)
q_sheet_infinity = (1, 0, -1, 0)
tau = tuple(a - b for a, b in zip(q_sheet_infinity, q_sheet_zero))

deck = (2, 3, 0, 1)


def permute(vector, permutation):
    result = [0] * len(vector)
    for source, target in enumerate(permutation):
        result[target] += vector[source]
    return tuple(result)


def mod_two(vector):
    return tuple(x % 2 for x in vector)


checks = {
    "odd_physical_boundary_is_tau": tau == (1, -1, -1, 1),
    "integral_completions_are_distinct": q_total != tau,
    "ordinary_boundary_is_deck_even": permute(q_total, deck) == q_total,
    "odd_boundary_is_deck_odd_integrally": (
        permute(tau, deck) == tuple(-x for x in tau)
    ),
    "boundaries_coincide_mod_two": mod_two(q_total) == mod_two(tau),
    "common_mod_two_boundary_is_nonzero": mod_two(tau) == (1, 1, 1, 1),
    "common_mod_two_boundary_has_reduced_degree_zero": sum(mod_two(tau)) % 2 == 0,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-torsion-physical-boundary.v1",
    "basis": ["p_infinity_plus", "p_0_plus", "p_infinity_minus", "p_0_minus"],
    "ordinary_trace_boundary": list(q_total),
    "sign_weighted_boundary": list(tau),
    "mod_two_boundary": list(mod_two(tau)),
    "chain_level_activation": (
        "the source sign-weighted relative cycle has boundary tau"
    ),
    "mod_two_alias": (
        "ordinary and sign-weighted completions have the same mod-two boundary"
    ),
    "disposition": (
        "physical activation is established at integral chain level, but a "
        "mod-two boundary readout forgets the source deck-character selection"
    ),
    "next_falsifier": (
        "derive an integral linking or polarized Weil-pairing functional from "
        "the source; do not choose a dual torsion class"
    ),
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("ordinary", q_total, "odd", tau, "mod2", mod_two(tau))
print(OUT)
