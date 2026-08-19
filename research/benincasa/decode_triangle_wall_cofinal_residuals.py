"""Decode cofinal triangle-wall residual columns into frozen target labels."""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NIMA = ROOT / "research" / "nima"
DEFAULT_INPUT = ROOT / "research" / "benincasa" / (
    "triangle-wall-cofinal-target-fast-residuals.json"
)
DEFAULT_OUTPUT = ROOT / "research" / "benincasa" / (
    "triangle-wall-cofinal-target-labelled-residuals.json"
)

parser = argparse.ArgumentParser()
parser.add_argument("--ambient", type=int, default=14)
parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
args = parser.parse_args()

sys.path.insert(0, str(NIMA))
with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module(
        "check_unbounded_twisted_derham_connection_commutator"
    )

charts = source.charts
old = (charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH)
charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = (
    args.ambient,
    6,
    4,
    2,
)
try:
    columns = charts.presentation(
        source.base.fiber_data, (2, 3, 5), charts.SOURCE_NAMES
    )["columns"]
finally:
    charts.AMBIENT, charts.CUTOFF, charts.K_DEPTH, charts.Q_DEPTH = old

labels = {index: label for label, index in columns.items()}
packet = json.loads(args.input.read_text())
decoded = []
distinct = {}
for probe_index, probe in enumerate(packet["probe_file"]):
    terms = []
    for column, value in probe["remainder"]:
        normal_block, within = divmod(column, len(columns))
        label = labels[within]
        k_pole = label[0]
        q_levels = label[1:-1]
        exponent = label[-1]
        record = {
            "column": column,
            "normal_block": normal_block,
            "base_column": within,
            "value": value,
            "k_pole": k_pole,
            "q_levels": list(q_levels),
            "exponent": list(exponent),
            "total_fiber_degree": sum(exponent),
        }
        terms.append(record)
        distinct[column] = record
    decoded.append(
        {
            "probe_index": probe_index,
            "tangent": "T1" if probe_index < 13 else "T2",
            "source_basis_index": probe_index % 13,
            "remainder_terms": probe["remainder_terms"],
            "terms": terms,
        }
    )

degree_counts = Counter(
    record["total_fiber_degree"] for record in distinct.values()
)
k_pole_counts = Counter(record["k_pole"] for record in distinct.values())
level_counts = Counter(
    tuple(record["q_levels"]) for record in distinct.values()
)
result = {
    "schema": "marici.triangle-wall-cofinal-labelled-residuals.v1",
    "source_result": str(args.input.relative_to(ROOT)).replace("\\", "/")
    if args.input.is_relative_to(ROOT)
    else str(args.input),
    "target_convention": {
        "ambient_degree": args.ambient,
        "cutoff": 6,
        "k_depth": 4,
        "q_depth": 2,
        "normal_point": [2, 3, 5],
        "column_count": len(columns),
    },
    "probe_count": len(decoded),
    "nonzero_probe_count": sum(
        item["remainder_terms"] != 0 for item in decoded
    ),
    "distinct_residual_column_count": len(distinct),
    "distinct_k_pole_counts": dict(sorted(k_pole_counts.items())),
    "distinct_total_degree_counts": dict(sorted(degree_counts.items())),
    "distinct_q_level_counts": {
        ",".join(map(str, key)): value
        for key, value in sorted(level_counts.items())
    },
    "residual_columns": [distinct[index] for index in sorted(distinct)],
    "probes": decoded,
}
args.output.write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {
            "nonzero_probes": result["nonzero_probe_count"],
            "distinct_columns": result["distinct_residual_column_count"],
            "k_poles": result["distinct_k_pole_counts"],
            "degrees": result["distinct_total_degree_counts"],
            "q_levels": result["distinct_q_level_counts"],
        },
        sort_keys=True,
    )
)
