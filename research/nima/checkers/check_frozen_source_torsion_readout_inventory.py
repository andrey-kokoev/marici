#!/usr/bin/env python3
"""Close the declared frozen-source inventory against the flat mu3 character."""

from __future__ import annotations

import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "frozen-source-torsion-readout-inventory.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    transport = load("frozen-soft-transport-holonomy.json")
    additive = load("integral-tate-product-readout-type.json")
    symmetry = load("d3-mu3-activation-no-go.json")
    character = load("all-soft-relative-differential-character.json")
    tensor = load("double-soft-transverse-tensor-explanation.json")
    flat = load("all-soft-flat-z3-character.json")

    checks = {
        "ordinary_complex_period_kills_torsion": bool(
            additive["ordinary_complex_period_must_vanish"]
        ),
        "frozen_norm_transport_is_trivial": transport["norm_holonomy"] == 1,
        "frozen_transport_does_not_activate_mu3": not bool(
            transport["primitive_mu3_phase_activated"]
        ),
        "mu2_deck_inventory_cannot_generate_mu3": symmetry["mu2_intersection_mu3"] == [1],
        "rank_one_linear_d3_activation_is_impossible": not bool(
            symmetry["primitive_rank_one_activation_possible"]
        ),
        "physical_supported_tensor_not_admitted": not bool(
            tensor["physical_supported_tensor_admitted"]
        ),
        "flat_character_has_no_de_rham_rank": character["de_rham_rank_contribution"] == 0,
        "cm_relative_chain_coupling_not_constructed": not bool(
            flat["Cayley_Menger_relative_chain_coupling_constructed"]
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.frozen-source-torsion-readout-inventory.v1",
        "status": "pass",
        "scope": "currently declared homogeneous three-site frozen-source operations",
        "inventory_result": "no_admitted_operation_accepts_the_flat_degree_three_character",
        "physical_prediction_in_scope": "torsion phase is silent",
        "reopening_requirements": [
            "source-derived relative two-cycle or boundary trivialization",
            "torsion-sensitive differential-character pairing",
            "enlarged source physics supplying an order-three flat coefficient operation",
        ],
        "not_claimed": (
            "No universal impossibility theorem beyond the frozen source inventory; "
            "the canonical parameter-space character remains nonzero."
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
