"""Relative low/high Rees audit for the rank-26 total-energy family."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

import check_rank26_total_energy_triple_relation_module as rees


AMBIENT = int(os.environ.get("MARICI_AMBIENT", "12"))
ENGINE = (
    ROOT
    / ".narada"
    / "runtime"
    / "benincasa"
    / "sparse_modular_relative_rank_stream.exe"
)


def reorder_column(column, width, low_count, jet_order):
    grade, base_column = divmod(column, width)
    assert grade < jet_order
    if base_column < low_count:
        return grade * low_count + base_column
    high_count = width - low_count
    return (
        jet_order * low_count
        + grade * high_count
        + base_column
        - low_count
    )


def write_row(stream, kind, row, width, low_count, jet_order):
    reordered = {}
    for column, value in row.items():
        value %= rees.base.PRIME
        if value:
            reordered[reorder_column(column, width, low_count, jet_order)] = value
    items = sorted(reordered.items())
    stream.write(struct.pack("<BI", kind, len(items)))
    for column, value in items:
        stream.write(struct.pack("<II", column, value))


def presentation(point):
    old_ambient, old_cutoff = rees.charts.AMBIENT, rees.charts.CUTOFF
    rees.charts.AMBIENT, rees.charts.CUTOFF = AMBIENT, rees.CUTOFF
    try:
        return rees.charts.presentation(rees.base.fiber_data, point, rees.NAMES)
    finally:
        rees.charts.AMBIENT, rees.charts.CUTOFF = old_ambient, old_cutoff


def main():
    assert ENGINE.exists(), f"compile the relative rank engine first: {ENGINE}"
    low_labels, columns = rees.column_packet()
    width = len(columns)
    low_count = len(low_labels)
    points = [
        (rees.POINT[0], rees.POINT[1], rees.POINT[2] + offset)
        for offset in rees.OFFSETS
    ]
    generators = [rees.raw_relations(point, columns) for point in points]
    check_generator = rees.raw_relations(
        (rees.POINT[0], rees.POINT[1], rees.POINT[2] + rees.CHECK_OFFSET),
        columns,
    )
    first_weights = rees.interpolation_weights(1)
    second_weights = rees.interpolation_weights(2)
    check_weights = rees.evaluation_weights(rees.CHECK_OFFSET)

    process = subprocess.Popen(
        [str(ENGINE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    assert process.stdin is not None
    process.stdin.write(
        struct.pack("<IIII", rees.base.PRIME, low_count, 2 * low_count, 3 * low_count)
    )
    relation_count = 0
    degree_bound_checks = 0
    for all_rows in zip(*generators, check_generator, strict=True):
        relation_count += 1
        sampled_rows = all_rows[:-1]
        check_row = all_rows[-1]
        predicted_check = rees.combine(sampled_rows, check_weights)
        assert rees.combine((predicted_check, check_row), (1, -1)) == {}
        degree_bound_checks += 1
        r0 = dict(sampled_rows[rees.OFFSETS.index(0)])
        r1 = rees.combine(sampled_rows, first_weights)
        r2 = rees.combine(sampled_rows, second_weights)

        write_row(process.stdin, 0, r0, width, low_count, 1)
        write_row(
            process.stdin, 1, rees.shifted_row(r0, width, 1), width, low_count, 2
        )
        write_row(
            process.stdin, 1, rees.assemble((r0, r1), width), width, low_count, 2
        )
        write_row(
            process.stdin, 2, rees.shifted_row(r0, width, 2), width, low_count, 3
        )
        write_row(
            process.stdin,
            2,
            rees.assemble(({}, r0, r1), width),
            width,
            low_count,
            3,
        )
        write_row(
            process.stdin,
            2,
            rees.assemble((r0, r1, r2), width),
            width,
            low_count,
            3,
        )

    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout = process.stdout.read()
    stderr = process.stderr.read()
    return_code = process.wait()
    if return_code:
        raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine_result = json.loads(stdout)

    special_reference = presentation(rees.POINT)
    generic_point = (rees.POINT[0], rees.POINT[1], rees.POINT[2] + 1)
    generic_reference = presentation(generic_point)
    low_ranks = engine_result["low_intersection_ranks"]
    dimensions = [
        (order + 1) * low_count - low_ranks[order] for order in range(3)
    ]
    assert dimensions[0] == len(special_reference["free_low"])
    generic_rank = len(generic_reference["free_low"])
    first_differences = [dimensions[1] - dimensions[0], dimensions[2] - dimensions[1]]
    affine_through_order_three = first_differences == [generic_rank, generic_rank]
    finite_costalk = generic_rank - dimensions[0]

    payload = {
        "schema": "marici.benincasa.rank26-total-energy-relative-low-rees.v1",
        "field": rees.base.PRIME,
        "point": list(rees.POINT),
        "generic_control_point": list(generic_point),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": rees.CUTOFF,
        "low_column_count": low_count,
        "full_column_count": width,
        "raw_relation_count": relation_count,
        "degree_bound_checks_passed": degree_bound_checks,
        "relative_object": "L_n / (R_n intersection L_n)",
        "low_rees_dimensions": {"T1": dimensions[0], "T2": dimensions[1], "T3": dimensions[2]},
        "first_differences": first_differences,
        "second_difference": first_differences[1] - first_differences[0],
        "generic_low_rank": generic_rank,
        "ordinary_special_low_rank": dimensions[0],
        "finite_costalk_candidate": finite_costalk,
        "affine_through_order_three": affine_through_order_three,
        "affine_formula_if_stable": (
            f"T_n={generic_rank}*n-{finite_costalk}"
            if affine_through_order_three
            else None
        ),
        "rank_engine": {
            "source": "research/benincasa/sparse_modular_relative_rank_stream.rs",
            "executable_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),
            "result": engine_result,
        },
        "typing": (
            "high Laurent columns are eliminated before low pivots are read; "
            "specialization/intersection noncommutation is retained"
        ),
        "scope": (
            "finite-cutoff relative algebra through E_T^3; affine behavior must "
            "still be replicated across ambient cutoffs, primes, and points"
        ),
    }
    point_suffix = ""
    if os.environ.get("MARICI_POINT"):
        encoded_point = "-".join(
            f"m{-value}" if value < 0 else str(value) for value in rees.POINT
        )
        point_suffix = f"-point-{encoded_point}"
    output = Path(__file__).with_name(
        f"rank26-total-energy-relative-low-rees-a{AMBIENT}"
        f"-p{rees.base.PRIME}{point_suffix}.json"
    )
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
