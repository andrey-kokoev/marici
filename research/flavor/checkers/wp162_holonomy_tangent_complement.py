"""Exact complementary tangent-probe audit for discrete/continuous aliases."""

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
orders = {
    "Z3": 3,
    "U1_order3": 3,
    "Z5": 5,
    "U1_order5": 5,
    "Z7": 7,
    "U1_order7": 7,
    "U1_irrational": 0,
}
continuous = {constructor: int(constructor.startswith("U1")) for constructor in constructors}


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


def returns(constructor: str, winding: int) -> int:
    if constructor == "U1_irrational":
        return 0
    return int(winding % orders[constructor] == 0)


base_rows = [[1] * len(constructors)] + [
    [returns(constructor, winding) for constructor in constructors]
    for winding in range(1, 8)
]
tangent_rows = [
    [continuous[constructor] * orders[constructor] ** power for constructor in constructors]
    for power in range(3)
]


def record(constructor: str, tangent_depth: int) -> tuple[int, ...]:
    column_index = constructors.index(constructor)
    rows = base_rows + tangent_rows[:tangent_depth]
    return tuple(row[column_index] for row in rows)


rank_base = rank(base_rows)
rank_tangent_1 = rank(base_rows + tangent_rows[:1])
rank_tangent_2 = rank(base_rows + tangent_rows[:2])
rank_tangent_3 = rank(base_rows + tangent_rows)

checks = {
    "base_return_rank_is_four": rank_base == 4,
    "binary_tangent_record_separates_every_alias_pair": all(record(f"Z{n}", 1) != record(f"U1_order{n}", 1) for n in (3, 5, 7)),
    "binary_tangent_records_make_point_partition_discrete": len({record(constructor, 1) for constructor in constructors}) == 7,
    "binary_tangent_rank_is_only_five": rank_tangent_1 == 5,
    "binary_tangent_mixture_kernel_dimension_is_two": len(constructors) - rank_tangent_1 == 2,
    "first_mixed_moment_raises_rank_to_six": rank_tangent_2 == 6,
    "second_mixed_moment_raises_rank_to_seven": rank_tangent_3 == 7,
    "three_tangent_rows_are_jointly_faithful": len(constructors) - rank_tangent_3 == 0,
    "continuous_nodes_are_distinct": len({orders[c] for c in constructors if continuous[c]}) == 4,
    "discrete_tangent_response_is_zero": all(tangent_rows[p][constructors.index(f"Z{n}")] == 0 for p in range(3) for n in (3, 5, 7)),
    "continuous_tangent_response_is_nonzero_at_depth_zero": all(tangent_rows[0][constructors.index(c)] == 1 for c in constructors if continuous[c]),
    "minimal_mixed_tangent_depth_is_three": [rank(base_rows + tangent_rows[:depth]) for depth in range(4)] == [4, 5, 6, 7],
}

result = {
    "work_package": "WP162",
    "title": "Holonomy tangent-complement audit",
    "constructors": list(constructors),
    "base_return_rank": rank_base,
    "rank_with_binary_tangent": rank_tangent_1,
    "rank_with_first_mixed_moment": rank_tangent_2,
    "rank_with_second_mixed_moment": rank_tangent_3,
    "point_partition_with_binary_tangent": "seven singletons",
    "mixture_kernel_after_binary_tangent": len(constructors) - rank_tangent_1,
    "classification": "one tangent probe separates point alternatives; three mixed tangent-order probes are jointly faithful on source mixtures",
    "selector": False,
    "source_identification": "conditional formal",
    "physical_instrument": False,
    "smallest_exact_falsifier": "binary tangent dimension yields seven distinct point records but response rank five, leaving a two-dimensional mixture kernel",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp162_holonomy_tangent_complement.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

