"""Export exact sparse triangle-wall relation rows for the Rust rank engine."""

import argparse
import contextlib
import importlib
import io
import struct
from pathlib import Path

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


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, required=True)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument(
    "--wall",
    choices=("x3", "x2"),
    default="x3",
    help="normal wall: x3=x1+x2 or its X2/X3 occurrence-reflected mate",
)
args = parser.parse_args()
nodes = tuple(range(-3, 4))


def normal_fiber(offset):
    if args.wall == "x3":
        return (2, 3, 5 + offset)
    return (2, 5 + offset, 3)


def capture_fiber(fiber, ambient):
    rows = []
    original = base.add_pivot

    def hook(row, pivots):
        rows.append(dict(row))
        original(row, pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    base.add_pivot = hook
    try:
        presentation = charts.presentation(base.fiber_data, fiber, charts.SOURCE_NAMES)
    finally:
        base.add_pivot = original
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    return presentation, rows


packets = [capture_fiber(normal_fiber(offset), args.ambient) for offset in nodes]
presentation, central_rows = packets[3]
row_packets = [packet[1] for packet in packets]
if len(set(map(len, row_packets))) != 1:
    raise RuntimeError("raw relation row counts do not agree")

def coefficient_weights(order):
    weights = []
    for node in nodes:
        polynomial = [1]
        denominator = 1
        for other in nodes:
            if other == node:
                continue
            next_polynomial = [0] * (len(polynomial) + 1)
            for degree, coefficient in enumerate(polynomial):
                next_polynomial[degree] = (next_polynomial[degree] - other * coefficient) % P
                next_polynomial[degree + 1] = (next_polynomial[degree + 1] + coefficient) % P
            polynomial = next_polynomial
            denominator = denominator * (node - other) % P
        weights.append(polynomial[order] * pow(denominator, P - 2, P) % P)
    return weights

first_weights = coefficient_weights(1)
second_weights = coefficient_weights(2)
derivative_rows = []
second_rows = []
for index in range(len(central_rows)):
    derivative = {}
    second = {}
    for rows, weight in zip(row_packets, first_weights):
        for column, value in rows[index].items():
            base.add_value(derivative, column, weight * value)
    for rows, weight in zip(row_packets, second_weights):
        for column, value in rows[index].items():
            base.add_value(second, column, weight * value)
    derivative_rows.append(derivative)
    second_rows.append(second)

with args.output.open("wb") as stream:
    stream.write(b"MRCIDR02")
    stream.write(struct.pack("<IIIII", P, args.ambient, len(presentation["ordered_columns"]), len(central_rows), len(presentation["pivots"])))
    for central, derivative, second in zip(central_rows, derivative_rows, second_rows):
        for row in (central, derivative, second):
            stream.write(struct.pack("<I", len(row)))
            for column, value in sorted(row.items()):
                stream.write(struct.pack("<II", column, value % P))

print(f"wall={args.wall} ambient={args.ambient} columns={len(presentation['ordered_columns'])} rows={len(central_rows)} central_rank={len(presentation['pivots'])} output={args.output}")
