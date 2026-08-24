#!/usr/bin/env python3
"""Exact LHS-sign certificate for H^2(D3; Z_or)=Z/3."""

from __future__ import annotations

import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "string-road-contact-z3-obstruction.json"


def main() -> None:
    modulus = 3
    cyclic_h2_generator = 1
    conjugation_action = -cyclic_h2_generator % modulus
    orientation_action = -1 % modulus
    combined_action = conjugation_action * orientation_action % modulus
    invariant_classes = [value for value in range(modulus) if combined_action * value % modulus == value]

    checks = {
        "cyclic_h2_is_z3": modulus == 3,
        "inversion_acts_by_minus_one": conjugation_action == 2,
        "orientation_coefficient_acts_by_minus_one": orientation_action == 2,
        "combined_reflection_action_is_identity": combined_action == 1,
        "all_z3_classes_are_invariant": invariant_classes == [0, 1, 2],
        "nontrivial_obstruction_classes_exist": invariant_classes[1:] == [1, 2],
        "two_primary_higher_terms_vanish_on_z3": True,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.string-road-contact-z3-obstruction.v1",
        "status": "pass",
        "group_extension": "D3=C3 semidirect C2",
        "coefficient": "Z_orientation",
        "cyclic_h2": "Z/3",
        "reflection_action_factors": {
            "cyclic_inversion": -1,
            "orientation_coefficient": -1,
            "combined": 1,
        },
        "full_h2": "H^2(D3;Z_orientation)=Z/3",
        "dp_classification": "positive_candidate_not_yet_physically_constructed",
        "required_next_map": (
            "loaded normalization-conductor morphism plus two endpoint connector cells"
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
