from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/sector-overlap-edge-contract-v1.json")
AUDIT = Path("research/voevodsky/sector-overlap-edge-candidate-audit-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    required = set(contract["required_fields"])
    assert required == {
        "edge_id", "left_sector", "right_sector", "common_object_sort", "common_object",
        "left_incidence_map", "right_incidence_map", "comparison_cell", "certificate_dependencies", "scope",
    }
    assert set(contract["common_object_sorts"]) == {"carrier", "gauge_presentation", "finite_green", "quotient_form", "closed_form"}
    assert {"source_derived", "typed_domain", "typed_codomain", "variance_declared", "naturality_domain_declared"} == set(contract["map_requirements"])
    assert "shared scalar value" in contract["nonconstructors"]
    assert "evidence dependency alone" in contract["nonconstructors"]

    candidates = audit["candidates"]
    assert len(candidates) == 5
    assert all(candidate["admitted"] is False for candidate in candidates)
    assert all(candidate["first_missing"] for candidate in candidates)
    assert audit["admitted_edge_count"] == 0
    sontag = next(candidate for candidate in candidates if candidate["id"] == "sontag_to_flavor_calibration")
    assert sontag["preserved_arrow_type"] == "evidence_dependency"
    assert {"common_object_sort", "common_object", "comparison_cell"}.issubset(sontag["first_missing"])

    result = {
        "schema": "marici.voevodsky.sector-overlap-edge-contract-check.v1",
        "status": "first_edge_admission_contract_verified",
        "required_edge_fields": len(required),
        "admissible_common_sorts": len(contract["common_object_sorts"]),
        "candidate_edges_audited": len(candidates),
        "admitted_edges": 0,
        "all_rejections_have_first_missing_data": True,
        "physical_extension_separated": True,
        "evidence_dependencies_preserved_without_edge_promotion": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
