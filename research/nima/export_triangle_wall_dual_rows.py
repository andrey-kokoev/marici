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


def capture_fiber(fiber, point, names, ambient):
    rows = []
    original = base.add_pivot

    def hook(row, pivots):
        rows.append(dict(row))
        original(row, pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    base.add_pivot = hook
    try:
        presentation = charts.presentation(fiber, point, names)
    finally:
        base.add_pivot = original
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    return presentation, rows


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, required=True)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--x1", type=int, default=2, help="first tangential wall coordinate")
parser.add_argument("--x2", type=int, default=3, help="second tangential wall coordinate")
parser.add_argument(
    "--wall",
    choices=("x3", "x2", "x2_typed"),
    default="x3",
    help="normal wall: x3=x1+x2 or its X2/X3 occurrence-reflected mate",
)
parser.add_argument(
    "--partner-first",
    action="store_true",
    help="place the fifth marked-divisor relation family before the other four",
)
parser.add_argument(
    "--marked-last",
    type=int,
    choices=range(5),
    help="place the selected marked relation family last (0=g1,...,4=g31)",
)
parser.add_argument(
    "--marked-mask",
    type=lambda value: int(value, 0),
    help="retain exactly this five-bit subset of marked relation families",
)
args = parser.parse_args()
nodes = tuple(range(-3, 4))


def normal_fiber(offset):
    if args.wall == "x3":
        return (args.x1, args.x2, args.x1 + args.x2 + offset)
    return (args.x1, args.x1 + args.x2 + offset, args.x2)


if args.wall == "x2_typed":
    packets = [
        capture_fiber(
            charts.g31_fiber_data, normal_fiber(offset), charts.TARGET_NAMES, args.ambient
        )
        for offset in nodes
    ]
else:
    packets = [
        capture_fiber(base.fiber_data, normal_fiber(offset), charts.SOURCE_NAMES, args.ambient)
        for offset in nodes
    ]
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

de_rham_count = 4 * len(base.monomials_at_most(args.ambient))
principal_count = 64 * len(base.monomials_at_most(args.ambient - 4))
marked_count = 48 * len(base.monomials_at_most(args.ambient - 1))
family_bounds = [de_rham_count, de_rham_count + principal_count]
family_bounds.extend(
    de_rham_count + principal_count + marked_count * (index + 1)
    for index in range(5)
)
if family_bounds[-1] != len(central_rows):
    raise RuntimeError("relation-family row census does not agree")
if sum(value is not None for value in (args.marked_last, args.marked_mask)) + args.partner_first > 1:
    raise RuntimeError("relation-family ordering/filter options are mutually exclusive")
marked_start = family_bounds[1]
marked_blocks = [
    list(range(marked_start + index * marked_count, marked_start + (index + 1) * marked_count))
    for index in range(5)
]
order = list(range(len(central_rows)))
if args.partner_first:
    order = list(range(marked_start)) + marked_blocks[4] + [row for block in marked_blocks[:4] for row in block]
elif args.marked_last is not None:
    marked_order = [index for index in range(5) if index != args.marked_last] + [args.marked_last]
    order = list(range(marked_start)) + [row for index in marked_order for row in marked_blocks[index]]
elif args.marked_mask is not None:
    if not 0 <= args.marked_mask < 32:
        raise RuntimeError("--marked-mask must be between 0 and 31")
    order = list(range(marked_start)) + [
        row for index, block in enumerate(marked_blocks) if args.marked_mask & (1 << index) for row in block
    ]

with args.output.open("wb") as stream:
    stream.write(b"MRCIDR03")
    stream.write(struct.pack("<IIIII", P, args.ambient, len(presentation["ordered_columns"]), len(order), 0))
    for output_index, index in enumerate(order):
        central, derivative, second = central_rows[index], derivative_rows[index], second_rows[index]
        if (args.partner_first or args.marked_last is not None) and output_index >= family_bounds[1]:
            family = 2 + (output_index - family_bounds[1]) // marked_count
        elif args.marked_mask is not None and output_index >= marked_start:
            original_family = next(
                family_index
                for family_index, block in enumerate(marked_blocks)
                if block[0] <= index <= block[-1]
            )
            family = 2 + original_family
        else:
            family = next(i for i, bound in enumerate(family_bounds) if output_index < bound)
        stream.write(struct.pack("<I", family))
        for row in (central, derivative, second):
            stream.write(struct.pack("<I", len(row)))
            for column, value in sorted(row.items()):
                stream.write(struct.pack("<II", column, value % P))

print(f"wall={args.wall} ambient={args.ambient} columns={len(presentation['ordered_columns'])} rows={len(order)} output={args.output}")
