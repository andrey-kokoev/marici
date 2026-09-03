from __future__ import annotations

import itertools
import json
from pathlib import Path


V1 = Path("research/voevodsky/r-zeta-u-g4-transfer-record-candidate-v1.json")
V2 = Path("research/voevodsky/r-zeta-u-g4-transfer-record-v2.json")
K_REGISTRY = Path("research/kitaev/coherence-pyramid-transfer-map-registry-v1.json")


def main() -> None:
    v1 = json.loads(V1.read_text(encoding="utf-8"))
    v2 = json.loads(V2.read_text(encoding="utf-8"))
    kitaev = json.loads(K_REGISTRY.read_text(encoding="utf-8"))["records"][0]

    assert v2["source"] == kitaev["source"] == "S_zeta^labels"
    assert v2["target"] == kitaev["target"] == "U_G4"
    assert v2["interface_descriptor"]["proposed_map_label"] == "R_zeta"
    assert v2["map_status"] == "authority_blocked"
    assert v2["physical_status"] == "not_applicable"

    poset = v2["certificate_dependency_poset"]
    nodes = set(poset["predicates"])
    edges = {tuple(edge) for edge in poset["edges"]}
    reach = {node: set() for node in nodes}
    for source, target in edges:
        reach[source].add(target)
    for pivot in nodes:
        for source in nodes:
            if pivot in reach[source]:
                reach[source] |= reach[pivot]
    assert all(node not in reach[node] for node in nodes)

    primitive_failures = frozenset(v2["evidence_backends"][0]["minimal_failures"])
    assert primitive_failures == frozenset(v1["minimal_failed_prerequisites"])
    assert primitive_failures == frozenset({"target_source_typed", "map_source_derived"})
    assert not any(right in reach[left] or left in reach[right] for left, right in itertools.combinations(primitive_failures, 2))

    repair_bundle = frozenset(v2["minimal_repair_bundles"][0])
    requirements = frozenset(v2["evidence_backends"][0]["requirements"])
    assert repair_bundle == requirements
    assert primitive_failures < repair_bundle

    # The v2 distinction: primitive current blockers are not the full bundle
    # required to admit the transfer theorem.
    assert "finite_identity" in repair_bundle
    assert "finite_identity" not in primitive_failures
    assert "completion verified" in v2["prohibited_interpretations"]

    result = {
        "schema": "marici.voevodsky.r-zeta-transfer-record-v2-check.v1",
        "status": "conjunctive_transfer_migration_verified",
        "Kitaev_registry_identity_preserved": True,
        "dependency_DAG_preserved": True,
        "primitive_failure_antichain_preserved": True,
        "full_repair_bundle_distinguished": True,
        "physical_not_applicable_preserved": True,
        "completion_nonpromotion_preserved": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
