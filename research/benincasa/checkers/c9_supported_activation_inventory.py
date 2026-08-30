#!/usr/bin/env python3
"""Inventory pre-existing C9 supported objects against the seam gate."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "nine-site-canonical-contour-packet.json"
JACOBIAN = ROOT / "results" / "nine-site-maximal-orbit-universal-jacobians.json"
GRAM_GATE = ROOT / "results" / "c9-seam-gram-normal-gate.json"
TARGET = ROOT / "results" / "c9-supported-activation-inventory.json"


def main() -> None:
    contour = json.loads(CONTOUR.read_text(encoding="utf-8"))
    jacobian = json.loads(JACOBIAN.read_text(encoding="utf-8"))
    gram_gate = json.loads(GRAM_GATE.read_text(encoding="utf-8"))
    physical_coordinates = set(contour["ambient_orientation"])
    assert "k" not in physical_coordinates and "l" not in physical_coordinates

    k0 = [next(row for row in item["Gram_specializations"] if row["k"] == "0") for item in jacobian["classes"]]
    km = [next(row for row in item["Gram_specializations"] if row["k"] == "-6/7") for item in jacobian["classes"]]
    distinct_k0_divisors = sorted({row["ideal_gcd"] for row in k0})

    supports = [
        {
            "support": "pure Gram normal k=0",
            "independently_derived_costalk": True,
            "costalk_profile": "480 reduced Cartier lines of length one",
            "seam_restriction_derived": True,
            "seam_image": "zero",
            "literal_physical_cycle_incidence": False,
            "accepted_activation": False,
            "reason": "k is absent from the physical contour and the uniform Gram-normal seam residue is zero",
        },
        {
            "support": "second Gram normal k=-6/7",
            "independently_derived_costalk": False,
            "costalk_profile": "Cartier length zero in all 480 classes",
            "seam_restriction_derived": False,
            "literal_physical_cycle_incidence": False,
            "accepted_activation": False,
            "reason": "no supported coefficient object exists",
        },
        {
            "support": "finite k=0 universal-cover Landau quadrics",
            "support_component_count": len(distinct_k0_divisors),
            "independently_derived_costalk": True,
            "costalk_profile": "reduced Cartier divisors inside the auxiliary universal-cover specialization",
            "seam_restriction_derived": False,
            "literal_physical_cycle_incidence": False,
            "accepted_activation": False,
            "reason": "no source map places the physical C9 contour or seam complex on the auxiliary universal-cover quadrics",
        },
        {
            "support": "frozen soft and lower physical factors",
            "independently_derived_costalk": False,
            "costalk_profile": "no factor survives the uniform Jacobian saturation",
            "classes_with_surviving_factor": sum(bool(item["removed_frozen_soft_lower_support_factors"]) for item in jacobian["classes"]),
            "seam_restriction_derived": False,
            "literal_physical_cycle_incidence": True,
            "accepted_activation": False,
            "reason": "finite contour residues are presentation-dependent decompositions and no invariant Landau/Gram costalk remains",
        },
    ]

    assert len(jacobian["classes"]) == 480
    assert all(row["cartier_length"] == 1 and row["reduced_cartier"] for row in k0)
    assert all(row["cartier_length"] == 0 for row in km)
    assert len(distinct_k0_divisors) == 11
    assert gram_gate["pure_gram_costalk_activation"] is False
    assert not any(support["accepted_activation"] for support in supports)

    result = {
        "schema": "marici.c9_supported_activation_inventory.v1",
        "acceptance_contract": [
            "pre-existing support",
            "already-derived coefficient/costalk",
            "typed seam restriction with nonzero H image",
            "literal physical-cycle incidence",
        ],
        "physical_contour_coordinates": sorted(physical_coordinates),
        "supports": supports,
        "accepted_support_count": 0,
        "conclusion": "the declared C9 seam-activation branch is closed under the frozen source inventory",
        "prohibited_repair": "do not promote auxiliary Landau quadrics or finite residue presentations to physical support without a new source-derived map",
    }
    TARGET.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"supports_tested": len(supports), "accepted": 0, "distinct_auxiliary_quadrics": 11}))


if __name__ == "__main__":
    main()
