from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/cross-sector-bridge-admission-registry-v2.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    records = {record["id"]: record for record in registry["records"]}
    assert len(records) == 4
    sources = {key: json.loads(Path(record["source_record"]).read_text(encoding="utf-8")) for key, record in records.items()}

    assert sources["markov-analytic-section"]["passed"] is True
    assert sources["kitaev-electric-associator-loop"]["map_status"] == "partially_constructed"
    theta = sources["kitaev-theta-clark-seam-pro-gram"]
    assert theta["machine_rejection"]["code"] == "theta_pro_gram_instantiation_blocked_missing_incidence"
    assert theta["machine_rejection"]["constructor_subset"] == ["S", "R_f", "D"]
    assert theta["requested_feature_map_status"]["single_common_J_X_matrix_constructed"] is False
    assert theta["currently_authorized_subsystem"]["full_mixed_Green_matrix_supplied"] is False
    missing_maps = theta["machine_rejection"]["missing_source_maps"]
    assert len(missing_maps) == 2 and all("boundary" in item for item in missing_maps)
    assert sources["R_zeta"]["map_status"] == "authority_blocked"

    admitted = [record for record in records.values() if record["admitted_to_sector_nerve"]]
    assert [record["id"] for record in admitted] == ["markov-analytic-section"]
    assert registry["overlap_edges"] == registry["cross_sector_cycles"] == registry["mixed_horns"] == []

    result = {
        "schema": "marici.voevodsky.cross-sector-bridge-admission-check.v2",
        "status": "expanded_cross_sector_nerve_census_verified",
        "candidate_sector_records": len(records),
        "admitted_sector_vertices": len(admitted),
        "typed_cross_sector_edges": 0,
        "cross_sector_cycle_rank": 0,
        "mixed_horn_count": 0,
        "theta_constructor_subset_preserved": True,
        "theta_full_vertex_admitted": False,
        "theta_first_missing_maps": missing_maps,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
