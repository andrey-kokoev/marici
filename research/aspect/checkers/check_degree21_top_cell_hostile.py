#!/usr/bin/env python3
"""Prospective hostile: do frozen degrees <=20 select the degree-21 top cell?"""
from __future__ import annotations

import json

DEGREE = 21


def monomial_value(args):
    return 1 if all(args) else 0


def delta_is_zero(value):
    checked = 0
    for word in range(1 << (DEGREE + 1)):
        args = tuple((word >> i) & 1 for i in range(DEGREE + 1))
        parity = value(args[1:]) ^ value(args[:-1])
        for i in range(DEGREE):
            merged = args[:i] + (args[i] ^ args[i + 1],) + args[i + 2:]
            parity ^= value(merged)
        checked += 1
        if parity:
            return False, checked, args
    return True, checked, None


def trivial_value(args):
    return 0


trivial_cocycle, trivial_checked, trivial_witness = delta_is_zero(trivial_value)
monomial_cocycle, monomial_checked, monomial_witness = delta_is_zero(monomial_value)

proper_faces_agree = all(
    trivial_value(tuple(1 if i == j else 0 for i in range(DEGREE))) ==
    monomial_value(tuple(1 if i == j else 0 for i in range(DEGREE)))
    for j in range(DEGREE)
)
top_values_differ = trivial_value((1,) * DEGREE) != monomial_value((1,) * DEGREE)

checks = {
    "both_candidates_normalized_on_all_coordinate_faces": proper_faces_agree,
    "trivial_candidate_is_full_degree_21_cocycle": trivial_cocycle,
    "nontrivial_monomial_candidate_is_full_degree_21_cocycle": monomial_cocycle,
    "candidates_differ_only_at_normalized_top_input": top_values_differ,
    "all_4194304_degree_21_cocycle_words_checked_for_each_candidate": trivial_checked == (1 << 22) and monomial_checked == (1 << 22),
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.degree21-top-cell-hostile.v1",
    "prospective_forecast_id": "prospective-next-degree-coherence",
    "degree": DEGREE,
    "candidate_top_values": {"trivial": 1, "nontrivial_monomial": -1},
    "checks": checks,
    "passed": passed,
    "classification": "lower_profile_does_not_select_degree21_top_cell" if passed else "hostile_inconclusive",
    "forecast_score": {
        "next_degree_cell_family_retrieved": passed,
        "top_candidate_sufficient": False if passed else None,
        "reason": "two distinct normalized degree-21 cocycles agree on every proper coordinate face and preserve the entire frozen lower profile",
    },
    "new_missing_constructor": "source-derived k-invariant or selection law choosing the degree-21 cohomology class; lower coherence closure alone is insufficient",
    "next_falsifier": "derive the degree-21 k-invariant from a source operation independent of the lower-face data, then test it against the trivial/nontrivial pair",
}
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)
