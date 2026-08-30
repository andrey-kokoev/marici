"""Derive a point-independent primitive source-word basis for the rank-26 module."""

from __future__ import annotations

import contextlib
import importlib
import io
import json
from collections import deque
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    cyclic = importlib.import_module("check_rank26_unsplit_source_cyclicity")

base = cyclic.base
audit = cyclic.audit
charts = cyclic.charts
AMBIENT = 14
CUTOFF = 6
REFERENCE_POINT = (2, 3, 4)
CONTROL_POINTS = ((3, 5, 7), (5, 7, 11))


def presentation(point):
    old_point = charts.SOURCE_POINT
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.SOURCE_POINT = point
    charts.AMBIENT, charts.CUTOFF = AMBIENT, CUTOFF
    try:
        return charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)
    finally:
        charts.SOURCE_POINT = old_point
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff


def raw_source(pres, point):
    _, q = base.fiber_data(*point)
    numerator = dict(q["g23"])
    for exponent, coefficient in q["g31"].items():
        numerator[exponent] = (numerator.get(exponent, 0) + coefficient) % base.PRIME
    prefix = (0, 1, 1, 1, 1, 1)
    row = {}
    for exponent, coefficient in numerator.items():
        base.add_value(row, pres["columns"][prefix + (exponent,)], coefficient)
    return row


def raw_source_derivative(pres, point, axis):
    _, qd = audit.parameter_derivative_data(base.fiber_data, point, axis)
    derivative = dict(qd["g23"])
    for exponent, coefficient in qd["g31"].items():
        derivative[exponent] = (derivative.get(exponent, 0) + coefficient) % base.PRIME
    prefix = (0, 1, 1, 1, 1, 1)
    row = {}
    for exponent, coefficient in derivative.items():
        label = prefix + (exponent,)
        if label in pres["columns"]:
            base.add_value(row, pres["columns"][label], coefficient)
    return row


def raw_connection(pres, point, row, axis):
    image = {}
    for column, coefficient in row.items():
        label = pres["ordered_columns"][column]
        for destination, value in audit.connection_image(
            label,
            charts.SOURCE_NAMES,
            axis,
            pres["columns"],
            base.fiber_data,
            point,
        ).items():
            base.add_value(image, destination, coefficient * value)
    return image


def root_rows(pres, point):
    source = raw_source(pres, point)
    roots = [("S", source)]
    for axis in range(3):
        derivative = raw_connection(pres, point, source, axis)
        correction = raw_source_derivative(pres, point, axis)
        for column, coefficient in correction.items():
            base.add_value(derivative, column, coefficient)
        roots.append((f"D{axis}", derivative))
    return roots


def descriptor_payload(root, path):
    return {"root": root, "connection_path": list(path), "depth": len(path)}


def derive_descriptors(point):
    pres = presentation(point)
    queue = deque((root, (), row) for root, row in root_rows(pres, point))
    span = {}
    descriptors = []
    raw_supports = []
    while queue and len(span) < 26:
        root, path, raw = queue.popleft()
        quotient = base.reduce_row(raw, pres["pivots"])
        before = len(span)
        base.add_pivot(dict(quotient), span)
        if len(span) == before:
            continue
        descriptors.append(descriptor_payload(root, path))
        raw_supports.append(len(raw))
        for axis in range(3):
            queue.append((root, path + (axis,), raw_connection(pres, point, raw, axis)))
    assert len(span) == 26, (len(span), len(queue))
    return descriptors, raw_supports


def evaluate_descriptor(pres, point, descriptor):
    roots = dict(root_rows(pres, point))
    row = roots[descriptor["root"]]
    for axis in descriptor["connection_path"]:
        row = raw_connection(pres, point, row, axis)
    return row


def descriptor_rank(point, descriptors):
    pres = presentation(point)
    span = {}
    for descriptor in descriptors:
        row = evaluate_descriptor(pres, point, descriptor)
        quotient = base.reduce_row(row, pres["pivots"])
        base.add_pivot(dict(quotient), span)
    return len(span)


def main():
    descriptors, raw_supports = derive_descriptors(REFERENCE_POINT)
    controls = [
        {"point": list(point), "rank": descriptor_rank(point, descriptors)}
        for point in CONTROL_POINTS
    ]
    assert all(record["rank"] == 26 for record in controls)
    result = {
        "schema": "marici.benincasa.rank26-source-word-basis.v1",
        "field": base.PRIME,
        "reference_point": list(REFERENCE_POINT),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": CUTOFF,
        "selection": (
            "breadth-first minimal primitive words; quotient reduction is used "
            "only for independence and never replaces the raw primitive"
        ),
        "descriptors": descriptors,
        "raw_support_sizes": raw_supports,
        "maximum_connection_depth": max(item["depth"] for item in descriptors),
        "reference_rank": 26,
        "control_ranks": controls,
        "status": "one primitive source-word basis spans at three generic points",
        "warning": (
            "Gauss-Manin closure and regular transition determinants along the "
            "total-energy normal remain to be proved"
        ),
    }
    output = Path(__file__).with_name("rank26-source-word-basis.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
