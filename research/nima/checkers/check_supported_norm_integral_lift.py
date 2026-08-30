#!/usr/bin/env python3
"""Certify the canonical integral lift of the supported mod-3 norm vector."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "supported-norm-integral-lift.json"


def convolution(left: list[int], right: list[int]) -> list[int]:
    return [
        sum(left[index] * right[(degree - index) % 3] for index in range(3))
        for degree in range(3)
    ]


def root_coordinates(vector: list[int]) -> sp.Matrix:
    assert sum(vector) == 0
    return sp.Matrix([vector[0], -vector[2]])


def rotate(vector: list[int]) -> list[int]:
    return [vector[2], vector[0], vector[1]]


def main() -> None:
    t = [-1, 1, 0]
    t2 = convolution(t, t)
    t3 = convolution(t2, t)
    supported_norm = [1, 1, 1]

    i2_basis = sp.Matrix.hstack(root_coordinates(t2), root_coordinates(rotate(t2)))
    i3_basis = sp.Matrix.hstack(root_coordinates(t3), root_coordinates(rotate(t3)))

    checks = {
        "supported_norm_reduces_to_t2_mod_three": all(
            (supported_norm[index] - t2[index]) % 3 == 0 for index in range(3)
        ),
        "t2_has_zero_augmentation": sum(t2) == 0,
        "i2_has_index_three_in_a2": abs(int(i2_basis.det())) == 3,
        "i3_equals_three_a2": abs(int(i3_basis.det())) == 9,
        "i3_generators_divide_to_unimodular_a2_basis": abs(int((i3_basis / 3).det())) == 1,
        "i2_over_i3_has_order_three": abs(int(i3_basis.det() / i2_basis.det())) == 3,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.supported-norm-integral-lift.v1",
        "status": "pass",
        "supported_norm_mod_three": supported_norm,
        "canonical_augmentation_zero_lift": t2,
        "i2_root_basis_matrix": [[int(x) for x in row] for row in i2_basis.tolist()],
        "i3_root_basis_matrix": [[int(x) for x in row] for row in i3_basis.tolist()],
        "conclusion": "augmentation-zero lifts form t^2 + I^3 and define one class in I^2/I^3",
        "checks": checks,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
