from __future__ import annotations

import json
from pathlib import Path


SIGNATURE = Path("research/voevodsky/coherence-pyramid-computad-signature.json")
CELLS = Path("research/voevodsky/coherence-pyramid-cells-and-laws.json")
OVERLAY = Path("research/voevodsky/coherence-pyramid-overlay-registry-v3.json")


def main() -> None:
    signature = json.loads(SIGNATURE.read_text(encoding="utf-8"))
    cells = json.loads(CELLS.read_text(encoding="utf-8"))
    overlay = json.loads(OVERLAY.read_text(encoding="utf-8"))

    object_sorts = sorted(signature["object_sorts"])
    arrow_key = next(key for key in signature if key not in {"schema", "object_sorts", "certificate_sorts"})
    arrows = signature[arrow_key]
    arrow_names = sorted(arrows)
    edge_boundaries = {name: [data["source_sort"], data["target_sort"]] for name, data in arrows.items()}
    assert all(source in object_sorts and target in object_sorts for source, target in edge_boundaries.values())
    adjacency = {name: set() for name in object_sorts}
    for source, target in edge_boundaries.values():
        adjacency[source].add(target)
        adjacency[target].add(source)
    unseen = set(object_sorts)
    components = []
    while unseen:
        frontier = {unseen.pop()}
        component = set(frontier)
        while frontier:
            node = frontier.pop()
            fresh = adjacency[node] - component
            component |= fresh
            frontier |= fresh
            unseen -= fresh
        components.append(sorted(component))
    components.sort()
    assert components == [["carrier", "gauge_presentation"], ["closed_form"], ["finite_green"], ["quotient_form"]]

    cell_names = sorted(cells["cells"])
    law_key = next(key for key in cells if key not in {"schema", "cells"})
    laws = cells[law_key]
    law_names = sorted(laws)

    # Current realization census: signature generators are presentation-level;
    # only the analytic Markov subnerve has a verified equipment realization.
    realization = {
        "presentation_vertices": len(object_sorts),
        "presentation_edges": len(arrow_names),
        "presentation_cell_classes": len(cell_names),
        "presentation_law_classes": len(law_names),
        "analytic_subnerve_verified": overlay["global_status"]["analytic_markov_equipment_fragment_verified"],
        "cross_sector_global_section_verified": overlay["global_status"]["cross_sector_global_section_verified"],
    }
    assert realization["analytic_subnerve_verified"] is True
    assert realization["cross_sector_global_section_verified"] is False

    # Every presentation cell is an obstruction-census row until a sourced
    # realization and its law certificate are linked.
    census_rows = [{"cell_class": name, "realization_status": "presentation_only_outside_verified_subnerve"} for name in cell_names]
    assert len(census_rows) == len(cell_names)

    result = {
        "schema": "marici.voevodsky.pyramid-nerve-obstruction-census.v1",
        "status": "presentation_nerve_census_verified",
        "object_sorts": object_sorts,
        "arrow_container": arrow_key,
        "arrow_names": arrow_names,
        "edge_boundaries": edge_boundaries,
        "cell_names": cell_names,
        "law_container": law_key,
        "law_names": law_names,
        "one_skeleton_components": components,
        "one_skeleton_connected": False,
        "closed_form_incident_one_generator": False,
        "realization": realization,
        "cell_census": census_rows,
        "presentation_is_global_realization": False,
        "passed": True,
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
