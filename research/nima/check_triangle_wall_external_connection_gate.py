"""Test the source external derivative on the complete triangle-wall presentation."""

from __future__ import annotations

import contextlib
import importlib
import io
import json

with contextlib.redirect_stdout(io.StringIO()):
    connection = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = connection.base, connection.charts
P = base.PRIME
POINT = (2, 3, 5)
NODES = tuple(range(-3, 4))


def capture(point):
    rows = []
    original = base.add_pivot

    def hook(row, pivots):
        rows.append(dict(row))
        original(row, pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = 10, 6
    base.add_pivot = hook
    try:
        presentation = charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)
    finally:
        base.add_pivot = original
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    return presentation, rows


def coefficient_weights(order):
    result = []
    for node in NODES:
        polynomial = [1]
        denominator = 1
        for other in NODES:
            if other == node:
                continue
            following = [0] * (len(polynomial) + 1)
            for degree, coefficient in enumerate(polynomial):
                following[degree] = (following[degree] - other * coefficient) % P
                following[degree + 1] = (following[degree + 1] + coefficient) % P
            polynomial = following
            denominator = denominator * (node - other) % P
        result.append(polynomial[order] * pow(denominator, P - 2, P) % P)
    return result


def shifted_point(tangent, offset):
    x1, x2, _ = POINT
    if tangent == "x1":
        x1 += offset
    else:
        x2 += offset
    return x1, x2, x1 + x2


def audit_tangent(tangent):
    packets = [capture(shifted_point(tangent, offset)) for offset in NODES]
    presentation, central_rows = packets[3]
    row_packets = [rows for _, rows in packets]
    if len(set(map(len, row_packets))) != 1:
        raise RuntimeError("raw relation row counts vary along the tangent")

    weights = coefficient_weights(1)
    derivative_rows = []
    for index in range(len(central_rows)):
        derivative = {}
        for rows, weight in zip(row_packets, weights):
            for column, value in rows[index].items():
                base.add_value(derivative, column, weight * value)
        derivative_rows.append(derivative)

    axes = (0, 2) if tangent == "x1" else (1, 2)
    family_bounds = [264, 2056, 4696, 7336, 9976, 12616, 15256]
    family_names = ["de_rham", "principal_K", "g1", "g2", "g3", "g23", "g31"]
    failures = {"plus": [], "minus": []}
    failure_families = {
        sign: {name: 0 for name in family_names} for sign in ("plus", "minus")
    }
    for index, (row, derivative) in enumerate(zip(central_rows, derivative_rows)):
        connection_part = {}
        for column, coefficient in row.items():
            label = presentation["ordered_columns"][column]
            for axis in axes:
                image = connection.connection_image(
                    label,
                    charts.SOURCE_NAMES,
                    axis,
                    presentation["columns"],
                    base.fiber_data,
                    POINT,
                )
                for target, value in image.items():
                    base.add_value(connection_part, target, coefficient * value)
        for sign, scalar in (("plus", 1), ("minus", -1)):
            covariant = dict(derivative)
            for target, value in connection_part.items():
                base.add_value(covariant, target, scalar * value)
            residual = base.reduce_row(covariant, presentation["pivots"])
            if residual:
                failures[sign].append({"row": index, "residual_terms": len(residual)})
                family = next(name for name, bound in zip(family_names, family_bounds) if index < bound)
                failure_families[sign][family] += 1

    return {
        "tangent": tangent,
        "axes": list(axes),
        "raw_relation_count": len(central_rows),
        "covariant_relation_failures": {sign: len(items) for sign, items in failures.items()},
        "failure_families": failure_families,
        "first_failures": {sign: items[:10] for sign, items in failures.items()},
        "chain_connection_gate_passed": not failures["plus"],
    }


result = {
    "schema": "marici.triangle-wall-external-connection-gate.v1",
    "field": P,
    "point": list(POINT),
    "ambient_relation_degree": 10,
    "tangents": [audit_tangent("x1"), audit_tangent("x2")],
}
result["all_chain_connection_gates_passed"] = all(
    item["chain_connection_gate_passed"] for item in result["tangents"]
)
print(json.dumps(result, indent=2))
