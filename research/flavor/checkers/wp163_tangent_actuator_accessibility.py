"""Exact finite-reach audit for the holonomy tangent complement."""

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
continuous = {constructor: constructor.startswith("U1") for constructor in constructors}
reach = Fraction(1)


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


base_rows = [[1] * 7] + [
    [returns(constructor, winding) for constructor in constructors]
    for winding in range(1, 8)
]


def operational_rows(masses: dict[str, Fraction]) -> list[list[int]]:
    rows = []
    for power in range(3):
        rows.append([
            int(continuous[constructor] and masses[constructor] < reach) * orders[constructor] ** power
            for constructor in constructors
        ])
    return base_rows + rows


low_masses = {constructor: Fraction(1, 2) for constructor in constructors if continuous[constructor]}
dilated_masses = {constructor: 4 * mass for constructor, mass in low_masses.items()}
partial_masses = {
    "U1_order3": Fraction(1, 2),
    "U1_order5": Fraction(3, 4),
    "U1_order7": Fraction(5, 4),
    "U1_irrational": Fraction(2),
}

rank_low = rank(operational_rows(low_masses))
rank_partial = rank(operational_rows(partial_masses))
rank_dilated = rank(operational_rows(dilated_masses))

checks = {
    "base_return_rank_is_four": rank(base_rows) == 4,
    "all_low_mass_continuous_modes_are_accessible": all(mass < reach for mass in low_masses.values()),
    "low_mass_operational_rank_is_seven": rank_low == 7,
    "low_mass_source_kernel_is_zero": len(constructors) - rank_low == 0,
    "partial_packet_has_two_accessible_modes": sum(mass < reach for mass in partial_masses.values()) == 2,
    "partial_operational_rank_is_six": rank_partial == 6,
    "partial_source_kernel_dimension_is_one": len(constructors) - rank_partial == 1,
    "dilation_factor_is_four": all(dilated_masses[c] == 4 * low_masses[c] for c in low_masses),
    "all_dilated_modes_are_inaccessible": all(mass > reach for mass in dilated_masses.values()),
    "dilated_operational_rank_returns_to_four": rank_dilated == 4,
    "dilated_source_kernel_dimension_is_three": len(constructors) - rank_dilated == 3,
    "scale_dilation_changes_rank_without_changing_return_rows": rank_low != rank_dilated and rank(base_rows) == 4,
}

result = {
    "work_package": "WP163",
    "title": "Tangent-actuator accessibility audit",
    "instrument_grammar": "on-shell continuous gauge-mode actuation with strict M<E_max",
    "reach": "E_max=1",
    "rank_low_mass": rank_low,
    "rank_partial": rank_partial,
    "rank_dilated": rank_dilated,
    "kernel_low_mass": len(constructors) - rank_low,
    "kernel_partial": len(constructors) - rank_partial,
    "kernel_dilated": len(constructors) - rank_dilated,
    "classification": "tangent complement is physically rank-faithful only on an accessibility-restricted source domain",
    "selector": False,
    "source_identification": "conditional on gauge-mode reach",
    "physical_instrument": "typed but not implemented",
    "smallest_exact_falsifier": "a common mass dilation from 1/2 to 2 preserves return records but collapses rank from seven to four",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp163_tangent_actuator_accessibility.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

