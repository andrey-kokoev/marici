"""Remap length-three probe rows by exact target-column labels."""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "research" / "nima"
sys.path.insert(0, str(NIMA))

with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module(
        "check_unbounded_twisted_derham_connection_commutator"
    )


def columns(ambient: int):
    charts = source.charts
    old = (charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH)
    charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = (
        ambient,
        6,
        4,
        2,
    )
    try:
        return charts.presentation(
            source.base.fiber_data, (2, 3, 5), charts.SOURCE_NAMES
        )["columns"]
    finally:
        charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old


parser = argparse.ArgumentParser()
parser.add_argument("--source-ambient", type=int, required=True)
parser.add_argument("--target-ambient", type=int, required=True)
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

source_columns = columns(args.source_ambient)
target_columns = columns(args.target_ambient)
source_inverse = {index: label for label, index in source_columns.items()}
source_width = len(source_columns)
target_width = len(target_columns)

lines = []
for line in args.input.read_text().splitlines():
    if not line.strip():
        continue
    remapped = {}
    for term in line.split(","):
        column_text, value = term.split(":")
        column = int(column_text)
        block, within = divmod(column, source_width)
        label = source_inverse[within]
        remapped[block * target_width + target_columns[label]] = value
    lines.append(
        ",".join(f"{column}:{remapped[column]}" for column in sorted(remapped))
    )

args.output.write_text("\n".join(lines) + "\n")
print(
    {
        "source_ambient": args.source_ambient,
        "target_ambient": args.target_ambient,
        "source_width": source_width,
        "target_width": target_width,
        "probe_count": len(lines),
    }
)
