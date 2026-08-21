#!/usr/bin/env python3
"""Audit whether five-site sheet coalescence determines a relative-chain lift."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-site-physical-sheet-orbit.json"
OUT = ROOT / "research/grothendieck/results/five-site-branch-chain-lift-gate.json"


def main():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    strata = {x["branch_subset_mask"]: x for x in source["branch_strata"]}
    assert source["deck_orbit_size"] == 32
    assert strata[1]["restricted_sheet_classes"] == 16

    # On one branch bit each pair (Gamma_+, Gamma_-) has one set-level image.
    # Normalize the selected positive chamber to coefficient 1.  Set-level
    # coalescence and positive orientation alone leave the other multiplicity a
    # undetermined.  Test two positive integral lifts.
    candidates = []
    for a in (1, 2):
        image_coefficients = [1, a]
        # q^*(1)=(1,1); adjunction on the two sheet basis vectors requires
        # <1,q_*Gamma_+>=<1,q_*Gamma_->=1.
        adjunction_defects = sum(x != 1 for x in image_coefficients)
        candidates.append({
            "negative_sheet_multiplicity": a,
            "positive_orientation": True,
            "same_target_sheet_label": True,
            "selected_positive_normalization": image_coefficients[0] == 1,
            "full_pairing_adjunction_defects": adjunction_defects,
            "orbit_trace_image_multiplicity": sum(image_coefficients),
        })

    assert all(c["positive_orientation"] for c in candidates)
    assert all(c["same_target_sheet_label"] for c in candidates)
    assert all(c["selected_positive_normalization"] for c in candidates)
    assert [c["full_pairing_adjunction_defects"] for c in candidates] == [0, 1]

    result = {
        "schema": "marici.grothendieck.five_site_branch_chain_lift_gate.v1",
        "source_branch_mask": 1,
        "generic_sheet_count": 32,
        "restricted_sheet_count": 16,
        "local_model": "C2 sheet-label quotient on one branch bit",
        "positive_integral_chain_lifts": candidates,
        "unique_lift_from_frozen_evidence": False,
        "adjunction_selects_multiplicity_one": True,
        "but_adjunction_is_source_admitted": False,
        "missing": [
            "map of physical relative pairs",
            "boundary-compatible chain specialization",
            "local degree/intersection multiplicity",
            "endpoint or regulator normalization",
        ],
        "verdict": (
            "Entry 1224 proves set-level coalescence, not the physical q_*. "
            "The multiplicity-one lift is the unique algebraic adjoint, but "
            "using that fact as physical evidence would assume the desired adjunction."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
