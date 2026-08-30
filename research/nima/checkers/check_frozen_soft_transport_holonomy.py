#!/usr/bin/env python3
"""Compose the frozen source factors acting on the cyclic soft norm line."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]
CYCLIC = MARICI / "research" / "benincasa" / "cyclic-leray-naturality-certificate.json"
SOFT = MARICI / "research" / "benincasa" / "results" / "rank12-soft-tate-cyclic-occurrences.json"
RADIAL = MARICI / "research" / "benincasa" / "all-soft-radial-strict-transform.json"
RESULT = ROOT / "results" / "frozen-soft-transport-holonomy.json"


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main() -> None:
    cyclic = json.loads(CYCLIC.read_text(encoding="utf-8"))
    soft = json.loads(SOFT.read_text(encoding="utf-8"))
    radial = json.loads(RADIAL.read_text(encoding="utf-8"))

    sigma = soft["cyclic_matrix"]
    norm = [1, 1, 1]
    assert mat_vec(sigma, norm) == norm
    assert soft["cyclic_composition"] == "sigma^3=I"
    assert soft["external_normal_orientation_sign"] == 1
    assert soft["loop_residue_orientation_sign"] == 1
    assert all(row["gysin_coefficient"] == 1 for row in soft["occurrences"])
    assert all(row["deck_character"] == -1 for row in soft["occurrences"])

    assert cyclic["leray_residue_commutes_with_cyclic_permutation"] is True
    assert cyclic["normal_jacobians"] == [1, 1, 1]
    assert cyclic["residue_orientations"] == [1, 1, 1]
    assert cyclic["residue_multiplicities"] == [1, 1, 1]
    assert cyclic["negative_imaginary_convex_tube_is_cyclic_invariant"] is True
    assert cyclic["positive_cayley_menger_sheet_is_cyclically_relabelled"] is True
    assert radial["strict_transform"]["radial_monodromy"] == 1

    paired_deck_character = (-1) * (-1)
    factors = {
        "norm_occurrence_transport": 1,
        "normal_jacobian": 1,
        "residue_orientation": 1,
        "residue_multiplicity": 1,
        "paired_deck_character": paired_deck_character,
        "radial_monodromy": 1,
        "cyclic_tube": 1,
    }
    holonomy = 1
    for value in factors.values():
        holonomy *= value
    assert holonomy == 1

    result = {
        "status": "PASS",
        "frozen_transport_factors": factors,
        "norm_holonomy": holonomy,
        "character_trace": 2,
        "primitive_mu3_phase_activated": False,
        "gauge_change_can_alter_one_dimensional_holonomy": False,
        "reopening_burden": "independently source-derived order-three flat coefficient twist",
        "conclusion": (
            "The supported relative class exists, but every admitted frozen-source "
            "transport factor acts trivially on its norm line."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
