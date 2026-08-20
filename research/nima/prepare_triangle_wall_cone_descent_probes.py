"""Prepare quotient and old-image probes for adjacent K-pole cones."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

P = 32003


def dense(entries: list[list[int]], width: int) -> list[int]:
    row = [0] * width
    for column, value in entries:
        row[column] = value % P
    return row


def pivots(rows: list[list[int]]) -> list[int]:
    work = [row[:] for row in rows]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(work[0])):
        found = next((i for i in range(pivot_row, len(work)) if work[i][column]), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        inverse = pow(work[pivot_row][column], P - 2, P)
        work[pivot_row] = [(value * inverse) % P for value in work[pivot_row]]
        for i, row in enumerate(work):
            if i == pivot_row or not row[column]:
                continue
            factor = row[column]
            work[i] = [(a - factor * b) % P for a, b in zip(row, work[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_columns


def inverse(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    work = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        found = next((i for i in range(column, n) if work[i][column]), None)
        if found is None:
            raise ValueError("self-coordinate matrix is singular")
        work[column], work[found] = work[found], work[column]
        scale = pow(work[column][column], P - 2, P)
        work[column] = [(value * scale) % P for value in work[column]]
        for i in range(n):
            if i == column or not work[i][column]:
                continue
            factor = work[i][column]
            work[i] = [(a - factor * b) % P for a, b in zip(work[i], work[column])]
    return [row[n:] for row in work]


def multiply(left: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        sum(left[i] * matrix[i][j] for i in range(len(left))) % P
        for j in range(len(matrix[0]))
    ]


def parse_sparse(line: str) -> dict[int, int]:
    return {
        int(column): int(value) % P
        for term in line.split(",")
        if term
        for column, value in [term.split(":", 1)]
    }


def combine(coefficients: list[int], rows: list[dict[int, int]]) -> dict[int, int]:
    out: dict[int, int] = {}
    for coefficient, row in zip(coefficients, rows):
        if not coefficient:
            continue
        for column, value in row.items():
            out[column] = (out.get(column, 0) + coefficient * value) % P
    return {column: value for column, value in out.items() if value}


def render(row: dict[int, int]) -> str:
    return ",".join(f"{column}:{value}" for column, value in sorted(row.items()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("coordinates_result")
    parser.add_argument("shifted_basis_probes")
    parser.add_argument("output")
    parser.add_argument("--metadata")
    parser.add_argument("--old-count", type=int, default=7)
    parser.add_argument("--basis-count", type=int, default=13)
    parser.add_argument("--mode-count", type=int, default=2)
    args = parser.parse_args()

    result = json.loads(Path(args.coordinates_result).read_text(encoding="utf-8"))
    probes = result["probe_file"]
    old_rows = [dense(item["coordinates"], args.basis_count) for item in probes[: args.old_count]]
    self_rows = [
        dense(item["coordinates"], args.basis_count)
        for item in probes[args.old_count : args.old_count + args.basis_count]
    ]
    if any(item["remainder_terms"] for item in probes[: args.old_count + args.basis_count]):
        raise ValueError("inclusion/self coordinate packet has nonzero remainders")
    self_inverse = inverse(self_rows)
    image_pivots = pivots(old_rows)
    quotient_columns = [column for column in range(args.basis_count) if column not in image_pivots]

    shifted_lines = [
        parse_sparse(line)
        for line in Path(args.shifted_basis_probes).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(shifted_lines) != args.mode_count * args.basis_count:
        raise ValueError("shifted basis probe count does not match declared modes")

    output_rows = []
    block_metadata = []
    for mode in range(args.mode_count):
        shifted = shifted_lines[mode * args.basis_count : (mode + 1) * args.basis_count]
        quotient_coefficients = [self_inverse[column] for column in quotient_columns]
        image_coefficients = [multiply(row, self_inverse) for row in old_rows]
        mode_rows = [combine(coefficients, shifted) for coefficients in quotient_coefficients + image_coefficients]
        output_rows.extend(mode_rows)
        block_metadata.append(
            {
                "mode_index": mode,
                "quotient_probe_count": len(quotient_coefficients),
                "old_image_probe_count": len(image_coefficients),
            }
        )

    Path(args.output).write_text("\n".join(render(row) for row in output_rows) + "\n", encoding="utf-8")
    metadata = {
        "schema": "marici.triangle-wall-cone-descent-probes.v1",
        "field": P,
        "source_dimension": args.basis_count,
        "old_image_rank": len(image_pivots),
        "image_pivot_columns": image_pivots,
        "quotient_coordinate_columns": quotient_columns,
        "blocks": block_metadata,
        "output_probe_count": len(output_rows),
    }
    if args.metadata:
        Path(args.metadata).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
