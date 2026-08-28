#!/usr/bin/env python3
"""Scan for a residue-field character on magnetic Pluecker jets."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
import math
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/period_729_layer_localization.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

layers = source["layers"]
det = source["det"]
P = 3
N_MAX = 250
SHIFTS = [3**r for r in range(1, 7)]


def valuation(x):
    if x == 0:
        return None
    x = abs(x)
    v = 0
    while x % P == 0:
        x //= P
        v += 1
    return v


def content_depth(values):
    return valuation(math.gcd(*(abs(x) for x in values)))


def row_minors(a):
    return [
        [[a[i][j] for j in range(3)] for i in rows]
        for rows in itertools.combinations(range(4), 3)
    ]


def maximal_minors(a):
    return [det(x) for x in row_minors(a)]


def replace_column(a, j, values):
    return [
        [values[i] if k == j else a[i][k] for k in range(3)]
        for i in range(3)
    ]


def scalar_ratio(section, jet):
    ratios = {
        (b * pow(a, -1, P)) % P
        for a, b in zip(section, jet)
        if a % P
    }
    if not ratios:
        return None
    chi = next(iter(ratios))
    if len(ratios) != 1:
        return "mixed"
    if any((b - chi * a) % P for a, b in zip(section, jet)):
        return "mixed"
    return chi


cache = {}


def matrix(n):
    if n not in cache:
        cache[n] = layers(n)["full"]
    return cache[n]


summary = []
records = []
for shift in SHIFTS:
    shift_records = []
    for n in range(N_MAX + 1):
        m = matrix(n)
        mp = matrix(n + shift)
        flat_m = [x for row in m for x in row]
        delta = [[y - x for x, y in zip(a, b)] for a, b in zip(m, mp)]
        flat_delta = [x for row in delta for x in row]
        s = content_depth(flat_m)
        u = content_depth(flat_delta)
        ell = content_depth(maximal_minors(m))
        if s is None or u is None or ell is None:
            continue
        jet_depth = u + 2 * s
        if ell != jet_depth:
            continue
        b = [[x // P**s for x in row] for row in m]
        h = [[x // P**u for x in row] for row in delta]
        section = [(x // P**ell) % P for x in maximal_minors(m)]
        jet = []
        for bm, hm in zip(row_minors(b), row_minors(h)):
            derivative = sum(
                det(replace_column(
                    bm, j, [hm[i][j] for i in range(3)]
                ))
                for j in range(3)
            )
            jet.append(derivative % P)
        chi = scalar_ratio(section, jet)
        right_depth = content_depth(maximal_minors(mp))
        record = {
            "grade": n,
            "shift": shift,
            "entry_depth": s,
            "perturbation_depth": u,
            "plucker_depth": ell,
            "section_mod3": section,
            "jet_mod3": jet,
            "chi": chi,
            "right_plucker_depth": right_depth,
            "depth_gain": right_depth is not None and right_depth > ell,
            "strict_first_order": u > s,
        }
        shift_records.append(record)
        records.append(record)
    summary.append({
        "shift": shift,
        "contact_count": len(shift_records),
        "scalar_character_count": sum(
            isinstance(x["chi"], int) for x in shift_records
        ),
        "mixed_count": sum(x["chi"] == "mixed" for x in shift_records),
        "strict_contact_count": sum(x["strict_first_order"] for x in shift_records),
        "cancellation_count": sum(x["depth_gain"] for x in shift_records),
        "strict_cancellation_count": sum(
            x["depth_gain"] and x["strict_first_order"] for x in shift_records
        ),
        "cancellation_grades": [
            x["grade"] for x in shift_records if x["depth_gain"]
        ],
    })

gates = {
    "known_729_contact_is_recovered": any(
        x["grade"] == 152 and x["shift"] == 729 and x["chi"] == 2
        and x["depth_gain"] for x in records
    ),
    "every_strict_depth_gain_has_character_minus_one": all(
        x["chi"] == 2
        for x in records if x["depth_gain"] and x["strict_first_order"]
    ),
    "strict_character_minus_one_iff_depth_gain": all(
        (x["chi"] == 2) == x["depth_gain"]
        for x in records if x["strict_first_order"]
    ),
    "equal_depth_nonlinear_counterexamples_exist": any(
        x["depth_gain"] and not x["strict_first_order"] and x["chi"] != 2
        for x in records
    ),
    "all_shifts_were_scanned": len(summary) == len(SHIFTS),
}
payload = {
    "schema": "marici.strominger.plucker_character_scan.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "scope": {"grades": [0, N_MAX], "shifts": SHIFTS},
    "summary": summary,
    "contact_records": records[:200],
    "contact_record_count": len(records),
    "contact_records_truncated": len(records) > 200,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))