"""Verify the labelled occurrence chain map on triangle-wall Rees samples."""

from __future__ import annotations

import contextlib
import importlib
import io
import json
from collections import Counter
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = audit.base, audit.charts
P = base.PRIME
AMBIENT = 10
NODES = tuple(range(-3, 4))


def capture(fiber, point, names):
    rows = []
    original = base.add_pivot

    def hook(row, pivots):
        rows.append(dict(row))
        original(row, pivots)

    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = AMBIENT, 6
    base.add_pivot = hook
    try:
        presentation = charts.presentation(fiber, point, names)
    finally:
        base.add_pivot = original
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    return presentation, rows


def normalized(row):
    if not row:
        return ()
    pivot = max(row)
    inverse = pow(row[pivot], P - 2, P)
    return tuple(sorted((column, value * inverse % P) for column, value in row.items()))


checks = []
for offset in NODES:
    source, source_rows = capture(
        base.fiber_data, (2, 3, 5 + offset), charts.SOURCE_NAMES
    )
    target, target_rows = capture(
        charts.g31_fiber_data, (2, 5 + offset, 3), charts.TARGET_NAMES
    )
    mapped = []
    for row in source_rows:
        transported = {}
        for column, coefficient in row.items():
            label = source["ordered_columns"][column]
            target_column = target["columns"][charts.map_label(label)]
            base.add_value(transported, target_column, coefficient)
        mapped.append(normalized(transported))
    source_counter = Counter(mapped)
    target_counter = Counter(normalized(row) for row in target_rows)
    checks.append(
        {
            "normal_offset": offset,
            "source_row_count": len(source_rows),
            "target_row_count": len(target_rows),
            "mapped_only": sum((source_counter - target_counter).values()),
            "target_only": sum((target_counter - source_counter).values()),
            "passed": source_counter == target_counter,
        }
    )

result = {
    "schema": "marici.triangle-wall-rees-occurrence-chain-map.v1",
    "field": P,
    "ambient_relation_degree": AMBIENT,
    "normal_nodes": list(NODES),
    "source_chart": "G12 with (X1,X2,X3)=(2,3,5+Lambda)",
    "target_chart": "G31 with (X1,X2,X3)=(2,5+Lambda,3)",
    "column_map": "label map with fiber-exponent swap",
    "row_comparison": "projectively normalized raw relation-row multisets",
    "checks": checks,
    "all_passed": all(check["passed"] for check in checks),
}

output = Path(__file__).with_name("triangle-wall-rees-occurrence-chain-map.json")
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
