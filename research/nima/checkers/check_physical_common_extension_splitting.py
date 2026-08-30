"""Test invariant splitting of the typed 25 -> 26 -> 1 localization sequence."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

OUT = ROOT / "research" / "nima" / "results" / (
    f"physical_common_extension_splitting_p{m.PRIME}.json"
)
NAMES = ("g1", "g2", "g3", "g23", "g31")
GAMMA, AMBIENT, CUTOFF = 5, 10, 5


def add_scaled(target, source, scale=1):
    for column, value in source.items():
        m.add_value(target, column, scale * value)


def rank(rows):
    pivots = {}
    for row in rows:
        m.add_pivot(dict(row), pivots)
    return len(pivots)


def solve_affine(rows, rhs, variable_count):
    augmented = []
    for row, value in zip(rows, rhs):
        candidate = {index: coefficient % m.PRIME for index, coefficient in row.items()}
        if value % m.PRIME:
            candidate[variable_count] = value % m.PRIME
        augmented.append(candidate)
    coefficient_rank = rank(rows)
    augmented_rank = rank(augmented)
    return coefficient_rank, augmented_rank, coefficient_rank == augmented_rank


def main():
    low, columns, quotient_pivots, free = m.presentation(
        NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    label_by_column = {columns[label]: label for label in low}

    def face(level_index):
        span = {}
        for label in low:
            if label[1 + level_index] == 0:
                m.add_pivot(
                    m.quotient_coordinates(label, columns, quotient_pivots, free), span
                )
        return span

    face23, face31 = face(4), face(3)
    face_sum = {}
    for row in list(face23.values()) + list(face31.values()):
        m.add_pivot(dict(row), face_sum)
    assert len(face_sum) == 25

    top = m.quotient_coordinates(
        (0, 0, 0, 0, 1, 1, (0, 0)), columns, quotient_pivots, free
    )
    top = m.reduce_row(top, face_sum)
    adapted_basis = list(face_sum.values()) + [top]
    assert rank(adapted_basis) == 26 == len(free)

    # Reduce vectors to coordinates in the source-labelled adapted basis.
    coordinate_pivots = {}
    coordinate_lifts = {}
    for index, vector in enumerate(adapted_basis):
        row, lift = dict(vector), {index: 1}
        while row and max(row) in coordinate_pivots:
            pivot = max(row)
            coefficient = row[pivot]
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(lift, coordinate_lifts[pivot], -coefficient)
        assert row
        pivot = max(row)
        inverse = pow(row[pivot], m.PRIME - 2, m.PRIME)
        coordinate_pivots[pivot] = {
            column: value * inverse % m.PRIME for column, value in row.items()
        }
        coordinate_lifts[pivot] = {
            column: value * inverse % m.PRIME for column, value in lift.items()
        }

    def coordinates(vector):
        row, result = dict(vector), {}
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            assert pivot in coordinate_pivots
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(result, coordinate_lifts[pivot], coefficient)
        return result

    def connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(label_by_column[column], NAMES, GAMMA, axis, columns),
                coefficient,
            )
        reduced = m.reduce_row(image, quotient_pivots)
        reduced = {column: reduced[column] for column in free if column in reduced}
        return coordinates(reduced)

    matrices = [
        [connection(vector, axis) for vector in adapted_basis] for axis in range(2)
    ]
    face_leaks = [
        sum(int(bool(matrix[index].get(25, 0))) for index in range(25))
        for matrix in matrices
    ]
    assert face_leaks == [0, 0]

    cocycles = []
    quotient_characters = []
    equations, rhs = [], []
    for matrix in matrices:
        top_image = matrix[25]
        alpha = top_image.get(25, 0)
        quotient_characters.append(alpha)
        cocycle = {index: top_image.get(index, 0) for index in range(25)}
        cocycle = {index: value for index, value in cocycle.items() if value}
        cocycles.append(cocycle)
        for target in range(25):
            row = {}
            for source in range(25):
                value = matrix[source].get(target, 0)
                if source == target:
                    value -= alpha
                if value % m.PRIME:
                    row[source] = value % m.PRIME
            equations.append(row)
            rhs.append(-cocycle.get(target, 0))

    coefficient_rank, augmented_rank, constant_split_exists = solve_affine(
        equations, rhs, 25
    )
    packet = {
        "schema": "marici.physical-common-extension-splitting.v1",
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "typed_sequence_dimensions": [25, 26, 1],
        "face_sum_connection_leaks": face_leaks,
        "quotient_connection_characters": quotient_characters,
        "extension_cocycle_ranks_by_axis": [rank([row]) for row in cocycles],
        "simultaneous_constant_lift_system": {
            "unknowns": 25,
            "equations": len(equations),
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "consistent": constant_split_exists,
        },
        "interpretation": (
            "A consistent system gives a simultaneous invariant constant lift at this "
            "finite-field fiber; inconsistency proves only constant-frame nonsplitting, "
            "not nonsplitting under parameter-dependent rational gauge."
        ),
        "passed": (
            len(adapted_basis) == 26
            and face_leaks == [0, 0]
            and len(quotient_characters) == 2
            and len(equations) == 50
        ),
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
