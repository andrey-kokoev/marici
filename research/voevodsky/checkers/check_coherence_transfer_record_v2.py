from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/coherence-transfer-record-contract-v2.json")
RECORD = Path("research/voevodsky/kitaev-associator-loop-partial-representation-v2.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert set(contract["required"]) <= set(record)
    assert set(record) <= set(contract["properties"])

    poset = record["certificate_dependency_poset"]
    nodes = set(poset["predicates"])
    edges = {tuple(edge) for edge in poset["edges"]}
    assert all(source in nodes and target in nodes and source != target for source, target in edges)
    reach = {node: set() for node in nodes}
    for source, target in edges:
        reach[source].add(target)
    for pivot in nodes:
        for source in nodes:
            if pivot in reach[source]:
                reach[source] |= reach[pivot]
    assert all(node not in reach[node] for node in nodes)

    backends = {backend["backend_id"]: backend for backend in record["evidence_backends"]}
    assert set(backends) == {"direct_proof", "operational_conservative_detection"}
    for backend in backends.values():
        requirements = set(backend["requirements"])
        satisfied = set(backend["satisfied"])
        failures = set(backend["minimal_failures"])
        assert satisfied <= requirements
        assert failures <= requirements - satisfied

    bundles = [frozenset(bundle) for bundle in record["minimal_repair_bundles"]]
    assert not any(left < right or right < left for i, left in enumerate(bundles) for right in bundles[i + 1:])
    assert bundles[0] == frozenset({"explicit_horn_filler", "higher_coherence"})
    assert "physical_controlled_cycle" in bundles[1] and "fault_independence" in bundles[1]

    assert record["map_status"] == "partially_constructed"
    assert record["physical_status"] == "blocked"
    assert "-1/8" in record["demonstrated_strength"]
    assert "global gluing verified" in record["prohibited_interpretations"]
    assert "direct_proof OR operational_conservative_detection" in record["admission_formula"]

    result = {
        "schema": "marici.voevodsky.coherence-transfer-record-v2-check.v1",
        "status": "alternative_backend_transfer_record_verified",
        "contract_required_fields_present": True,
        "certificate_dependencies_DAG": True,
        "backend_requirements_separate": True,
        "repair_bundles_incomparable": True,
        "algebraic_strength_preserved": True,
        "physical_block_preserved": True,
        "global_gluing_nonpromotion_preserved": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
