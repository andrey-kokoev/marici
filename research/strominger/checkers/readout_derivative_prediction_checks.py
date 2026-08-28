#!/usr/bin/env python3
"""Universal readout derivative and preregistered strict-contact predictions."""

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
DERIVATIVE_WINDOW = range(0, 51)
DERIVATIVE_SHIFTS = [9, 27, 81, 243, 729]
PREDICTIONS = [
    {"grade": 251, "shift": 9, "predicted_chi": 2, "predicted_depth_gain": True},
    {"grade": 287, "shift": 27, "predicted_chi": 2, "predicted_depth_gain": True},
    {"grade": 314, "shift": 81, "predicted_chi": 2, "predicted_depth_gain": True},
]


def valuation(x):
    if x == 0:
        return None
    x = abs(x)
    answer = 0
    while x % P == 0:
        answer += 1
        x //= P
    return answer


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


cache = {}


def matrix(n):
    if n not in cache:
        cache[n] = layers(n)["full"]
    return cache[n]


def normalized_response_difference(n, shift):
    a, b = matrix(n), matrix(n + shift)
    r = 0
    q = shift
    while q > 1:
        q //= P
        r += 1
    scale = P**(r + 1)
    return tuple(
        ((y - x) // scale) % P
        for ar, br in zip(a, b)
        for x, y in zip(ar, br)
    )


reference_response = normalized_response_difference(0, DERIVATIVE_SHIFTS[0])
derivative_records = []
for n in DERIVATIVE_WINDOW:
    responses = [
        normalized_response_difference(n, shift)
        for shift in DERIVATIVE_SHIFTS
    ]
    derivative_records.append({
        "grade": n,
        "independent_of_shift": len(set(responses)) == 1,
        "equals_reference": all(x == reference_response for x in responses),
    })


def contact_record(prediction):
    n, shift = prediction["grade"], prediction["shift"]
    m, mp = matrix(n), matrix(n + shift)
    delta = [[y - x for x, y in zip(a, b)] for a, b in zip(m, mp)]
    s = content_depth([x for row in m for x in row])
    u = content_depth([x for row in delta for x in row])
    ell = content_depth(maximal_minors(m))
    right_ell = content_depth(maximal_minors(mp))
    base = [[x // P**s for x in row] for row in m]
    direction = [[x // P**u for x in row] for row in delta]
    section = [(x // P**ell) % P for x in maximal_minors(m)]
    jet = []
    for bm, hm in zip(row_minors(base), row_minors(direction)):
        derivative = sum(
            det(replace_column(bm, j, [hm[i][j] for i in range(3)]))
            for j in range(3)
        )
        jet.append(derivative % P)
    ratios = {
        (b * pow(a, -1, P)) % P
        for a, b in zip(section, jet)
        if a % P
    }
    chi = next(iter(ratios)) if len(ratios) == 1 and all(
        (b - next(iter(ratios)) * a) % P == 0
        for a, b in zip(section, jet)
    ) else "mixed"
    return {
        **prediction,
        "entry_depth": s,
        "perturbation_depth": u,
        "plucker_depth": ell,
        "right_plucker_depth": right_ell,
        "strict_contact": u > s and ell == u + 2 * s,
        "observed_chi": chi,
        "observed_depth_gain": right_ell > ell,
        "prediction_passed":
            chi == prediction["predicted_chi"]
            and (right_ell > ell) == prediction["predicted_depth_gain"],
    }


prediction_records = [contact_record(x) for x in PREDICTIONS]
gates = {
    "normalized_response_is_shift_independent":
        all(x["independent_of_shift"] for x in derivative_records),
    "normalized_response_is_grade_independent":
        all(x["equals_reference"] for x in derivative_records),
    "all_predictions_are_strict_contacts":
        all(x["strict_contact"] for x in prediction_records),
    "all_preregistered_signs_and_gains_are_confirmed":
        all(x["prediction_passed"] for x in prediction_records),
}
payload = {
    "schema": "marici.strominger.readout_derivative_prediction_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "derivative_scope": {
        "grades": [DERIVATIVE_WINDOW.start, DERIVATIVE_WINDOW.stop - 1],
        "shifts": DERIVATIVE_SHIFTS,
    },
    "universal_normalized_response_mod3": list(reference_response),
    "derivative_record_count": len(derivative_records),
    "preregistered_predictions": prediction_records,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
