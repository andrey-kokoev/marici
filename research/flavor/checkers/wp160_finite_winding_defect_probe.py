"""Exact finite-winding return probe for rival protector groups."""

from fractions import Fraction
import json
from pathlib import Path


constructors = ("Z3", "Z5", "Z7", "U1_generic")
orders = {"Z3": 3, "Z5": 5, "Z7": 7, "U1_generic": None}


def returns(constructor: str, winding: int) -> int:
    order = orders[constructor]
    return int(order is not None and winding % order == 0)


def response(constructor: str, max_winding: int) -> tuple[int, ...]:
    return (1,) + tuple(returns(constructor, winding) for winding in range(1, max_winding + 1))


def matrix(max_winding: int) -> list[list[int]]:
    columns = [response(constructor, max_winding) for constructor in constructors]
    return [list(row) for row in zip(*columns)]


def rank(integer_matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in integer_matrix]
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


def partition(max_winding: int) -> list[list[str]]:
    classes: dict[tuple[int, ...], list[str]] = {}
    for constructor in constructors:
        classes.setdefault(response(constructor, max_winding), []).append(constructor)
    return sorted(classes.values(), key=lambda group: constructors.index(group[0]))


minimal_faithful_winding = next(w for w in range(1, 16) if rank(matrix(w)) == 4)

checks = {
    "Z3_first_returns_at_three": [w for w in range(1, 8) if returns("Z3", w)][0] == 3,
    "Z5_first_returns_at_five": [w for w in range(1, 8) if returns("Z5", w)][0] == 5,
    "Z7_first_returns_at_seven": [w for w in range(1, 8) if returns("Z7", w)][0] == 7,
    "generic_U1_has_no_return_through_fifteen": all(not returns("U1_generic", w) for w in range(1, 16)),
    "winding_four_partition_has_two_classes": partition(4) == [["Z3"], ["Z5", "Z7", "U1_generic"]],
    "winding_six_leaves_Z7_U1_pair": partition(6) == [["Z3"], ["Z5"], ["Z7", "U1_generic"]],
    "winding_six_rank_is_three": rank(matrix(6)) == 3,
    "winding_seven_partition_is_discrete": all(len(group) == 1 for group in partition(7)),
    "winding_seven_rank_is_four": rank(matrix(7)) == 4,
    "minimal_faithful_winding_is_seven": minimal_faithful_winding == 7,
    "normalization_port_is_required_for_U1_column": rank(matrix(7)[1:]) == 3,
    "full_tower_adds_new_relational_experiment": rank(matrix(7)) > 1,
}

result = {
    "work_package": "WP160",
    "title": "Finite-winding defect-probe audit",
    "constructors": list(constructors),
    "probe": "normalized return-to-identity records R_m for windings 1..W",
    "partition_W4": partition(4),
    "partition_W6": partition(6),
    "partition_W7": partition(7),
    "rank_W6": rank(matrix(6)),
    "rank_W7": rank(matrix(7)),
    "minimal_faithful_winding": minimal_faithful_winding,
    "classification": "ideal normalized winding tower is jointly faithful on the frozen rival family at W=7",
    "selector": False,
    "source_identification": "conditional ideal",
    "physical_instrument": False,
    "smallest_exact_falsifier": "at W=6, Z7 and generic U1 have identical normalized return records",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp160_finite_winding_defect_probe.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

