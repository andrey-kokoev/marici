#!/usr/bin/env python3
"""Test Euler closure after adjoining the complete moving q-relation image."""

import contextlib
import importlib
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

audit = moving.audit
words = moving.words
base = moving.base


def run_direction(point, pres, axis):
    defect = moving.euler_defect(pres, axis, point)
    span = {}
    nonzero = 0
    processed = 0
    complete_count = (
        len(words.charts.SOURCE_NAMES)
        * (words.charts.K_DEPTH + 1)
        * (2 ** (len(words.charts.SOURCE_NAMES) - 1))
        * len(base.monomials_at_most(words.AMBIENT - 1))
    )
    for derived in moving.iter_derived_q_relations(pres, point, axis):
        processed += 1
        if derived:
            nonzero += 1
            base.add_pivot(dict(derived), span)
        residual = base.reduce_row(defect, span)
        if not residual:
            break

    residual = base.reduce_row(defect, span)
    return {
        "axis": axis,
        "complete_relation_generator_count": complete_count,
        "processed_prefix_witness_count": processed,
        "nonzero_derived_rows_in_witness": nonzero,
        "witness_span_rank": len(span),
        "defect_support": len(defect),
        "residual_support": len(residual),
        "status": "pass" if not residual else "fail",
    }


def main():
    points = (words.REFERENCE_POINT,) + words.CONTROL_POINTS
    runs = []
    for point in points:
        pres = words.presentation(point)
        directions = [run_direction(point, pres, axis) for axis in range(3)]
        runs.append({"point": list(point), "directions": directions})

    checks = {
        "three_frozen_points_tested": len(runs) == 3,
        "all_nine_differentiated_euler_defects_absorbed": all(
            direction["status"] == "pass"
            for run in runs
            for direction in run["directions"]
        ),
    }
    result = {
        "schema": "marici.rank26-corrected-adapter-euler.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "adapter": (
            "finite quotient transport totalized with the derivative image of "
            "the complete labelled q-multiplication relation map"
        ),
        "selection_rule": (
            "the complete labelled relation map is canonical; each processed "
            "prefix is reported only as a finite containment witness"
        ),
        "runs": runs,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-corrected-adapter-euler.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
