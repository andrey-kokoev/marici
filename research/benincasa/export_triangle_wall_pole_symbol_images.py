"""Export provisional depth-three-to-four pole-raising images.

The source rows use the pole-extension stage-two ordering from
``export_triangle_wall_dual_rows.py``.  Each image retains only the naive
degree-plus-one operation obtained by multiplying a source relation by
``(gamma-k) T(K)`` and raising its Cayley--Menger pole index.  It is evaluated
on seven normal fibers and interpolated through second normal order.

Reduction by ``triangle_wall_dual_rank`` is the typing gate: a nonzero
remainder means that this provisional operation does not descend to the
depth-four exact-valuation object.  No connection morphism is assumed.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "research" / "nima"
sys.path.insert(0, str(NIMA))

with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module(
        "check_unbounded_twisted_derham_connection_commutator"
    )

base, charts = source.base, source.charts
P = source.P
NAMES = source.NAMES
GAMMA = source.GAMMA
NODES = tuple(range(-3, 4))


def add(row, key, value):
    base.add_value(row, key, value % P)


def coefficient_weights(order):
    weights = []
    for node in NODES:
        polynomial = [1]
        denominator = 1
        for other in NODES:
            if other == node:
                continue
            nxt = [0] * (len(polynomial) + 1)
            for degree, coefficient in enumerate(polynomial):
                nxt[degree] = (nxt[degree] - other * coefficient) % P
                nxt[degree + 1] = (nxt[degree + 1] + coefficient) % P
            polynomial = nxt
            denominator = denominator * (node - other) % P
        weights.append(polynomial[order] * pow(denominator, P - 2, P) % P)
    return weights


WEIGHTS = [coefficient_weights(order) for order in range(3)]


def descriptors(ambient):
    levels_all = list(product(range(1, 3), repeat=len(NAMES)))
    de_rham = []
    for k_pole in range(3):
        levels = (1,) * len(NAMES)
        for axis in range(2):
            for exponent in base.monomials_at_most(ambient):
                de_rham.append(("de_rham", k_pole, levels, exponent, axis))

    principal = []
    for k_pole in range(3):
        for levels in levels_all:
            for exponent in base.monomials_at_most(ambient - 4):
                principal.append(("principal", k_pole, levels, exponent, None))

    marked = []
    for marked_index in range(len(NAMES)):
        for k_pole in range(4):
            for levels in levels_all:
                if levels[marked_index] == 2:
                    continue
                for exponent in base.monomials_at_most(ambient - 1):
                    marked.append(
                        ("marked", k_pole, levels, exponent, marked_index)
                    )

    # Pole-extension stage two: complete depth-two source first, followed by
    # the new k=2 de Rham and principal strata.  New k=3 marked strata are not
    # yet admitted.
    ordered = [item for item in de_rham if item[1] < 2]
    ordered += [item for item in principal if item[1] < 2]
    ordered += [item for item in marked if item[1] < 3]
    ordered += [item for item in de_rham if item[1] == 2]
    ordered += [item for item in principal if item[1] == 2]
    return ordered


def external_data(point, axes):
    return source.external_data(point, axes)


def moved_descriptors(descriptor, point, axes):
    family, k_pole, levels, exponent, extra = descriptor
    kd, _ = external_data(point, axes)
    moved = {}
    k_weight = GAMMA - k_pole - (1 if family == "principal" else 0)
    for term, coefficient in base.multiply_monomial(kd, exponent, k_weight):
        add(moved, (k_pole + 1, *levels, term), coefficient)
    # Keep only the degree +1 Cayley--Menger symbol.  The q-derivative terms
    # have K-degree zero and belong to a separate marked-pole filtration.
    return [
        ((family, label[0], tuple(label[1:-1]), label[-1], extra), coefficient)
        for label, coefficient in moved.items()
    ]


def relation_labels(descriptor, point):
    family, k_pole, levels, exponent, extra = descriptor
    label = (k_pole, *levels, exponent)
    if family == "de_rham":
        return source.de_rham_row(label, point, extra)
    if family == "principal":
        return source.principal_row(label, point)
    return source.marked_row(label, point, extra)


def target_columns(ambient, point):
    old = (charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH)
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    charts.K_DEPTH, charts.Q_DEPTH = 4, 2
    try:
        return charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)[
            "columns"
        ]
    finally:
        charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old


def image_at(descriptor, point, axes, columns):
    row = {}
    for moved, source_coefficient in moved_descriptors(descriptor, point, axes):
        for label, value in relation_labels(moved, point).items():
            # The finite target packet is the ambient-degree truncation.  A
            # differentiated source monomial can cross that boundary; such a
            # term belongs to the next cutoff and is not a coordinate of this
            # packet.  This mirrors the packet builder's admission rule.
            column = columns.get(label)
            if column is None:
                continue
            add(row, column, source_coefficient * value)
    return row


def normal_image(descriptor, tangent, ambient, columns):
    axes = (0, 2) if tangent == "T1" else (1, 2)
    fibers = []
    for offset in NODES:
        point = (2, 3, 5 + offset)
        fibers.append(image_at(descriptor, point, axes, columns))
    width = len(columns)
    result = {}
    for order, weights in enumerate(WEIGHTS):
        for row, weight in zip(fibers, weights):
            for column, value in row.items():
                add(result, order * width + column, weight * value)
    return result


parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, default=10)
parser.add_argument("--row-index", type=int, action="append", required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

ordered = descriptors(args.ambient)
columns = target_columns(args.ambient, (2, 3, 5))
items = []
for row_index in args.row_index:
    descriptor = ordered[row_index]
    tangent_images = {}
    for tangent in ("T1", "T2"):
        image = normal_image(descriptor, tangent, args.ambient, columns)
        tangent_images[tangent] = {
            "term_count": len(image),
            "probe": ",".join(f"{column}:{value}" for column, value in image.items()),
        }
    items.append(
        {
            "row_index": row_index,
            "descriptor": repr(descriptor),
            "images": tangent_images,
        }
    )

packet = {
    "schema": "marici.triangle-wall-pole-symbol-images.v1",
    "field": P,
    "ambient_relation_degree": args.ambient,
    "source_k_depth": 3,
    "target_k_depth": 4,
    "source_stage": 2,
    "target_column_count": len(columns),
    "items": items,
}
args.output.write_text(json.dumps(packet, indent=2), encoding="utf-8")
print(json.dumps({
    "schema": packet["schema"],
    "target_column_count": len(columns),
    "row_count": len(items),
    "output": str(args.output),
}))
