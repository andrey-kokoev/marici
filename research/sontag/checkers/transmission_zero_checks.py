#!/usr/bin/env python3
"""Exact dependency-free checks for the selected-port zero packet."""

from fractions import Fraction as Q
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


A = Q(3, 5)
B = Q(-12, 25)
C = [[Q(4, 5)], [Q(0)]]
D = [[Q(9, 25)], [Q(4, 5)]]
V = [[A, B], [C[0][0], D[0][0]], [C[1][0], D[1][0]]]
lam = Q(5, 3)
x = Q(-9, 20)
u = Q(1)

selected_det = (lam - A) * D[0][0] + B * C[0][0]
checks = {
    "full_colligation_isometry": mm(transpose(V), V) == [[Q(1), Q(0)], [Q(0), Q(1)]],
    "state_is_schur_stable": abs(A) < 1,
    "minimal_controllable": B != 0,
    "complete_output_observable": any(row[0] != 0 for row in C),
    "selected_zero_is_outside_schur_disk": abs(lam) > 1,
    "selected_rosenbrock_rank_loss": selected_det == 0,
    "zero_witness_dynamics": (lam - A) * x - B * u == 0,
    "zero_witness_selected_port_dark": C[0][0] * x + D[0][0] * u == 0,
    "zero_witness_complementary_port_bright": C[1][0] * x + D[1][0] * u == Q(4, 5),
    "storage_identity_x_only": A * A + sum(row[0] ** 2 for row in C) == 1,
    "storage_identity_u_only": B * B + sum(row[0] ** 2 for row in D) == 1,
    "storage_cross_term_zero": A * B + sum(C[i][0] * D[i][0] for i in range(2)) == 0,
    "bare_collocation_hostile_has_outer_zero": Q(1, 2) * Q(-2) + 1 == 0,
}

result = {
    "schema": "marici.sontag.transmission-zero.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "exact_arithmetic": True,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "witnesses": {
        "A": str(A), "B": str(B), "C": [[str(v) for v in r] for r in C],
        "D": [[str(v) for v in r] for r in D], "zero": str(lam),
        "kernel_vector_x_u": [str(x), str(u)],
        "selected_determinant_at_zero": str(selected_det),
        "complementary_output": str(C[1][0] * x + D[1][0] * u),
    },
    "claim_boundary": "finite-dimensional rational discrete-time scalar-input multi-output realization",
}

out = Path(__file__).resolve().parents[1] / "results" / "transmission_zero.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
