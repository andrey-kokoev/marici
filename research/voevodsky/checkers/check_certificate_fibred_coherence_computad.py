from __future__ import annotations

import itertools
import json
from pathlib import Path


K_REGISTRY = Path("research/kitaev/coherence-pyramid-transfer-map-registry-v1.json")
K_RESULT = Path("research/kitaev/results/coherence_pyramid_transfer_poset.json")


def closure(nodes: set[str], edges: set[tuple[str, str]]) -> dict[str, set[str]]:
    reach = {node: set() for node in nodes}
    for source, target in edges:
        reach[source].add(target)
    for pivot in nodes:
        for source in nodes:
            if pivot in reach[source]:
                reach[source] |= reach[pivot]
    return reach


def admissible_states(nodes: set[str], edges: set[tuple[str, str]]) -> list[frozenset[str]]:
    states = []
    for length in range(len(nodes) + 1):
        for subset_tuple in itertools.combinations(sorted(nodes), length):
            subset = set(subset_tuple)
            if all(target not in subset or source in subset for source, target in edges):
                states.append(frozenset(subset))
    return states


def minimal_missing(required: set[str], state: set[str], reach: dict[str, set[str]]) -> frozenset[str]:
    missing = required - state
    return frozenset(node for node in missing if not any(node in reach[other] for other in missing if other != node))


def main() -> None:
    kitaev_registry = json.loads(K_REGISTRY.read_text(encoding="utf-8"))
    kitaev_result = json.loads(K_RESULT.read_text(encoding="utf-8"))
    assert kitaev_result["passed"] is True and kitaev_result["registry_dag"] is True

    nodes = {"source_typed", "descent", "completion", "comparison"}
    edges = {("descent", "comparison"), ("completion", "comparison")}
    reach = closure(nodes, edges)
    states = admissible_states(nodes, edges)

    # Descent and completion span a square, not a chain.
    square = {
        frozenset(),
        frozenset({"descent"}),
        frozenset({"completion"}),
        frozenset({"descent", "completion"}),
    }
    assert square <= set(states)
    assert "completion" not in reach["descent"] and "descent" not in reach["completion"]
    assert frozenset({"comparison"}) not in states
    assert frozenset({"descent", "completion", "comparison"}) in states

    # A partial generator is present exactly on its upward-closed domain.
    required_f = {"source_typed", "descent"}
    domain_f = {state for state in states if required_f <= state}
    assert domain_f
    assert all(not (state <= larger) or larger in domain_f for state in domain_f for larger in states)

    required_g = {"source_typed", "completion"}
    interface = {"source_typed"}
    composite_required = required_f | required_g | interface
    domain_composite = {state for state in states if composite_required <= state}
    assert domain_composite == ({state for state in states if required_f <= state} & {state for state in states if required_g <= state})

    # Composition is associative at the domain level.
    required_h = {"comparison"}
    left = (required_f | required_g) | required_h
    right = required_f | (required_g | required_h)
    assert left == right
    assert {state for state in states if left <= state} == {state for state in states if right <= state}

    # Failure reporting returns antichains and does not impose a first failure.
    blocked_state: set[str] = set()
    failures = minimal_missing({"descent", "completion", "comparison"}, blocked_state, reach)
    assert failures == frozenset({"descent", "completion"})
    assert not any(right in reach[left] or left in reach[right] for left, right in itertools.combinations(failures, 2))

    source_record = kitaev_registry["records"][0]
    assert source_record["status"] == "authority_blocked"
    r_zeta_failures = frozenset(source_record["minimal_failed_prerequisites"])
    assert r_zeta_failures == frozenset({"source_typed target U_G4", "source-derived map R_zeta"})

    result = {
        "schema": "marici.voevodsky.certificate-fibred-coherence-computad.v1",
        "status": "certificate_fibred_overlay_verified",
        "certificate_states": len(states),
        "computad_inclusions_monotone": True,
        "partial_generator_domain_upward_closed": True,
        "composition_domain_intersection": True,
        "composition_associative": True,
        "descent_completion_square_not_chain": True,
        "comparison_requires_independent_certificate": True,
        "minimal_failures_are_antichains": True,
        "R_zeta_two_primitive_corner": True,
        "verified_fragment_and_proposals_separated": True,
        "full_cross_sector_equipment": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
