"""Remap a normal-jet basis between ambient cutoffs by labelled columns."""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "nima"))
with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = audit.base, audit.charts


def columns_at(ambient, k_depth, q_depth):
    old = charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    charts.K_DEPTH, charts.Q_DEPTH = k_depth, q_depth
    try:
        return charts.presentation(base.fiber_data, (2, 3, 5), charts.SOURCE_NAMES)["columns"]
    finally:
        charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old


parser = argparse.ArgumentParser()
parser.add_argument("--source-ambient", type=int, required=True)
parser.add_argument("--target-ambient", type=int, required=True)
parser.add_argument("--k-depth", type=int, default=3)
parser.add_argument("--q-depth", type=int, default=2)
parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

old_columns = columns_at(args.source_ambient, args.k_depth, args.q_depth)
new_columns = columns_at(args.target_ambient, args.k_depth, args.q_depth)
old_inverse = {column: label for label, column in old_columns.items()}

lines = []
for line in args.input.read_text(encoding="utf-8").splitlines():
    remapped = {}
    for term in line.split(","):
        if not term:
            continue
        column_text, value = term.split(":")
        column = int(column_text)
        block, within = divmod(column, len(old_columns))
        label = old_inverse[within]
        remapped[block * len(new_columns) + new_columns[label]] = int(value)
    lines.append(",".join(f"{column}:{value}" for column, value in sorted(remapped.items())))

args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f'{{"rows":{len(lines)},"source_columns":{len(old_columns)},"target_columns":{len(new_columns)}}}')
