"""Compute the fixed-low-basis relation filtration of the adapter pencil."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
LOW_LABELS = [(i, j) for i in range(8) for j in range(8 - i)]


def add(row: dict[int, int], column: int, value: int, prime: int) -> None:
    value = (row.get(column, 0) + value) % prime
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def rows_at(packet: dict, numerator: int, denominator: int, count: int):
    prime = packet["p"]
    gamma = numerator * pow(denominator, prime - 2, prime) % prime
    rows = [dict() for _ in range(count)]
    for i, j, value in packet["a"]:
        if i < count:
            add(rows[i], j, value, prime)
    for i, j, value in packet["b"]:
        if i < count:
            add(rows[i], j, gamma * value, prime)
    return rows


def row_basis(rows, prime: int):
    pivots = {}
    for source in rows:
        row = dict(source)
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, prime - 2, prime)
                pivots[pivot] = {
                    column: value * inverse % prime for column, value in row.items()
                }
                break
            for column, value in pivots[pivot].items():
                add(row, column, -coefficient * value, prime)
    return pivots


def reduce_modulo(row, pivots, prime: int):
    row = dict(row)
    for pivot in sorted(pivots, reverse=True):
        coefficient = row.get(pivot, 0)
        if coefficient:
            for column, value in pivots[pivot].items():
                add(row, column, -coefficient * value, prime)
    return row


def kernel(rows, width: int, prime: int):
    pivots = row_basis(rows, prime)
    free = [column for column in range(width) if column not in pivots]
    result = []
    for free_column in free:
        vector = {free_column: 1}
        for pivot in sorted(pivots):
            total = sum(
                value * vector.get(column, 0)
                for column, value in pivots[pivot].items()
                if column != pivot
            ) % prime
            if total:
                vector[pivot] = -total % prime
        result.append(vector)
    return result


def analyze(packet: dict, point: tuple[int, int]):
    prime = packet["p"]
    rows = rows_at(packet, *point, 756)
    source_basis = row_basis(rows[:720], prime)
    low_remainders = [reduce_modulo(row, source_basis, prime) for row in rows[720:]]
    coordinates = sorted(set().union(*(set(row) for row in low_remainders)))
    equations = [
        {index: row[column] for index, row in enumerate(low_remainders) if column in row}
        for column in coordinates
    ]
    relation_kernel = kernel(equations, 36, prime)
    by_degree = []
    for degree in range(8):
        selected = [
            row for row, label in zip(low_remainders, LOW_LABELS) if sum(label) <= degree
        ]
        by_degree.append(len(selected) - len(row_basis(selected, prime)))
    return {
        "prime": prime,
        "point": list(point),
        "source_rank": len(source_basis),
        "relative_rank": len(row_basis(low_remainders, prime)),
        "relation_dimension": len(relation_kernel),
        "relation_dimension_by_degree_0_through_7": by_degree,
        "kernel": [sorted(vector.items()) for vector in relation_kernel],
    }


def main() -> None:
    analyses = []
    intersections = []
    points = ((17, 1), (-5, 4), (-7, 4))
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        group = [analyze(packet, point) for point in points]
        analyses.extend(group)
        for left_index in range(3):
            for right_index in range(left_index + 1, 3):
                left, right = group[left_index], group[right_index]
                left_vectors = [dict(vector) for vector in left["kernel"]]
                right_vectors = [dict(vector) for vector in right["kernel"]]
                union_rank = len(row_basis(left_vectors + right_vectors, prime))
                dimension = (
                    left["relation_dimension"]
                    + right["relation_dimension"]
                    - union_rank
                )
                intersections.append(
                    {
                        "prime": prime,
                        "left": left["point"],
                        "right": right["point"],
                        "dimension_in_fixed_low_basis": dimension,
                    }
                )

    expected_filtrations = {
        (17, 1): [0, 0, 0, 0, 0, 0, 3, 10],
        (-5, 4): [0, 0, 0, 0, 0, 2, 9, 15],
        (-7, 4): [0, 0, 0, 0, 0, 2, 9, 17],
    }
    for analysis in analyses:
        assert analysis["source_rank"] == 479
        assert analysis["relation_dimension_by_degree_0_through_7"] == expected_filtrations[
            tuple(analysis["point"])
        ]
    assert [item["dimension_in_fixed_low_basis"] for item in intersections] == [5, 5, 6, 5, 5, 6]

    output = {
        "status": "pass",
        "low_basis": "monomials a^i b^j with i+j<=7, ordered by i then j",
        "analyses": [
            {key: value for key, value in analysis.items() if key != "kernel"}
            for analysis in analyses
        ],
        "intersections": intersections,
    }
    (RESULTS / "exponent_adapter_defect_filtration.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
