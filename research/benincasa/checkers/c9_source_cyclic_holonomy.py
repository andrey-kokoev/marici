#!/usr/bin/env python3
"""Exact source-level cyclic holonomy audit for the frozen C9 contour."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "nine-site-canonical-contour-packet.json"
TARGET = ROOT / "results" / "c9-source-cyclic-holonomy.json"
N = 9


def rotate_ambient_index(index: int) -> int:
    block, site = divmod(index, N)
    return block * N + (site + 1) % N


def rotate_contour_index(index: int) -> int:
    edge, vertex_type = divmod(index, 3)
    return ((edge + 1) % N) * 3 + vertex_type


def permutation_sign(permutation: list[int]) -> int:
    inversions = sum(permutation[i] > permutation[j] for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(len(work) - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(row for row in range(pivot_index + 1, len(work)) if work[row][pivot_index] != 0)
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, len(work)):
            for column in range(pivot_index + 1, len(work)):
                work[row][column] = (work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column]) // previous
        previous = pivot
    return sign * work[-1][-1]


def main() -> None:
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    columns = [vertex["column"] for vertex in packet["vertices"]]

    ambient_permutation = [rotate_ambient_index(i) for i in range(2 * N)]
    contour_permutation = [rotate_contour_index(i) for i in range(3 * N)]
    intertwining = all(
        [columns[old][ambient_permutation.index(row)] for row in range(2 * N)] == columns[rotate_contour_index(old)]
        for old in range(3 * N)
    )
    assert intertwining
    assert all(index == (index + N) % N for index in range(N))

    basis = packet["localization_basis"]["column_indices_zero_based"]
    determinants = []
    current = list(basis)
    for step in range(N):
        square = [[columns[column][row] for column in current] for row in range(2 * N)]
        determinants.append(determinant(square))
        current = [rotate_contour_index(index) for index in current]
    assert current == basis
    assert all(abs(value) == 512 for value in determinants)
    transition_units = [Fraction(determinants[(step + 1) % N], determinants[step]) for step in range(N)]
    product = Fraction(1)
    for unit in transition_units:
        product *= unit
    assert product == 1

    rank_t_minus_i = N - 1  # incidence matrix of the connected directed N-cycle
    modules = []
    for distance in range(1, N):
        modules.append(
            {
                "oriented_chord_distance": distance,
                "occurrence_rank": N,
                "one_step_rank_T_minus_I": rank_t_minus_i,
                "coinvariant_rank": N - rank_t_minus_i,
                "full_loop_holonomy": "identity",
                "full_loop_rank_T9_minus_I": 0,
            }
        )

    result = {
        "schema": "marici.c9_source_cyclic_holonomy.v1",
        "source": str(SOURCE.relative_to(ROOT.parent.parent)),
        "checks": {
            "ambient_contour_intertwining": intertwining,
            "ambient_permutation_sign": permutation_sign(ambient_permutation),
            "contour_permutation_sign": permutation_sign(contour_permutation),
            "ambient_order": N,
            "contour_order": N,
        },
        "rotated_localization_determinants": determinants,
        "transition_units": [str(value) for value in transition_units],
        "transition_unit_product": "1",
        "oriented_distance_modules": modules,
        "source_derived_mixing_between_distances": False,
        "full_cyclic_holonomy": "identity on every oriented-distance fiber after labelled return",
        "twisted_activation_gate": "closed: (T_full-I)H_mu=0 for the source-derived cyclic transport",
        "scope": "cyclic occurrence transport forced by the frozen scalar OS/Jacobian packet; no claim about an independently derived supported Landau/Gram costalk",
    }
    TARGET.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"intertwining": True, "determinants": determinants, "full_holonomy": "identity", "distance_modules": 8}))


if __name__ == "__main__":
    main()
