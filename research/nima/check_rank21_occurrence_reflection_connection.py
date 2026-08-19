"""Connection naturality of the source-derived rank-21 chart transition."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENINCASA = ROOT / "research" / "benincasa"
sys.path.insert(0, str(BENINCASA))

import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts

P = base.PRIME


def parameter_derivative_data(fiber, point, axis):
    weights = (1, -8, 0, 8, -1)
    inverse_twelve = pow(12, P - 2, P)
    k_result = {}
    q_result = {}
    for offset, weight in zip((-2, -1, 0, 1, 2), weights):
        shifted = list(point)
        shifted[axis] += offset
        k, q = fiber(*shifted)
        for exponent, coefficient in k.items():
            k_result[exponent] = (k_result.get(exponent, 0) + weight * coefficient) % P
        for name, polynomial in q.items():
            target = q_result.setdefault(name, {})
            for exponent, coefficient in polynomial.items():
                target[exponent] = (target.get(exponent, 0) + weight * coefficient) % P
    k_result = {e: c * inverse_twelve % P for e, c in k_result.items() if c}
    q_result = {
        name: {e: c * inverse_twelve % P for e, c in polynomial.items() if c}
        for name, polynomial in q_result.items()
    }
    return k_result, q_result


def connection_image(label, names, axis, columns, fiber, point):
    k_pole, *rest = label
    exponent = rest.pop()
    levels = rest
    kd, qd = parameter_derivative_data(fiber, point, axis)
    row = {}
    if k_pole < 2:
        for term, coefficient in base.multiply_monomial(kd, exponent, charts.GAMMA - k_pole):
            target = (k_pole + 1, *levels, term)
            if target in columns:
                base.add_value(row, columns[target], coefficient)
    for qi, level in enumerate(levels):
        if level >= 2:
            continue
        raised = list(levels)
        raised[qi] += 1
        for term, coefficient in base.multiply_monomial(qd[names[qi]], exponent, -level):
            target = (k_pole, *raised, term)
            if target in columns:
                base.add_value(row, columns[target], coefficient)
    return row


def connection_matrix(pres, names, fiber, point, axis):
    free = pres["free_low"]
    position = {column: i for i, column in enumerate(free)}
    matrix = [[0] * len(free) for _ in free]
    for source_index, column in enumerate(free):
        label = pres["ordered_columns"][column]
        image = connection_image(label, names, axis, pres["columns"], fiber, point)
        reduced = base.reduce_row(image, pres["pivots"])
        for target_column, value in reduced.items():
            if target_column in position:
                matrix[position[target_column]][source_index] = value
    return matrix


def connection_leakage(pres, names, fiber, point, axis):
    free = set(pres["free_low"])
    leaking_sources = 0
    outside_columns = set()
    for column in pres["free_low"]:
        label = pres["ordered_columns"][column]
        image = connection_image(label, names, axis, pres["columns"], fiber, point)
        reduced = base.reduce_row(image, pres["pivots"])
        outside = set(reduced) - free
        if outside:
            leaking_sources += 1
            outside_columns.update(outside)
    return {
        "leaking_source_basis_vectors": leaking_sources,
        "distinct_outside_columns": len(outside_columns),
        "outside_labels": [pres["ordered_columns"][column] for column in sorted(outside_columns)],
        "connection_stable": leaking_sources == 0,
    }


def matmul(left, right):
    rows, middle, cols = len(left), len(right), len(right[0])
    assert len(left[0]) == middle
    out = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    out[i][j] = (out[i][j] + value * other) % P
    return out


source = charts.presentation(base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES)
target = charts.presentation(charts.g31_fiber_data, charts.TARGET_POINT, charts.TARGET_NAMES)

target_pos = {column: i for i, column in enumerate(target["free_low"])}
transport = [[0] * 21 for _ in range(21)]
for source_index, source_column in enumerate(source["free_low"]):
    label = source["ordered_columns"][source_column]
    row = charts.quotient_vector(charts.map_label(label), target, -1)
    for target_column, value in row.items():
        transport[target_pos[target_column]][source_index] = value

source_connections = [
    connection_matrix(source, charts.SOURCE_NAMES, base.fiber_data, charts.SOURCE_POINT, axis)
    for axis in range(3)
]
target_connections = [
    connection_matrix(target, charts.TARGET_NAMES, charts.g31_fiber_data, charts.TARGET_POINT, axis)
    for axis in range(3)
]
source_leakage = [
    connection_leakage(source, charts.SOURCE_NAMES, base.fiber_data, charts.SOURCE_POINT, axis)
    for axis in range(3)
]
target_leakage = [
    connection_leakage(target, charts.TARGET_NAMES, charts.g31_fiber_data, charts.TARGET_POINT, axis)
    for axis in range(3)
]

axis_map = {0: 0, 1: 2, 2: 1}
raw_derivative_checks = []
for source_axis, target_axis in axis_map.items():
    sk, sq = parameter_derivative_data(base.fiber_data, charts.SOURCE_POINT, source_axis)
    tk, tq = parameter_derivative_data(charts.g31_fiber_data, charts.TARGET_POINT, target_axis)
    q_ok = all(
        charts.swap_exponents(sq[sname]) == tq[tname]
        for sname, tname in zip(charts.SOURCE_NAMES, charts.TARGET_NAMES)
    )
    raw_derivative_checks.append({
        "source_axis": source_axis,
        "target_axis": target_axis,
        "K_derivative_match": charts.swap_exponents(sk) == tk,
        "q_derivatives_match": q_ok,
    })
chain_level_failures = []
for source_axis, target_axis in axis_map.items():
    failures = 0
    for source_column in source["free_low"]:
        label = source["ordered_columns"][source_column]
        source_image = connection_image(
            label, charts.SOURCE_NAMES, source_axis, source["columns"],
            base.fiber_data, charts.SOURCE_POINT,
        )
        mapped_source_image = charts.map_row(source_image, source, target, -1)
        route_one = base.reduce_row(mapped_source_image, target["pivots"])
        target_image = connection_image(
            charts.map_label(label), charts.TARGET_NAMES, target_axis,
            target["columns"], charts.g31_fiber_data, charts.TARGET_POINT,
        )
        route_two = base.reduce_row(
            {column: (-value) % P for column, value in target_image.items()},
            target["pivots"],
        )
        if route_one != route_two:
            failures += 1
    chain_level_failures.append({
        "source_axis": source_axis,
        "target_axis": target_axis,
        "free_basis_failures": failures,
    })
checks = []
for source_axis, target_axis in axis_map.items():
    left = matmul(transport, source_connections[source_axis])
    right = matmul(target_connections[target_axis], transport)
    failures = sum(a != b for row_a, row_b in zip(left, right) for a, b in zip(row_a, row_b))
    sign_failures = sum(a != (-b) % P for row_a, row_b in zip(left, right) for a, b in zip(row_a, row_b))
    checks.append({
        "source_axis": source_axis,
        "target_axis": target_axis,
        "entry_failures": failures,
        "opposite_sign_entry_failures": sign_failures,
        "passed": failures == 0,
    })

payload = {
    "schema": "marici.rank21-occurrence-reflection-connection.v1",
    "field": P,
    "source_chart": "G12 at (2,3,4)",
    "target_chart": "G31 at (2,4,3)",
    "transport_rank": charts.matrix_rank([
        {i: value for i, value in enumerate(row) if value}
        for row in transport
    ]),
    "transport_orientation_sign": -1,
    "axis_map": {"X1": "X1", "X2": "X3", "X3": "X2"},
    "source_low_block_leakage": source_leakage,
    "target_low_block_leakage": target_leakage,
    "intertwining_checks": checks,
    "raw_derivative_checks": raw_derivative_checks,
    "chain_level_naturality": chain_level_failures,
    "all_intertwining_checks_passed": all(check["passed"] for check in checks),
    "transport_sha256": hashlib.sha256(json.dumps(transport, separators=(",", ":")).encode()).hexdigest(),
    "status": (
        "chain_natural_but_rank21_projection_not_connection_stable"
        if (
            all(check["free_basis_failures"] == 0 for check in chain_level_failures)
            and any(not check["connection_stable"] for check in source_leakage + target_leakage)
        )
        else "intertwining_failed"
    ),
}

out = Path(__file__).with_name("rank21-occurrence-reflection-connection.json")
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2, sort_keys=True))
