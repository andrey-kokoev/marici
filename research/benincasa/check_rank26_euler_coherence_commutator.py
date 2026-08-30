#!/usr/bin/env python3
"""Test the lift-independent mixed commutator of Euler-coherence defects."""

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
P = base.PRIME


def covariant_defect_derivative(pres, point, defect_axis, derivative_axis):
    result = {}
    for offset, weight in zip(audit.NODES, audit.WEIGHTS):
        shifted = list(point)
        shifted[derivative_axis] += offset
        row = moving.euler_defect(pres, defect_axis, tuple(shifted))
        for column, coefficient in row.items():
            base.add_value(result, column, weight * coefficient)

    central = moving.euler_defect(pres, defect_axis, point)
    connection = words.raw_connection(
        pres, point, central, derivative_axis
    )
    for column, coefficient in connection.items():
        base.add_value(result, column, coefficient)
    return base.reduce_row(result, pres["pivots"])


def subtract(left, right):
    result = dict(left)
    for column, coefficient in right.items():
        base.add_value(result, column, -coefficient)
    return {column: coefficient % P for column, coefficient in result.items() if coefficient % P}


def main():
    points = (words.REFERENCE_POINT,) + words.CONTROL_POINTS
    runs = []
    for point in points:
        pres = words.presentation(point)
        pairs = []
        for first in range(3):
            for second in range(first + 1, 3):
                route_1 = covariant_defect_derivative(
                    pres, point, first, second
                )
                route_2 = covariant_defect_derivative(
                    pres, point, second, first
                )
                commutator = base.reduce_row(
                    subtract(route_1, route_2), pres["pivots"]
                )
                pairs.append({
                    "axes": [first, second],
                    "first_route_support": len(route_1),
                    "second_route_support": len(route_2),
                    "commutator_support": len(commutator),
                    "commutator_vanishes": not commutator,
                })
        runs.append({"point": list(point), "pairs": pairs})

    checks = {
        "three_points_tested": len(runs) == 3,
        "all_nine_mixed_commutators_vanish": all(
            pair["commutator_vanishes"]
            for run in runs
            for pair in run["pairs"]
        ),
    }
    result = {
        "schema": "marici.rank26-euler-coherence-commutator.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "construction": (
            "mixed covariant commutator of the Euler-coherence defect; "
            "no primitive correction lift or occurrence projector"
        ),
        "runs": runs,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-euler-coherence-commutator.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
