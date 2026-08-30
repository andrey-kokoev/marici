"""Occurrence reflection of the literal rank-26 source on a soft fiber."""

import contextlib
import importlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "nima"))
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

with contextlib.redirect_stdout(io.StringIO()):
    stable = importlib.import_module("check_rank21_stable_horizontal_closure")

base, audit, charts = stable.base, stable.audit, stable.charts


def source_row(presentation, names):
    numerator = {}
    for name in names[-2:]:
        for exponent, coefficient in presentation["q"][name].items():
            numerator[exponent] = (numerator.get(exponent, 0) + coefficient) % base.PRIME
    prefix = (0, 1, 1, 1, 1, 1)
    row = {}
    for exponent, coefficient in numerator.items():
        base.add_value(row, presentation["columns"][(prefix + (exponent,))], coefficient)
    return base.reduce_row(row, presentation["pivots"])


def numerator_derivative_row(presentation, fiber, point, names, axis):
    _, derivatives = audit.parameter_derivative_data(fiber, point, axis)
    derivative = {}
    for name in names[-2:]:
        for exponent, coefficient in derivatives[name].items():
            derivative[exponent] = (derivative.get(exponent, 0) + coefficient) % base.PRIME
    prefix = (0, 1, 1, 1, 1, 1)
    row = {}
    for exponent, coefficient in derivative.items():
        label = prefix + (exponent,)
        if label in presentation["columns"]:
            base.add_value(row, presentation["columns"][label], coefficient)
    return row


def connection_image(presentation, vector, fiber, point, names, axis):
    image = {}
    for column, coefficient in vector.items():
        label = presentation["ordered_columns"][column]
        for destination, value in audit.connection_image(
            label, names, axis, presentation["columns"], fiber, point
        ).items():
            base.add_value(image, destination, coefficient * value)
    return base.reduce_row(image, presentation["pivots"])


def tangent_image(presentation, vector, fiber, point, names, tangent):
    image = {}
    for axis, coefficient in enumerate(tangent):
        if not coefficient:
            continue
        component = connection_image(presentation, vector, fiber, point, names, axis)
        for column, value in component.items():
            base.add_value(image, column, coefficient * value)
    return base.reduce_row(image, presentation["pivots"])


def tangent_numerator_derivative(presentation, fiber, point, names, tangent):
    row = {}
    for axis, coefficient in enumerate(tangent):
        if not coefficient:
            continue
        component = numerator_derivative_row(presentation, fiber, point, names, axis)
        for column, value in component.items():
            base.add_value(row, column, coefficient * value)
    return row


def closure(fiber, point, names, tangents):
    old = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = 14, 6
    try:
        presentation = charts.presentation(fiber, point, names)
    finally:
        charts.AMBIENT, charts.CUTOFF = old
    source = source_row(presentation, names)
    span, frontier = {}, [source]
    # The first derivative of the literal source includes its numerator jet.
    first_images = []
    for tangent in tangents:
        image = tangent_image(presentation, source, fiber, point, names, tangent)
        correction = tangent_numerator_derivative(
            presentation, fiber, point, names, tangent
        )
        for column, coefficient in correction.items():
            base.add_value(image, column, coefficient)
        image = base.reduce_row(image, presentation["pivots"])
        first_images.append(image)
        frontier.append(image)
    while frontier:
        vector = frontier.pop()
        before = len(span)
        base.add_pivot(dict(vector), span)
        if len(span) == before:
            continue
        for tangent in tangents:
            image = tangent_image(presentation, vector, fiber, point, names, tangent)
            if image:
                frontier.append(image)
    return presentation, source, span, first_images


def main():
    source_point = (3, 0, 5)
    target_point = (3, 5, 0)
    source_tangents = ((1, 0, 0), (0, 0, 1))
    target_tangents = ((1, 0, 0), (0, 1, 0))
    source, _, source_span, _ = closure(
        base.fiber_data, source_point, charts.SOURCE_NAMES, source_tangents
    )
    target, _, target_span, _ = closure(
        charts.g31_fiber_data, target_point, charts.TARGET_NAMES, target_tangents
    )
    mapped_span, failures = {}, 0
    for vector in source_span.values():
        mapped = charts.map_row(vector, source, target, -1)
        mapped = base.reduce_row(mapped, target["pivots"])
        base.add_pivot(dict(mapped), mapped_span)
        if base.reduce_row(mapped, target_span):
            failures += 1
    result = {
        "schema": "marici.benincasa.rank26-soft-occurrence-transport.v1",
        "field": base.PRIME,
        "source_chart": "G12",
        "source_point": list(source_point),
        "source_numerator": "q_g23+q_g31",
        "target_chart": "G31",
        "target_point": list(target_point),
        "target_numerator": "q_g23+q_g12",
        "source_tangents": [list(value) for value in source_tangents],
        "target_tangents": [list(value) for value in target_tangents],
        "poincare_residue_orientation": -1,
        "source_rank": len(source_span),
        "target_rank": len(target_span),
        "mapped_rank": len(mapped_span),
        "containment_failures": failures,
    }
    result["isomorphism_verified"] = (
        result["source_rank"] == result["target_rank"] == result["mapped_rank"]
        and failures == 0
    )
    assert result["isomorphism_verified"]
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
