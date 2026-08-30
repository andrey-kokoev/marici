#!/usr/bin/env python3
"""Exact finite-field checks for the source-framed Pluecker connection."""

from __future__ import annotations

import itertools
import json

P = 3


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % P


def minors(a):
    return tuple(
        det3([[a[i][j] for j in range(3)] for i in rows])
        for rows in itertools.combinations(range(4), 3)
    )


def derivative(b, h):
    answer = []
    for rows in itertools.combinations(range(4), 3):
        bm = [[b[i][j] for j in range(3)] for i in rows]
        hm = [[h[i][j] for j in range(3)] for i in rows]
        total = 0
        for column in range(3):
            x = [row[:] for row in bm]
            for i in range(3):
                x[i][column] = hm[i][column]
            total += det3(x)
        answer.append(total % P)
    return tuple(answer)


def add(a, b):
    return [[(x + y) % P for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) % P for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def vec_sub(a, b):
    return tuple((x - y) % P for x, y in zip(a, b))


B = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
CHI = 2
H = [[CHI, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = minors(B)
dp = derivative(B, H)

# Moving domain gauge V(e)=I+eK.
K = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
domain_gauge_term = mul(B, K)
naive_domain = derivative(B, add(H, domain_gauge_term))
domain_connection_term = derivative(B, domain_gauge_term)
corrected_domain = vec_sub(naive_domain, domain_connection_term)

# Moving codomain gauge U(e)=I+eA, including a transverse Pluecker term.
A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
row_gauge_term = mul(A, B)
naive_row = derivative(B, add(H, row_gauge_term))
row_connection_term = derivative(B, row_gauge_term)
corrected_row = vec_sub(naive_row, row_connection_term)

# Fixed gauges: a row swap and compensating column swap.
U = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
V = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
fixed_B = mul(mul(U, B), V)
fixed_H = mul(mul(U, H), V)
fixed_p = minors(fixed_B)
fixed_dp = derivative(fixed_B, fixed_H)

gates = {
    "baseline_derivative_is_radial": dp == tuple(CHI * x % P for x in p),
    "moving_domain_gauge_changes_naive_character": naive_domain != dp,
    "domain_connection_restores_character": corrected_domain == dp,
    "moving_row_gauge_adds_transverse_coordinate": any(
        x != 0 and y == 0 for x, y in zip(row_connection_term, p)
    ),
    "row_connection_restores_full_pluecker_jet": corrected_row == dp,
    "fixed_unimodular_gauge_preserves_radial_character": fixed_dp == tuple(
        CHI * x % P for x in fixed_p
    ),
    "projective_tangent_is_zero": all(
        (dp[i] * p[j] - dp[j] * p[i]) % P == 0
        for i in range(4) for j in range(4)
    ),
}

payload = {
    "schema": "marici.strominger.framed_determinantal_jet_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "field": "F_3",
    "baseline_pluecker": p,
    "baseline_derivative": dp,
    "naive_domain_gauge_derivative": naive_domain,
    "domain_connection_term": domain_connection_term,
    "row_connection_term": row_connection_term,
    "interpretation": {
        "unframed_projective_jet": "stationary",
        "naive_scalar_character": "moving-gauge dependent",
        "covariant_scalar_character": "gauge invariant",
        "required_extra_structure": "source-authorized connection on the determinant line",
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
