"""Fast exact Rees census and source-closure comparison at total energy."""

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

import check_rank26_tangent_support_closure as support
import check_rank26_total_energy_triple_relation_module as rees


AMBIENT = int(os.environ.get("MARICI_AMBIENT", "8"))
ENGINE = ROOT / ".narada" / "runtime" / "benincasa" / "sparse_modular_rank_stream.exe"
TANGENTS = ((1, 0, -1), (0, 1, -1))


def write_row(stream, kind, row):
    items = sorted((column, value % rees.base.PRIME) for column, value in row.items() if value % rees.base.PRIME)
    stream.write(struct.pack("<BI", kind, len(items)))
    for column, value in items:
        stream.write(struct.pack("<II", column, value))


def main():
    assert ENGINE.exists(), f"compile the rank stream engine first: {ENGINE}"
    low_labels, columns = rees.column_packet()
    width = len(columns)
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
    process.stdin.write(struct.pack("<I", rees.base.PRIME))
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

        write_row(process.stdin, 0, r0)
        write_row(process.stdin, 1, rees.shifted_row(r0, width, 1))
        write_row(process.stdin, 1, rees.assemble((r0, r1), width))
        write_row(process.stdin, 2, rees.shifted_row(r0, width, 2))
        write_row(process.stdin, 2, rees.assemble(({}, r0, r1), width))
        write_row(process.stdin, 2, rees.assemble((r0, r1, r2), width))

    special_reference, source_span, _, source_record = support.tangent_closure_data(
        rees.POINT, TANGENTS, AMBIENT
    )
    ordered = [None] * width
    for label, column in columns.items():
        ordered[column] = label
    assert ordered == special_reference["ordered_columns"]
    assert len(source_span) == 7
    source_rows = list(source_span.values())
    for shift, kind in enumerate((3, 4, 5)):
        for row in source_rows:
            write_row(process.stdin, kind, rees.shifted_row(row, width, shift))

    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout = process.stdout.read()
    stderr = process.stderr.read()
    return_code = process.wait()
    if return_code:
        raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine_result = json.loads(stdout)

    old_ambient, old_cutoff = rees.charts.AMBIENT, rees.charts.CUTOFF
    rees.charts.AMBIENT, rees.charts.CUTOFF = AMBIENT, rees.CUTOFF
    try:
        generic_reference = rees.charts.presentation(
            rees.base.fiber_data,
            (rees.POINT[0], rees.POINT[1], rees.POINT[2] + 1),
            rees.NAMES,
        )
    finally:
        rees.charts.AMBIENT, rees.charts.CUTOFF = old_ambient, old_cutoff

    special_rank, dual_rank, triple_rank = engine_result["relation_ranks"]
    assert special_rank == len(special_reference["pivots"])
    special_dimension = width - special_rank
    generic_dimension = width - len(generic_reference["pivots"])
    dual_dimension = 2 * width - dual_rank
    triple_dimension = 3 * width - triple_rank
    support_excess = special_dimension - generic_dimension
    length_one = 2 * special_dimension - dual_dimension
    length_two = 2 * dual_dimension - special_dimension - triple_dimension
    length_at_least_three = support_excess - length_one - length_two
    assert min(support_excess, length_one, length_two, length_at_least_three) >= 0

    source_ranks = engine_result["image_ranks"]
    assert source_ranks[0] == len(source_span)
    payload = {
        "schema": "marici.benincasa.rank26-total-energy-rees-source-comparison.v1",
        "field": rees.base.PRIME,
        "point": list(rees.POINT),
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": rees.CUTOFF,
        "column_count": width,
        "low_column_count": len(low_labels),
        "raw_relation_count": relation_count,
        "degree_bound_checks_passed": degree_bound_checks,
        "degree_bound_check_offset": rees.CHECK_OFFSET,
        "normal_interpolation_offsets": list(rees.OFFSETS),
        "relation_ranks": {
            "special": special_rank,
            "dual": dual_rank,
            "triple": triple_rank,
            "generic": len(generic_reference["pivots"]),
        },
        "cokernel_dimensions": {
            "generic": generic_dimension,
            "special": special_dimension,
            "dual": dual_dimension,
            "triple": triple_dimension,
        },
        "support_excess": support_excess,
        "elementary_length_census": {
            "length_1": length_one,
            "length_2": length_two,
            "length_at_least_3": length_at_least_three,
        },
        "tangent_source_closure": {
            "declared_rank": len(source_span),
            "multiplication_image_ranks": {
                "E_T^0": source_ranks[0],
                "E_T^1": source_ranks[1],
                "E_T^2": source_ranks[2],
            },
            "source_record": source_record,
            "map": "canonical inclusion into the identical labelled Laurent presentation",
        },
        "rank_engine": {
            "source": "research/benincasa/sparse_modular_rank_stream.rs",
            "executable_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),
            "result": engine_result,
        },
        "scope": (
            "finite-cutoff source comparison inside the complete labelled Laurent "
            "presentation; physical nearby-cycle and Betti pairings remain separate"
        ),
    }
    point_suffix = ""
    if os.environ.get("MARICI_POINT"):
        encoded_point = "-".join(
            f"m{-value}" if value < 0 else str(value) for value in rees.POINT
        )
        point_suffix = f"-point-{encoded_point}"
    output = Path(__file__).with_name(
        f"rank26-total-energy-rees-source-comparison-a{AMBIENT}"
        f"-p{rees.base.PRIME}{point_suffix}.json"
    )
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
