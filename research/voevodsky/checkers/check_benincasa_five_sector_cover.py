from __future__ import annotations

import json
from pathlib import Path


OVERLAP = Path("research/benincasa/results/five-site-region-pair-total-soft-overlap-gate.json")
PAIRING = Path("research/benincasa/results/five-site-g5-transverse-pair-physical-pairing-gate.json")


def main() -> None:
    overlap = json.loads(OVERLAP.read_text(encoding="utf-8"))
    pairing = json.loads(PAIRING.read_text(encoding="utf-8"))
    assert "five source residue sectors" in overlap["available"]
    assert "cyclic relabelling isomorphisms" in overlap["available"]
    required_overlap_data = {
        "pairwise overlap coefficient objects",
        "restriction maps to overlaps",
        "source-derived Cech differential",
        "proof of descent or colimit assembly",
    }
    assert set(overlap["absent"]) == required_overlap_data
    assert overlap["cyclic_covariance_status"] == "equivariant direct sum, not gluing"
    assert overlap["missing_map_status"] == "undefined, not zero"
    assert overlap["new_carrier_datum"] is False
    assert "not cohomology" in overlap["rank_34_kernel_status"]

    required_physical_data = {"integration_chain", "contour_orientation", "denominator_regulator_map", "relative_boundary_map"}
    assert set(pairing["missing_required_fields"]) == required_physical_data
    assert pairing["physical_relative_chain_map_status"] == "undefined"
    assert pairing["physical_pairing_status"] == "undefined, neither zero nor nonzero"

    result = {
        "schema": "marici.voevodsky.benincasa-five-sector-cover.v1",
        "status": "local_family_without_overlap_nerve_verified",
        "local_sector_vertices": 5,
        "cyclic_relabelling_isomorphisms_available": True,
        "typed_pairwise_overlap_edges": 0,
        "overlap_incidence_object_defined": False,
        "intended_five_cycle_rank": None,
        "cech_differential_defined": False,
        "descent_assembly_defined": False,
        "rank_34_kernel_is_overlap_cohomology": False,
        "physical_pairing_defined": False,
        "new_carrier_datum": False,
        "first_reopening_object": "source-derived pairwise-overlap correspondence with two restriction maps",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
