"""Tangent Gauss--Manin closure on declared rank-26 support divisors."""

import json
from concurrent.futures import ProcessPoolExecutor

import check_rank26_unsplit_source_cyclicity as cyclic


def linear_image(presentation, vector, tangent):
    image = {}
    for axis, coefficient in enumerate(tangent):
        if not coefficient:
            continue
        component = cyclic.connection_image(presentation, vector, axis)
        for column, value in component.items():
            cyclic.base.add_value(image, column, coefficient * value)
    return cyclic.base.reduce_row(image, presentation["pivots"])


def linear_numerator_derivative(presentation, tangent):
    row = {}
    for axis, coefficient in enumerate(tangent):
        if not coefficient:
            continue
        component = cyclic.numerator_derivative_row(presentation, axis)
        for column, value in component.items():
            cyclic.base.add_value(row, column, coefficient * value)
    return row


def tangent_closure_data(point, tangents, ambient=14):
    cyclic.charts.SOURCE_POINT = point
    old = cyclic.charts.AMBIENT, cyclic.charts.CUTOFF
    cyclic.charts.AMBIENT, cyclic.charts.CUTOFF = ambient, 6
    try:
        presentation = cyclic.charts.presentation(
            cyclic.base.fiber_data, point, cyclic.charts.SOURCE_NAMES
        )
    finally:
        cyclic.charts.AMBIENT, cyclic.charts.CUTOFF = old
    source = cyclic.source_row(presentation)
    span, frontier = {}, [source]
    for tangent in tangents:
        image = linear_image(presentation, source, tangent)
        correction = linear_numerator_derivative(presentation, tangent)
        for column, value in correction.items():
            cyclic.base.add_value(image, column, value)
        image = cyclic.base.reduce_row(image, presentation["pivots"])
        if image:
            frontier.append(image)
    while frontier:
        vector = frontier.pop()
        before = len(span)
        cyclic.base.add_pivot(dict(vector), span)
        if len(span) == before:
            continue
        for tangent in tangents:
            image = linear_image(presentation, vector, tangent)
            if image:
                frontier.append(image)
    record = {
        "point": list(point),
        "tangents": [list(tangent) for tangent in tangents],
        "tangent_closure_rank": len(span),
        "relation_rank": len(presentation["pivots"]),
        "source_support": len(source),
    }
    return presentation, span, source, record


def tangent_closure(point, tangents, ambient=14):
    return tangent_closure_data(point, tangents, ambient)[3]


CASES = {
    "total_energy": ((2, 3, -5), ((1, 0, -1), (0, 1, -1))),
    "X1_soft": ((0, 3, 5), ((0, 1, 0), (0, 0, 1))),
    "X2_soft": ((3, 0, 5), ((1, 0, 0), (0, 0, 1))),
    "X3_soft": ((3, 5, 0), ((1, 0, 0), (0, 1, 0))),
}


def main():
    names = list(CASES)
    arguments = [CASES[name] for name in names]
    with ProcessPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(_run_case, arguments))
    result = dict(zip(names, records))
    print(json.dumps({
        "schema": "marici.benincasa.rank26-tangent-support-closure.v1",
        "field": cyclic.base.PRIME,
        "cases": result,
        "warning": (
            "these are tangent connection closures in the specialized quotient; "
            "they are not a complete derived pullback or nearby-cycle object"
        ),
    }, sort_keys=True))


def _run_case(arguments):
    point, tangents = arguments
    return tangent_closure(point, tangents)


if __name__ == "__main__":
    main()
