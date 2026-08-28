#!/usr/bin/env python3
"""Test finite constructor-germ depths for SCC congruence."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))
packet = source["packet"]

DATA_LOWER, DATA_UPPER = -50, 50
CENTER_LOWER, CENTER_UPPER = -35, 35
MAX_RADIUS = 8


def valuation_packet(n):
    record = packet(n)
    return (record["v3_d1"], record["v3_d2"], record["v3_d3"])


packets = {n: valuation_packet(n) for n in range(DATA_LOWER, DATA_UPPER + 1)}


def germ(n, radius):
    return tuple(packets[j] for j in range(n - radius, n + radius + 1))


radius_records = []
for radius in range(MAX_RADIUS + 1):
    centers = range(CENTER_LOWER, CENTER_UPPER + 1)
    fibers = {}
    for n in centers:
        fibers.setdefault(germ(n, radius), []).append(n)

    witnesses = []
    for sig, grades in fibers.items():
        if len(grades) < 2:
            continue
        for left, right in itertools.combinations(grades, 2):
            directions = []
            if germ(left + 1, radius) != germ(right + 1, radius):
                directions.append("+1")
            if germ(left - 1, radius) != germ(right - 1, radius):
                directions.append("-1")
            if directions:
                witnesses.append({
                    "left": left,
                    "right": right,
                    "directions_that_split": directions,
                })
    witnesses.sort(key=lambda w: (
        max(abs(w["left"]), abs(w["right"])),
        abs(w["left"] - w["right"]),
        w["left"],
        w["right"],
    ))
    radius_records.append({
        "radius": radius,
        "width": 2 * radius + 1,
        "distinct_germ_count": len(fibers),
        "repeated_fiber_count": sum(len(v) > 1 for v in fibers.values()),
        "split_fiber_count": sum(
            1
            for sig, grades in fibers.items()
            if len(grades) > 1 and any(
                germ(left + direction, radius) != germ(right + direction, radius)
                for left, right in itertools.combinations(grades, 2)
                for direction in (-1, 1)
            )
        ),
        "smallest_split_witness": witnesses[0] if witnesses else None,
        "bounded_congruence_gate_passes": not witnesses,
    })

first_passing = next(
    (record["radius"] for record in radius_records
     if record["bounded_congruence_gate_passes"]),
    None,
)
payload = {
    "schema": "marici.strominger.constructor_germ_depth_checks.v1",
    "status": "passed",
    "data_range": [DATA_LOWER, DATA_UPPER],
    "center_range": [CENTER_LOWER, CENTER_UPPER],
    "max_radius": MAX_RADIUS,
    "first_bounded_congruence_radius": first_passing,
    "radius_records": radius_records,
    "interpretation": (
        "A finite constructor germ closes the bounded SCC gate at the reported "
        "radius; this is bounded evidence, not an unbounded termination theorem."
        if first_passing is not None
        else
        "Every tested finite germ radius has a split fiber, supporting a "
        "pro-germ interpretation."
    ),
}
print(json.dumps(payload, indent=2))
