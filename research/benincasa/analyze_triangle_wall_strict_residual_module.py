"""Exact module census for Entry 1059's strict ambient-13 remainders."""

from __future__ import annotations

import json
from pathlib import Path

P = 32003
ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/benincasa/triangle-wall-cofinal-target-ambient13-labelled-residuals.json"
OUTPUT = ROOT / "research/benincasa/triangle-wall-strict-residual-module.json"


def sparse_rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        row = {column: value % P for column, value in source.items() if value % P}
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, P - 2, P)
                pivots[pivot] = {
                    column: value * inverse % P for column, value in row.items()
                }
                break
            existing = pivots[pivot]
            for column, value in existing.items():
                updated = (row.get(column, 0) - coefficient * value) % P
                if updated:
                    row[column] = updated
                else:
                    row.pop(column, None)
    return len(pivots)


def proportional(left: dict[int, int], right: dict[int, int]) -> int | None:
    if set(left) != set(right) or not left:
        return None
    pivot = max(left)
    ratio = right[pivot] * pow(left[pivot], P - 2, P) % P
    return ratio if all(right[key] % P == ratio * value % P for key, value in left.items()) else None


packet = json.loads(INPUT.read_text())
probes = packet["probes"]

remainders = [
    {term["column"]: term["value"] for term in probe["terms"]} for probe in probes
]
coordinates = [
    {index: value for index, value in probe["coordinates"]} for probe in probes
]
t1, t2 = remainders[:13], remainders[13:]
c1, c2 = coordinates[:13], coordinates[13:]
differences = [
    {
        column: (right.get(column, 0) - left.get(column, 0)) % P
        for column in set(left) | set(right)
        if (right.get(column, 0) - left.get(column, 0)) % P
    }
    for left, right in zip(t1, t2)
]
coordinate_differences = [
    {
        column: (right.get(column, 0) - left.get(column, 0)) % P
        for column in set(left) | set(right)
        if (right.get(column, 0) - left.get(column, 0)) % P
    }
    for left, right in zip(c1, c2)
]

paired_ratios = [proportional(left, right) for left, right in zip(t1, t2)]
support_t1 = set().union(*(set(row) for row in t1))
support_t2 = set().union(*(set(row) for row in t2))

result = {
    "schema": "marici.triangle-wall-strict-residual-module.v1",
    "field_prime": P,
    "source": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
    "ranks": {
        "t1": sparse_rank(t1),
        "t2": sparse_rank(t2),
        "combined": sparse_rank(remainders),
        "paired_differences": sparse_rank(differences),
        "coordinates_t1": sparse_rank(c1),
        "coordinates_t2": sparse_rank(c2),
        "coordinates_combined": sparse_rank(coordinates),
        "coordinate_paired_differences": sparse_rank(coordinate_differences),
    },
    "intersection_dimensions": {
        "remainder_t1_t2": sparse_rank(t1) + sparse_rank(t2) - sparse_rank(remainders),
        "coordinate_t1_t2": sparse_rank(c1) + sparse_rank(c2) - sparse_rank(coordinates),
    },
    "supports": {
        "t1_columns": len(support_t1),
        "t2_columns": len(support_t2),
        "intersection_columns": len(support_t1 & support_t2),
        "union_columns": len(support_t1 | support_t2),
        "t1_only_columns": sorted(support_t1 - support_t2),
        "t2_only_columns": sorted(support_t2 - support_t1),
    },
    "paired_proportional_ratios": paired_ratios,
    "paired_exact_equal": [left == right for left, right in zip(t1, t2)],
    "coordinate_paired_exact_equal": [left == right for left, right in zip(c1, c2)],
    "interpretation_gate": (
        "Ranks and support overlap classify the finite residual module only; "
        "they do not define its next target map or direct-limit fate."
    ),
}

OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, sort_keys=True))
