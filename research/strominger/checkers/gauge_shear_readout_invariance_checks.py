#!/usr/bin/env python3
"""Exact action of the natural gauge-shear stabilizer on magnetic readouts."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/period_729_layer_localization.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

layers = source["layers"]
multiply = source["multiply"]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]
N = [[1, -1, 1, -1] for _ in range(4)]
P = [[int(i == j) - int(j == 3) for j in range(4)] for i in range(3)]
GRADES = range(-10, 11)
SHEARS = range(-5, 6)


def rectangular_multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


records = []
for n in GRADES:
    packet = layers(n)
    response = packet["response"]
    full = packet["full"]
    for a in SHEARS:
        U = [[I4[i][j] + a * N[i][j] for j in range(4)] for i in range(4)]
        Ui = [[I4[i][j] - a * N[i][j] for j in range(4)] for i in range(4)]
        conjugated = multiply(U, response, Ui)
        left_sheared_full = rectangular_multiply(U, full)
        records.append({
            "grade": n,
            "shear": a,
            "response_fixed_by_conjugation": conjugated == response,
            "quotient_projection_fixed": rectangular_multiply(P, U) == P,
            "relational_readout_fixed_under_left_shear":
                rectangular_multiply(P, left_sheared_full) == packet["relational"],
            "full_readout_fixed_under_left_shear":
                left_sheared_full == full,
        })

gates = {
    "all_derived_responses_are_exactly_conjugation_fixed":
        all(x["response_fixed_by_conjugation"] for x in records),
    "quotient_projection_is_fixed_by_every_gauge_shear":
        all(x["quotient_projection_fixed"] for x in records),
    "relational_readout_is_basic_under_every_sampled_shear":
        all(x["relational_readout_fixed_under_left_shear"] for x in records),
    "full_readout_is_already_horizontal_for_the_gauge_shear":
        all(x["full_readout_fixed_under_left_shear"] for x in records),
}

payload = {
    "schema": "marici.strominger.gauge_shear_readout_invariance_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "grade_range": [GRADES.start, GRADES.stop - 1],
    "shear_range": [SHEARS.start, SHEARS.stop - 1],
    "record_count": len(records),
    "action_typing": {
        "source_automorphism": "Delta maps to U Delta U^-1",
        "quotient_readout": "P Delta with P U = P",
        "rejected_surrogate": "Delta maps to U Delta without transforming the source port",
    },
    "interpretation": (
        "The non-scalar stabilizer is genuine gauge symmetry, not a framing defect. "
        "It fixes every derived response by conjugation and acts trivially after "
        "the relational projection. Stronger still, the selected full readout is "
        "already horizontal: the gauge shear annihilates it before quotienting."
    ),
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
