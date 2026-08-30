"""Cyclicity of the literal unsplit source in the typed rank-26 closure."""

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
    closure = importlib.import_module("check_rank21_stable_horizontal_closure")

base = closure.base
audit = closure.audit
charts = closure.charts


def source_row(pres):
    _, q = base.fiber_data(*charts.SOURCE_POINT)
    numerator = dict(q["g23"])
    for exponent, coefficient in q["g31"].items():
        numerator[exponent] = (numerator.get(exponent, 0) + coefficient) % base.PRIME
    prefix = (0, 1, 1, 1, 1, 1)
    row = {}
    for exponent, coefficient in numerator.items():
        base.add_value(row, pres["columns"][(prefix + (exponent,))], coefficient)
    return base.reduce_row(row, pres["pivots"])


def numerator_derivative_row(pres, axis):
    _, qd = audit.parameter_derivative_data(base.fiber_data, charts.SOURCE_POINT, axis)
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


def connection_image(pres, vector, axis):
    image = {}
    for column, coefficient in vector.items():
        label = pres["ordered_columns"][column]
        for destination, value in audit.connection_image(
            label, charts.SOURCE_NAMES, axis, pres["columns"],
            base.fiber_data, charts.SOURCE_POINT,
        ).items():
            base.add_value(image, destination, coefficient * value)
    return base.reduce_row(image, pres["pivots"])


def source_closure(ambient):
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    try:
        pres = charts.presentation(base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES)
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    source = source_row(pres)
    first = {}
    base.add_pivot(dict(source), first)
    frontier = [source]
    for axis in range(3):
        image = connection_image(pres, source, axis)
        correction = numerator_derivative_row(pres, axis)
        for column, coefficient in correction.items():
            base.add_value(image, column, coefficient)
        image = base.reduce_row(image, pres["pivots"])
        base.add_pivot(dict(image), first)
        frontier.append(image)
    span = {}
    while frontier:
        vector = frontier.pop()
        before = len(span)
        base.add_pivot(dict(vector), span)
        if len(span) == before:
            continue
        for axis in range(3):
            image = connection_image(pres, vector, axis)
            if image:
                frontier.append(image)
    record = {
        "ambient_relation_degree": ambient,
        "source_support": len(source),
        "first_covariant_jet_rank": len(first),
        "horizontal_cyclic_rank": len(span),
    }
    return pres, span, source, record


def census(ambient):
    return source_closure(ambient)[3]


if __name__ == "__main__":
    records = [census(ambient) for ambient in (12, 14, 16)]
    assert all(record["horizontal_cyclic_rank"] == 26 for record in records)
    print(json.dumps({
        "schema": "marici.benincasa.rank26_unsplit_source_cyclicity.v1",
        "field": base.PRIME,
        "kinematics": list(charts.SOURCE_POINT),
        "source": "q_g23+q_g31",
        "records": records,
        "status": "literal unsplit source is cyclic for the typed rank-26 moving-wall extension",
    }, sort_keys=True))
