"""Verify external/fiber commutation before finite pole and degree truncation."""

from __future__ import annotations

import contextlib
import importlib
import io
import json
from itertools import product

with contextlib.redirect_stdout(io.StringIO()):
    connection = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = connection.base, connection.charts
P = base.PRIME
POINT = (2, 3, 5)
NODES = tuple(range(-3, 4))
NAMES = charts.SOURCE_NAMES
GAMMA = charts.GAMMA


def add(row, label, value):
    value = (row.get(label, 0) + value) % P
    if value:
        row[label] = value
    else:
        row.pop(label, None)


def weights(order):
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


FIRST_WEIGHTS = weights(1)


def exact_parameter_derivative_data(point, axis):
    k_result = {}
    q_result = {name: {} for name in NAMES}
    for offset, weight in zip(NODES, FIRST_WEIGHTS):
        shifted = list(point)
        shifted[axis] += offset
        k, q = base.fiber_data(*shifted)
        for exponent, coefficient in k.items():
            add(k_result, exponent, weight * coefficient)
        for name in NAMES:
            for exponent, coefficient in q[name].items():
                add(q_result[name], exponent, weight * coefficient)
    return k_result, q_result


def shifted_point(tangent, offset):
    x1, x2, _ = POINT
    if tangent == "x1":
        x1 += offset
    else:
        x2 += offset
    return x1, x2, x1 + x2


def external_data(point, axes):
    kd = {}
    qd = {name: {} for name in NAMES}
    for axis in axes:
        axis_k, axis_q = exact_parameter_derivative_data(point, axis)
        for exponent, coefficient in axis_k.items():
            add(kd, exponent, coefficient)
        for name in NAMES:
            for exponent, coefficient in axis_q[name].items():
                add(qd[name], exponent, coefficient)
    return kd, qd


def form_connection(label, point, axes):
    k_pole, *rest = label
    exponent = rest.pop()
    levels = rest
    kd, qd = external_data(point, axes)
    row = {}
    for term, coefficient in base.multiply_monomial(kd, exponent, GAMMA - k_pole):
        add(row, (k_pole + 1, *levels, term), coefficient)
    for qi, level in enumerate(levels):
        raised = list(levels)
        raised[qi] += 1
        for term, coefficient in base.multiply_monomial(qd[NAMES[qi]], exponent, -level):
            add(row, (k_pole, *raised, term), coefficient)
    return row


def de_rham_row(label, point, fiber_axis):
    k_pole, *rest = label
    exponent = rest.pop()
    levels = rest
    k, q = base.fiber_data(*point)
    row = {}
    if exponent[fiber_axis]:
        derived = list(exponent)
        derived[fiber_axis] -= 1
        add(row, (k_pole, *levels, tuple(derived)), exponent[fiber_axis])
    for term, coefficient in base.multiply_monomial(base.derivative(k, fiber_axis), exponent, GAMMA - k_pole):
        add(row, (k_pole + 1, *levels, term), coefficient)
    for qi, level in enumerate(levels):
        raised = list(levels)
        raised[qi] += 1
        for term, coefficient in base.multiply_monomial(base.derivative(q[NAMES[qi]], fiber_axis), exponent, -level):
            add(row, (k_pole, *raised, term), coefficient)
    return row


def principal_row(label, point):
    k_pole, *rest = label
    exponent = rest.pop()
    levels = rest
    k, _ = base.fiber_data(*point)
    row = {label: 1}
    for term, coefficient in base.multiply_monomial(k, exponent, -1):
        add(row, (k_pole + 1, *levels, term), coefficient)
    return row


def marked_row(label, point, marked_index):
    k_pole, *rest = label
    exponent = rest.pop()
    levels = rest
    _, q = base.fiber_data(*point)
    raised = list(levels)
    raised[marked_index] += 1
    row = {label: 1}
    for term, coefficient in base.multiply_monomial(q[NAMES[marked_index]], exponent, -1):
        add(row, (k_pole, *raised, term), coefficient)
    return row


def tangent_derivative(row_function, tangent):
    result = {}
    for offset, weight in zip(NODES, FIRST_WEIGHTS):
        for label, coefficient in row_function(shifted_point(tangent, offset)).items():
            add(result, label, weight * coefficient)
    return result


def audit(tangent):
    axes = (0, 2) if tangent == "x1" else (1, 2)
    connection_cache = {}

    def cached_connection(label):
        if label not in connection_cache:
            connection_cache[label] = form_connection(label, POINT, axes)
        return connection_cache[label]

    def covariant_residual(row_function):
        residual = tangent_derivative(row_function, tangent)
        central = row_function(POINT)
        for output, coefficient in central.items():
            for target, value in cached_connection(output).items():
                add(residual, target, coefficient * value)
        return residual

    kd, qd = external_data(POINT, axes)

    def principal_source_connection(label):
        k_pole, *rest = label
        exponent = rest.pop()
        levels = rest
        moved = {}
        for term, coefficient in base.multiply_monomial(kd, exponent, GAMMA - k_pole - 1):
            add(moved, (k_pole + 1, *levels, term), coefficient)
        for qi, level in enumerate(levels):
            raised = list(levels)
            raised[qi] += 1
            for term, coefficient in base.multiply_monomial(qd[NAMES[qi]], exponent, -level):
                add(moved, (k_pole, *raised, term), coefficient)
        return moved

    def marked_source_connection(label, marked_index):
        k_pole, *rest = label
        exponent = rest.pop()
        levels = rest
        moved = {}
        for term, coefficient in base.multiply_monomial(kd, exponent, GAMMA - k_pole):
            add(moved, (k_pole + 1, *levels, term), coefficient)
        for qi, level in enumerate(levels):
            raised = list(levels)
            raised[qi] += 1
            effective_level = level + (1 if qi == marked_index else 0)
            for term, coefficient in base.multiply_monomial(
                qd[NAMES[qi]], exponent, -effective_level
            ):
                add(moved, (k_pole, *raised, term), coefficient)
        return moved

    failures = 0
    checked = 0
    first = []
    levels = [1] * len(NAMES)
    for k_pole in range(2):
        for fiber_axis in range(2):
            for exponent in base.monomials_at_most(10):
                primitive = (k_pole, *levels, exponent)
                left = tangent_derivative(
                    lambda point: de_rham_row(primitive, point, fiber_axis), tangent
                )
                central = de_rham_row(primitive, POINT, fiber_axis)
                for output, coefficient in central.items():
                    for target, value in cached_connection(output).items():
                        add(left, target, coefficient * value)
                right = {}
                for moved_primitive, coefficient in cached_connection(primitive).items():
                    for target, value in de_rham_row(moved_primitive, POINT, fiber_axis).items():
                        add(right, target, coefficient * value)
                residual = dict(left)
                for target, value in right.items():
                    add(residual, target, -value)
                checked += 1
                if residual:
                    failures += 1
                    if len(first) < 10:
                        first.append({"primitive": primitive, "residual_terms": len(residual)})
    principal_failures = 0
    principal_checked = 0
    principal_first = []
    for k_pole in range(2):
        for pole_levels in product(range(1, 3), repeat=len(NAMES)):
            for exponent in base.monomials_at_most(6):
                label = (k_pole, *pole_levels, exponent)
                principal_checked += 1
                residual = covariant_residual(lambda point, label=label: principal_row(label, point))
                for moved, coefficient in principal_source_connection(label).items():
                    for target, value in principal_row(moved, POINT).items():
                        add(residual, target, -coefficient * value)
                if residual:
                    principal_failures += 1
                    if len(principal_first) < 1:
                        principal_first.append({
                            "label": label,
                            "residual": [[list(target[:-1]) + [list(target[-1])], value] for target, value in list(residual.items())[:20]],
                        })

    marked_checked = {name: 0 for name in NAMES}
    marked_failures = {name: 0 for name in NAMES}
    for marked_index, name in enumerate(NAMES):
        for k_pole in range(3):
            for pole_levels in product(range(1, 3), repeat=len(NAMES)):
                if pole_levels[marked_index] == 2:
                    continue
                for exponent in base.monomials_at_most(9):
                    label = (k_pole, *pole_levels, exponent)
                    marked_checked[name] += 1
                    residual = covariant_residual(
                        lambda point, label=label, marked_index=marked_index:
                            marked_row(label, point, marked_index)
                    )
                    for moved, coefficient in marked_source_connection(label, marked_index).items():
                        for target, value in marked_row(moved, POINT, marked_index).items():
                            add(residual, target, -coefficient * value)
                    if residual:
                        marked_failures[name] += 1

    return {
        "tangent": tangent,
        "axes": list(axes),
        "de_rham_commutators_checked": checked,
        "de_rham_commutator_failures": failures,
        "principal_commutators_checked": principal_checked,
        "principal_commutator_failures": principal_failures,
        "principal_first_failures": principal_first,
        "marked_commutators_checked": marked_checked,
        "marked_commutator_failures": marked_failures,
        "first_failures": first,
    }


result = {
    "schema": "marici.unbounded-twisted-derham-connection-commutator.v1",
    "field": P,
    "point": list(POINT),
    "ambient_primitive_degree": 10,
    "tangents": [audit("x1"), audit("x2")],
}
result["all_commutators_zero"] = all(
    item["de_rham_commutator_failures"] == 0
    and item["principal_commutator_failures"] == 0
    and all(value == 0 for value in item["marked_commutator_failures"].values())
    for item in result["tangents"]
)
print(json.dumps(result, indent=2))
