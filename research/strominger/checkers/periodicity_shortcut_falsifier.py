#!/usr/bin/env python3
"""Falsify the unbounded-valuation shortcut and test bounded translation periods."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))
packet = source["packet"]

UPPER = 728
PERIOD_MAX = 100


def R(n):
    p = packet(n)
    return (p["v3_d1"], p["v3_d2"], p["v3_d3"])


records = [packet(n) for n in range(UPPER + 1)]
snake = [r["v3_snake_index"] for r in records]
record_breakers = []
best = -1
for r in records:
    if r["v3_snake_index"] > best:
        best = r["v3_snake_index"]
        record_breakers.append([r["exponent"], best])

lift_candidates = [152, 395, 638]
lift_packets = [records[n] for n in lift_candidates]
period_witnesses = {}
for period in range(1, PERIOD_MAX + 1):
    witness = next(
        (n for n in range(UPPER + 1 - period) if R(n) != R(n + period)),
        None,
    )
    period_witnesses[str(period)] = witness

gates = {
    "record_breaker_branch_is_reproduced":
        record_breakers == [[0, 0], [8, 1], [17, 2], [71, 3], [152, 5]],
    "all_mod_729_lifts_are_checked":
        [r["exponent"] for r in lift_packets] == lift_candidates,
    "apparent_hensel_branch_has_no_valuation_six_lift":
        max(r["v3_snake_index"] for r in lift_packets) == 5,
    "no_larger_snake_valuation_occurs_below_729":
        max(snake) == 5,
    "every_candidate_period_through_100_has_a_witness":
        all(v is not None for v in period_witnesses.values()),
}
payload = {
    "schema": "marici.strominger.periodicity_shortcut_falsifier.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "range": [0, UPPER],
    "candidate_period_range": [1, PERIOD_MAX],
    "record_breakers": record_breakers,
    "lift_packets": [
        {
            "exponent": r["exponent"],
            "v3_d3": r["v3_d3"],
            "v3_snake_index": r["v3_snake_index"],
        }
        for r in lift_packets
    ],
    "maximum_snake_valuation": max(snake),
    "period_witnesses": period_witnesses,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The apparent terminal-valuation Hensel branch terminates before "
        "valuation six. Unboundedness is not established. Every translation "
        "period 1..100 is nevertheless falsified on the bounded window."
    ),
}
print(json.dumps(payload, indent=2))
