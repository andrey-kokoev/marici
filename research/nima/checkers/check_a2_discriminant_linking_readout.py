#!/usr/bin/env python3
"""Exact certificate for the A2 discriminant linking readout."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "a2-discriminant-linking-readout.json"


def integral(vector: sp.Matrix) -> bool:
    return all(value.q == 1 for value in vector)


def main() -> None:
    gram = sp.Matrix([[2, -1], [-1, 2]])
    rotation = sp.Matrix([[0, -1], [1, -1]])
    signed_reflection = sp.Matrix([[1, -1], [0, -1]])
    occurrence_reflection = sp.Matrix([[1, 0], [1, -1]])
    weight = gram.inv() * sp.Matrix([1, 0])
    linking = (weight.T * gram * weight)[0]

    checks = {
        "gram_discriminant_is_three": gram.det() == 3,
        "rotation_isometry": rotation.T * gram * rotation == gram,
        "signed_reflection_isometry": signed_reflection.T * gram * signed_reflection == gram,
        "occurrence_reflection_isometry": occurrence_reflection.T * gram * occurrence_reflection == gram,
        "rotation_order_three": rotation**3 == sp.eye(2),
        "signed_reflection_order_two": signed_reflection**2 == sp.eye(2),
        "occurrence_reflection_order_two": occurrence_reflection**2 == sp.eye(2),
        "signed_dihedral_relation": signed_reflection * rotation * signed_reflection == rotation.inv(),
        "occurrence_dihedral_relation": occurrence_reflection * rotation * occurrence_reflection == rotation.inv(),
        "weight_not_integral": not integral(weight),
        "weight_has_order_three": integral(3 * weight),
        "self_linking_is_two_thirds": linking == sp.Rational(2, 3),
        "rotation_fixes_discriminant_class": integral(rotation * weight - weight),
        "signed_reflection_inverts_discriminant_class": integral(signed_reflection * weight + weight),
        "occurrence_reflection_fixes_discriminant_class": integral(occurrence_reflection * weight - weight),
        "primitive_phase_trace_is_minus_one": 2 * sp.cos(4 * sp.pi / 3) == -1,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.a2-discriminant-linking-readout.v1",
        "status": "pass",
        "gram": [[int(value) for value in row] for row in gram.tolist()],
        "discriminant": int(gram.det()),
        "discriminant_generator": [str(x) for x in weight],
        "self_linking_mod_one": str(linking),
        "phase": "exp(2*pi*i*2/3)",
        "unframed_character_trace": -1,
        "interpretation": {
            "rotation_on_discriminant_group": "identity",
            "occurrence_reflection_on_discriminant_group": "identity",
            "signed_reflection_on_discriminant_group": "inversion",
            "transport_holonomy": "not identified with the linking phase",
        },
        "checks": checks,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
