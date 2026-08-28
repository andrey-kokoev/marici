#!/usr/bin/env python3
"""Locate where the 729-shift first changes magnetic Smith data."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
import math
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

multiply = source["multiply"]
fast_power = source["fast_power"]
anti_commutator = source["anti_commutator"]
C, Ci = source["C"], source["Ci"]
X, Xi = source["X"], source["Xi"]
Z, Zi = source["Z"], source["Zi"]
right_block, right_block_i = source["right_block"], source["right_block_i"]
I4 = source["I4"]


def valuation(value):
    if value == 0:
        return None
    value = abs(value)
    answer = 0
    while value % 3 == 0:
        answer += 1
        value //= 3
    return answer


def content_v3(values):
    g = math.gcd(*(abs(x) for x in values))
    return valuation(g)


def flat(A):
    return [x for row in A for x in row]


def difference_content(A, B):
    return content_v3([b - a for a, b in zip(flat(A), flat(B))])


def det(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def minors(A, size):
    return [
        det([[A[i][j] for j in columns] for i in rows])
        for rows in itertools.combinations(range(len(A)), size)
        for columns in itertools.combinations(range(len(A[0])), size)
    ]


def layers(n):
    U = fast_power(C, Ci, n)
    V = fast_power(Ci, C, n)
    tail = multiply(U, X)
    tail_i = multiply(Xi, V)
    left = anti_commutator(Z, Zi, tail, tail_i)
    left_i = anti_commutator(tail, tail_i, Z, Zi)
    response = anti_commutator(left, left_i, right_block, right_block_i)
    full = [[response[i][j] - int(i == j) for j in range(3)] for i in range(4)]
    relational = [[full[i][j] - full[3][j] for j in range(3)] for i in range(3)]
    return {
        "U": U,
        "V": V,
        "tail": tail,
        "tail_inverse": tail_i,
        "left_commutator": left,
        "left_inverse": left_i,
        "response": response,
        "full": full,
        "relational": relational,
    }


left_grade, period = 152, 729
right_grade = left_grade + period
L, R = layers(left_grade), layers(right_grade)
period_increment = fast_power(C, Ci, period)
increment_v3 = difference_content(I4, period_increment)

layer_differences = {
    name: difference_content(L[name], R[name])
    for name in L
}
minor_records = {}
for name in ("full", "relational"):
    maximum = min(len(L[name]), len(L[name][0]))
    minor_records[name] = {}
    for size in range(1, maximum + 1):
        lm, rm = minors(L[name], size), minors(R[name], size)
        minor_records[name][str(size)] = {
            "left_gcd_v3": content_v3(lm),
            "right_gcd_v3": content_v3(rm),
            "minor_vector_difference_v3": content_v3(
                [b - a for a, b in zip(lm, rm)]
            ),
        }

full_left_maximal = minors(L["full"], 3)
full_right_maximal = minors(R["full"], 3)
leading_scale = min(
    minor_records["full"]["3"]["left_gcd_v3"],
    minor_records["full"]["3"]["right_gcd_v3"],
)
leading_maximal_minor_mod3 = {
    "scale_v3": leading_scale,
    "left": [(x // (3 ** leading_scale)) % 3 for x in full_left_maximal],
    "right": [(x // (3 ** leading_scale)) % 3 for x in full_right_maximal],
    "difference": [
        ((b - a) // (3 ** leading_scale)) % 3
        for a, b in zip(full_left_maximal, full_right_maximal)
    ],
}

gates = {
    "period_increment_is_identity_mod_high_power": increment_v3 >= 7,
    "every_pre_smith_layer_is_congruent_mod_same_power":
        all(v >= increment_v3 for v in layer_differences.values()),
    "d1_and_d2_valuations_are_preserved":
        minor_records["full"]["1"]["left_gcd_v3"]
        == minor_records["full"]["1"]["right_gcd_v3"]
        and minor_records["relational"]["2"]["left_gcd_v3"]
        == minor_records["relational"]["2"]["right_gcd_v3"],
    "d3_valuation_changes":
        minor_records["full"]["3"]["left_gcd_v3"]
        != minor_records["full"]["3"]["right_gcd_v3"],
}
payload = {
    "schema": "marici.strominger.period_729_layer_localization.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "grades": [left_grade, right_grade],
    "translation": period,
    "period_increment_identity_difference_v3": increment_v3,
    "layer_difference_v3": layer_differences,
    "minor_records": minor_records,
    "leading_maximal_minor_mod3": leading_maximal_minor_mod3,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The 729-shift is invisible through high 3-adic precision at every "
        "linear and nested-commutator layer. The split is created only when "
        "gcd valuations of already highly divisible maximal minors are read."
    ),
}
print(json.dumps(payload, indent=2))
