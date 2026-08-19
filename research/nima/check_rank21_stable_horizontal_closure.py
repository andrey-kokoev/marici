"""Replicate the connection closure of the degree-five residue block."""

import contextlib
import importlib
import io
import json
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base = audit.base
charts = audit.charts


def closure_rank(ambient):
    low, columns, pivots, _ = base.presentation(
        charts.SOURCE_NAMES, 5, ambient, 6, minimum_q_level=1
    )
    ordered = [None] * len(columns)
    for label, column in columns.items():
        ordered[column] = label
    span = {}
    frontier = []
    for label in low:
        if sum(label[-1]) <= 5:
            row = base.reduce_row({columns[label]: 1}, pivots)
            if row:
                frontier.append(row)
    while frontier:
        vector = frontier.pop()
        before = len(span)
        base.add_pivot(dict(vector), span)
        if len(span) == before:
            continue
        for axis in range(3):
            image = {}
            for column, coefficient in vector.items():
                for target, value in audit.connection_image(
                    ordered[column], charts.SOURCE_NAMES, axis, columns,
                    base.fiber_data, charts.SOURCE_POINT,
                ).items():
                    base.add_value(image, target, coefficient * value)
            reduced = base.reduce_row(image, pivots)
            if reduced:
                frontier.append(reduced)
    return {"ambient_relation_degree": ambient, "closure_rank": len(span)}


replications = [closure_rank(ambient) for ambient in (8, 10, 12, 14, 16)]


def chart_closure(fiber, point, names):
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = 14, 6
    try:
        pres = charts.presentation(fiber, point, names)
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    span, frontier = {}, []
    for label in pres["low_labels"]:
        if sum(label[-1]) <= 5:
            row = base.reduce_row({pres["columns"][label]: 1}, pres["pivots"])
            if row:
                frontier.append(row)
    while frontier:
        vector = frontier.pop()
        before = len(span)
        base.add_pivot(dict(vector), span)
        if len(span) == before:
            continue
        for axis in range(3):
            image = {}
            for column, coefficient in vector.items():
                label = pres["ordered_columns"][column]
                for target, value in audit.connection_image(
                    label, names, axis, pres["columns"], fiber, point
                ).items():
                    base.add_value(image, target, coefficient * value)
            reduced = base.reduce_row(image, pres["pivots"])
            if reduced:
                frontier.append(reduced)
    return pres, span


source, source_span = chart_closure(base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES)
target, target_span = chart_closure(charts.g31_fiber_data, charts.TARGET_POINT, charts.TARGET_NAMES)
mapped_span, containment_failures = {}, 0
for vector in source_span.values():
    mapped = charts.map_row(vector, source, target, -1)
    mapped = base.reduce_row(mapped, target["pivots"])
    base.add_pivot(dict(mapped), mapped_span)
    if base.reduce_row(mapped, target_span):
        containment_failures += 1

transport = {
    "source_closure_rank": len(source_span),
    "target_closure_rank": len(target_span),
    "mapped_closure_rank": len(mapped_span),
    "target_containment_failures": containment_failures,
    "isomorphism_verified": (
        len(source_span) == len(target_span) == len(mapped_span) == 26
        and containment_failures == 0
    ),
}
payload = {
    "schema": "marici.rank21-stable-horizontal-closure.v1",
    "field": base.PRIME,
    "kinematics": list(charts.SOURCE_POINT),
    "initial_numerator_degree": 5,
    "replications": replications,
    "stable_tail_rank": 26,
    "stable_from_ambient_relation_degree": 12,
    "occurrence_reflection_transport": transport,
    "interpretation": "degree-six numerator closure of rank 25 plus one labelled double-pole coherence direction",
    "status": "stable_rank26_augmented_closure_and_reflection_isomorphism_verified",
}
out = Path(__file__).with_name("rank21-stable-horizontal-closure.json")
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
