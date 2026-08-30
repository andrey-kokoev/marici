"""Test mixed-direction path independence of the labelled GM adapters."""

from __future__ import annotations

import json
import os
from pathlib import Path

import check_adapted_true_covariant_source_jets as adapted
import check_cutoff_inclusion_gauss_manin_adapter as adapter


source = adapted.source
jets = adapted.jets
P = source.P
POINT = tuple(int(value) for value in os.environ.get("MARICI_JET_POINT", "2,3,-4").split(","))
SOURCE_AMBIENT = 8
SOURCE_K_DEPTH = source.rees.charts.K_DEPTH
SOURCE_Q_DEPTHS = [source.rees.charts.Q_DEPTH] * len(source.rees.NAMES)
INCIDENCE = {
    0: {"g2", "g23"},
    1: {"g1", "g31"},
    2: {"g1", "g2", "g3"},
}


def ordered(columns):
    result = [None] * len(columns)
    for label, column in columns.items():
        result[column] = label
    return result


def shifted_depths(*axes):
    return [
        SOURCE_Q_DEPTHS[i] + sum(source.rees.NAMES[i] in INCIDENCE[axis] for axis in axes)
        for i in range(len(source.rees.NAMES))
    ]


def embed(row, source_ordered, target_columns):
    return {target_columns[source_ordered[column]]: value for column, value in row.items()}


def subtract(left, right):
    result = dict(left)
    for column, value in right.items():
        next_value = jets.jadd(result.get(column, {}), value, -1)
        if next_value:
            result[column] = next_value
        else:
            result.pop(column, None)
    return result


def main():
    _, source_columns = adapter.packet(SOURCE_AMBIENT, SOURCE_K_DEPTH, SOURCE_Q_DEPTHS)
    source_ordered = ordered(source_columns)
    k, q = jets.fiber_data(POINT)
    pair_results = {}
    for first, second in ((0, 1), (0, 2), (1, 2)):
        first_q = shifted_depths(first)
        second_q = shifted_depths(second)
        final_q = shifted_depths(first, second)
        _, first_columns = adapter.packet(SOURCE_AMBIENT + 4, SOURCE_K_DEPTH + 1, first_q)
        _, second_columns = adapter.packet(SOURCE_AMBIENT + 4, SOURCE_K_DEPTH + 1, second_q)
        _, final_columns = adapter.packet(SOURCE_AMBIENT + 8, SOURCE_K_DEPTH + 2, final_q)
        first_ordered = ordered(first_columns)
        second_ordered = ordered(second_columns)
        final_ordered = ordered(final_columns)
        nonzero = []
        for source_column, label in enumerate(source_ordered):
            unit = {source_column: jets.jconstant(1)}

            row_first = embed(unit, source_ordered, first_columns)
            row_first = adapted.covariant(
                row_first, first, first_ordered, first_columns, k, q, SOURCE_K_DEPTH + 1, first_q
            )
            row_first = embed(row_first, first_ordered, final_columns)
            route_first_second = adapted.covariant(
                row_first, second, final_ordered, final_columns, k, q, SOURCE_K_DEPTH + 2, final_q
            )

            row_second = embed(unit, source_ordered, second_columns)
            row_second = adapted.covariant(
                row_second, second, second_ordered, second_columns, k, q, SOURCE_K_DEPTH + 1, second_q
            )
            row_second = embed(row_second, second_ordered, final_columns)
            route_second_first = adapted.covariant(
                row_second, first, final_ordered, final_columns, k, q, SOURCE_K_DEPTH + 2, final_q
            )

            commutator = jets.center(subtract(route_first_second, route_second_first))
            if commutator:
                nonzero.append({"source_column": source_column, "source_label": label, "term_count": len(commutator)})
        key = f"{first}{second}"
        pair_results[key] = {
            "axes": [first, second],
            "first_target_q_depths": dict(zip(source.rees.NAMES, first_q, strict=True)),
            "second_target_q_depths": dict(zip(source.rees.NAMES, second_q, strict=True)),
            "least_common_target_q_depths": dict(zip(source.rees.NAMES, final_q, strict=True)),
            "least_common_target_ambient": SOURCE_AMBIENT + 8,
            "least_common_target_K_depth": SOURCE_K_DEPTH + 2,
            "source_column_tests": len(source_columns),
            "nonzero_literal_commutators": len(nonzero),
            "first_nonzero_examples": nonzero[:10],
        }
    assert all(item["nonzero_literal_commutators"] == 0 for item in pair_results.values())
    result = {
        "schema": "marici.benincasa.directional-adapter-mixed-paths.v1",
        "status": "passed",
        "field": P,
        "point": list(POINT),
        "source_column_count": len(source_columns),
        "directional_incidence": {str(axis): sorted(names) for axis, names in INCIDENCE.items()},
        "mixed_pairs": pair_results,
        "classification": "all mixed directional adapters commute literally on every labelled source basis column before quotient reduction",
    }
    suffix = "-".join(f"m{-value}" if value < 0 else str(value) for value in POINT)
    output_name = "directional-adapter-mixed-paths.json" if POINT == (2, 3, -4) else f"directional-adapter-mixed-paths-point-{suffix}.json"
    output = Path(__file__).with_name(output_name)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
