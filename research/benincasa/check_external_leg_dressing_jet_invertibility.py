#!/usr/bin/env python3
"""Prove that analytic external-leg dressing preserves the finite normal tower."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


MONOMIALS = [
    (0, 0, 0),
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (2, 0, 0), (1, 1, 0), (1, 0, 1),
    (0, 2, 0), (0, 1, 1), (0, 0, 2),
    (1, 1, 1),
]
INDEX = {monomial: index for index, monomial in enumerate(MONOMIALS)}


def add(left: tuple[int, int, int], right: tuple[int, int, int]):
    result = tuple(left[i] + right[i] for i in range(3))
    return result if result in INDEX else None


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result *= -1
        pivot_value = work[col][col]
        result *= pivot_value
        work[col] = [value / pivot_value for value in work[col]]
        for row in range(col + 1, len(work)):
            scale = work[row][col]
            if scale:
                work[row] = [
                    value - scale * pivot_entry
                    for value, pivot_entry in zip(work[row], work[col])
                ]
    return result


# A hostile generic analytic dressing jet with F(0)=1.  The determinant is
# independent of the displayed nonconstant coefficients because degree is
# filtration-increasing.
dressing = {
    monomial: Fraction(index + 1)
    for index, monomial in enumerate(MONOMIALS)
}
dressing[(0, 0, 0)] = Fraction(1)

matrix = [[Fraction(0) for _ in MONOMIALS] for _ in MONOMIALS]
for source_index, source_monomial in enumerate(MONOMIALS):
    for dressing_monomial, coefficient in dressing.items():
        target = add(source_monomial, dressing_monomial)
        if target is not None:
            matrix[INDEX[target]][source_index] += coefficient

det = determinant(matrix)
response_block = [row[1:] for row in matrix[1:]]
response_det = determinant(response_block)

checks = {
    "complete_constant_plus_response_tower_is_invertible": det == 1,
    "ten_response_tower_is_invertible": response_det == 1,
    "degree_filtration_is_preserved": all(
        matrix[row][col] == 0
        for row, target in enumerate(MONOMIALS)
        for col, source in enumerate(MONOMIALS)
        if sum(target) < sum(source)
    ),
    "all_diagonal_entries_equal_F0": all(matrix[i][i] == 1 for i in range(11)),
}

packet = {
    "schema": "marici.benincasa.external-leg-dressing-jet-invertibility.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "normal_monomials": [list(monomial) for monomial in MONOMIALS],
    "complete_tower_determinant_at_F0_1": str(det),
    "response_tower_determinant_at_F0_1": str(response_det),
    "general_determinant": {
        "constant_plus_responses": "F(0)^11",
        "responses_only": "F(0)^10",
    },
    "source_operation": (
        "sewing a two-point self-energy packet to any labelled external leg "
        "multiplies the three-point normal jet by an analytic site-local factor"
    ),
    "rank7_consequence": (
        "Projection of the dressed jet onto the original eleven labelled coordinates "
        "is triangular and invertible wherever F(0) is nonzero. Composing that "
        "projection with the established rank-seven source quotient preserves "
        "faithfulness."
    ),
    "coefficient_enlargement": (
        "A generic dressing can also create monomials outside the CM-generated tower, "
        "such as pure cubic normal jets. These are additional coefficient/readout "
        "coordinates, not new Carrier incidences and not needed to recover R7."
    ),
    "failure_support": "F(0)=0, which is not perturbatively reachable from F(0)=1",
    "new_carrier_support": False,
}

output = Path(__file__).with_name("external-leg-dressing-jet-invertibility.json")
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
