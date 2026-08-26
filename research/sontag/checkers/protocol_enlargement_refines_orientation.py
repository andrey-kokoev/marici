#!/usr/bin/env python3
"""Exact protocol-relative completion and refinement audit."""

import json
from itertools import product
from pathlib import Path

import sympy as sp


I = sp.I
ONE = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])


def pair_for_word(word):
    ordinary = ONE
    opposite = ONE
    for letter in word:
        ordinary = ordinary * letter
        opposite = letter * opposite
    return ordinary, opposite


def vector(pair):
    return sp.Matrix(list(pair[0]) + list(pair[1]))


def defect(pair):
    return sp.simplify(sp.trace(pair[0]) - sp.trace(pair[1]))


def audit(alphabet, max_depth):
    columns = []
    ranks = []
    separators = []
    for depth in range(max_depth + 1):
        for word in product(alphabet, repeat=depth):
            pair = pair_for_word(word)
            columns.append(vector(pair))
            if defect(pair) != 0:
                separators.append(depth)
        ranks.append(sp.Matrix.hstack(*columns).rank())
    return ranks, separators


old_ranks, old_separators = audit([X, Z], 7)
new_ranks, new_separators = audit([X, Y, Z], 7)

checks = {
    "old_protocol_rank_stabilizes": old_ranks[-1] == old_ranks[-2],
    "old_protocol_has_no_separator_through_bound": not old_separators,
    "old_all_words_equivalence_certified": not old_separators and old_ranks[-1] == old_ranks[-2],
    "new_protocol_has_separator": bool(new_separators),
    "new_first_separator_depth_three": min(new_separators) == 3,
    "protocol_enlargement_increases_reachable_rank": new_ranks[-1] > old_ranks[-1],
    "new_protocol_reaches_full_comparison_space": new_ranks[-1] == 8,
}

result = {
    "schema": "marici.sontag.protocol_enlargement_refines_orientation.v1",
    "claim_strength": "finite exact protocol-relative theorem fixture",
    "old_protocol": {
        "alphabet": ["X", "Z"],
        "rank_by_depth_zero_through_seven": old_ranks,
        "separating_depths": old_separators,
    },
    "enriched_protocol": {
        "alphabet": ["X", "Y", "Z"],
        "rank_by_depth_zero_through_seven": new_ranks,
        "first_separating_depth": min(new_separators),
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
}

out = Path(__file__).parents[1] / "results" / "protocol_enlargement_refines_orientation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
