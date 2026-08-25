#!/usr/bin/env python3
"""Separate the B-simple-current sheet from geometric ribbon reversal."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
FUSION = K / "results" / "s3-fusion-ring.json"
RIBBON = K / "results" / "s3-oriented-ribbon-algebra.json"
TORSOR = K / "results" / "s3-wilson-orientation-simple-current-torsor.json"
EXEC = K / "results" / "s3-controlled-wilson-executability.json"
OUT = K / "results" / "s3-simple-current-sheet-vs-ribbon-reversal.json"


def compose(left: dict[str, str], right: dict[str, str]) -> dict[str, str]:
    return {label: left[right[label]] for label in right}


def main() -> None:
    fusion = json.loads(FUSION.read_text(encoding="utf-8"))
    ribbon = json.loads(RIBBON.read_text(encoding="utf-8"))
    torsor = json.loads(TORSOR.read_text(encoding="utf-8"))
    executable = json.loads(EXEC.read_text(encoding="utf-8"))
    labels = tuple("ABCDEFGH")

    source_labels = fusion["anyon_labels"]
    assert source_labels["A"] == {"sector": "e", "irrep": "triv", "quantum_dimension": 1}
    assert source_labels["B"] == {"sector": "e", "irrep": "sign", "quantum_dimension": 1}
    assert source_labels["D"]["sector"] == source_labels["E"]["sector"] == "t"
    assert source_labels["D"]["irrep"] == "plus" and source_labels["E"]["irrep"] == "minus"
    assert source_labels["G"]["irrep"] == "omega" and source_labels["H"]["irrep"] == "omega2"

    b_sheet = dict(zip(labels, ("B", "A", "C", "E", "D", "F", "G", "H")))
    ribbon_reversal = dict(zip(labels, ("A", "B", "C", "D", "E", "F", "H", "G")))
    identity = {label: label for label in labels}
    assert compose(b_sheet, b_sheet) == identity
    assert compose(ribbon_reversal, ribbon_reversal) == identity
    assert compose(b_sheet, ribbon_reversal) == compose(ribbon_reversal, b_sheet)
    klein = {
        tuple(action[label] for label in labels)
        for action in (identity, b_sheet, ribbon_reversal, compose(b_sheet, ribbon_reversal))
    }
    assert len(klein) == 4
    assert b_sheet != ribbon_reversal

    assert ribbon["orientation_intertwiner"] == "phi(F_L(h,g))=F_R(h^-1,g)"
    assert ribbon["noncommuting_witness"]["clockwise_h_product"] == "(012)"
    assert ribbon["noncommuting_witness"]["counterclockwise_h_product"] == "(021)"
    assert torsor["simple_current"]["fusion_action_B_tensor_x"] == b_sheet
    assert executable["microscopic_constructor_audit"]["closed_ribbon_insertion"].startswith(
        "produces a Wilson eigenvalue/amplitude"
    )
    result = {
        "schema": "marici.kitaev.s3-simple-current-sheet-vs-ribbon-reversal.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (FUSION, RIBBON, TORSOR, EXEC)
        },
        "source_rooted_labels": {
            "tensor_unit_A": "(identity flux, trivial representation)",
            "simple_current_B": "(identity flux, sign representation)",
            "D_E": "transposition flux with plus/minus Z2 centralizer representation",
            "G_H": "three-cycle flux with omega/omega2 centralizer representation",
        },
        "involutions": {
            "B_simple_current_sheet": {
                "permutation": "(A B)(D E)",
                "moves_tensor_unit": True,
                "fixes_G_H_individually": True,
            },
            "geometric_ribbon_reversal": {
                "permutation_on_simple_labels": "(G H)",
                "fixed_D_E_individually": True,
                "reason": "transpositions are self-inverse while omega and omega2 are conjugate under three-cycle inversion",
                "fixed_ribbon_intertwiner": "h -> h^-1",
            },
            "equal": False,
            "commute": True,
            "generated_group": "C2 x C2",
        },
        "terminology_correction": {
            "deprecated_ambiguous_phrase": "absolute D/E orientation",
            "precise_name": "B-simple-current sheet or signed Wilson D/E frame",
            "geometric_ribbon_orientation_already_frozen": True,
        },
        "operational_boundary": {
            "oriented_fixed_ribbon_algebra_supplied": True,
            "closed_ribbon_insertion_equals_controlled_quarter_evolution": False,
            "interface_preserves_source_rooted_Wilson_sign": False,
            "remaining_map": "source-rooted ribbon/character normalization -> controlled exp(2 pi i W_x/4) -> digit-interface primitive",
        },
        "verdict": "The hidden Wilson C2 is not geometric ribbon reversal. It is translation by the sign simple current B, acting as (A B)(D E); geometric reversal acts by group inversion and exchanges G/H while fixing D/E. The two commuting involutions generate C2xC2. Source data already distinguish A=(e,triv) from B=(e,sign) and freeze ribbon orientation, but the admitted closed-ribbon insertion is not the required controlled quarter evolution. The unresolved operational datum is sign-preserving compilation from the source-rooted Wilson character to the charged digit interface.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
