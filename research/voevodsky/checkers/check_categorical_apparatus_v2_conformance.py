from __future__ import annotations

import json
from pathlib import Path


PROFILES = Path("research/voevodsky/categorical-apparatus-v2-conformance-profiles.json")
EVIDENCE = {
    "markov": Path("research/voevodsky/results/five_sort_markov_analytic_section.json"),
    "rh": Path("research/voevodsky/results/rh_modular_filling_invariance.json"),
    "kitaev": Path("research/voevodsky/kitaev-associator-loop-partial-representation-v2.json"),
    "theta": Path("research/kitaev/results/theta-clark-seam-pro-gram-instantiation.json"),
    "benincasa": Path("research/voevodsky/results/benincasa_five_sector_cover.json"),
    "edge": Path("research/voevodsky/results/sector_overlap_edge_contract.json"),
}


def main() -> None:
    registry = json.loads(PROFILES.read_text(encoding="utf-8"))
    evidence = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in EVIDENCE.items()}
    dimensions = set(registry["dimensions"])
    profiles = {profile["id"]: profile for profile in registry["profiles"]}
    assert len(dimensions) == 10 and len(profiles) == 5
    for profile in profiles.values():
        assert dimensions.issubset(profile)
        assert all(profile[dimension] for dimension in dimensions)

    assert evidence["markov"]["passed"] is True
    assert profiles["markov_analytic"]["sector_vertex"] == "admitted"
    assert profiles["markov_analytic"]["horn_coverage"] == "degree_4_declared_laws"
    assert evidence["rh"]["relative_class_determined_by_endpoint_incidence"] is True
    assert evidence["rh"]["strict_chain_representative_determined"] is False
    assert profiles["RH_mellin_interface"]["completion"] == "blocked"
    assert evidence["kitaev"]["map_status"] == "partially_constructed"
    assert profiles["kitaev_associator_loop"]["physical_backend"] == "blocked"
    assert evidence["theta"]["machine_rejection"]["code"] == "theta_pro_gram_instantiation_blocked_missing_incidence"
    assert evidence["benincasa"]["overlap_incidence_object_defined"] is False
    assert evidence["edge"]["admitted_edges"] == 0

    summary = registry["summary"]
    assert summary == {"profiles": 5, "admitted_sector_vertices": 1, "admitted_sector_edges": 0, "profiles_with_completed_mathematical_realization": 1, "profiles_with_physical_backend": 0}
    result = {
        "schema": "marici.voevodsky.categorical-apparatus-v2-conformance-check.v1",
        "status": "five_profile_conformance_matrix_verified",
        "profiles_checked": len(profiles),
        "dimensions_per_profile": len(dimensions),
        **summary,
        "all_profiles_have_explicit_nonpromotion_status": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
