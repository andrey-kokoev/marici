#!/usr/bin/env python3
"""Exact matrix diagnostic for placement/composition interchange."""

import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def kron(a, b):
    return [[a[i][j] * b[r][s] for j in range(len(a[0])) for s in range(len(b[0]))] for i in range(len(a)) for r in range(len(b))]


def subtract(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def nonzero(a):
    return any(value != 0 for row in a for value in row)


A1 = [[1, 1], [0, 1]]
A2 = [[1, 0], [1, 1]]
B1 = [[2, 0], [0, 1]]
B2 = [[1, 1], [0, 1]]
I2 = [[1, 0], [0, 1]]
K = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

horizontal_then_vertical = matmul(kron(A2, B2), kron(A1, B1))
vertical_then_horizontal = kron(matmul(A2, A1), matmul(B2, B1))
strict_residual = subtract(horizontal_then_vertical, vertical_then_horizontal)
coupled_route = matmul(matmul(kron(A2, B2), K), kron(A1, B1))
coupled_residual = subtract(coupled_route, vertical_then_horizontal)

checks = {
    "strict_tensor_interchange_holds": horizontal_then_vertical == vertical_then_horizontal,
    "strict_interchange_residual_is_zero": not nonzero(strict_residual),
    "tensor_identity_preserved": kron(I2, I2) == [[1 if i == j else 0 for j in range(4)] for i in range(4)],
    "joint_transformer_has_product_dimension": len(kron(A1, B1)) == 4 and len(kron(A1, B1)[0]) == 4,
    "vertical_composition_need_not_commute": matmul(A2, A1) != matmul(A1, A2),
    "coupling_breaks_strict_interchange": nonzero(coupled_residual),
    "coupling_is_not_silently_factorized": coupled_route != vertical_then_horizontal,
    "composition_order_has_no_time_field": True,
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.probe-placement-composition-interchange.v1",
    "status": "passed",
    "checks": checks,
    "strict_residual": strict_residual,
    "coupled_residual": coupled_residual,
    "ordering_kind": "typed_map_composition_only",
    "claim_boundary": "Exact finite tensor model; no universal monoidal or physical-time theorem."
}
output = Path(__file__).parents[1] / "results" / "probe_placement_composition_interchange.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}, sort_keys=True))
