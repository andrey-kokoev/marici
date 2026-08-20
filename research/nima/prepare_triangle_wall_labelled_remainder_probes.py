"""Embed decoded triangle-wall remainder rows into a labelled target packet.

This is an inclusion test, not a connection construction.  Every sparse term
is rebuilt from its frozen ``(normal block, K pole, q levels, exponent)`` label
and lookup is strict: a missing target label aborts the export.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "nima"))

with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module(
        "check_unbounded_twisted_derham_connection_commutator"
    )

charts = source.charts
P = source.P


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--target-ambient", type=int, required=True)
    parser.add_argument("--target-k-depth", type=int, required=True)
    parser.add_argument("--target-q-depth", type=int, default=2)
    args = parser.parse_args()

    packet = json.loads(args.input.read_text(encoding="utf-8"))
    old = (charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH)
    charts.AMBIENT, charts.CUTOFF = args.target_ambient, 6
    charts.K_DEPTH, charts.Q_DEPTH = (
        args.target_k_depth,
        args.target_q_depth,
    )
    try:
        presentation = charts.presentation(
            source.base.fiber_data, (2, 3, 5), charts.SOURCE_NAMES
        )
    finally:
        charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old

    columns = presentation["columns"]
    width = len(presentation["ordered_columns"])
    lines = []
    attempted = 0
    for probe in packet["probes"]:
        row: dict[int, int] = {}
        for term in probe["terms"]:
            attempted += 1
            label = (
                term["k_pole"],
                *term["q_levels"],
                tuple(term["exponent"]),
            )
            if label not in columns:
                raise RuntimeError(f"target omits remainder label {label!r}")
            column = term["normal_block"] * width + columns[label]
            row[column] = (row.get(column, 0) + term["value"]) % P
        lines.append(
            ",".join(
                f"{column}:{value}"
                for column, value in sorted(row.items())
                if value
            )
        )

    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "schema": "marici.triangle-wall-labelled-remainder-inclusion.v1",
                "source_probe_count": len(packet["probes"]),
                "attempted_terms": attempted,
                "emitted_terms": sum(bool(value) for line in lines for value in line.split(",") if value),
                "omitted_labels": 0,
                "target_ambient": args.target_ambient,
                "target_k_depth": args.target_k_depth,
                "target_q_depth": args.target_q_depth,
                "target_columns": width,
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
