#!/usr/bin/env python3
"""Certify the source-oriented comparison I^2/I^3 -> A2*/A2."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "norm-grade-to-a2-discriminant-comparison.json"


def convolution(left: list[int], right: list[int]) -> list[int]:
    return [
        sum(left[index] * right[(degree - index) % 3] for index in range(3))
        for degree in range(3)
    ]


def root_coordinates(vector: list[int]) -> sp.Matrix:
    # b1=(1,-1,0), b2=(0,1,-1) on the sum-zero occurrence lattice.
    assert sum(vector) == 0
    return sp.Matrix([vector[0], -vector[2]])


def integral(vector: sp.Matrix) -> bool:
    return all(value.q == 1 for value in vector)


def main() -> None:
    gram = sp.Matrix([[2, -1], [-1, 2]])
    t = [-1, 1, 0]
    t2 = convolution(t, t)
    t3 = convolution(t2, t)
    norm_lift = gram.inv() * root_coordinates(t2)
    ambiguity_lift = gram.inv() * root_coordinates(t3)

    reflected_t2 = [t2[0], t2[2], t2[1]]
    reflected_lift = gram.inv() * root_coordinates(reflected_t2)
    rotated_t2 = [t2[2], t2[0], t2[1]]
    rotated_lift = gram.inv() * root_coordinates(rotated_t2)

    self_linking = (norm_lift.T * gram * norm_lift)[0]
    checks = {
        "t2_is_expected_norm_vector": t2 == [1, -2, 1],
        "t3_is_expected_relation": t3 == [0, 3, -3],
        "i3_ambiguity_maps_integrally": integral(ambiguity_lift),
        "norm_lift_is_nonintegral": not integral(norm_lift),
        "three_norm_lift_is_integral": integral(3 * norm_lift),
        "self_linking_is_two_thirds": self_linking == sp.Rational(2, 3),
        "occurrence_reflection_is_equivariant_mod_lattice": integral(reflected_lift - norm_lift),
        "cyclic_rotation_is_equivariant_mod_lattice": integral(rotated_lift - norm_lift),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.norm-grade-to-a2-discriminant-comparison.v1",
        "status": "pass",
        "augmentation_generator_t": t,
        "norm_generator_t2": t2,
        "i3_relation_t3": t3,
        "inverse_cartan_norm_lift": [str(value) for value in norm_lift],
        "inverse_cartan_i3_lift": [str(value) for value in ambiguity_lift],
        "induced_map": "I^2/I^3 -> A2*/A2 is an isomorphism",
        "self_linking_mod_one": str(self_linking),
        "checks": checks,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
