#!/usr/bin/env python3
"""Bulk naturality audit for all marked-pole families and all base axes."""

import contextlib
import importlib
import inspect
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    local = importlib.import_module("check_rank26_moving_relation_chart_naturality")

audit = local.audit
words = local.words
base = local.base
charts = local.charts


def capture_all(point, fiber, names):
    captured = {}
    original = base.add_pivot

    def capture(row, _pivots):
        frame = inspect.currentframe().f_back
        if frame.f_lineno == 130 and row:
            captured[local.relation_key(frame)] = dict(row)

    base.add_pivot = capture
    try:
        pres = charts.presentation(fiber, point, names)
    finally:
        base.add_pivot = original
    return pres, captured


def audit_axis(source_axis):
    target_axis = {0: 0, 1: 2, 2: 1}[source_axis]
    source_samples = []
    target_samples = []
    source_pres = target_pres = None
    for offset in audit.NODES:
        source_point = list(charts.SOURCE_POINT)
        source_point[source_axis] += offset
        spres, srows = capture_all(tuple(source_point), base.fiber_data, charts.SOURCE_NAMES)
        target_point = list(charts.TARGET_POINT)
        target_point[target_axis] += offset
        tpres, trows = capture_all(tuple(target_point), charts.g31_fiber_data, charts.TARGET_NAMES)
        source_samples.append(srows)
        target_samples.append(trows)
        if offset == 0:
            source_pres, target_pres = spres, tpres

    records = []
    for qi, (source_name, target_name) in enumerate(zip(charts.SOURCE_NAMES, charts.TARGET_NAMES)):
        source_keys = {key for key in source_samples[3] if key[0] == qi}
        target_keys = {key for key in target_samples[3] if key[0] == qi}
        failures = 0
        orientation_failures = 0
        for key in source_keys:
            target_key = local.mapped_key(key)
            source_derived = local.derived(
                [sample[key] for sample in source_samples], source_samples[3][key], source_pres,
                charts.SOURCE_POINT, source_axis, charts.SOURCE_NAMES, base.fiber_data
            )
            target_derived = local.derived(
                [sample[target_key] for sample in target_samples], target_samples[3][target_key], target_pres,
                charts.TARGET_POINT, target_axis, charts.TARGET_NAMES, charts.g31_fiber_data
            )
            mapped = charts.map_row(source_derived, source_pres, target_pres, sign=1)
            if mapped != target_derived:
                failures += 1
            mapped_oriented = charts.map_row(source_derived, source_pres, target_pres, sign=-1)
            expected_oriented = {column: -coefficient % base.PRIME for column, coefficient in target_derived.items()}
            if mapped_oriented != expected_oriented:
                orientation_failures += 1
        records.append(
            {
                "source_axis": source_axis,
                "target_axis": target_axis,
                "occurrence_map": f"{source_name}->{target_name}",
                "source_generator_count": len(source_keys),
                "target_generator_count": len(target_keys),
                "key_bijection": {local.mapped_key(key) for key in source_keys} == target_keys,
                "raw_failures": failures,
                "orientation_failures": orientation_failures,
            }
        )
    return records


def main():
    records = [record for axis in range(3) for record in audit_axis(axis)]
    checks = {
        "fifteen_occurrence_direction_blocks_tested": len(records) == 15,
        "all_blocks_have_2640_generators": all(
            record["source_generator_count"] == record["target_generator_count"] == 2640 for record in records
        ),
        "all_key_maps_are_bijective": all(record["key_bijection"] for record in records),
        "all_raw_squares_commute": all(record["raw_failures"] == 0 for record in records),
        "all_orientation_squares_commute": all(record["orientation_failures"] == 0 for record in records),
    }
    result = {
        "schema": "marici.rank26-full-g12-g31-relation-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "block_count": len(records),
        "total_generator_comparisons": sum(record["source_generator_count"] for record in records),
        "records": records,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-full-g12-g31-relation-naturality.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
