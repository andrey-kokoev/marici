#!/usr/bin/env python3
"""Exact finite audit for same-preparation charged bridge observation."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "charged_joint_instrument_same_preparation_checks.json"


def rank(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    if not work:
        return 0
    r = 0
    for c in range(len(work[0])):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        p = work[r][c]
        work[r] = [x / p for x in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                q = work[i][c]
                work[i] = [x - q * y for x, y in zip(work[i], work[r])]
        r += 1
    return r


def kernel_dimension(matrix, domain_dim):
    return domain_dim - rank(matrix)

# Same two-sector preparation state x=(E,M).  Rows are applied by one declared
# multi-output instrument, not by re-preparing x.
electric_row = [[1, 0]]
magnetic_row = [[0, 1]]
joint_rows = [[1, 0], [0, 1]]
repeated_electric_rows = [[1, 0], [1, 0]]

# Product-of-preparations hostile: two separate source states (E1,M1,E2,M2)
# with one row applied to each.  The output has two numbers, but its kernel is
# two-dimensional and does not identify one source state.
two_preparation_rows = [[1, 0, 0, 0], [0, 0, 0, 1]]

# Charged bridge channel.  The synthesis bridge b has charge 2 and the retained
# dual analysis line alpha has charge 1.  Their pairing is invariant while b
# alone is not.  The instrument output retains its provenance tags.
MOD = 3
bridge_charge = 2
analysis_line_charge = 1
pair_charge = (bridge_charge + analysis_line_charge) % MOD
scalar_trivialized_bridge_charge = bridge_charge % MOD

# Minimal finite source: x=(E,M,B,A), where B is the charged bridge amplitude
# and A is the dual analysis amplitude.  The invariant charged readout is the
# bilinear product A*B, not a scalarized B.  Linear faithfulness is only for the
# retained E/M sector; bridge detection is multiplicative and provenance typed.
samples = [
    {"x": (1, 0, 0, 1), "joint": (1, 0, 0), "bridge_scalarized": 0},
    {"x": (0, 1, 0, 1), "joint": (0, 1, 0), "bridge_scalarized": 0},
    {"x": (0, 0, 1, 1), "joint": (0, 0, 1), "bridge_scalarized": 1},
    {"x": (0, 0, 1, 0), "joint": (0, 0, 0), "bridge_scalarized": 1},
]
# The last two cases have the same charged bridge coordinate B but differ by
# retained dual analysis availability.  Only the line-paired instrument sees
# the authorized invariant bridge channel.
paired_distinguishes_analysis_availability = samples[2]["joint"] != samples[3]["joint"]
scalarized_fails_analysis_availability = samples[2]["bridge_scalarized"] == samples[3]["bridge_scalarized"]

# Hidden copying hostile: a pair of separate preparations can fake any desired
# pair of scalar outputs without constraining the unobserved coordinates.  The
# same-preparation row matrix has zero kernel; the two-preparation matrix has
# kernel dimension two.
checks = {
    "electric_row_alone_has_kernel": kernel_dimension(electric_row, 2) == 1,
    "magnetic_row_alone_has_kernel": kernel_dimension(magnetic_row, 2) == 1,
    "repeating_one_row_does_not_improve_rank": rank(repeated_electric_rows) == rank(electric_row) == 1,
    "same_preparation_joint_rows_are_faithful": kernel_dimension(joint_rows, 2) == 0,
    "two_preparation_outputs_are_not_same_preparation_faithful": kernel_dimension(two_preparation_rows, 4) == 2,
    "bridge_with_dual_analysis_is_deck_invariant": pair_charge == 0,
    "bare_bridge_scalarization_fails_descent": scalar_trivialized_bridge_charge != 0,
    "line_paired_output_detects_authorized_bridge_channel": paired_distinguishes_analysis_availability,
    "scalarized_bridge_fails_dual_analysis_provenance": scalarized_fails_analysis_availability,
}

payload = {
    "schema": "marici.strominger.charged_joint_instrument_same_preparation.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "ranks": {
        "electric_only": rank(electric_row),
        "repeated_electric": rank(repeated_electric_rows),
        "same_preparation_joint_E_M": rank(joint_rows),
        "two_preparation_hostile": rank(two_preparation_rows),
    },
    "kernel_dimensions": {
        "same_preparation_joint_E_M": kernel_dimension(joint_rows, 2),
        "two_preparation_hostile": kernel_dimension(two_preparation_rows, 4),
    },
    "charged_pairing": {
        "bridge_charge": bridge_charge,
        "dual_analysis_line_charge": analysis_line_charge,
        "pair_charge": pair_charge,
        "bare_bridge_charge": scalar_trivialized_bridge_charge,
    },
    "verdict": (
        "The productive instrument is a single multi-output preparation law. "
        "Repeating one scalar row or using two separately prepared states does "
        "not certify faithfulness. The charged bridge is observable only through "
        "a retained dual-line pairing; scalarizing the bridge loses descent and "
        "dual-analysis provenance."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
