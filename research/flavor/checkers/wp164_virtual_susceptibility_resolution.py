"""Exact virtual susceptibility and detector-resolution rank audit."""

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
resolution = Fraction(1, 4)


def rank(matrix: list[list[Fraction]]) -> int:
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


base_rows = [[Fraction(1)] * 7] + [
    [Fraction(returns(constructor, winding)) for constructor in constructors]
    for winding in range(1, 8)
]


def response_rows(masses: dict[str, Fraction], detector_typed: bool) -> list[list[Fraction]]:
    susceptibilities = {
        constructor: Fraction(1, masses[constructor] ** 2)
        for constructor in constructors
        if continuous[constructor]
    }
    if detector_typed:
        susceptibilities = {
            constructor: value if value >= resolution else Fraction(0)
            for constructor, value in susceptibilities.items()
        }
    complement = [
        [
            susceptibilities.get(constructor, Fraction(0)) * orders[constructor] ** power
            for constructor in constructors
        ]
        for power in range(3)
    ]
    return base_rows + complement


unit_masses = {constructor: Fraction(1) for constructor in constructors if continuous[constructor]}
dilated_masses = {constructor: Fraction(3) for constructor in constructors if continuous[constructor]}
partial_masses = {
    "U1_order3": Fraction(1),
    "U1_order5": Fraction(1),
    "U1_order7": Fraction(3),
    "U1_irrational": Fraction(3),
}

formal_unit_rank = rank(response_rows(unit_masses, False))
formal_dilated_rank = rank(response_rows(dilated_masses, False))
detected_unit_rank = rank(response_rows(unit_masses, True))
detected_partial_rank = rank(response_rows(partial_masses, True))
detected_dilated_rank = rank(response_rows(dilated_masses, True))

checks = {
    "unit_susceptibility_is_one": Fraction(1, unit_masses["U1_order3"] ** 2) == 1,
    "dilated_susceptibility_is_one_ninth": Fraction(1, dilated_masses["U1_order3"] ** 2) == Fraction(1, 9),
    "unit_response_exceeds_resolution": Fraction(1) >= resolution,
    "dilated_response_is_below_resolution": Fraction(1, 9) < resolution,
    "formal_unit_rank_is_seven": formal_unit_rank == 7,
    "formal_dilated_rank_remains_seven": formal_dilated_rank == 7,
    "detected_unit_rank_is_seven": detected_unit_rank == 7,
    "partial_detector_rank_is_six": detected_partial_rank == 6,
    "partial_detector_kernel_dimension_is_one": len(constructors) - detected_partial_rank == 1,
    "dilated_detector_rank_collapses_to_four": detected_dilated_rank == 4,
    "dilated_detector_kernel_dimension_is_three": len(constructors) - detected_dilated_rank == 3,
    "nonzero_formal_response_is_not_operational_detection": formal_dilated_rank > detected_dilated_rank,
}

result = {
    "work_package": "WP164",
    "title": "Virtual-susceptibility resolution audit",
    "response_law": "chi=g^2/M^2 with g=1",
    "detector_resolution": "delta=1/4",
    "formal_rank_unit_mass": formal_unit_rank,
    "formal_rank_dilated_mass": formal_dilated_rank,
    "detected_rank_unit_mass": detected_unit_rank,
    "detected_rank_partial": detected_partial_rank,
    "detected_rank_dilated_mass": detected_dilated_rank,
    "classification": "virtual response is algebraically faithful at finite mass but not uniformly detectable at fixed resolution",
    "selector": False,
    "source_identification": "resolution-relative",
    "physical_instrument": "detector response typed but not implemented",
    "smallest_exact_falsifier": "mass dilation 1 to 3 leaves formal rank seven but suppresses chi from 1 to 1/9 below delta=1/4, giving detected rank four",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp164_virtual_susceptibility_resolution.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

