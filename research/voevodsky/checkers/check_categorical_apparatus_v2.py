from __future__ import annotations

import json
from pathlib import Path


MANIFEST = Path("research/voevodsky/coherence-pyramid-categorical-apparatus-v2.json")
RESULTS = [
    Path("research/voevodsky/results/filler_layer_conservative_extension.json"),
    Path("research/voevodsky/results/filler_layer_minimality.json"),
    Path("research/voevodsky/results/bounded_categorical_completeness.json"),
    Path("research/voevodsky/results/typed_horn_obstruction_tower_status.json"),
    Path("research/voevodsky/results/sector_overlap_edge_contract.json"),
]


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    layers = {layer["id"]: layer for layer in manifest["layers"]}
    assert len(layers) == 8
    assert set(layers) == {"base_computad", "cells_and_laws", "partial_completion", "filler_fiber_selection", "certificate_transfer", "sector_overlap", "horn_tower", "bounded_completeness"}

    schemas: dict[str, str] = {}
    for layer in layers.values():
        path = Path(layer["artifact"])
        assert path.exists()
        document = json.loads(path.read_text(encoding="utf-8"))
        schema = document.get("schema", document.get("$id"))
        assert schema is not None, str(path)
        assert schema not in schemas, (schema, schemas[schema], str(path))
        schemas[schema] = str(path)
        assert all(dependency in layers for dependency in layer["depends_on"])

    visiting: set[str] = set()
    visited: set[str] = set()
    order: list[str] = []
    def visit(node: str) -> None:
        assert node not in visiting
        if node in visited:
            return
        visiting.add(node)
        for dependency in layers[node]["depends_on"]:
            visit(dependency)
        visiting.remove(node)
        visited.add(node)
        order.append(node)
    for node in layers:
        visit(node)
    assert order.index("base_computad") < order.index("bounded_completeness")
    assert order.index("sector_overlap") < order.index("horn_tower")

    results = [json.loads(path.read_text(encoding="utf-8")) for path in RESULTS]
    assert all(result["passed"] is True for result in results)
    completeness = results[2]
    horn = results[3]
    edge = results[4]
    assert completeness["markov_degree_4_declared_law_completeness"] is True
    assert edge["admitted_edges"] == 0
    assert horn["cross_sector_higher_obstructions_defined"] is False

    output = {
        "schema": "marici.voevodsky.coherence-pyramid-categorical-apparatus-check.v2",
        "status": "canonical_layered_manifest_verified",
        "layers": len(layers),
        "artifact_schemas_unique": True,
        "layer_dependency_DAG_acyclic": True,
        "topological_order": order,
        "supporting_results_passed": len(results),
        "markov_bounded_realization": True,
        "cross_sector_edge_realized": False,
        "unbounded_global_claim": False,
        "passed": True,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
