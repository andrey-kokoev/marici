"""Exhaustive tangent normal-response census for shared sparse faces.

For every concrete pair of edge deletions representing one canonical
codimension-one face in distinct prior incidence components, solve the
linearized full-readout transport in both directions.  A candidate ordinary
face identification must transport each logarithmic normal with slope -1
(up to numerical/finite-point correction) and have negligible tangent
readout residual in both directions.
"""
from collections import defaultdict
import json
import sys

import numpy as np

sys.path.insert(0, "research/flavor/checkers")
from wp7_ensemble import SIGMA, build_texture, mask_slots, observables17

ATLAS = "research/flavor/results/wp10_sparse_fiber_face_atlas.json"
INCIDENCE = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
ENSEMBLE = "research/flavor/results/wp7_ensemble.json"
OUTPUT = (
    "research/flavor/results/"
    "wp10_sparse_fiber_normal_response_census.json")
SLOPE_WINDOWS = (0.05, 0.10, 0.20, 0.25)
TANGENT_RESIDUAL_MAX = 1e-6


def labels(member):
    mu, md = member
    return ([('u', *slot) for slot in mask_slots(mu)]
            +[('d', *slot) for slot in mask_slots(md)])


def observable(record, theta):
    edge = record["phase_edge"]
    yu, yd = build_texture(
        *record["member"], edge[0], tuple(edge[1:]), theta)
    return observables17(yu, yd)/SIGMA


def jacobian(record, theta):
    result = np.empty((17, 10))
    for column in range(10):
        step = 2e-6 if column < 9 else 1e-6
        plus, minus = theta.copy(), theta.copy()
        plus[column] += step
        minus[column] -= step
        result[:, column] = (
            observable(record, plus)-observable(record, minus))/(2*step)
    return result


def components_from_edges(n, edges):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return sorted(groups.values(), key=lambda g: (len(g), g), reverse=True)


def main():
    atlas = json.load(open(ATLAS))
    incidence = json.load(open(INCIDENCE))
    ensemble = json.load(open(ENSEMBLE))
    raw = []
    for orbit in ensemble["orbits"]:
        for record in orbit["viable_minima"]:
            raw.append({"orbit": orbit["orbit_index"], **record})

    vertex_component = {}
    for component_id, component in enumerate(incidence["components"]):
        for vertex in component["vertices"]:
            vertex_component[vertex] = component_id

    records, thetas, jacobians, pseudoinverses = {}, {}, {}, {}
    for vertex in incidence["vertices"]:
        candidates = [
            record for record in raw
            if record["orbit"] == vertex["orbit"]
            and record["member"] == vertex["member"]
            and record["phase_edge"] == vertex["phase_edge"]
            and abs(record["phi_folded"]-vertex["phi_folded"]) < 1e-6
        ]
        assert candidates, vertex
        record = min(
            candidates,
            key=lambda r: abs(r["phi_folded"]-vertex["phi_folded"]))
        vid = vertex["id"]
        theta = np.array(record["log_mags"]+[record["phi"]], dtype=float)
        matrix = jacobian(record, theta)
        records[vid], thetas[vid], jacobians[vid] = record, theta, matrix
        pseudoinverses[vid] = np.linalg.pinv(matrix, rcond=1e-10)

    occurrences = defaultdict(list)
    for vertex_text, faces in atlas["vertex_faces"].items():
        vertex = int(vertex_text)
        for face in faces:
            label = (face["sector"], face["row"], face["column"])
            occurrences[face["canonical_face"]].append({
                "vertex": vertex,
                "component": vertex_component[vertex],
                "label": label,
                "parameter_index": labels(
                    records[vertex]["member"]).index(label),
            })

    audits = []
    for face, items in sorted(occurrences.items()):
        for left_index, left in enumerate(items):
            for right in items[left_index+1:]:
                if left["component"] == right["component"]:
                    continue
                a, b = left["vertex"], right["vertex"]
                ia, ib = left["parameter_index"], right["parameter_index"]
                source_a = -jacobians[a][:, ia]
                source_b = -jacobians[b][:, ib]
                response_b = pseudoinverses[b]@source_a
                response_a = pseudoinverses[a]@source_b
                residual_ab = float(
                    np.linalg.norm(jacobians[b]@response_b-source_a)
                    /max(np.linalg.norm(source_a), 1e-300))
                residual_ba = float(
                    np.linalg.norm(jacobians[a]@response_a-source_b)
                    /max(np.linalg.norm(source_b), 1e-300))
                audits.append({
                    "canonical_face": face,
                    "left_vertex": a,
                    "right_vertex": b,
                    "left_component": left["component"],
                    "right_component": right["component"],
                    "left_deleted_edge": list(left["label"]),
                    "right_deleted_edge": list(right["label"]),
                    "left_to_right_normal_slope": float(response_b[ib]),
                    "right_to_left_normal_slope": float(response_a[ia]),
                    "left_to_right_relative_tangent_residual": residual_ab,
                    "right_to_left_relative_tangent_residual": residual_ba,
                    "reciprocal_slope_product": float(
                        response_b[ib]*response_a[ia]),
                })

    window_audits = {}
    for window in SLOPE_WINDOWS:
        candidates = [
            audit for audit in audits
            if abs(audit["left_to_right_normal_slope"]+1) <= window
            and abs(audit["right_to_left_normal_slope"]+1) <= window
            and audit["left_to_right_relative_tangent_residual"]
                <= TANGENT_RESIDUAL_MAX
            and audit["right_to_left_relative_tangent_residual"]
                <= TANGENT_RESIDUAL_MAX
        ]
        component_edges = sorted({
            tuple(sorted((
                audit["left_component"], audit["right_component"])))
            for audit in candidates})
        graph_components = components_from_edges(
            len(incidence["components"]), component_edges)
        window_audits[str(window)] = {
            "candidate_occurrence_pair_count": len(candidates),
            "candidate_component_edge_count": len(component_edges),
            "candidate_component_graph_component_count":
                len(graph_components),
            "candidate_component_graph_component_sizes":
                [len(group) for group in graph_components],
        }
        for audit in candidates:
            audit.setdefault("accepted_slope_windows", []).append(window)

    retained = [
        audit for audit in audits if "accepted_slope_windows" in audit]
    strict = [
        audit for audit in audits
        if abs(audit["left_to_right_normal_slope"]+1) <= SLOPE_WINDOWS[0]
        and abs(audit["right_to_left_normal_slope"]+1) <= SLOPE_WINDOWS[0]
        and audit["left_to_right_relative_tangent_residual"]
            <= TANGENT_RESIDUAL_MAX
        and audit["right_to_left_relative_tangent_residual"]
            <= TANGENT_RESIDUAL_MAX
    ]
    best_by_component_edge = {}
    for audit in strict:
        edge = tuple(sorted((
            audit["left_component"], audit["right_component"])))
        score = max(
            abs(audit["left_to_right_normal_slope"]+1),
            abs(audit["right_to_left_normal_slope"]+1),
            audit["left_to_right_relative_tangent_residual"],
            audit["right_to_left_relative_tangent_residual"])
        if edge not in best_by_component_edge or (
                score < best_by_component_edge[edge][0]):
            best_by_component_edge[edge] = (score, audit)
    tree_parent = list(range(len(incidence["components"])))
    def tree_find(a):
        while tree_parent[a] != a:
            tree_parent[a] = tree_parent[tree_parent[a]]
            a = tree_parent[a]
        return a
    strict_tree = []
    for score, audit in sorted(best_by_component_edge.values(),
                               key=lambda item: item[0]):
        a, b = audit["left_component"], audit["right_component"]
        ra, rb = tree_find(a), tree_find(b)
        if ra == rb:
            continue
        tree_parent[rb] = ra
        strict_tree.append({**audit, "conditioning_score": score})
    out = {
        "schema": "marici.flavor.sparse_fiber_normal_response_census.v1",
        "strength": "finite_numerical_infinitesimal_census",
        "sources": [ATLAS, INCIDENCE, ENSEMBLE],
        "shared_face_occurrence_pair_count": len(audits),
        "tangent_residual_max": TANGENT_RESIDUAL_MAX,
        "slope_windows": list(SLOPE_WINDOWS),
        "window_audits": window_audits,
        "retained_at_any_window_count": len(retained),
        "strict_best_component_edge_count": len(best_by_component_edge),
        "strict_best_component_edges": [
            {**audit, "conditioning_score": score}
            for score, audit in sorted(best_by_component_edge.values(),
                                       key=lambda item: item[0])
        ],
        "strict_unit_normal_spanning_tree_edge_count": len(strict_tree),
        "strict_unit_normal_spanning_tree": strict_tree,
        "retained_audits": retained,
        "scope": (
            "unit normal response is necessary, not sufficient; retained "
            "pairs still require nonlinear asymptotic continuation and "
            "phase/deck coherence"),
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps({
        "shared_face_occurrence_pair_count": len(audits),
        "maximum_tangent_residual": max(max(
            audit["left_to_right_relative_tangent_residual"],
            audit["right_to_left_relative_tangent_residual"])
            for audit in audits),
        "window_audits": window_audits,
        "retained_at_any_window_count": len(retained),
        "strict_unit_normal_spanning_tree_edge_count": len(strict_tree),
    }, indent=2))


if __name__ == "__main__":
    main()
