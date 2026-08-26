#!/usr/bin/env python3
"""Exact reachable-rank horizon for ordinary versus opposite Pauli products."""

import json
from itertools import product
from pathlib import Path

import sympy as sp


I = sp.I
ONE = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
alphabet = [X, Y, Z]


def flatten_pair(a, b):
    return sp.Matrix(list(a) + list(b))


def pair_for_word(word):
    ordinary = ONE
    opposite = ONE
    for letter in word:
        ordinary = ordinary * letter
        opposite = letter * opposite
    return ordinary, opposite


def output_difference(pair):
    return sp.simplify(sp.trace(pair[0]) - sp.trace(pair[1]))


rank_by_depth = []
columns = []
first_separator = None
for depth in range(8):
    for word in product(alphabet, repeat=depth):
        pair = pair_for_word(word)
        columns.append(flatten_pair(*pair))
        if first_separator is None and output_difference(pair) != 0:
            first_separator = depth
    rank_by_depth.append(sp.Matrix.hstack(*columns).rank())

checks = {
    "comparison_dimension_is_eight": len(flatten_pair(ONE, ONE)) == 8,
    "rank_stabilizes_by_dimension_bound": rank_by_depth[6] == rank_by_depth[7],
    "reachable_rank_is_full": rank_by_depth[-1] == 8,
    "first_separator_is_depth_three": first_separator == 3,
    "no_false_separator_before_three": all(
        output_difference(pair_for_word(word)) == 0
        for depth in range(3)
        for word in product(alphabet, repeat=depth)
    ),
    "dimension_bound_exceeds_observed_depth": first_separator <= 7,
}

result = {
    "schema": "marici.sontag.finite_realization_horizon.v1",
    "claim_strength": "finite exact realization audit",
    "comparison_state_dimension": 8,
    "rank_by_depth_zero_through_seven": rank_by_depth,
    "first_separating_depth": first_separator,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
}

out = Path(__file__).parents[1] / "results" / "finite_realization_horizon.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
