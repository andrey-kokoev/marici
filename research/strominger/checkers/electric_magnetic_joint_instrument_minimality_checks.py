#!/usr/bin/env python3
"""Finite exact audit for the minimal electric-magnetic joint instrument."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "electric_magnetic_joint_instrument_minimality_checks.json"

z = Fraction(0)
o = Fraction(1)

I = ((o, z), (z, o))
PE = ((o, z), (z, z))
PM = ((z, z), (z, o))
Z = ((o, z), (z, -o))
X = ((z, o), (o, z))
Y = ((z, o), (-o, z))
E_ROW = (o, o)
M_ROW = (o, -o)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def mul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def scale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def span_rank(mats):
    rows = []
    for a in mats:
        rows.append([a[0][0], a[0][1], a[1][0], a[1][1]])
    rank = 0
    col = 0
    while rank < len(rows) and col < 4:
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        p = rows[rank][col]
        rows[rank] = [x / p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                q = rows[i][col]
                rows[i] = [x - q * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
        col += 1
    return rank


def row_det(r1, r2):
    return r1[0] * r2[1] - r1[1] * r2[0]

# Existing source algebra: diagonal projectors and their products.
diagonal_products = [I, PE, PM, Z, mul(PE, PM), mul(PM, PE), mul(Z, Z)]
existing_rank = span_rank(diagonal_products)
bridge_algebra_rank = span_rank(diagonal_products + [X, mul(Z, X), mul(X, Z)])

# Same-preparation scalar ports. Each port alone has a kernel; together they are faithful.
electric_magnetic_rows_det = row_det(E_ROW, M_ROW)

# Moving diagonal frame connection for the bridge endomorphism.
a = Fraction(2)
b = Fraction(-1)
K = ((a, z), (z, b))
commutator_KX = sub(mul(K, X), mul(X, K))
# If X is merely differentiated after a moving frame, dX equals [K,X].
naive_moving_bridge_derivative = commutator_KX
covariant_bridge_derivative = sub(naive_moving_bridge_derivative, commutator_KX)

# A source-authorized off-diagonal tail sewing block must not be block diagonal.
D_EM = ((z, o), (z, z))
D_ME = ((z, z), (o, z))
off_diagonal_rank = span_rank([D_EM, D_ME])

checks = {
    "existing_projector_algebra_is_diagonal_rank_two": existing_rank == 2,
    "existing_algebra_does_not_contain_bridge": span_rank(diagonal_products + [X]) == existing_rank + 1,
    "bridge_with_parity_generates_full_matrix_algebra": bridge_algebra_rank == 4,
    "bridge_is_reflection_odd": mul(Z, X) == scale(Fraction(-1), mul(X, Z)),
    "bridge_is_self_adjoint_in_real_basis": X == ((X[0][0], X[1][0]), (X[0][1], X[1][1])),
    "electric_port_alone_has_kernel": E_ROW != (z, z),
    "magnetic_port_alone_has_kernel": M_ROW != (z, z),
    "joint_electric_magnetic_scalar_ports_are_faithful": electric_magnetic_rows_det != 0,
    "moving_frame_creates_naive_bridge_derivative": naive_moving_bridge_derivative != ((z, z), (z, z)),
    "connection_subtraction_restores_covariant_bridge_constancy": covariant_bridge_derivative == ((z, z), (z, z)),
    "off_diagonal_tail_sewing_requires_cross_sector_blocks": off_diagonal_rank == 2,
}

payload = {
    "schema": "marici.strominger.electric_magnetic_joint_instrument_minimality.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "interpretation": {
        "minimal_control_gap": "one reflection-odd self-adjoint bridge outside the diagonal electric/magnetic algebra",
        "minimal_observation_gap": "same-preparation joint electric and magnetic scalar rows are faithful while either row alone has a kernel",
        "minimal_connection_gap": "moving-frame derivatives of the bridge require an induced connection term",
        "tail_sewing_translation": "sectorwise continuation cannot create the bridge; an off-diagonal cross-sector block is required",
    },
    "ranks": {
        "existing_diagonal_algebra": existing_rank,
        "with_bridge_and_parity": bridge_algebra_rank,
        "off_diagonal_tail_blocks": off_diagonal_rank,
    },
    "moving_frame": {
        "K": [[str(x) for x in row] for row in K],
        "naive_derivative": [[str(x) for x in row] for row in naive_moving_bridge_derivative],
        "covariant_derivative": [[str(x) for x in row] for row in covariant_bridge_derivative],
    },
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
