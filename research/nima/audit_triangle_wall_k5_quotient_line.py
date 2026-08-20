"""Audit the Entry-1063 quotient line after labelled K5 inclusion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

P = 32003


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def rref(rows: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    matrix = [[value % P for value in row] for row in rows]
    pivots: list[int] = []
    pivot_row = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        selected = next(
            (index for index in range(pivot_row, len(matrix)) if matrix[index][column]),
            None,
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        scale = inv(matrix[pivot_row][column])
        matrix[pivot_row] = [(scale * value) % P for value in matrix[pivot_row]]
        for index, row in enumerate(matrix):
            if index == pivot_row or not row[column]:
                continue
            factor = row[column]
            matrix[index] = [
                (left - factor * right) % P
                for left, right in zip(row, matrix[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return matrix, pivots


def nullspace(matrix: list[list[int]]) -> list[list[int]]:
    reduced, pivots = rref(matrix)
    width = len(matrix[0]) if matrix else 0
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for column in free:
        vector = [0] * width
        vector[column] = 1
        for row_index, pivot in enumerate(pivots):
            vector[pivot] = (-reduced[row_index][column]) % P
        basis.append(vector)
    return basis


def rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        row = {key: value % P for key, value in source.items() if value % P}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                scale = inv(row[pivot])
                pivots[pivot] = {key: value * scale % P for key, value in row.items()}
                break
            factor = row[pivot]
            for key, value in pivots[pivot].items():
                next_value = (row.get(key, 0) - factor * value) % P
                if next_value:
                    row[key] = next_value
                else:
                    row.pop(key, None)
    return len(pivots)


def combine(coefficients: list[int], rows: list[dict[int, int]]) -> dict[int, int]:
    result: dict[int, int] = {}
    for coefficient, row in zip(coefficients, rows):
        for column, value in row.items():
            result[column] = (result.get(column, 0) + coefficient * value) % P
            if not result[column]:
                del result[column]
    return result


def main() -> None:
    global P
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-coordinates", type=Path, required=True)
    parser.add_argument("--target-result", type=Path, required=True)
    parser.add_argument("--prime", type=int, default=P)
    parser.add_argument(
        "--target-source-indices",
        help="Comma-separated original probe indices when zero source rows were omitted.",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    P = args.prime

    source = json.loads(args.source_coordinates.read_text(encoding="utf-8"))
    target = json.loads(args.target_result.read_text(encoding="utf-8"))
    coordinate_rows = source.get("probe_file", source.get("probes"))
    if coordinate_rows is None:
        raise ValueError("source packet has neither probe_file nor probes")
    coordinate_width = 1 + max(
        index for probe in coordinate_rows for index, _ in probe["coordinates"]
    )
    coordinates = [
        {index: value % P for index, value in probe["coordinates"]}
        for probe in coordinate_rows
    ]
    # Relations among the 26 row vectors are null vectors of C^T.
    transpose = [
        [coordinates[probe].get(column, 0) for probe in range(len(coordinates))]
        for column in range(coordinate_width)
    ]
    kernel = nullspace(transpose)
    lambda_row = [0] * len(coordinates)
    if "probes" in source:
        for index, probe in enumerate(coordinate_rows):
            lambda_row[index] = next(
                (
                    term["value"] % P
                    for term in probe.get("terms", [])
                    if term.get("normal_block") == 1
                ),
                0,
            )
    else:
        # Legacy cofinal packet: the sole first-normal label occurs in rows 6 and 19.
        lambda_row[6] = 10
        lambda_row[19] = 10
    lambda_values = [
        sum(left * right for left, right in zip(lambda_row, relation)) % P
        for relation in kernel
    ]
    nonzero_index = next(index for index, value in enumerate(lambda_values) if value)
    representative = [
        value * inv(lambda_values[nonzero_index]) % P
        for value in kernel[nonzero_index]
    ]
    graph_zero = []
    for index, relation in enumerate(kernel):
        if index == nonzero_index:
            continue
        correction = lambda_values[index]
        graph_zero.append(
            [
                (value - correction * base) % P
                for value, base in zip(relation, representative)
            ]
        )

    captured_target_rows = [
        {column: value % P for column, value in probe["remainder"]}
        for probe in target["probe_file"]
    ]
    if args.target_source_indices:
        source_indices = [int(value) for value in args.target_source_indices.split(",")]
        if len(source_indices) != len(captured_target_rows):
            raise ValueError("target-source-indices length does not match captured probes")
        target_rows = [{} for _ in coordinates]
        for source_index, row in zip(source_indices, captured_target_rows):
            target_rows[source_index] = row
    else:
        target_rows = captured_target_rows
    if len(target_rows) != len(coordinates):
        raise ValueError("target and source probe counts differ; provide --target-source-indices")
    zero_images = [combine(relation, target_rows) for relation in graph_zero]
    representative_image = combine(representative, target_rows)
    zero_rank = rank(zero_images)
    augmented_rank = rank([*zero_images, representative_image])
    width = target["column_count"]
    block_counts: dict[int, int] = {}
    for column in representative_image:
        block = column // width
        block_counts[block] = block_counts.get(block, 0) + 1

    result = {
        "schema": "marici.triangle-wall-k5-quotient-line-audit.v1",
        "field_prime": P,
        "probe_count": len(coordinates),
        "coordinate_rank": len(coordinates) - len(kernel),
        "coordinate_relation_dimension": len(kernel),
        "graph_zero_relation_dimension": len(graph_zero),
        "graph_zero_image_rank": zero_rank,
        "augmented_image_rank": augmented_rank,
        "quotient_line_image_rank": augmented_rank - zero_rank,
        "representative_image_terms": len(representative_image),
        "representative_image_normal_block_counts": block_counts,
        "no_block_two": all(column // width < 2 for row in target_rows for column in row),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
