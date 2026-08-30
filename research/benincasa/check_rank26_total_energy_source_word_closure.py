"""Strict normal Gauss--Manin closure of the source-word Rees lattice."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess
from pathlib import Path

import check_rank26_total_energy_source_word_rees as source


ROOT = source.ROOT
HERE = source.HERE
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "14"))
LOGARITHMIC = os.environ.get("MARICI_LOGARITHMIC", "0") == "1"
ENGINE = ROOT / ".narada" / "runtime" / "benincasa" / "sparse_modular_submodule_closure_stream.exe"
P = source.P


def normal_covariant_derivative(row, ordered, columns, derivatives):
    """Return d/dE(row)+A_z(row), retaining coefficients through E^1."""
    result = {}
    for column, jet in row.items():
        derivative = (jet[1], 2 * jet[2] % P, 0)
        if any(derivative):
            source.row_add(result, column, derivative)
    connection = source.raw_connection(row, 2, ordered, columns, derivatives)
    for column, value in connection.items():
        source.row_add(result, column, value)
    return result


def relation_rows(columns, width, process):
    points = [
        (source.rees.POINT[0], source.rees.POINT[1], source.rees.POINT[2] + offset)
        for offset in source.rees.OFFSETS
    ]
    generators = [source.rees.raw_relations(point, columns) for point in points]
    check_generator = source.rees.raw_relations(
        (source.rees.POINT[0], source.rees.POINT[1], source.rees.POINT[2] + source.rees.CHECK_OFFSET),
        columns,
    )
    first_weights = source.rees.interpolation_weights(1)
    count = 0
    for all_rows in zip(*generators, check_generator, strict=True):
        count += 1
        sampled_rows, check_row = all_rows[:-1], all_rows[-1]
        assert source.rees.combine(
            (source.rees.combine(sampled_rows, source.rees.evaluation_weights(source.rees.CHECK_OFFSET)), check_row),
            (1, -1),
        ) == {}
        r0 = dict(sampled_rows[source.rees.OFFSETS.index(0)])
        r1 = source.rees.combine(sampled_rows, first_weights)
        source.write_numeric_row(process.stdin, 0, r0)
        source.write_numeric_row(process.stdin, 1, source.rees.shifted_row(r0, width, 1))
        source.write_numeric_row(process.stdin, 1, source.rees.assemble((r0, r1), width))
    return count


def main():
    assert ENGINE.exists()
    checks = source.validate_parameter_jets()
    _, columns = source.rees.column_packet()
    width = len(columns)
    ordered = [None] * width
    for label, column in columns.items():
        ordered[column] = label
    x, y, z0 = source.rees.POINT
    z = (z0 % P, 1, 0)
    derivatives = [source.derivative_jet_data(x, y, z, axis) for axis in range(3)]
    rows = source.source_word_jets(columns)
    normal_rows = [normal_covariant_derivative(row, ordered, columns, derivatives) for row in rows]

    process = subprocess.Popen([str(ENGINE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I", P))
    relation_count = relation_rows(columns, width, process)
    for order in (1, 2):
        for row in rows:
            for shift in range(order):
                source.write_numeric_row(process.stdin, order + 1, source.source_row_at_order(row, width, order, shift))
    for order in (1, 2):
        for row in normal_rows:
            shift = 1 if LOGARITHMIC else 0
            source.write_numeric_row(
                process.stdin,
                order + 3,
                source.source_row_at_order(row, width, order, shift),
            )
    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout, stderr = process.stdout.read(), process.stderr.read()
    if process.wait():
        raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine = json.loads(stdout)
    result = {
        "schema": "marici.benincasa.rank26-total-energy-source-word-closure.v1",
        "field": P,
        "point": list(source.rees.POINT),
        "ambient_relation_degree": AMBIENT,
        "source_word_count": len(rows),
        "relation_count": relation_count,
        "parameter_jet_checks": checks,
        "normal_connection": (
            "E*(d/dE + A_z) at fixed x,y with z=E-x-y"
            if LOGARITHMIC
            else "d/dE + A_z at fixed x,y with z=E-x-y"
        ),
        "source_image_ranks": engine["source_image_ranks"],
        "normal_derivative_extension_ranks": engine["test_extension_ranks"],
        "closure_mode": "logarithmic" if LOGARITHMIC else "strict",
        "normal_closure": engine["test_extension_ranks"] == [0, 0],
        "rank_engine": {
            "source": "research/benincasa/sparse_modular_submodule_closure_stream.rs",
            "executable_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),
            "result": engine,
        },
    }
    point_suffix = ""
    if os.environ.get("MARICI_POINT"):
        encoded = "-".join(f"m{-v}" if v < 0 else str(v) for v in source.rees.POINT)
        point_suffix = f"-point-{encoded}"
    mode_suffix = "-log" if LOGARITHMIC else ""
    output = HERE / f"rank26-total-energy-source-word-closure{mode_suffix}-a{AMBIENT}-p{P}{point_suffix}.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
