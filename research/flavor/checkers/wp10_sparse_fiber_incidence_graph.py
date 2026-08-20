"""Finite source-defined incidence graph on the 61-point flavor fiber.

Only two predeclared generator types are admitted:
  (1) S3^3 transport inside one oriented orbit and one phase sheet;
  (2) certified same-chart multisheet continuation.

Arbitrary U(3)^3 equivalence is deliberately excluded: it would make the
graph complete and erase the sparse presentation geometry being tested.
"""
from collections import defaultdict
import json
import sys

import numpy as np

sys.path.insert(0, "research/flavor/checkers")
from wp7_ensemble import SIGMA, build_texture, observables17

ENSEMBLE = "research/flavor/results/wp7_ensemble.json"
OUTPUT = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
PHYS_TOL = 1e-4


def union_find(n, edges):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def join(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for a, b, _ in edges:
        join(a, b)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return sorted(groups.values(), key=lambda g: (len(g), g), reverse=True)


def phase_groups(points, tolerance):
    ordered = sorted(range(len(points)), key=lambda i: points[i]["phi_folded"])
    groups = []
    for i in ordered:
        for group in groups:
            if abs(points[i]["phi_folded"] -
                   points[group[0]]["phi_folded"]) < tolerance:
                group.append(i)
                break
        else:
            groups.append([i])
    labels = {}
    for label, group in enumerate(groups):
        for i in group:
            labels[i] = label
    return groups, labels


def main():
    data = json.load(open(ENSEMBLE))
    points = []
    for orbit in data["orbits"]:
        for record in orbit["viable_minima"]:
            edge = record["phase_edge"]
            theta = np.array(record["log_mags"] + [record["phi"]])
            yu, yd = build_texture(
                *record["member"], edge[0], tuple(edge[1:]), theta)
            points.append({
                "orbit": orbit["orbit_index"],
                "member": record["member"],
                "phase_edge": edge,
                "phi_folded": record["phi_folded"],
                "chi2": record["chi2"],
                "obs": observables17(yu, yd),
            })

    best = min(points, key=lambda p: p["chi2"])
    fiber = [p for p in points if
             np.max(np.abs(p["obs"] - best["obs"]) / SIGMA) <= PHYS_TOL]
    fiber.sort(key=lambda p: (p["phi_folded"], p["orbit"],
                              tuple(p["member"])))

    threshold_audits = {}
    selected = None
    for tolerance in (1e-5, 1e-6, 1e-7):
        groups, labels = phase_groups(fiber, tolerance)
        symmetry_classes = defaultdict(list)
        chart_classes = defaultdict(list)
        for i, point in enumerate(fiber):
            symmetry_classes[(point["orbit"], labels[i])].append(i)
            chart_classes[(point["orbit"], tuple(point["member"]),
                           tuple(point["phase_edge"]))].append(i)

        edges = []
        # A spanning tree is enough to encode each declared symmetry class.
        for members in symmetry_classes.values():
            for a, b in zip(sorted(members), sorted(members)[1:]):
                edges.append((
                    a, b, "maximal_declared_s3_cubed_orbit_phase_closure"))
        for members in chart_classes.values():
            ordered = sorted(members, key=lambda i: fiber[i]["phi_folded"])
            for a, b in zip(ordered, ordered[1:]):
                if labels[a] != labels[b]:
                    edges.append((a, b, "same_chart_multisheet_continuation"))

        components = union_find(len(fiber), edges)
        audit = {
            "phase_group_count": len(groups),
            "declared_symmetry_class_count": len(symmetry_classes),
            "same_chart_multisheet_edge_count": sum(
                kind == "same_chart_multisheet_continuation"
                for _, _, kind in edges),
            "minimal_generator_edge_count": len(edges),
            "connected_component_count": len(components),
            "component_sizes": [len(c) for c in components],
        }
        threshold_audits[str(tolerance)] = audit
        if tolerance == 1e-6:
            selected = (groups, labels, edges, components,
                        symmetry_classes, chart_classes)

    groups, labels, edges, components, symmetry_classes, _ = selected
    vertices = [{
        "id": i,
        "orbit": p["orbit"],
        "member": p["member"],
        "phase_edge": p["phase_edge"],
        "phi_folded": p["phi_folded"],
        "phase_group": labels[i],
    } for i, p in enumerate(fiber)]
    component_packet = [{
        "size": len(component),
        "phase_groups": sorted({labels[i] for i in component}),
        "orbits": sorted({fiber[i]["orbit"] for i in component}),
        "vertices": component,
    } for component in components]

    out = {
        "schema": "marici.flavor.sparse_fiber_incidence_graph.v1",
        "strength": "finite_numerical_incidence_census",
        "source": ENSEMBLE,
        "fiber_convention": {
            "physical_tolerance_sigma": PHYS_TOL,
            "phase_group_tolerance": 1e-6,
        },
        "vertex_count": len(fiber),
        "phase_group_count": len(groups),
        "declared_symmetry_class_count": len(symmetry_classes),
        "generator_types": [
            "maximal_declared_s3_cubed_orbit_phase_closure",
            "same_chart_multisheet_continuation",
        ],
        "edges": [{"source": a, "target": b, "kind": kind}
                  for a, b, kind in edges],
        "connected_component_count": len(components),
        "component_sizes": [len(c) for c in components],
        "components": component_packet,
        "vertices": vertices,
        "threshold_stability": threshold_audits,
        "conservative_scope": (
            "same-orbit/same-phase points are joined without requiring an "
            "individual parameter-transport certificate; this maximizes the "
            "declared S3^3 closure, so disconnectedness cannot be caused by "
            "under-counting those symmetry arrows"),
        "minimum_additional_edges_for_connectedness": len(components) - 1,
        "deliberate_exclusion": (
            "arbitrary full-U(3)^3 arrows are not source-defined sparse "
            "incidences and would tautologically complete the graph"),
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps({
        "vertex_count": out["vertex_count"],
        "phase_group_count": out["phase_group_count"],
        "minimal_generator_edge_count": len(edges),
        "connected_component_count": out["connected_component_count"],
        "component_sizes": out["component_sizes"],
        "threshold_stability": out["threshold_stability"],
    }, indent=2))


if __name__ == "__main__":
    main()
