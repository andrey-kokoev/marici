"""Stream a covariant source-jet rank into a declared finite target."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess
from pathlib import Path

import check_adapted_true_covariant_source_jets as adapted
import check_cutoff_inclusion_gauss_manin_adapter as adapter


source = adapted.source
jets = adapted.jets
P = source.P
DEPTH = adapted.DEPTH
AMBIENT = int(os.environ.get("MARICI_TARGET_AMBIENT", "12"))
K_DEPTH = int(os.environ.get("MARICI_TARGET_K_DEPTH", "3"))
Q_DEPTHS = [int(value) for value in os.environ.get("MARICI_TARGET_Q_DEPTHS", "3,3,3,3,3").split(",")]
AXES = [int(value) for value in os.environ.get("MARICI_JET_AXES", "0,1,2").split(",")]
ENGINE = Path(os.environ.get(
    "MARICI_RANK_ENGINE",
    source.ROOT / ".narada" / "runtime" / "benincasa" / "sparse_modular_submodule_closure_stream.exe",
))


def main():
    assert len(Q_DEPTHS) == len(source.rees.NAMES)
    assert AXES and all(axis in (0, 1, 2) for axis in AXES)
    point = tuple(int(value) for value in os.environ.get("MARICI_JET_POINT", "2,3,-4").split(","))
    _, columns = adapter.packet(AMBIENT, K_DEPTH, Q_DEPTHS)
    ordered = [None] * len(columns)
    for label, column in columns.items():
        ordered[column] = label
    relations = adapter.relations(point, columns, AMBIENT, K_DEPTH, Q_DEPTHS)
    k, q = jets.fiber_data(point)

    rows = []
    frontier = [jets.raw_source(columns, q)]
    frontier_labels = ["S"]
    word_labels = []
    words_per_depth = []
    for depth in range(DEPTH + 1):
        words_per_depth.append(len(frontier))
        rows.extend(jets.center(row) for row in frontier)
        word_labels.extend(frontier_labels)
        if depth < DEPTH:
            frontier = [
                adapted.covariant(row, axis, ordered, columns, k, q, K_DEPTH, Q_DEPTHS)
                for row in frontier
                for axis in AXES
            ]
            frontier_labels = [f"{label}.D{axis}" for label in frontier_labels for axis in AXES]

    process = subprocess.Popen([str(ENGINE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I", P))
    for row in relations:
        source.write_numeric_row(process.stdin, 0, row)
    for row in rows:
        source.write_numeric_row(process.stdin, 4, row)
    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout, stderr = process.stdout.read(), process.stderr.read()
    if process.wait():
        raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine = json.loads(stdout)
    result = {
        "schema": "marici.benincasa.streamed-covariant-source-jet-rank.v1",
        "field": P,
        "point": list(point),
        "maximum_jet_depth": DEPTH,
        "target_ambient": AMBIENT,
        "target_K_depth": K_DEPTH,
        "target_q_depths": dict(zip(source.rees.NAMES, Q_DEPTHS, strict=True)),
        "target_column_count": len(columns),
        "target_relation_count": len(relations),
        "words_per_exact_depth": words_per_depth,
        "derivative_axes": AXES,
        "cumulative_word_count": len(rows),
        "ordered_word_labels": word_labels,
        "cumulative_quotient_rank": engine.get("test_rank", engine.get("test_extension_ranks", [None])[0]),
        "rank_engine_sha256": hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),
        "rank_engine_result": engine,
        "convention": "all covariant words through declared depth streamed after the complete target exact image",
    }
    suffix = "-".join(f"m{-value}" if value < 0 else str(value) for value in point)
    q_suffix = "-".join(map(str, Q_DEPTHS))
    output = Path(__file__).with_name(
        f"streamed-covariant-source-jet-rank-d{DEPTH}-a{AMBIENT}-k{K_DEPTH}-q{q_suffix}-p{P}-point-{suffix}.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
