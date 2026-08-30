"""Rees ranks of the primitive source-word rank-26 packet at total energy."""

from __future__ import annotations

import contextlib
import hashlib
import importlib
import io
import json
import os
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "research" / "nima"))

import check_rank26_total_energy_triple_relation_module as rees

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")


ORDER = 3
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "14"))
ENGINE = (
    ROOT
    / ".narada"
    / "runtime"
    / "benincasa"
    / "sparse_modular_submodule_rank_stream.exe"
)
DESCRIPTORS = json.loads((HERE / "rank26-source-word-basis.json").read_text())[
    "descriptors"
]
P = rees.base.PRIME


def jet_constant(value):
    return (value % P,) + (0,) * (ORDER - 1)


def jet_add(left, right):
    return tuple((a + b) % P for a, b in zip(left, right, strict=True))


def jet_scale(value, scale):
    return tuple(scale * coefficient % P for coefficient in value)


def jet_multiply(left, right):
    result = [0] * ORDER
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j < ORDER:
                result[i + j] = (result[i + j] + a * b) % P
    return tuple(result)


def jet_square(value):
    return jet_multiply(value, value)


def clean(polynomial):
    return {exponent: value for exponent, value in polynomial.items() if any(value)}


def fiber_jet_data(x, y, z):
    xj, yj = jet_constant(x), jet_constant(y)
    energy = jet_add(jet_add(xj, yj), z)
    x2, y2, z2, c2 = map(jet_square, (xj, yj, z, energy))
    x2_minus_y2_z2 = jet_add(x2, jet_scale(jet_add(y2, z2), -1))
    y2_minus_x2_z2 = jet_add(y2, jet_scale(jet_add(x2, z2), -1))
    z2_minus_x2_y2 = jet_add(z2, jet_scale(jet_add(x2, y2), -1))
    k = {
        (4, 0): x2,
        (2, 2): jet_scale(jet_add(jet_add(x2, y2), jet_scale(z2, -1)), -1),
        (0, 4): y2,
        (2, 0): jet_add(
            jet_multiply(x2, x2_minus_y2_z2),
            jet_multiply(c2, jet_add(y2, jet_scale(jet_add(x2, z2), -1))),
        ),
        (0, 2): jet_add(
            jet_multiply(y2, y2_minus_x2_z2),
            jet_multiply(c2, jet_add(x2, jet_scale(jet_add(y2, z2), -1))),
        ),
        (0, 0): jet_add(
            jet_add(jet_multiply(z2, jet_square(c2)), jet_multiply(jet_multiply(c2, z2), z2_minus_x2_y2)),
            jet_multiply(jet_multiply(z2, x2), y2),
        ),
    }
    q = {
        "g1": {(0, 1): jet_constant(1), (0, 0): jet_scale(jet_add(yj, z), -1)},
        "g2": {(1, 0): jet_constant(1), (0, 0): jet_scale(jet_add(xj, z), -1)},
        "g3": {(1, 0): jet_constant(1), (0, 1): jet_constant(1), (0, 0): z},
        "g23": {(0, 1): jet_constant(1), (0, 0): jet_scale(xj, -1)},
        "g31": {(1, 0): jet_constant(1), (0, 0): jet_scale(yj, -1)},
    }
    return clean(k), {name: clean(poly) for name, poly in q.items()}


def polynomial_add(target, source, scale=1):
    for exponent, value in source.items():
        target[exponent] = jet_add(
            target.get(exponent, jet_constant(0)), jet_scale(value, scale)
        )
        if not any(target[exponent]):
            target.pop(exponent)


def derivative_jet_data(x, y, z, axis):
    nodes = rees.OFFSETS
    weights = rees.interpolation_weights(1)
    k_result = {}
    q_result = {}
    for offset, weight in zip(nodes, weights, strict=True):
        shifted_x, shifted_y, shifted_z = x, y, z
        if axis == 0:
            shifted_x += offset
        elif axis == 1:
            shifted_y += offset
        else:
            shifted_z = jet_add(z, jet_constant(offset))
        k, q = fiber_jet_data(shifted_x, shifted_y, shifted_z)
        polynomial_add(k_result, k, weight)
        for name, polynomial in q.items():
            polynomial_add(q_result.setdefault(name, {}), polynomial, weight)
    return clean(k_result), {name: clean(poly) for name, poly in q_result.items()}


def interpolate_numeric_polynomials(samples, degree):
    weights = rees.interpolation_weights(degree)
    result = {}
    for polynomial, weight in zip(samples, weights, strict=True):
        for exponent, value in polynomial.items():
            result[exponent] = (result.get(exponent, 0) + weight * value) % P
    return {exponent: value for exponent, value in result.items() if value}


def jet_polynomial_coefficient(polynomial, degree):
    return {
        exponent: value[degree]
        for exponent, value in polynomial.items()
        if value[degree]
    }


def validate_parameter_jets():
    x, y, z0 = rees.POINT
    z = (z0 % P, 1, 0)
    k_jet, q_jet = fiber_jet_data(x, y, z)
    sampled_fibers = [
        rees.base.fiber_data(x, y, z0 + offset) for offset in rees.OFFSETS
    ]
    for degree in range(ORDER):
        assert jet_polynomial_coefficient(k_jet, degree) == interpolate_numeric_polynomials(
            [sample[0] for sample in sampled_fibers], degree
        )
        for name in rees.NAMES:
            assert jet_polynomial_coefficient(q_jet[name], degree) == interpolate_numeric_polynomials(
                [sample[1][name] for sample in sampled_fibers], degree
            )
    for axis in range(3):
        kd_jet, qd_jet = derivative_jet_data(x, y, z, axis)
        sampled_derivatives = [
            audit.parameter_derivative_data(
                rees.base.fiber_data, (x, y, z0 + offset), axis
            )
            for offset in rees.OFFSETS
        ]
        for degree in range(ORDER):
            assert jet_polynomial_coefficient(kd_jet, degree) == interpolate_numeric_polynomials(
                [sample[0] for sample in sampled_derivatives], degree
            )
            for name in rees.NAMES:
                assert jet_polynomial_coefficient(qd_jet[name], degree) == interpolate_numeric_polynomials(
                    [sample[1][name] for sample in sampled_derivatives], degree
                )
    return 4 * ORDER


def row_add(target, column, value):
    target[column] = jet_add(target.get(column, jet_constant(0)), value)
    if not any(target[column]):
        target.pop(column)


def raw_source(columns, q):
    numerator = dict(q["g23"])
    polynomial_add(numerator, q["g31"])
    prefix = (0, 1, 1, 1, 1, 1)
    return {columns[prefix + (exponent,)]: value for exponent, value in numerator.items()}


def raw_source_derivative(columns, qd):
    derivative = dict(qd["g23"])
    polynomial_add(derivative, qd["g31"])
    prefix = (0, 1, 1, 1, 1, 1)
    return {
        columns[prefix + (exponent,)]: value
        for exponent, value in derivative.items()
        if prefix + (exponent,) in columns
    }


def raw_connection(row, axis, ordered, columns, derivatives):
    kd, qd = derivatives[axis]
    image = {}
    for column, coefficient in row.items():
        k_pole, *rest = ordered[column]
        exponent = rest.pop()
        levels = rest
        if k_pole < rees.charts.K_DEPTH:
            for term, value in kd.items():
                target = (k_pole + 1, *levels, rees.base.shifted(exponent, term))
                if target in columns:
                    row_add(
                        image,
                        columns[target],
                        jet_scale(jet_multiply(coefficient, value), rees.charts.GAMMA - k_pole),
                    )
        for qi, level in enumerate(levels):
            if level >= rees.charts.Q_DEPTH:
                continue
            raised = list(levels)
            raised[qi] += 1
            for term, value in qd[rees.NAMES[qi]].items():
                target = (k_pole, *raised, rees.base.shifted(exponent, term))
                if target in columns:
                    row_add(
                        image,
                        columns[target],
                        jet_scale(jet_multiply(coefficient, value), -level),
                    )
    return image


def source_word_jets(columns):
    ordered = [None] * len(columns)
    for label, column in columns.items():
        ordered[column] = label
    x, y, _ = rees.POINT
    z = (rees.POINT[2] % P, 1, 0)
    _, q = fiber_jet_data(x, y, z)
    derivatives = [derivative_jet_data(x, y, z, axis) for axis in range(3)]
    source = raw_source(columns, q)
    roots = {"S": source}
    for axis in range(3):
        derivative = raw_connection(source, axis, ordered, columns, derivatives)
        correction = raw_source_derivative(columns, derivatives[axis][1])
        for column, value in correction.items():
            row_add(derivative, column, value)
        roots[f"D{axis}"] = derivative
    rows = []
    for descriptor in DESCRIPTORS:
        row = roots[descriptor["root"]]
        for axis in descriptor["connection_path"]:
            row = raw_connection(row, axis, ordered, columns, derivatives)
        rows.append(row)
    return rows


def write_numeric_row(stream, kind, row):
    items = sorted((column, value % P) for column, value in row.items() if value % P)
    stream.write(struct.pack("<BI", kind, len(items)))
    for column, value in items:
        stream.write(struct.pack("<II", column, value))


def source_row_at_order(row, width, order, shift):
    result = {}
    for column, jet in row.items():
        for grade, value in enumerate(jet[: order - shift]):
            if value:
                result[(grade + shift) * width + column] = value
    return result


def main():
    assert ENGINE.exists()
    parameter_jet_checks = validate_parameter_jets()
    low_labels, columns = rees.column_packet()
    width = len(columns)
    points = [
        (rees.POINT[0], rees.POINT[1], rees.POINT[2] + offset)
        for offset in rees.OFFSETS
    ]
    generators = [rees.raw_relations(point, columns) for point in points]
    check_generator = rees.raw_relations(
        (rees.POINT[0], rees.POINT[1], rees.POINT[2] + rees.CHECK_OFFSET), columns
    )
    first_weights = rees.interpolation_weights(1)
    second_weights = rees.interpolation_weights(2)
    check_weights = rees.evaluation_weights(rees.CHECK_OFFSET)

    process = subprocess.Popen(
        [str(ENGINE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I", P))
    relation_count = 0
    for all_rows in zip(*generators, check_generator, strict=True):
        relation_count += 1
        sampled_rows, check_row = all_rows[:-1], all_rows[-1]
        assert rees.combine((rees.combine(sampled_rows, check_weights), check_row), (1, -1)) == {}
        r0 = dict(sampled_rows[rees.OFFSETS.index(0)])
        r1 = rees.combine(sampled_rows, first_weights)
        r2 = rees.combine(sampled_rows, second_weights)
        write_numeric_row(process.stdin, 0, r0)
        write_numeric_row(process.stdin, 1, rees.shifted_row(r0, width, 1))
        write_numeric_row(process.stdin, 1, rees.assemble((r0, r1), width))
        write_numeric_row(process.stdin, 2, rees.shifted_row(r0, width, 2))
        write_numeric_row(process.stdin, 2, rees.assemble(({}, r0, r1), width))
        write_numeric_row(process.stdin, 2, rees.assemble((r0, r1, r2), width))

    source_rows = source_word_jets(columns)
    assert len(source_rows) == 26
    for order in range(1, ORDER + 1):
        for row in source_rows:
            for shift in range(order):
                write_numeric_row(
                    process.stdin,
                    order + 2,
                    source_row_at_order(row, width, order, shift),
                )
    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout, stderr = process.stdout.read(), process.stderr.read()
    return_code = process.wait()
    if return_code:
        raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine_result = json.loads(stdout)
    ranks = engine_result["source_image_ranks"]
    result = {
        "schema": "marici.benincasa.rank26-total-energy-source-word-rees.v1",
        "field": P,
        "point": list(rees.POINT),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": rees.CUTOFF,
        "source_word_count": len(source_rows),
        "maximum_connection_depth": max(item["depth"] for item in DESCRIPTORS),
        "source_rees_image_ranks": {"T1": ranks[0], "T2": ranks[1], "T3": ranks[2]},
        "first_differences": [ranks[1] - ranks[0], ranks[2] - ranks[1]],
        "relation_count": relation_count,
        "parameter_jet_checks": parameter_jet_checks,
        "rank_engine": {
            "source": "research/benincasa/sparse_modular_submodule_rank_stream.rs",
            "executable_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),
            "result": engine_result,
        },
        "primitive_convention": (
            "breadth-first unreduced source words; exact truncated parameter jets; "
            "relations are applied only after all primitives are constructed"
        ),
        "warning": (
            "these A-word primitives must still pass Gauss-Manin closure and "
            "regular source-basis invariance before being called the nearby lattice"
        ),
    }
    point_suffix = ""
    if os.environ.get("MARICI_POINT"):
        encoded_point = "-".join(
            f"m{-value}" if value < 0 else str(value) for value in rees.POINT
        )
        point_suffix = f"-point-{encoded_point}"
    output = HERE / (
        f"rank26-total-energy-source-word-rees-a{AMBIENT}-p{P}{point_suffix}.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
