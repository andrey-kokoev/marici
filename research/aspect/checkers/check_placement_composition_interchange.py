#!/usr/bin/env python3
"""Finite interchange and nonseparable-interaction diagnostic."""

import itertools
import json
from pathlib import Path

BITS = (0, 1)
PAIRS = tuple(itertools.product(BITS, repeat=2))
# Every unary bit function, represented by its outputs at 0 and 1.
UNARY = tuple(itertools.product(BITS, repeat=2))


def apply(function, value):
    return function[value]


def compose(outer, inner):
    return tuple(apply(outer, apply(inner, value)) for value in BITS)


def horizontal(left, right, pair):
    return apply(left, pair[0]), apply(right, pair[1])


def joint(pair):
    left, right = pair
    return left, left ^ right


interchange_cases = 0
for f1, f2, g1, g2 in itertools.product(UNARY, repeat=4):
    for pair in PAIRS:
        left_side = horizontal(g1, g2, horizontal(f1, f2, pair))
        right_side = horizontal(compose(g1, f1), compose(g2, f2), pair)
        assert left_side == right_side
        interchange_cases += 1

factorizations = []
for unary_left, unary_right in itertools.product(UNARY, repeat=2):
    if all(horizontal(unary_left, unary_right, pair) == joint(pair) for pair in PAIRS):
        factorizations.append((unary_left, unary_right))

# A boundary mismatch example: codomain label of first differs from domain label of second.
def vertically_composable(first_codomain, second_domain):
    return first_codomain == second_domain

checks = {
    "all_unary_bit_functions_enumerated": len(UNARY) == 4,
    "all_input_pairs_enumerated": len(PAIRS) == 4,
    "componentwise_interchange_exhaustive": interchange_cases == len(UNARY) ** 4 * len(PAIRS),
    "joint_xor_map_is_total": all(joint(pair) in PAIRS for pair in PAIRS),
    "joint_xor_map_has_no_componentwise_factorization": len(factorizations) == 0,
    "joint_second_output_depends_on_left_input": joint((0, 0))[1] != joint((1, 0))[1],
    "boundary_match_allows_vertical_composition": vertically_composable("Q", "Q"),
    "boundary_mismatch_rejects_vertical_composition": not vertically_composable("Q", "R"),
    "placement_preserves_pair_arity": all(len(horizontal(UNARY[0], UNARY[-1], pair)) == 2 for pair in PAIRS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.placement-composition-interchange.v1", "status": "passed", "checks": checks, "interchange_cases": interchange_cases, "joint_map": {str(pair): joint(pair) for pair in PAIRS}, "factorization_count": len(factorizations), "claim_boundary": "Finite strict-product diagnostic; no physical-time semantics or general strictness theorem."}
output = Path(__file__).parents[1] / "results" / "placement_composition_interchange.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "interchange_cases": interchange_cases, "factorization_count": len(factorizations)}, sort_keys=True))
