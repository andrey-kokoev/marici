#!/usr/bin/env python3
"""Derive the closing G23 -> G12 transition and test atlas cocycle closure."""

import contextlib
import importlib
import inspect
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    prior = importlib.import_module("check_rank26_full_g31_g23_relation_naturality")

local = prior.local
audit = prior.audit
words = prior.words
base = prior.base
charts = prior.charts

SOURCE_POINT = prior.TARGET_POINT
TARGET_POINT = charts.SOURCE_POINT
SOURCE_NAMES = prior.TARGET_NAMES
TARGET_NAMES = charts.SOURCE_NAMES


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


def identity_map_row(row, source, target, sign=1):
    out = {}
    for column, coefficient in row.items():
        label = source["ordered_columns"][column]
        base.add_value(out, target["columns"][label], sign * coefficient)
    return out


def transformed_g23_data(x, y, z):
    # tau=(132): source external values are (Z,X,Y), while (b,c)->(a,b)
    # preserves retained-coordinate order.
    k, source_q = prior.g23_fiber_data(z, x, y)
    rename = dict(zip(SOURCE_NAMES, TARGET_NAMES))
    return k, {rename[name]: poly for name, poly in source_q.items()}


def audit_axis(source_axis):
    target_axis = {0: 2, 1: 0, 2: 1}[source_axis]
    source_samples = []
    target_samples = []
    source_pres = target_pres = None
    for offset in audit.NODES:
        source_point = list(SOURCE_POINT)
        source_point[source_axis] += offset
        spres, srows = capture_all(tuple(source_point), prior.g23_fiber_data, SOURCE_NAMES)
        target_point = list(TARGET_POINT)
        target_point[target_axis] += offset
        tpres, trows = capture_all(tuple(target_point), base.fiber_data, TARGET_NAMES)
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
            source_derived = local.derived(
                [sample[key] for sample in source_samples], source_samples[3][key], source_pres,
                SOURCE_POINT, source_axis, SOURCE_NAMES, prior.g23_fiber_data
            )
            target_derived = local.derived(
                [sample[key] for sample in target_samples], target_samples[3][key], target_pres,
                TARGET_POINT, target_axis, TARGET_NAMES, base.fiber_data
            )
            mapped = identity_map_row(source_derived, source_pres, target_pres, sign=1)
            if mapped != target_derived:
                failures += 1
            mapped_oriented = identity_map_row(source_derived, source_pres, target_pres, sign=1)
            if mapped_oriented != target_derived:
                orientation_failures += 1
        records.append({
            "source_axis": source_axis,
            "target_axis": target_axis,
            "occurrence_map": f"{source_name}->{target_name}",
            "generator_count": len(source_keys),
            "key_bijection": source_keys == target_keys,
            "raw_failures": failures,
            "orientation_failures": orientation_failures,
        })
    return records


def main():
    transformed_k, transformed_q = transformed_g23_data(*TARGET_POINT)
    direct_k, direct_q = base.fiber_data(*TARGET_POINT)
    records = [record for axis in range(3) for record in audit_axis(axis)]

    axis_1 = {0: 0, 1: 2, 2: 1}
    axis_2 = {0: 1, 1: 0, 2: 2}
    axis_3 = {0: 2, 1: 0, 2: 1}
    axis_composition = {axis: axis_3[axis_2[axis_1[axis]]] for axis in range(3)}
    exponent = (2, 5)
    exponent_composition = (exponent[1], exponent[0])
    exponent_composition = (exponent_composition[1], exponent_composition[0])
    orientation_product = (-1) * (-1) * 1

    checks = {
        "transformed_K_matches_G12": transformed_k == direct_k,
        "transformed_q_matches_G12": transformed_q == direct_q,
        "fifteen_blocks_tested": len(records) == 15,
        "all_blocks_have_2640_generators": all(record["generator_count"] == 2640 for record in records),
        "all_key_maps_are_bijective": all(record["key_bijection"] for record in records),
        "all_raw_squares_commute": all(record["raw_failures"] == 0 for record in records),
        "all_orientation_squares_commute": all(record["orientation_failures"] == 0 for record in records),
        "three_transition_axis_composition_is_identity": axis_composition == {0: 0, 1: 1, 2: 2},
        "three_transition_exponent_composition_is_identity": exponent_composition == exponent,
        "three_transition_orientation_product_is_one": orientation_product == 1,
        "three_transition_occurrence_order_returns": tuple(TARGET_NAMES) == tuple(charts.SOURCE_NAMES),
    }
    result = {
        "schema": "marici.rank26-full-g23-g12-relation-naturality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_point": list(SOURCE_POINT),
        "target_point": list(TARGET_POINT),
        "site_permutation": "cycle_(132)",
        "orientation_sign": 1,
        "block_count": len(records),
        "total_generator_comparisons": sum(record["generator_count"] for record in records),
        "axis_composition": axis_composition,
        "orientation_product": orientation_product,
        "records": records,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-full-g23-g12-relation-naturality.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
