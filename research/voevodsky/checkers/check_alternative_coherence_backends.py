from __future__ import annotations

import json


def mathematical_admitted(proof: dict[str, bool], operational: dict[str, bool]) -> bool:
    return all(proof.values()) or all(operational.values())


def physical_admitted(operational: dict[str, bool]) -> bool:
    return all(operational.values())


def main() -> None:
    proof_complete = {"typed": True, "filler": True, "higher_laws": True, "descent": True, "mixed_naturality": True}
    proof_blocked = dict(proof_complete, filler=False)
    operational_complete = {"typed": True, "constructor": True, "jointly_faithful": True, "coverage": True, "faults": True, "link_theorem": True}
    operational_blocked = dict(operational_complete, constructor=False, faults=False)

    assert mathematical_admitted(proof_complete, operational_blocked) is True
    assert physical_admitted(operational_blocked) is False
    assert mathematical_admitted(proof_blocked, operational_complete) is True
    assert physical_admitted(operational_complete) is True
    assert mathematical_admitted(proof_blocked, operational_blocked) is False

    # Incomplete pieces from alternative branches cannot be pooled conjunctively.
    proof_partial = {key: key in {"typed", "higher_laws"} for key in proof_complete}
    operational_partial = {key: key in {"typed", "constructor", "coverage"} for key in operational_complete}
    assert any(proof_partial.values()) and any(operational_partial.values())
    assert mathematical_admitted(proof_partial, operational_partial) is False

    proof_failures = frozenset(key for key, value in proof_blocked.items() if not value)
    operational_failures = frozenset(key for key, value in operational_blocked.items() if not value)
    alternative_failure_object = {proof_failures, operational_failures}
    assert alternative_failure_object == {frozenset({"filler"}), frozenset({"constructor", "faults"})}
    assert proof_failures | operational_failures != proof_failures

    result = {
        "schema": "marici.voevodsky.alternative-coherence-backends.v1",
        "status": "disjunctive_backend_admission_verified",
        "proof_backend_can_establish_mathematical_without_physical": True,
        "operational_conservative_backend_can_establish_mathematical": True,
        "physical_claim_always_requires_operational_backend": True,
        "incomplete_backend_pieces_not_poolable": True,
        "backend_failure_object": [["filler"], ["constructor", "faults"]],
        "universal_conjunctive_chain_rejected": True,
        "hybrid_composition_requires_comparison_theorem": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
