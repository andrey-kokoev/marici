from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/coherence-pyramid-analytic-fragment-registry-v2.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    evidence = [json.loads(Path(path).read_text(encoding="utf-8")) for path in registry["evidence"]]
    assert len(evidence) == 10
    assert all(result["passed"] is True for result in evidence)

    path = registry["path_sector"]
    assert path["finite_fibers"] == "varying dimensions admitted"
    assert "ordered-subset source-derived restriction" in path["horizontal_arrows"]
    assert path["descent"].startswith("faithful orthogonal quotient")
    assert path["completion"].startswith("uniform normalized contraction")

    branch = registry["branch_sector"]
    assert branch["completion"] is None
    assert "rooted" in branch["objects"]

    partial = registry["partial_pyramid_representations"]
    kitaev_registry = json.loads(Path(partial["registry"]).read_text(encoding="utf-8"))
    kitaev_result = json.loads(Path(partial["checker_result"]).read_text(encoding="utf-8"))
    assert kitaev_result["passed"] is True and kitaev_result["registry_dag"] is True
    assert partial["linear_certificate_chain_rejected"] is True
    assert partial["descent_and_completion_independent"] is True
    assert partial["current_record"]["included_as_analytic_evidence"] is False
    source_record = kitaev_registry["records"][0]
    assert partial["current_record"]["source"] == source_record["source"]
    assert partial["current_record"]["target"] == source_record["target"]
    assert partial["current_record"]["status"] == source_record["status"]
    assert set(partial["current_record"]["minimal_failed_prerequisites"]) == set(source_record["minimal_failed_prerequisites"])

    scope = registry["global_scope"]
    assert scope["analytic_fragment_verified"] is True
    assert scope["full_cross_sector_partial_double_category"] is False
    assert scope["full_cross_sector_equipment"] is False
    assert scope["transfer_certificate_dependencies"] == "DAG, not universal chain"

    required_refusals = {
        "pointwise contraction without uniform or alternative Schur certificate",
        "unbounded metric family",
        "unbounded GL arrow or inverse at completion",
        "naive noncontiguous retained-edge list",
        "duplicate or reversed ordered-subset map",
        "rooted-tree cycle",
        "conflicting parent assignment",
        "arbitrary cyclic graph amalgamation"
    }
    assert set(registry["refusals"]) == required_refusals

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-analytic-fragment-registry-check.v2",
        "status": "expanded_analytic_fragment_registry_verified",
        "evidence_documents_passed": len(evidence),
        "varying_fiber_path_equipment": True,
        "metric_transition_descent_and_completion": True,
        "ordered_subset_beck_chevalley": True,
        "finite_rooted_branch_amalgamation": True,
        "partial_pyramid_representation_projection": True,
        "partial_representation_separated_from_analytic_evidence": True,
        "certificate_dependency_DAG": True,
        "refusal_boundary_complete_for_registry": True,
        "cross_sector_nonpromotion_verified": True,
        "full_cross_sector_equipment": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
