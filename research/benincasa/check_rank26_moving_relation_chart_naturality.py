#!/usr/bin/env python3
"""Test chart naturality of a complete labelled moving-pole relation family."""

import contextlib
import importlib
import inspect
import io
import json
import os
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank26_differentiated_euler_quotient")

words = audit.words
base = words.base
charts = words.charts


def relation_key(frame):
    return (
        frame.f_locals["qi"],
        frame.f_locals["k_pole"],
        tuple(frame.f_locals["levels"]),
        tuple(frame.f_locals["exponent"]),
    )


def capture_presentation(fiber, point, names, selected_qi=0):
    captured = {}
    original = base.add_pivot

    def capture(row, _pivots):
        frame = inspect.currentframe().f_back
        if frame.f_lineno == 130 and frame.f_locals.get("qi") == selected_qi and row:
            captured[relation_key(frame)] = dict(row)

    base.add_pivot = capture
    try:
        pres = charts.presentation(fiber, point, names)
    finally:
        base.add_pivot = original
    return pres, captured


def generic_connection(row, pres, point, axis, names, fiber):
    result = {}
    for column, coefficient in row.items():
        label = pres["ordered_columns"][column]
        image = words.audit.connection_image(label, names, axis, pres["columns"], fiber, point)
        for destination, value in image.items():
            base.add_value(result, destination, coefficient * value)
    return result


def derived(samples, central, pres, point, axis, names, fiber):
    result = {}
    for sample, weight in zip(samples, audit.WEIGHTS):
        for column, coefficient in sample.items():
            base.add_value(result, column, weight * coefficient)
    connection = generic_connection(central, pres, point, axis, names, fiber)
    for column, coefficient in connection.items():
        base.add_value(result, column, coefficient)
    return result


def mapped_key(key):
    qi, k_pole, levels, exponent = key
    return qi, k_pole, levels, (exponent[1], exponent[0])


def main():
    selected_qi = int(os.environ.get("MARICI_SELECTED_QI", "0"))
    source_axis = int(os.environ.get("MARICI_SOURCE_AXIS", "0"))
    target_axis = {0: 0, 1: 2, 2: 1}[source_axis]
    source_samples = []
    target_samples = []
    source_pres = target_pres = None
    for offset in audit.NODES:
        source_point = list(charts.SOURCE_POINT)
        source_point[source_axis] += offset
        source_pres_i, source_rows = capture_presentation(
            base.fiber_data, tuple(source_point), charts.SOURCE_NAMES, selected_qi
        )
        target_point = list(charts.TARGET_POINT)
        target_point[target_axis] += offset
        target_pres_i, target_rows = capture_presentation(
            charts.g31_fiber_data, tuple(target_point), charts.TARGET_NAMES, selected_qi
        )
        source_samples.append(source_rows)
        target_samples.append(target_rows)
        if offset == 0:
            source_pres, target_pres = source_pres_i, target_pres_i

    source_keys = set(source_samples[3])
    target_keys = set(target_samples[3])
    key_bijection = {mapped_key(key) for key in source_keys} == target_keys
    failures = 0
    orientation_failures = 0
    for key in source_keys:
        target_key = mapped_key(key)
        source_derived = derived(
            [sample[key] for sample in source_samples], source_samples[3][key], source_pres,
            charts.SOURCE_POINT, source_axis, charts.SOURCE_NAMES, base.fiber_data
        )
        target_derived = derived(
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

    checks = {
        "complete_occurrence_family_captured": len(source_keys) == 2640,
        "generator_keys_transport_bijectively": key_bijection,
        "raw_derived_relation_map_is_natural": failures == 0,
        "poincare_orientation_is_compatible": orientation_failures == 0,
    }
    result = {
        "schema": "marici.rank26-moving-relation-chart-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_chart": "G12",
        "target_chart": "G31",
        "site_permutation": "sigma_23",
        "occurrence_map": f"{charts.SOURCE_NAMES[selected_qi]}->{charts.TARGET_NAMES[selected_qi]}",
        "source_axis": source_axis,
        "target_axis": target_axis,
        "generator_count": len(source_keys),
        "raw_naturality_failures": failures,
        "orientation_failures": orientation_failures,
        "checks": checks,
    }
    occurrence = charts.SOURCE_NAMES[selected_qi]
    output = Path(__file__).with_name(
        f"rank26-moving-relation-chart-naturality-{occurrence}-axis-{source_axis}.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
