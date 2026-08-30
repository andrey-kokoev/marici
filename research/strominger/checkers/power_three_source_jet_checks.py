#!/usr/bin/env python3
"""Exact power-of-three source-jet recurrence for the magnetic constructor."""

from __future__ import annotations

import contextlib
import io
import json
import math
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

C, Ci = source["C"], source["Ci"]
fast_power = source["fast_power"]
I = source["I4"]
P = 3
R_MAX = 8


def valuation(x):
    answer = 0
    while x and x % P == 0:
        answer += 1
        x //= P
    return answer


def depth(a):
    return min(valuation(abs(x)) for row in a for x in row if x)


def rank_mod3(a):
    m = [[x % P for x in row] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][col], -1, P)
        m[r] = [(x * inv) % P for x in m[r]]
        for i in range(rows):
            if i != r and m[i][col]:
                q = m[i][col]
                m[i] = [(x - q * y) % P for x, y in zip(m[i], m[r])]
        r += 1
    return r


records = []
reference_jet = None
for r in range(R_MAX + 1):
    shift = P**r
    power = fast_power(C, Ci, shift)
    difference = [[b - a for a, b in zip(x, y)] for x, y in zip(I, power)]
    d = depth(difference)
    jet = [[(x // P**d) % P for x in row] for row in difference]
    if reference_jet is None:
        reference_jet = jet
    records.append({
        "r": r,
        "shift": shift,
        "difference_depth": d,
        "normalized_jet_mod3": jet,
        "rank_mod3": rank_mod3(jet),
        "equals_reference_jet": jet == reference_jet,
    })

gates = {
    "depth_law_holds": all(x["difference_depth"] == x["r"] + 1 for x in records),
    "normalized_jet_is_constant": all(x["equals_reference_jet"] for x in records),
    "universal_source_jet_has_rank_three":
        all(x["rank_mod3"] == 3 for x in records),
    "bridge_line_hypothesis_is_falsified":
        all(x["rank_mod3"] != 1 for x in records),
}
payload = {
    "schema": "marici.strominger.power_three_source_jet_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "range": [0, R_MAX],
    "source_law": "C^(3^r)=I+3^(r+1)J mod 3^(r+2)",
    "reference_jet_mod3": reference_jet,
    "reference_rank_mod3": rank_mod3(reference_jet),
    "records": records,
    "induction_note": (
        "Cubing I+3^(r+1)J preserves J modulo 3 after division by "
        "3^(r+2); all terms with at least two J factors are deeper."
    ),
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
