#!/usr/bin/env python3
"""Build a lossless labelled handoff packet for the K5 remainder adapter."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/benincasa/triangle-wall-cofinal-target-ambient13-labelled-residuals.json"
OUTPUT = ROOT / "research/benincasa/triangle-wall-residual-adapter-manifest.json"
PRIME = 32003


def rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for original in rows:
        row = {column: value % PRIME for column, value in original.items() if value % PRIME}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], PRIME - 2, PRIME)
                pivots[pivot] = {
                    column: value * inverse % PRIME for column, value in row.items()
                }
                break
            coefficient = row[pivot]
            for column, value in pivots[pivot].items():
                updated = (row.get(column, 0) - coefficient * value) % PRIME
                if updated:
                    row[column] = updated
                else:
                    row.pop(column, None)
    return len(pivots)


def label(term: dict) -> tuple:
    return (
        term["normal_block"],
        term["base_column"],
        term["k_pole"],
        tuple(term["q_levels"]),
        tuple(term["exponent"]),
    )


payload = json.loads(SOURCE.read_text())
probes = payload["probes"]
labels: dict[tuple, dict] = {}
incidence: dict[tuple, list[dict]] = defaultdict(list)
rows_by_tangent_block: dict[tuple[str, int], list[dict[int, int]]] = defaultdict(list)
full_rows_by_tangent: dict[str, list[dict[int, int]]] = defaultdict(list)

for probe in probes:
    split_rows: dict[int, dict[int, int]] = defaultdict(dict)
    full_row: dict[int, int] = {}
    for term in probe["terms"]:
        key = label(term)
        labels.setdefault(
            key,
            {
                "normal_block": term["normal_block"],
                "base_column": term["base_column"],
                "k_pole": term["k_pole"],
                "q_levels": term["q_levels"],
                "exponent": term["exponent"],
                "total_fiber_degree": term["total_fiber_degree"],
            },
        )
        incidence[key].append(
            {
                "tangent": probe["tangent"],
                "source_basis_index": probe["source_basis_index"],
                "value": term["value"],
            }
        )
        split_rows[term["normal_block"]][term["base_column"]] = term["value"]
        full_row[term["column"]] = term["value"]
    full_rows_by_tangent[probe["tangent"]].append(full_row)
    for block in range(3):
        rows_by_tangent_block[(probe["tangent"], block)].append(split_rows[block])

ordered = sorted(labels)
label_ids = {key: index for index, key in enumerate(ordered)}
manifest_labels = []
for key in ordered:
    item = dict(labels[key])
    item["label_id"] = label_ids[key]
    item["incidence"] = sorted(
        incidence[key], key=lambda value: (value["tangent"], value["source_basis_index"])
    )
    manifest_labels.append(item)

block_ranks = {}
for block in range(3):
    t1 = rows_by_tangent_block[("T1", block)]
    t2 = rows_by_tangent_block[("T2", block)]
    block_ranks[str(block)] = {
        "label_count": sum(1 for key in ordered if key[0] == block),
        "t1": rank(t1),
        "t2": rank(t2),
        "combined": rank(t1 + t2),
        "intersection": rank(t1) + rank(t2) - rank(t1 + t2),
    }

block_one_pair_ratios = []
for left, right in zip(
    rows_by_tangent_block[("T1", 1)], rows_by_tangent_block[("T2", 1)]
):
    common = sorted(set(left) & set(right))
    ratio = None
    if common:
        pivot = common[0]
        ratio = right[pivot] * pow(left[pivot], PRIME - 2, PRIME) % PRIME
        if any(right.get(column, 0) != ratio * value % PRIME for column, value in left.items()):
            ratio = None
        if any(column not in left and value for column, value in right.items()):
            ratio = None
    block_one_pair_ratios.append(ratio)

coordinate_rows = [dict(probe["coordinates"]) for probe in probes]
coordinate_rows_with_graph_value = []
for probe, row in zip(probes, coordinate_rows):
    augmented = dict(row)
    graph_value = next(
        (
            term["value"]
            for term in probe["terms"]
            if term["normal_block"] == 1
        ),
        0,
    )
    if graph_value:
        augmented[1_000_000] = graph_value
    coordinate_rows_with_graph_value.append(augmented)

result = {
    "schema": "marici.triangle-wall-residual-adapter-manifest.v1",
    "field_prime": PRIME,
    "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
    "probe_count": len(probes),
    "label_count": len(manifest_labels),
    "block_ranks": block_ranks,
    "block_one_paired_ratios_t2_over_t1": block_one_pair_ratios,
    "projection_to_block_zero": {
        "full_rank": rank(full_rows_by_tangent["T1"] + full_rows_by_tangent["T2"]),
        "projected_rank": block_ranks["0"]["combined"],
        "kernel_dimension": rank(
            full_rows_by_tangent["T1"] + full_rows_by_tangent["T2"]
        )
        - block_ranks["0"]["combined"],
        "graph_functional_support": [
            {
                "tangent": tangent,
                "source_basis_index": source_basis_index,
                "value": value,
            }
            for tangent, source_basis_index, value in (
                (entry["tangent"], entry["source_basis_index"], entry["value"])
                for entry in next(
                    item for item in manifest_labels if item["normal_block"] == 1
                )["incidence"]
            )
        ],
    },
    "quadratic_coordinate_descent": {
        "coordinate_rank": rank(coordinate_rows),
        "rank_with_graph_value": rank(coordinate_rows_with_graph_value),
        "graph_functional_factors": rank(coordinate_rows)
        == rank(coordinate_rows_with_graph_value),
    },
    "labels": manifest_labels,
    "acceptance_gate": (
        "A jet-level adapter must account for every label_id and preserve normal_block, "
        "tangent, source_basis_index, and coefficient incidence."
    ),
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: result[key] for key in ("probe_count", "label_count", "block_ranks")}))
