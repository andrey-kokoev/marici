from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/cross-sector-bridge-admission-registry-v1.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    records = registry["records"]
    assert len(records) == 3
    by_id = {record["id"]: record for record in records}
    assert len(by_id) == len(records)

    sources = {record_id: json.loads(Path(record["source_record"]).read_text(encoding="utf-8")) for record_id, record in by_id.items()}
    markov = sources["markov-analytic-section"]
    kitaev = sources["kitaev-electric-associator-loop"]
    r_zeta = sources["R_zeta"]
    assert markov["passed"] is True and markov["status"] == "restricted_global_analytic_section_verified"
    assert kitaev["map_status"] == "partially_constructed"
    assert r_zeta["map_status"] == "authority_blocked"

    kitaev_text = json.dumps(kitaev).lower()
    assert all(name in kitaev_text for name in by_id["kitaev-electric-associator-loop"]["minimal_failures"])
    r_text = json.dumps(r_zeta)
    assert "target_source_typed" in r_text and "map_source_derived" in r_text

    admitted = [record for record in records if record["admitted_to_sector_nerve"]]
    assert [record["id"] for record in admitted] == ["markov-analytic-section"]
    assert by_id["markov-analytic-section"]["computad_incidence_status"] == "typed_all_five_sorts"
    assert all(by_id[name]["computad_incidence_status"] == "untyped" for name in ["kitaev-electric-associator-loop", "R_zeta"])

    # One admitted vertex has no nondegenerate edges, cycles, triangles, or horns.
    assert registry["overlap_edges"] == []
    assert registry["cross_sector_cycles"] == []
    assert registry["mixed_horns"] == []
    admitted_vertices = len(admitted)
    edge_count = 0
    cycle_rank = edge_count - admitted_vertices + 1 if admitted_vertices else 0
    assert cycle_rank == 0

    result = {
        "schema": "marici.voevodsky.cross-sector-bridge-admission-check.v1",
        "status": "first_cross_sector_nerve_census_verified",
        "candidate_sector_records": len(records),
        "admitted_sector_vertices": admitted_vertices,
        "typed_cross_sector_edges": edge_count,
        "cross_sector_cycle_rank": cycle_rank,
        "mixed_horn_count": 0,
        "markov_section_admitted": True,
        "kitaev_partial_representation_admitted": False,
        "R_zeta_transfer_admitted": False,
        "scalar_coincidence_creates_edge": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
