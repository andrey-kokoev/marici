"""Embed triangle-wall quadratic basis rows by exact column labels.

Column numbers are not assumed stable when ambient degree grows.  This script
reconstructs both presentations and maps each of the three normal-jet blocks
through the common labelled source column.
"""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = audit.base, audit.charts
P = base.PRIME


def columns(ambient: int, k_depth: int, q_depth: int):
    old = (charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH)
    charts.AMBIENT, charts.CUTOFF = ambient, 6
    charts.K_DEPTH, charts.Q_DEPTH = k_depth, q_depth
    try:
        presentation = charts.presentation(
            base.fiber_data, (2, 3, 5), charts.SOURCE_NAMES
        )
        return tuple(presentation["ordered_columns"])
    finally:
        charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old


def parse_row(line: str):
    return {
        int(column): int(value) % P
        for term in line.strip().split(",")
        if term
        for column, value in (term.split(":"),)
    }


parser = argparse.ArgumentParser()
parser.add_argument("--source-ambient", type=int, default=10)
parser.add_argument("--target-ambient", type=int, default=11)
parser.add_argument("--k-depth", type=int, default=3)
parser.add_argument("--source-k-depth", type=int)
parser.add_argument("--target-k-depth", type=int)
parser.add_argument("--q-depth", type=int, default=2)
parser.add_argument("--basis", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

source_k_depth = args.k_depth if args.source_k_depth is None else args.source_k_depth
target_k_depth = args.k_depth if args.target_k_depth is None else args.target_k_depth
source_columns = columns(args.source_ambient, source_k_depth, args.q_depth)
target_columns = columns(args.target_ambient, target_k_depth, args.q_depth)
target_index = {label: index for index, label in enumerate(target_columns)}
missing = [label for label in source_columns if label not in target_index]
if missing:
    raise RuntimeError(f"{len(missing)} source labels missing from target")

rows = [parse_row(line) for line in args.basis.read_text().splitlines() if line]
embedded = []
for row in rows:
    mapped = {}
    for column, value in row.items():
        block, within = divmod(column, len(source_columns))
        if block >= 3:
            raise RuntimeError(f"unexpected normal-jet block {block}")
        target = block * len(target_columns) + target_index[source_columns[within]]
        mapped[target] = value
    embedded.append(mapped)

args.output.write_text(
    "\n".join(
        ",".join(f"{column}:{value}" for column, value in sorted(row.items()))
        for row in embedded
    )
    + "\n",
    encoding="utf-8",
)
print(
    f'{{"schema":"marici.triangle-wall-ambient-inclusion-probes.v1",'
    f'"source_ambient":{args.source_ambient},'
    f'"target_ambient":{args.target_ambient},'
        f'"source_k_depth":{source_k_depth},'
        f'"target_k_depth":{target_k_depth},"q_depth":{args.q_depth},'
    f'"source_columns":{len(source_columns)},'
    f'"target_columns":{len(target_columns)},'
    f'"probe_count":{len(embedded)},"missing_labels":0}}'
)
