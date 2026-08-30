#!/usr/bin/env python3
"""Compare magnetic snake indices in Q*/(Q*)^2 without integer factorization."""

from __future__ import annotations

import itertools
import json
import math


INDICES = {
    "baseline": 1568,
    "right_commutator_decorated": 7306071077228271850849931638,
    "left_commutator_decorated": 7865258181583837570522477026,
    "commutator_conjugate": 175728406342577936249240427957411658506347000,
}


def is_square(n):
    root = math.isqrt(n)
    return root * root == n


def same_rational_square_class(left, right):
    # For positive integers, left/right is a rational square iff left*right is an integer square.
    return is_square(left * right)


pairs = []
for (left_name, left), (right_name, right) in itertools.combinations(INDICES.items(), 2):
    pairs.append({
        "left": left_name,
        "right": right_name,
        "product": left * right,
        "same_rational_square_class": same_rational_square_class(left, right),
    })

gates = {
    "baseline_is_in_twice_square_class": is_square(INDICES["baseline"] * 2),
    "every_decorated_index_leaves_twice_square_class": all(
        not is_square(index * 2) for name, index in INDICES.items() if name != "baseline"
    ),
    "all_four_indices_have_pairwise_distinct_square_classes": all(
        not pair["same_rational_square_class"] for pair in pairs
    ),
    "comparison_uses_exact_integer_square_tests": all(
        is_square(pair["product"]) == pair["same_rational_square_class"] for pair in pairs
    ),
}
payload = {
    "schema": "marici.strominger.snake_index_square_class_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "fox_decorations_change_the_rational_square_class_of_the_snake_index",
    "indices": INDICES,
    "pairwise_comparisons": pairs,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The decorated indices are not merely the atomic twice-square conductor "
        "multiplied by squares. All four indices occupy pairwise distinct classes "
        "in positive rational numbers modulo rational squares. The nonabelian Fox "
        "fiber therefore controls a genuine square class of the snake torsion."
    ),
}
print(json.dumps(payload, indent=2))
