from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SIGNATURE = Path("research/voevodsky/coherence-pyramid-computad-signature.json")
COMPLETION = Path("research/voevodsky/coherence-pyramid-completion-interface.json")
COMPOSITION = Path("research/voevodsky/coherence-pyramid-partial-composition.json")


def strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in strings(item)]
    if isinstance(value, dict):
        return [text for key, item in value.items() for text in [key, *strings(item)]]
    return []


def components(nodes: set[str], hyperedges: list[set[str]]) -> list[list[str]]:
    adjacency = {node: set() for node in nodes}
    for edge in hyperedges:
        for left in edge:
            adjacency[left] |= edge - {left}
    unseen = set(nodes)
    result = []
    while unseen:
        frontier = {unseen.pop()}
        component = set(frontier)
        while frontier:
            node = frontier.pop()
            fresh = adjacency[node] - component
            component |= fresh
            frontier |= fresh
            unseen -= fresh
        result.append(sorted(component))
    return sorted(result)


def main() -> None:
    signature = json.loads(SIGNATURE.read_text(encoding="utf-8"))
    completion = json.loads(COMPLETION.read_text(encoding="utf-8"))
    composition = json.loads(COMPOSITION.read_text(encoding="utf-8"))
    sorts = set(signature["object_sorts"])
    one_generators = signature["one_generators"]
    one_edges = [{data["source_sort"], data["target_sort"]} for data in one_generators.values()]

    completion_tokens = strings(completion)
    completion_incidence = {sort for sort in sorts if any(sort in token for token in completion_tokens)}
    composition_tokens = strings(composition)
    composition_incidence = {sort for sort in sorts if any(sort in token for token in composition_tokens)}
    assert completion["constructor"] == "complete_finite_form_system"
    assert completion["partial"] is True
    assert completion_incidence == {"finite_green", "closed_form", "quotient_form"}
    assert composition_incidence == {"finite_green", "quotient_form"}

    one_components = components(sorts, one_edges)
    augmented_hyperedges = one_edges + [completion_incidence]
    augmented_components = components(sorts, augmented_hyperedges)
    assert one_components == [["carrier", "gauge_presentation"], ["closed_form"], ["finite_green"], ["quotient_form"]]
    assert augmented_components == [["carrier", "gauge_presentation"], ["closed_form", "finite_green", "quotient_form"]]

    # Completion is a partial hyperedge, not a total one-generator.
    assert completion["constructor"] not in one_generators
    assert len(augmented_components) == 2

    result = {
        "schema": "marici.voevodsky.constructor-augmented-nerve.v1",
        "status": "partial_constructor_incidence_verified",
        "one_skeleton_components": one_components,
        "completion_constructor_incidence": sorted(completion_incidence),
        "composition_module_sort_incidence": sorted(composition_incidence),
        "composition_module_cooccurrence_is_bridge": False,
        "constructor_augmented_components": augmented_components,
        "completion_connects_finite_green_to_closed_form": True,
        "completion_is_total_one_generator": False,
        "completion_connects_quotient_green_closed_component": True,
        "carrier_gauge_component_still_disconnected_from_green_completion": True,
        "global_augmented_nerve_connected": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
