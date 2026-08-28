#!/usr/bin/env python3
"""Exact spectral-extension structure of the magnetic constructor."""

from __future__ import annotations

import contextlib
import io
import json
import math
from fractions import Fraction
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

C = source["C"]
multiply = source["multiply"]
DIM = 4
I = [[int(i == j) for j in range(DIM)] for i in range(DIM)]
T = 147458


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(DIM)] for i in range(DIM)]


def scale(k, a):
    return [[k * x for x in row] for row in a]


def zero(a):
    return all(x == 0 for row in a for x in row)


def content(a):
    return math.gcd(*(abs(x) for row in a for x in row))


def v3(x):
    answer = 0
    while x and x % 3 == 0:
        answer += 1
        x //= 3
    return answer


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    rows, cols = len(m), len(m[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if m[i][col]), None)
        if pivot is None:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        p = m[pivot_row][col]
        m[pivot_row] = [x / p for x in m[pivot_row]]
        for i in range(rows):
            if i != pivot_row and m[i][col]:
                q = m[i][col]
                m[i] = [x - q * y for x, y in zip(m[i], m[pivot_row])]
        pivot_row += 1
    return pivot_row


def charpoly_coefficients(a):
    b = I
    coefficients = [1]
    for k in range(1, DIM + 1):
        ab = multiply(a, b)
        ck = -sum(ab[i][i] for i in range(DIM)) // k
        coefficients.append(ck)
        b = add(ab, scale(ck, I))
    return coefficients, b


coefficients, cayley_hamilton_residual = charpoly_coefficients(C)
N = add(C, scale(-1, I))
Q = add(add(multiply(C, C), scale(-T, C)), I)
bridge = multiply(N, Q)
bridge_killed = multiply(N, bridge)

gates = {
    "characteristic_polynomial_factors_as_claimed":
        coefficients == [1, -147460, 294918, -147460, 1],
    "cayley_hamilton_is_exact": zero(cayley_hamilton_residual),
    "spectral_trace_gap_has_exact_three_adic_depth_two":
        T - 2 == 3**2 * 2**14,
    "identity_factor_has_rank_three": rank(N) == 3,
    "quadratic_factor_has_rank_two": rank(Q) == 2,
    "spectral_bridge_is_nonzero_rank_one":
        not zero(bridge) and rank(bridge) == 1,
    "spectral_bridge_has_exact_three_adic_depth_three":
        v3(content(bridge)) == 3 and content(bridge) == 3**3 * 2**11,
    "one_more_identity_factor_kills_bridge": zero(bridge_killed),
    "constructor_identity_increment_has_depth_one": v3(content(N)) == 1,
    "quadratic_factor_has_depth_two": v3(content(Q)) == 2,
}
payload = {
    "schema": "marici.strominger.constructor_spectral_extension_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "characteristic_polynomial_coefficients": coefficients,
    "factorization": "(lambda-1)^2*(lambda^2-147458*lambda+1)",
    "spectral_trace": T,
    "spectral_trace_gap": {
        "value": T - 2,
        "factorization": "3^2*2^14",
    },
    "operators": {
        "N": {
            "definition": "C-I",
            "rank": rank(N),
            "content": content(N),
            "v3_content": v3(content(N)),
        },
        "Q": {
            "definition": "C^2-147458*C+I",
            "rank": rank(Q),
            "content": content(Q),
            "v3_content": v3(content(Q)),
        },
        "bridge": {
            "definition": "(C-I)*(C^2-147458*C+I)",
            "rank": rank(bridge),
            "content": content(bridge),
            "v3_content": v3(content(bridge)),
            "matrix": bridge,
        },
        "bridge_killed_by_N": zero(bridge_killed),
    },
    "classification":
        "nonsemisimple_rank_one_spectral_extension_at_exact_three_adic_depth_three",
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
