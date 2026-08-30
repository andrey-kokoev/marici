#!/usr/bin/env python3
"""Derive and audit the complete G31 -> G23 moving-relation transition."""

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

SOURCE_POINT = charts.TARGET_POINT
TARGET_POINT = (SOURCE_POINT[1], SOURCE_POINT[0], SOURCE_POINT[2])
SOURCE_NAMES = charts.TARGET_NAMES
TARGET_NAMES = ("g2", "g3", "g1", "g31", "g12")


def clean(poly):
    return {exponent: coefficient % base.PRIME for exponent, coefficient in poly.items() if coefficient % base.PRIME}


def g23_fiber_data(x, y, z):
    # Independent cyclic derivation from G12: old labels i map to sigma(i),
    # so old external values are (Y,Z,X) at target coordinates (X,Y,Z).
    k, old_q = base.fiber_data(y, z, x)
    rename = {"g1": "g2", "g2": "g3", "g3": "g1", "g23": "g31", "g31": "g12"}
    return k, {rename[name]: clean(poly) for name, poly in old_q.items()}


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


def transformed_g31_data(x, y, z):
    # sigma_12 sends G31 to G23 and (c,a) to (c,b); reorder target as (b,c).
    k, source_q = charts.g31_fiber_data(y, x, z)
    rename = {"g1": "g2", "g3": "g3", "g2": "g1", "g23": "g31", "g12": "g12"}
    return charts.swap_exponents(k), {
        rename[name]: charts.swap_exponents(poly) for name, poly in source_q.items()
    }


def audit_axis(source_axis):
    target_axis = {0: 1, 1: 0, 2: 2}[source_axis]
    source_samples = []
    target_samples = []
    source_pres = target_pres = None
    for offset in audit.NODES:
        source_point = list(SOURCE_POINT)
        source_point[source_axis] += offset
        spres, srows = capture_all(tuple(source_point), charts.g31_fiber_data, SOURCE_NAMES)
        target_point = list(TARGET_POINT)
        target_point[target_axis] += offset
        tpres, trows = capture_all(tuple(target_point), g23_fiber_data, TARGET_NAMES)
        source_samples.append(srows)
        target_samples.append(trows)
        if offset == 0:
            source_pres, target_pres = spres, tpres

    records = []
    for qi, (source_name, target_name) in enumerate(zip(SOURCE_NAMES, TARGET_NAMES)):
        source_keys = {key for key in source_samples[3] if key[0] == qi}
        target_keys = {key for key in target_samples[3] if key[0] == qi}
        failures = orientation_failures = 0
        for key in source_keys:
            target_key = local.mapped_key(key)
            source_derived = local.derived(
                [sample[key] for sample in source_samples], source_samples[3][key], source_pres,
                SOURCE_POINT, source_axis, SOURCE_NAMES, charts.g31_fiber_data
            )
            target_derived = local.derived(
                [sample[target_key] for sample in target_samples], target_samples[3][target_key], target_pres,
                TARGET_POINT, target_axis, TARGET_NAMES, g23_fiber_data
            )
            mapped = charts.map_row(source_derived, source_pres, target_pres, sign=1)
            if mapped != target_derived:
                failures += 1
            mapped_oriented = charts.map_row(source_derived, source_pres, target_pres, sign=-1)
            expected_oriented = {column: -coefficient % base.PRIME for column, coefficient in target_derived.items()}
            if mapped_oriented != expected_oriented:
                orientation_failures += 1
        records.append({
            "source_axis": source_axis,
            "target_axis": target_axis,
            "occurrence_map": f"{source_name}->{target_name}",
            "generator_count": len(source_keys),
            "key_bijection": {local.mapped_key(key) for key in source_keys} == target_keys,
            "raw_failures": failures,
            "orientation_failures": orientation_failures,
        })
    return records


def main():
    direct_k, direct_q = g23_fiber_data(*TARGET_POINT)
    transformed_k, transformed_q = transformed_g31_data(*TARGET_POINT)
    source_formula_checks = {
        "independent_K_formulas_agree": direct_k == transformed_k,
        "independent_q_formulas_agree": direct_q == transformed_q,
    }
    records = [record for axis in range(3) for record in audit_axis(axis)]
    checks = {
        **source_formula_checks,
        "fifteen_blocks_tested": len(records) == 15,
        "all_blocks_have_2640_generators": all(record["generator_count"] == 2640 for record in records),
        "all_key_maps_are_bijective": all(record["key_bijection"] for record in records),
        "all_raw_squares_commute": all(record["raw_failures"] == 0 for record in records),
        "all_orientation_squares_commute": all(record["orientation_failures"] == 0 for record in records),
    }
    result = {
        "schema": "marici.rank26-full-g31-g23-relation-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_point": list(SOURCE_POINT),
        "target_point": list(TARGET_POINT),
        "site_permutation": "sigma_12",
        "orientation_sign": -1,
        "block_count": len(records),
        "total_generator_comparisons": sum(record["generator_count"] for record in records),
        "records": records,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-full-g31-g23-relation-naturality.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
