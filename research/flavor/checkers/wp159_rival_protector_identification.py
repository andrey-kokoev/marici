"""Exact low-energy and formal-port rank audit for rival protector sources."""

from fractions import Fraction
import json
from pathlib import Path


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


constructors = ["Z3", "Z5", "Z7", "U1F"]
orders = [3, 5, 7, 0]  # zero is a formal label for the continuous rival.

# Rows: forbid NN, forbid NbarNbar, allow N Nbar, zero Z4 residue,
# faithful anomaly kernel size, accessible topology flag.
low_energy = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [16, 16, 16, 16],
    [1, 1, 1, 1],
]

# A formal moment tower of protector order/holonomy labels. This is algebraic
# source separation only; no executable defect instrument is asserted.
formal_ports = [[order ** power for order in orders] for power in range(4)]

low_rank = rank(low_energy)
formal_rank = rank(formal_ports)

checks = {
    "four_inequivalent_protectors_frozen": len(set(constructors)) == 4,
    "all_low_energy_columns_are_identical": all(row.count(row[0]) == len(row) for row in low_energy),
    "low_energy_rank_is_one": low_rank == 1,
    "low_energy_source_kernel_dimension_is_three": len(constructors) - low_rank == 3,
    "Z3_and_Z5_are_low_energy_equivalent": all(row[0] == row[1] for row in low_energy),
    "formal_port_matrix_is_four_by_four": len(formal_ports) == 4 and all(len(row) == 4 for row in formal_ports),
    "formal_nodes_are_distinct": len(set(orders)) == 4,
    "formal_tower_rank_is_four": formal_rank == 4,
    "formal_source_kernel_is_zero": len(constructors) - formal_rank == 0,
    "zeroth_formal_port_is_uninformative_alone": rank([formal_ports[0]]) == 1,
    "one_formal_moment_is_not_jointly_faithful": rank(formal_ports[:2]) == 2,
    "full_formal_tower_adds_new_source_experiment": formal_rank > low_rank,
}

result = {
    "work_package": "WP159",
    "title": "Rival protector-identification audit",
    "constructors": constructors,
    "authorized_low_energy_rank": low_rank,
    "authorized_source_kernel_dimension": len(constructors) - low_rank,
    "authorized_contextual_partition": [constructors],
    "formal_port_rank": formal_rank,
    "formal_port_kernel_dimension": len(constructors) - formal_rank,
    "classification": "selector protection is low-energy source-nonidentifying; formal defect ports separate only in a new experiment",
    "selector": "all rivals implement the same conditional WP154 selector",
    "rigidifier": "protector choice rigidifies stability but is not identified",
    "physical_instrument": False,
    "smallest_exact_falsifier": "Z3 and Z5 protectors have identical complete authorized low-energy response columns",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp159_rival_protector_identification.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

