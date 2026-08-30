#!/usr/bin/env python3
"""Reduce mixed Euler-coherence commutators by the frozen moving relation map."""

import contextlib
import importlib
import io
import json
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    comm = importlib.import_module("check_rank26_euler_coherence_commutator")

moving = comm.moving
audit = comm.audit
words = comm.words
base = comm.base


def commutators(pres, point):
    rows = []
    for first in range(3):
        for second in range(first + 1, 3):
            route_1 = comm.covariant_defect_derivative(
                pres, point, first, second
            )
            route_2 = comm.covariant_defect_derivative(
                pres, point, second, first
            )
            rows.append({
                "axes": [first, second],
                "row": base.reduce_row(comm.subtract(route_1, route_2), pres["pivots"]),
            })
    return rows


def moving_span_until_containment(pres, point, targets):
    span = {}
    axis_records = []
    for axis in range(3):
        processed = 0
        nonzero = 0
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
            if all(not base.reduce_row(target["row"], span) for target in targets):
                break
        axis_records.append({
            "axis": axis,
            "complete_generator_count": complete_count,
            "processed_prefix_witness_count": processed,
            "nonzero_rows": nonzero,
            "cumulative_span_rank": len(span),
        })
        if all(not base.reduce_row(target["row"], span) for target in targets):
            break
    return span, axis_records


def main():
    points = (words.REFERENCE_POINT,) + words.CONTROL_POINTS
    runs = []
    for point in points:
        pres = words.presentation(point)
        targets = commutators(pres, point)
        span, axis_records = moving_span_until_containment(pres, point, targets)
        reduced = []
        for target in targets:
            residual = base.reduce_row(target["row"], span)
            reduced.append({
                "axes": target["axes"],
                "initial_support": len(target["row"]),
                "residual_support": len(residual),
                "absorbed": not residual,
            })
        runs.append({
            "point": list(point),
            "axis_witnesses": axis_records,
            "commutators": reduced,
        })

    checks = {
        "three_points_tested": len(runs) == 3,
        "all_nine_commutators_absorbed": all(
            record["absorbed"]
            for run in runs
            for record in run["commutators"]
        ),
    }
    result = {
        "schema": "marici.rank26-euler-commutator-relation-reduction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "reduction_object": (
            "direct sum of all three derivatives of the complete labelled "
            "q-multiplication relation map"
        ),
        "selection_rule": (
            "processed prefixes are finite containment witnesses only; the "
            "adapter retains the complete labelled map in every direction"
        ),
        "runs": runs,
        "checks": checks,
    }
    output = Path(__file__).with_name(
        "rank26-euler-commutator-relation-reduction.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
