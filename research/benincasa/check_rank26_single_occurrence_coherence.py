#!/usr/bin/env python3
"""Test whether one labelled marked-pole family already absorbs each defect."""

import contextlib
import importlib
import inspect
import io
import json
import os
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

audit = moving.audit
words = moving.words
base = moving.base
charts = moving.charts


def capture_q_relations(point, selected_qi):
    rows = []
    original = base.add_pivot

    def capture(row, _pivots):
        frame = inspect.currentframe().f_back
        if frame.f_lineno == 130 and frame.f_locals.get("qi") == selected_qi and row:
            rows.append(dict(row))

    base.add_pivot = capture
    try:
        charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)
    finally:
        base.add_pivot = original
    return rows


def test_axis(pres, axis, selected_qi):
    samples = []
    for offset in audit.NODES:
        shifted = list(words.REFERENCE_POINT)
        shifted[axis] += offset
        samples.append(capture_q_relations(tuple(shifted), selected_qi))
    counts = {len(sample) for sample in samples}
    assert len(counts) == 1
    count = counts.pop()
    defect = moving.euler_defect(pres, axis)
    span = {}
    processed = 0
    for index in range(count):
        processed += 1
        derived = moving.derived_relation(
            [sample[index] for sample in samples], samples[3][index], pres, axis
        )
        if derived:
            base.add_pivot(dict(derived), span)
        residual = base.reduce_row(defect, span)
        if not residual:
            break
    return {
        "axis": axis,
        "occurrence": charts.SOURCE_NAMES[selected_qi],
        "generator_count": count,
        "processed_count": processed,
        "derived_span_rank": len(span),
        "defect_support": len(defect),
        "residual_support": len(base.reduce_row(defect, span)),
        "contains_defect": not base.reduce_row(defect, span),
    }


def main():
    pres = words.presentation(words.REFERENCE_POINT)
    # Entry 2728 reached containment before leaving the first q-family in the
    # frozen source ordering, so test that declared occurrence independently.
    selected_qi = int(os.environ.get("MARICI_SELECTED_QI", "0"))
    runs = [test_axis(pres, axis, selected_qi) for axis in range(3)]
    checks = {
        "selected_occurrence_is_declared": 0 <= selected_qi < len(charts.SOURCE_NAMES),
        "all_three_directions_tested": len(runs) == 3,
        "single_occurrence_contains_all_three_defects": all(run["contains_defect"] for run in runs),
    }
    result = {
        "schema": "marici.rank26-single-occurrence-coherence.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(words.REFERENCE_POINT),
        "runs": runs,
        "checks": checks,
        "interpretation": (
            "Containment by one occurrence family is an algebraic existence result. It is canonical only if cyclic transport "
            "selects the corresponding occurrence in the other residue charts."
        ),
    }
    occurrence = charts.SOURCE_NAMES[selected_qi]
    output = Path(__file__).with_name(f"rank26-single-occurrence-coherence-{occurrence}.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
