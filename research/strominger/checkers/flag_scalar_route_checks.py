#!/usr/bin/env python3
"""Exact 1+2+1 flag block and scalar route decomposition."""

from __future__ import annotations

import contextlib
from fractions import Fraction
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
S = [
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
]
CONTACTS = [(251, 9), (287, 27), (314, 81)]


def inverse(a):
    n = len(a)
    x = [
        [Fraction(a[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for column in range(n):
        pivot = next(r for r in range(column, n) if x[r][column])
        x[column], x[pivot] = x[pivot], x[column]
        scale = x[column][column]
        x[column] = [v / scale for v in x[column]]
        for r in range(n):
            if r != column and x[r][column]:
                scale = x[r][column]
                x[r] = [v - scale * w for v, w in zip(x[r], x[column])]
    return [[int(v) for v in row[n:]] for row in x]


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
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


def maximal_minor_gcd(b):
    values = [
        det([[b[i][j] for j in range(3)] for i in rows])
        for rows in itertools.combinations(range(4), 3)
    ]
    return math.gcd(*(abs(x) for x in values))


Si = inverse(S)


def scalar_packet(n):
    response = layers(n)["response"]
    delta = [[response[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    adapted = multiply(multiply(Si, delta), S)
    K = [row[1:4] for row in adapted[0:3]]
    alpha = K[0][0:2]
    beta = K[0][2]
    A = [K[1][0:2], K[2][0:2]]
    gamma = [K[1][2], K[2][2]]
    detA = det(A)
    adjA = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
    mixed = sum(alpha[i] * adjA[i][j] * gamma[j] for i in range(2) for j in range(2))
    direct = beta * detA
    scalar = direct - mixed
    full = layers(n)["full"]
    return {
        "grade": n,
        "adapted_zero_first_column": all(adapted[i][0] == 0 for i in range(4)),
        "adapted_zero_last_row": all(adapted[3][j] == 0 for j in range(4)),
        "determinant_scalar": scalar,
        "direct_route": direct,
        "mixed_route": mixed,
        "middle_determinant": detA,
        "maximal_minor_gcd": maximal_minor_gcd(full),
        "scalar_matches_full_fitting_divisor": abs(scalar) == maximal_minor_gcd(full),
    }


window = [scalar_packet(n) for n in range(0, 71)]
contacts = []
for n, shift in CONTACTS:
    left = scalar_packet(n)
    right = scalar_packet(n + shift)
    differences = {
        key: right[key] - left[key]
        for key in ("determinant_scalar", "direct_route", "mixed_route", "middle_determinant")
    }
    route_keys = ("determinant_scalar", "direct_route", "mixed_route", "middle_determinant")
    contacts.append({
        "grade": n,
        "shift": shift,
        "left_v3": {key: valuation(left[key]) for key in route_keys},
        "right_v3": {key: valuation(right[key]) for key in route_keys},
        "difference_v3": {key: valuation(value) for key, value in differences.items()},
        "left_scalar_matches_full_fitting_divisor":
            left["scalar_matches_full_fitting_divisor"],
        "right_scalar_matches_full_fitting_divisor":
            right["scalar_matches_full_fitting_divisor"],
        "total_gain": valuation(right["determinant_scalar"]) > valuation(left["determinant_scalar"]),
    })

gates = {
    "adapted_flag_pattern_holds_on_window":
        all(x["adapted_zero_first_column"] and x["adapted_zero_last_row"] for x in window),
    "scalar_equals_full_third_determinantal_divisor_on_window":
        all(x["scalar_matches_full_fitting_divisor"] for x in window),
    "all_preregistered_contacts_gain_scalar_depth":
        all(x["total_gain"] for x in contacts),
}

payload = {
    "schema": "marici.strominger.flag_scalar_route_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "adapted_basis_columns": ["iota", "e1+e2", "e2+e3", "e1"],
    "window": [0, 50],
    "window_record_count": len(window),
    "contacts": contacts,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
