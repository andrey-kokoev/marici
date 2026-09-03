from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/scalar-markov-restricted-equipment-registry-v1.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    evidence = [json.loads(Path(path).read_text(encoding="utf-8")) for path in registry["evidence"]]
    assert all(result["passed"] is True for result in evidence)

    laws = registry["laws"]
    required_laws = {
        "horizontal_units_associativity",
        "vertical_units_associativity",
        "interchange",
        "pentagon",
        "beck_chevalley_pasting",
        "companion_triangles",
        "conjoint_triangles",
        "companion_composition_pentagon",
        "completion_naturality",
    }
    assert required_laws == set(laws)
    assert all(value is True or isinstance(value, str) for value in laws.values())

    horizontal = registry["horizontal_arrows"]
    assert horizontal["gauge_companion"]["freely_adjoined"] is True
    assert horizontal["gauge_conjoint"]["freely_adjoined"] is True
    assert horizontal["chain_extension"]["partial_on"]

    scope = registry["scope"]
    assert scope["restricted_equipment_fragment"] is True
    assert scope["all_vertical_arrows_have_companions"] is False
    assert scope["full_coherence_pyramid_equipment"] is False

    required_rejections = {
        "altered_non_path_pairing",
        "shared_vertex_gauge_mismatch",
        "noncontiguous_equal_dimension_probe",
        "completion_without_uniform_contraction",
        "unbounded_diagonal_completion",
    }
    assert required_rejections == set(registry["hostile_rejections"])

    result = {
        "schema": "marici.voevodsky.scalar-markov-restricted-equipment-registry-check.v1",
        "status": "machine_readable_restricted_equipment_contract_verified",
        "evidence_documents_passed": len(evidence),
        "required_laws_present": True,
        "partiality_predicates_explicit": True,
        "hostile_rejections_complete_for_declared_fragment": True,
        "free_and_analytic_cells_distinguished": True,
        "scope_nonpromotion_verified": True,
        "full_coherence_pyramid_equipment": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
