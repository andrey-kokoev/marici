#!/usr/bin/env python3
"""Derive the first source-jet recurrence omitted by the rank-26 word basis."""

import contextlib
import importlib
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    words = importlib.import_module("derive_rank26_source_word_basis")


def solve_columns(columns, target, prime):
    coordinates = sorted(set(target).union(*(column.keys() for column in columns)))
    rows = [[column.get(key, 0) % prime for column in columns] + [target.get(key, 0) % prime] for key in coordinates]
    pivot_row = 0
    pivot_columns = []
    for column in range(len(columns)):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, prime)
        rows[pivot_row] = [value * inverse % prime for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [(rows[row][j] - factor * rows[pivot_row][j]) % prime for j in range(len(rows[row]))]
        pivot_columns.append(column)
        pivot_row += 1
    if any(all(row[column] == 0 for column in range(len(columns))) and row[-1] != 0 for row in rows):
        raise RuntimeError("third derivative is outside the source-word span")
    if len(pivot_columns) != len(columns):
        raise RuntimeError("source-word columns are not independent")
    solution = [0] * len(columns)
    for row, column in enumerate(pivot_columns):
        solution[column] = rows[row][-1]
    return solution


def run(point, descriptors):
    pres = words.presentation(point)
    roots = dict(words.root_rows(pres, point))
    columns = [
        words.base.reduce_row(words.evaluate_descriptor(pres, point, descriptor), pres["pivots"])
        for descriptor in descriptors
    ]
    target = words.base.reduce_row(roots["D2"], pres["pivots"])
    coefficients = solve_columns(columns, target, words.base.PRIME)
    inverse_p3 = pow(point[2], -1, words.base.PRIME)
    expected = [
        28 * inverse_p3 % words.base.PRIME,
        -point[0] * inverse_p3 % words.base.PRIME,
        -point[1] * inverse_p3 % words.base.PRIME,
    ] + [0] * (len(descriptors) - 3)
    reconstruction = {}
    for coefficient, column in zip(coefficients, columns):
        for key, value in column.items():
            words.base.add_value(reconstruction, key, coefficient * value)
    assert words.base.reduce_row(reconstruction, pres["pivots"]) == target
    return {
        "point": list(point),
        "nonzero_coefficient_count": sum(value != 0 for value in coefficients),
        "coefficients": coefficients,
        "matches_degree_28_euler_relation": coefficients == expected,
    }


def main():
    packet = json.loads(Path(words.__file__).with_name("rank26-source-word-basis.json").read_text())
    descriptors = packet["descriptors"]
    points = [tuple(packet["reference_point"])] + [tuple(item["point"]) for item in packet["control_ranks"]]
    runs = [run(point, descriptors) for point in points]
    checks = {
        "all_three_points_have_a_unique_recurrence": len(runs) == 3,
        "third_derivative_is_not_itself_a_basis_root": all(
            descriptor["root"] != "D2" for descriptor in descriptors
        ),
        "all_recurrences_are_nonzero": all(item["nonzero_coefficient_count"] > 0 for item in runs),
        "all_recurrences_are_the_degree_28_euler_relation": all(
            item["matches_degree_28_euler_relation"] for item in runs
        ),
    }
    result = {
        "schema": "marici.rank26_third_source_derivative_recurrence.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "field": words.base.PRIME,
        "descriptor_order": descriptors,
        "runs": runs,
        "checks": checks,
        "interpretation": (
            "The unique recurrence is P1^2 D0 + P2^2 D1 + P3^2 D2 = 28 S. For any dual readout, "
            "the same Euler identity holds among the four physical period jets. This is the first finite recurrence "
            "that a characteristic-zero Leray evaluation must reproduce."
        ),
    }
    output = Path(__file__).with_name("rank26-third-source-derivative-recurrence.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
