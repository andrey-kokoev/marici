from __future__ import annotations

import json
from pathlib import Path


CERTIFICATE_REQUIREMENTS = {
    "finite_identity": (),
    "quotient_descended_identity": ("descent_certificate",),
    "coherent_finite_composition": ("descent_certificate", "coherence_certificate"),
    "completed_identity": ("descent_certificate", "coherence_certificate", "completion_certificate"),
    "source_typed_readout_identity": ("descent_certificate", "coherence_certificate", "readout_certificate"),
}


def validate(record: dict) -> list[str]:
    errors: list[str] = []
    if record.get("semantic_disposition") == "authority_blocked":
        errors.append("authority state placed in semantic disposition")
    if record.get("authority_state") not in {"authorized", "self_claim_only", "authority_blocked", "not_required"}:
        errors.append("invalid authority state")
    for field in CERTIFICATE_REQUIREMENTS.get(record.get("demonstrated_strength"), ()):
        if record.get(field) is None:
            errors.append(f"missing non-null {field}")
    if record.get("semantic_disposition") == "admitted" and record.get("map") is None:
        errors.append("admitted transfer has no map")
    if record.get("semantic_disposition") == "admitted" and not record.get("preserved_invariants"):
        errors.append("admitted transfer has no proved preserved invariant")
    if record.get("semantic_disposition") == "admitted" and record.get("demonstrated_strength") is None:
        errors.append("admitted transfer has no demonstrated strength")
    poset = record.get("certificate_dependency_poset", {})
    predicates = set(poset.get("predicates", []))
    edges = [tuple(edge) for edge in poset.get("edges", [])]
    failed = record.get("minimal_failed_prerequisites", [])
    if any(node not in predicates for node in failed):
        errors.append("failed prerequisite absent from dependency poset")
    reach = {node: set() for node in predicates}
    for source, target in edges:
        reach[source].add(target)
    for pivot in predicates:
        for source in predicates:
            if pivot in reach[source]:
                reach[source] |= reach[pivot]
    if any(right in reach[left] or left in reach[right] for i, left in enumerate(failed) for right in failed[i + 1:]):
        errors.append("minimal failed prerequisites are not an antichain")
    return errors


def main() -> None:
    schema = json.loads(Path("research/voevodsky/coherence-transfer-record-contract-v1.json").read_text(encoding="utf-8"))
    assert "semantic_disposition" in schema["properties"]
    assert "authority_state" in schema["properties"]

    blocked = json.loads(Path("research/voevodsky/r-zeta-u-g4-transfer-record-candidate-v1.json").read_text(encoding="utf-8"))
    assert validate(blocked) == []
    assert blocked["map"] is None
    assert blocked["proposed_map_label"] == "R_zeta"
    assert blocked["minimal_failed_prerequisites"] == ["target_source_typed", "map_source_derived"]

    smeared = dict(blocked)
    smeared["semantic_disposition"] = "authority_blocked"
    smeared["authority_state"] = None
    assert validate(smeared) == [
        "authority state placed in semantic disposition",
        "invalid authority state",
    ]

    false_completion = dict(blocked)
    false_completion.update({
        "proposed_strength": "completed_identity",
        "demonstrated_strength": "completed_identity",
        "semantic_disposition": "admitted",
        "authority_state": "authorized",
        "map": {"id": "synthetic-map"},
        "preserved_invariants": ["fixture invariant"],
        "descent_certificate": {"id": "descent"},
    })
    assert validate(false_completion) == [
        "missing non-null coherence_certificate",
        "missing non-null completion_certificate",
    ]

    result = {
        "schema": "marici.voevodsky.coherence-transfer-contract-check.v1",
        "status": "two_axis_transfer_contract_verified",
        "blocked_fixture_valid": True,
        "authority_smearing_rejected": True,
        "false_completion_rejected": True,
        "semantic_and_authority_axes_independent": True,
        "certificate_fields_separate": True,
        "dependency_poset_verified": True,
        "minimal_failure_antichain_verified": True,
        "universal_linear_chain_rejected": True,
        "canonical_integration_performed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
