from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


LAYER = Path("research/voevodsky/filler-fiber-selection-layer-v1.json")
RH = Path("research/voevodsky/results/rh_modular_filling_invariance.json")
MARKOV = Path("research/voevodsky/results/markov_amalgamation_pentagon_horn.json")


def edge_boundary(chain: dict[tuple[str, str], int]) -> dict[str, int]:
    out: defaultdict[str, int] = defaultdict(int)
    for (left, right), coefficient in chain.items():
        out[left] -= coefficient
        out[right] += coefficient
    return {key: value for key, value in out.items() if value}


def main() -> None:
    layer = json.loads(LAYER.read_text(encoding="utf-8"))
    rh = json.loads(RH.read_text(encoding="utf-8"))
    markov = json.loads(MARKOV.read_text(encoding="utf-8"))
    assert rh["passed"] is True and markov["passed"] is True
    assert set(layer["object_sorts"]) == {"boundary_datum", "filler", "relative_class", "completed_filler"}
    assert layer["constructors"]["selection"]["partial"] is True
    assert layer["constructors"]["completion"]["partial"] is True

    direct = {("w", "-w"): 1}
    detour = {("w", "a"): 1, ("a", "-w"): 1}
    triangle_boundary = {("a", "-w"): 1, ("w", "-w"): -1, ("w", "a"): 1}
    assert edge_boundary(direct) == edge_boundary(detour)
    difference = {edge: detour.get(edge, 0) - direct.get(edge, 0) for edge in set(direct) | set(detour)}
    assert difference == triangle_boundary
    assert edge_boundary(triangle_boundary) == {}
    assert direct != detour

    dependencies = layer["certificate_dependencies"]
    graph = {name: {item for item in items if item in dependencies} for name, items in dependencies.items()}
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        assert node not in visiting
        if node in visited:
            return
        visiting.add(node)
        for child in graph[node]:
            visit(child)
        visiting.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)

    assert markov["filler_unique_in_faithful_ordered_list_coordinate"] is True
    assert rh["relative_class_determined_by_endpoint_incidence"] is True
    assert rh["strict_chain_representative_determined"] is False
    assert rh["completed_filler_verified"] is False

    result = {
        "schema": "marici.voevodsky.filler-fiber-selection-layer-check.v1",
        "status": "conservative_filler_layer_verified",
        "new_object_sorts": 4,
        "new_cell_classes": len(layer["cells"]),
        "certificate_DAG_acyclic": True,
        "equal_boundary_distinct_fillers_witnessed": True,
        "difference_is_d2_boundary": True,
        "relative_class_and_selection_separated": True,
        "selection_and_completion_separated": True,
        "markov_singleton_fiber_instance_preserved": True,
        "RH_nonunique_chain_instance_preserved": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
