#!/usr/bin/env python3
"""Finite exact audit of the RH mate commutator gate transferred from magnetism."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_mate_commutator_gate_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def rank(a):
    work = [[Fraction(x) for x in row] for row in a]
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


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def eye(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def zero(a):
    return all(x == 0 for row in a for x in row)


def diag(values):
    return [[values[i] if i == j else Fraction(0) for j in range(len(values))] for i in range(len(values))]


def vandermonde_columns(lambdas, max_power):
    n = len(lambdas)
    rows = []
    mean = sum(lambdas) / n
    for k in range(1, max_power + 1):
        moment = sum(x**k for x in lambdas) / n
        rows.append([x**k - moment for x in lambdas])
    return transpose(rows)

lambdas = [Fraction(0), Fraction(1), Fraction(3)]
n = len(lambdas)
ones_col = [[Fraction(1)] for _ in lambdas]
E = [[Fraction(1, n) for _ in range(n)] for __ in range(n)]
I = eye(n)
K = sub(I, E)
L = diag(lambdas)
C = matmul(matmul(K, L), E)
commutator = sub(matmul(E, L), matmul(L, E))
variance = sum(x * x for x in lambdas) / n - (sum(lambdas) / n) ** 2
CtC = matmul(transpose(C), C)
expected_CtC = scale(variance, E)
moments = vandermonde_columns(lambdas, n - 1)
constant_lambdas = [Fraction(2), Fraction(2), Fraction(2)]
E_const = E
K_const = K
L_const = diag(constant_lambdas)
C_const = matmul(matmul(K_const, L_const), E_const)

# Finite holonomy hostile: identity finite holonomy and nonzero C can coexist.
# Identity maps around a triangle carry no curvature, yet the descent/Mellin
# commutator is nonzero because descent averages distinct scales.
holonomy_identity = matmul(matmul(eye(n), eye(n)), eye(n)) == eye(n)

checks = {
    "E_is_projection": matmul(E, E) == E,
    "C_is_off_diagonal_from_descended_to_complement": matmul(K, C) == C and matmul(C, E) == C,
    "C_matches_commutator_off_diagonal_up_to_sign": C == scale(Fraction(-1), matmul(K, commutator)),
    "CtC_is_variance_on_descended_line": CtC == expected_CtC and variance > 0,
    "C_nonzero_iff_fiber_scales_not_constant_positive_case": not zero(C),
    "C_zero_for_constant_fiber_scales": zero(C_const),
    "centered_moment_tower_spans_complement_for_distinct_scales": rank(moments) == n - 1,
    "finite_identity_holonomy_does_not_kill_commutator": holonomy_identity and not zero(C),
}

payload = {
    "schema": "marici.strominger.rh_mate_commutator_gate.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "finite_fiber_lambdas": [str(x) for x in lambdas],
    "variance": str(variance),
    "ranks": {
        "descended_line": rank(E),
        "complement": rank(K),
        "commutator_image": rank(C),
        "centered_moment_tower": rank(moments),
    },
    "verdict": (
        "The RH mate direction survives the first finite audit: descent over "
        "distinct Mellin scales produces a source-native off-diagonal current, "
        "its energy is the scale variance on the descended line, and centered "
        "moments span the finite complement. This still has no zero-confining "
        "force: identity finite holonomy can coexist with the nonzero commutator. "
        "The next gate is a noncircular zero-to-state or completion-stable inverse "
        "bound connecting completed zeros to this positive current."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
