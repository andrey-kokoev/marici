"""Compute the first-normal rank of the triangle-wall relation module."""

import argparse
import contextlib
import importlib
import io
import json

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = audit.base, audit.charts
P = base.PRIME


def capture(z, ambient):
    rows = []
    original = base.add_pivot

    def hook(row, pivots):
        rows.append(dict(row))
        original(row, pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    base.add_pivot = hook
    try:
        presentation = charts.presentation(base.fiber_data, (2, 3, z), charts.SOURCE_NAMES)
    finally:
        base.add_pivot = original
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    return presentation, rows


def calculate(ambient):
    packets = [capture(5 + offset, ambient) for offset in (-2, -1, 0, 1, 2)]
    presentation, central_rows = packets[2]
    row_packets = [packet[1] for packet in packets]
    if len(set(map(len, row_packets))) != 1:
        raise RuntimeError("raw relation row counts do not agree")
    weights = (1, -8, 0, 8, -1)
    inverse_twelve = pow(12, P - 2, P)
    column_count = len(presentation["ordered_columns"])
    block_pivots = {}
    original = base.add_pivot
    for index, central in enumerate(central_rows):
        normal_derivative = {}
        for rows, weight in zip(row_packets, weights):
            for column, value in rows[index].items():
                base.add_value(normal_derivative, column, weight * value * inverse_twelve)
        first_row = dict(central)
        for column, value in normal_derivative.items():
            base.add_value(first_row, column_count + column, value)
        original(first_row, block_pivots)
        original({column_count + column: value for column, value in central.items()}, block_pivots)
    central_rank = len(presentation["pivots"])
    return {
        "ambient_relation_degree": ambient,
        "column_count": column_count,
        "raw_relation_row_count": len(central_rows),
        "central_relation_rank": central_rank,
        "dual_block_rank": len(block_pivots),
        "first_normal_rank": len(block_pivots) - 2 * central_rank,
    }


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, required=True)
args = parser.parse_args()
print(json.dumps(calculate(args.ambient), indent=2))
