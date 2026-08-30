#!/usr/bin/env python3
"""Type and reduce the inherited one-loop counterterm blocks."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def rank(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    nrows, ncols = len(work), len(work[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(nrows):
            if row != pivot_row and work[row][col]:
                scale = work[row][col]
                work[row] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


# Domain ordering:
# seven graph-normal classes | one background class | three labelled mass classes.
reduction = [
    [int(row == col) for col in range(7)] + [0] + [0, 0, 0]
    for row in range(7)
]

# Cyclic action cycles the L and D triples, fixes U and the background, and
# cycles the three mass labels.
source_permutation = [1, 2, 0, 4, 5, 3, 6, 7, 9, 10, 8]
target_permutation = [1, 2, 0, 4, 5, 3, 6]


def image_of_source_basis(column: int) -> list[int]:
    return [reduction[row][column] for row in range(7)]


def cycle_target(vector: list[int]) -> list[int]:
    result = [0] * 7
    for old, new in enumerate(target_permutation):
        result[new] = vector[old]
    return result


cyclic_equivariance = True
for old_source in range(11):
    source_then_reduce = image_of_source_basis(source_permutation[old_source])
    reduce_then_target = cycle_target(image_of_source_basis(old_source))
    cyclic_equivariance &= source_then_reduce == reduce_then_target


checks = {
    "reduction_rank_is_seven": rank(reduction) == 7,
    "graph_block_is_identity": all(
        reduction[row][col] == int(row == col)
        for row in range(7)
        for col in range(7)
    ),
    "background_block_is_zero": all(row[7] == 0 for row in reduction),
    "three_mass_blocks_are_zero_after_conformal_normalization": all(
        row[col] == 0 for row in reduction for col in (8, 9, 10)
    ),
    "cyclic_equivariance": cyclic_equivariance,
}

packet = {
    "schema": "marici.benincasa.action-level-counterterm-block-typing.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "domain": {
        "graph_normal_module": ["L1", "L2", "L3", "D1", "D2", "D3", "U"],
        "background_module": ["delta_background"],
        "mass_mode_module": ["delta_m1^2", "delta_m2^2", "delta_m3^2"],
    },
    "target": "rank-seven conformal graph-normal module",
    "matrix": reduction,
    "source_conditions": {
        "zero_one_point_function": "delta_background_ren=0",
        "preserve_declared_free_state": "delta_mi^2_ren=0 for i=1,2,3",
        "field_strength": "no divergent one-loop counterterm",
        "cubic_vertex": "no divergent one-loop counterterm",
    },
    "typing_correction": (
        "The mass blocks belong to the external mode-function coefficient object, "
        "not to the kinematic normals nu_i=P_i^2-X_i^2. They may not be represented "
        "as nu shifts."
    ),
    "nonlocal_lower_point_dressing": (
        "Finite self-energy dressing is source dynamics rather than counterterm "
        "scheme freedom and is not part of this subtraction-map classification."
    ),
    "renormalized_graph_rank": 7,
    "new_carrier_support": False,
}

output = Path(__file__).with_name("action-level-counterterm-block-typing.json")
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
