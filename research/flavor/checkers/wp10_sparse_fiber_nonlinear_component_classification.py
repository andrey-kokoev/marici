"""Classify components of the surviving all-strict nonlinear edge graph."""
from collections import defaultdict
import json

CONTINUATION = (
    "research/flavor/results/"
    "wp10_sparse_fiber_all_strict_normal_continuation.json")
INCIDENCE = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
OUTPUT = (
    "research/flavor/results/"
    "wp10_sparse_fiber_nonlinear_component_classification.json")


def main():
    continuation = json.load(open(CONTINUATION))
    incidence = json.load(open(INCIDENCE))
    parent = list(range(len(incidence["components"])))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    survivors = []
    for audit in continuation["audits"]:
        if not (
            audit["termination"] == "depth_ten_reached"
            and audit["nominated_target_edge_is_minimum_at_end"]
            and abs(audit["finite_depth_target_normal_slope"]+1) < 0.25
        ):
            continue
        a, b = audit["source_component"], audit["target_component"]
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
        survivors.append((a, b))
    groups = defaultdict(list)
    for component in range(len(parent)):
        groups[find(component)].append(component)
    classified = []
    vertex_by_id = {
        vertex["id"]: vertex for vertex in incidence["vertices"]}
    for group in sorted(groups.values(), key=lambda g: (len(g), g),
                        reverse=True):
        vertex_ids = sorted(
            vertex for component in group
            for vertex in incidence["components"][component]["vertices"])
        classified.append({
            "size": len(group),
            "input_components": group,
            "orbits": sorted({
                orbit for component in group
                for orbit in incidence["components"][component]["orbits"]}),
            "phase_groups": sorted({
                phase for component in group
                for phase in
                incidence["components"][component]["phase_groups"]}),
            "vertex_count": sum(
                incidence["components"][component]["size"]
                for component in group),
            "phase_values": sorted({
                vertex_by_id[vertex]["phi_folded"] for vertex in vertex_ids}),
            "vertices": [{
                "id": vertex,
                "orbit": vertex_by_id[vertex]["orbit"],
                "member": vertex_by_id[vertex]["member"],
                "phase_edge": vertex_by_id[vertex]["phase_edge"],
                "phi_folded": vertex_by_id[vertex]["phi_folded"],
            } for vertex in vertex_ids],
        })
    out = {
        "schema": (
            "marici.flavor.sparse_fiber_nonlinear_components.v1"),
        "strength": "bounded_numerical_depth_ten_graph_classification",
        "sources": [CONTINUATION, INCIDENCE],
        "surviving_edge_count": len(set(
            tuple(sorted(edge)) for edge in survivors)),
        "component_count": len(classified),
        "component_sizes": [group["size"] for group in classified],
        "components": classified,
        "scope": (
            "classification is relative to depth ten, the 5-percent "
            "infinitesimal prefilter, and the 25-percent finite-slope gate"),
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
