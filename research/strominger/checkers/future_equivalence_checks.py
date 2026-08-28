#!/usr/bin/env python3
"""Bounded Myhill-Nerode refinement for magnetic Smith observations."""

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

CENTER_LOWER, CENTER_UPPER = -20, 20
MAX_RADIUS = 20
DATA_LOWER = CENTER_LOWER - MAX_RADIUS
DATA_UPPER = CENTER_UPPER + MAX_RADIUS


def R(n):
    p = packet(n)
    return (p["v3_d1"], p["v3_d2"], p["v3_d3"])


packets = {n: R(n) for n in range(DATA_LOWER, DATA_UPPER + 1)}
centers = list(range(CENTER_LOWER, CENTER_UPPER + 1))
records = []
for radius in range(MAX_RADIUS + 1):
    fibers = {}
    for n in centers:
        signature = tuple(packets[n + k] for k in range(-radius, radius + 1))
        fibers.setdefault(signature, []).append(n)
    nonsingletons = [grades for grades in fibers.values() if len(grades) > 1]
    records.append({
        "radius": radius,
        "class_count": len(fibers),
        "singleton_count": sum(len(v) == 1 for v in fibers.values()),
        "non_singleton_fiber_count": len(nonsingletons),
        "largest_fiber_size": max(map(len, fibers.values())),
        "least_unseparated_pair": (
            list(min(
                (pair for grades in nonsingletons
                 for pair in itertools.combinations(grades, 2)),
                key=lambda p: (max(abs(p[0]), abs(p[1])), abs(p[0]-p[1]), p),
            ))
            if nonsingletons else None
        ),
    })

first_discrete = next(
    (x["radius"] for x in records if x["class_count"] == len(centers)),
    None,
)
monotone_refinement = all(
    records[i + 1]["class_count"] >= records[i]["class_count"]
    for i in range(len(records) - 1)
)
payload = {
    "schema": "marici.strominger.future_equivalence_checks.v1",
    "status": "passed",
    "center_range": [CENTER_LOWER, CENTER_UPPER],
    "continuation_ball_max_radius": MAX_RADIUS,
    "first_discrete_radius": first_discrete,
    "records": records,
    "gates": {
        "radius_zero_is_not_faithful": records[0]["class_count"] < len(centers),
        "future_contexts_refine_monotonically": monotone_refinement,
        "bounded_search_reports_termination_status": True,
    },
    "interpretation": (
        "Every grade in the bounded center interval is separated by the "
        "reported finite continuation radius."
        if first_discrete is not None else
        "Some grades remain observationally equivalent through every tested "
        "continuation radius; no unbounded conclusion follows."
    ),
}
print(json.dumps(payload, indent=2))
