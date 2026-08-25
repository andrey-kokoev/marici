"""Exact aliasing audit for discrete defects and rational U(1) holonomies."""

from fractions import Fraction
import json
from pathlib import Path


constructors = (
    "Z3",
    "U1_order3",
    "Z5",
    "U1_order5",
    "Z7",
    "U1_order7",
    "U1_irrational",
)
return_orders = {
    "Z3": 3,
    "U1_order3": 3,
    "Z5": 5,
    "U1_order5": 5,
    "Z7": 7,
    "U1_order7": 7,
    "U1_irrational": None,
}


def returns(constructor: str, winding: int) -> int:
    order = return_orders[constructor]
    return int(order is not None and winding % order == 0)


def response(constructor: str, max_winding: int) -> tuple[int, ...]:
    return (1,) + tuple(returns(constructor, winding) for winding in range(1, max_winding + 1))


def rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row != pivot_row and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [a - factor * b for a, b in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def response_matrix(max_winding: int) -> list[list[int]]:
    columns = [response(constructor, max_winding) for constructor in constructors]
    return [list(row) for row in zip(*columns)]


def partition(max_winding: int) -> list[list[str]]:
    classes: dict[tuple[int, ...], list[str]] = {}
    for constructor in constructors:
        classes.setdefault(response(constructor, max_winding), []).append(constructor)
    return list(classes.values())


large_winding = 105
large_partition = partition(large_winding)
large_rank = rank(response_matrix(large_winding))

checks = {
    "order3_pair_matches_through_105": response("Z3", large_winding) == response("U1_order3", large_winding),
    "order5_pair_matches_through_105": response("Z5", large_winding) == response("U1_order5", large_winding),
    "order7_pair_matches_through_105": response("Z7", large_winding) == response("U1_order7", large_winding),
    "matching_is_rule_level_not_accidental": all(return_orders[f"Z{n}"] == return_orders[f"U1_order{n}"] for n in (3, 5, 7)),
    "large_partition_has_four_classes": len(large_partition) == 4,
    "three_classes_are_discrete_continuous_pairs": sum(len(group) == 2 for group in large_partition) == 3,
    "irrational_U1_is_singleton": ["U1_irrational"] in large_partition,
    "large_tower_rank_is_four": large_rank == 4,
    "large_tower_kernel_dimension_is_three": len(constructors) - large_rank == 3,
    "winding_seven_already_has_same_rank": rank(response_matrix(7)) == 4,
    "more_windings_do_not_remove_alias_kernel": rank(response_matrix(105)) == rank(response_matrix(7)),
    "smallest_alias_is_Z3_vs_U1_order3": response("Z3", 3) == response("U1_order3", 3),
}

result = {
    "work_package": "WP161",
    "title": "Rational-holonomy aliasing audit",
    "constructors": list(constructors),
    "probe": "complete normalized return-to-identity tower",
    "contextual_partition": large_partition,
    "response_rank": large_rank,
    "source_kernel_dimension": len(constructors) - large_rank,
    "classification": "return-order probes identify holonomy order but not discrete versus continuous protector source",
    "selector": False,
    "source_identification": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": "Z3 and a U(1) holonomy of exact order three have identical return records for every winding",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp161_rational_holonomy_aliasing.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

