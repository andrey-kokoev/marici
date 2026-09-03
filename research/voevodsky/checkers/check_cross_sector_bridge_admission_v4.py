from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/cross-sector-bridge-admission-registry-v4.json")
MARKOV = Path("research/voevodsky/results/five_sort_markov_analytic_section.json")
ASPECT_NEAR = Path("research/voevodsky/results/aspect_markov_route_gram_overlap.json")
EDGE_V2 = Path("research/voevodsky/results/sector_overlap_edge_contract_v2.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    markov = json.loads(MARKOV.read_text(encoding="utf-8"))
    aspect = json.loads(ASPECT_NEAR.read_text(encoding="utf-8"))
    edge_v2 = json.loads(EDGE_V2.read_text(encoding="utf-8"))
    assert all(result["passed"] is True for result in [markov, aspect, edge_v2])
    vertices = registry["admitted_vertices"]
    assert [vertex["id"] for vertex in vertices] == ["metric_transition_markov", "aspect_optical_route_frame"]
    assert markov["object_sort_count"] == 5
    assert aspect["left_sector_vertex_admitted"] is True
    assert aspect["aspect_gram_exact"] is True
    assert aspect["common_object_sort"] == "finite_green"
    assert aspect["physical_overlap_claimed"] is False

    assert registry["admitted_edges"] == []
    near = registry["near_edges"][0]
    assert near["admitted"] is False
    assert aspect["typed_cross_sector_edge_admitted"] is False
    assert aspect["source_derived_label_correspondence"] is False
    assert edge_v2["false_edge_promotion_repaired"] is True

    census = registry["census"]
    vertices_count = len(vertices)
    edges_count = len(registry["admitted_edges"])
    components = census["connected_components"]
    cycle_rank = edges_count - vertices_count + components
    assert (vertices_count, edges_count, components, cycle_rank) == (2, 0, 2, 0)
    assert census["cycle_rank"] == cycle_rank
    assert census["triangles"] == census["mixed_horns"] == 0

    result = {
        "schema": "marici.voevodsky.cross-sector-bridge-admission-check.v4",
        "status": "two_vertex_zero_edge_census_verified",
        "admitted_sector_vertices": vertices_count,
        "admitted_cross_sector_edges": edges_count,
        "connected_components": components,
        "cycle_rank": cycle_rank,
        "near_edges": len(registry["near_edges"]),
        "aspect_finite_green_vertex_admitted": True,
        "aspect_markov_edge_admitted": False,
        "identity_provenance_gate_active": True,
        "mixed_horns": 0,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
