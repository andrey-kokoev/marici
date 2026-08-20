"""Depth-ten nonlinear continuation of the strict unit-normal tree."""
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import json
import os
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "research/flavor/checkers")
from wp10_sparse_fiber_boundary_readout_pilot import labels, observable

NORMAL = (
    "research/flavor/results/wp10_sparse_fiber_normal_response_census.json")
INCIDENCE = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
ENSEMBLE = "research/flavor/results/wp7_ensemble.json"
OUTPUT = (
    "research/flavor/results/"
    "wp10_sparse_fiber_strict_normal_continuation.json")
MAX_DEPTH = float(os.environ.get("MARICI_MAX_DEPTH", "10"))
DEPTHS = np.linspace(0.0, MAX_DEPTH, int(round(4*MAX_DEPTH))+1)
BASE_ALL = (
    "research/flavor/results/"
    "wp10_sparse_fiber_all_strict_normal_continuation.json")
ISLAND_COMPONENTS = {21, 23, 25, 26}


def reached_maximum_depth(audit):
    """Accept legacy depth-ten packets and the parameterized terminology."""
    return audit["termination"] in {
        "depth_ten_reached", "maximum_depth_reached"}


def graph_components(n, edges):
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
    normal = json.load(open(NORMAL))
    incidence = json.load(open(INCIDENCE))
    ensemble = json.load(open(ENSEMBLE))
    raw = []
    for orbit in ensemble["orbits"]:
        for record in orbit["viable_minima"]:
            raw.append({"orbit": orbit["orbit_index"], **record})
    records = {}
    for vertex in incidence["vertices"]:
        candidates = [
            record for record in raw
            if record["orbit"] == vertex["orbit"]
            and record["member"] == vertex["member"]
            and record["phase_edge"] == vertex["phase_edge"]
            and abs(record["phi_folded"]-vertex["phi_folded"]) < 1e-6
        ]
        assert candidates, vertex
        records[vertex["id"]] = min(
            candidates,
            key=lambda r: abs(r["phi_folded"]-vertex["phi_folded"]))

    def run(index_and_edge):
        tree_index, edge = index_and_edge
        source_vertex = edge["left_vertex"]
        target_vertex = edge["right_vertex"]
        source_record = records[source_vertex]
        target_record = records[target_vertex]
        source_label = tuple(edge["left_deleted_edge"])
        target_label = tuple(edge["right_deleted_edge"])
        source_index = labels(source_record["member"]).index(source_label)
        target_index = labels(target_record["member"]).index(target_label)
        source_theta0 = np.array(
            source_record["log_mags"]+[source_record["phi"]], dtype=float)
        target_theta0 = np.array(
            target_record["log_mags"]+[target_record["phi"]], dtype=float)
        tracked = target_theta0.copy()
        samples = []
        termination = "maximum_depth_reached"
        lower = np.r_[np.full(9, -50.0), -20*np.pi]
        upper = np.r_[np.full(9, 5.0), 20*np.pi]
        for depth in DEPTHS:
            source_theta = source_theta0.copy()
            source_theta[source_index] -= depth
            wanted = observable(source_record, source_theta)
            solve = least_squares(
                lambda theta: observable(target_record, theta)-wanted,
                tracked, jac="3-point", x_scale="jac", xtol=1e-11,
                ftol=1e-11, gtol=1e-11, max_nfev=400,
                bounds=(lower, upper))
            tracked = solve.x
            residual = float(np.linalg.norm(solve.fun))
            target_minimum = int(np.argmin(tracked[:-1]))
            samples.append({
                "depth": float(depth),
                "success": bool(solve.success),
                "normalized_readout_l2_residual": residual,
                "normalized_readout_max_residual": float(
                    np.max(np.abs(solve.fun))),
                "target_face_log_displacement": float(
                    tracked[target_index]-target_theta0[target_index]),
                "target_minimum_edge_index": target_minimum,
                "nominated_target_edge_is_minimum":
                    target_minimum == target_index,
            })
            if not solve.success or residual > 1e-4:
                termination = "readout_mismatch_or_solver_failure"
                break
        slope = (
            (samples[-1]["target_face_log_displacement"]
             -samples[0]["target_face_log_displacement"])
            /(samples[-1]["depth"]-samples[0]["depth"])
            if len(samples) > 1 else None)
        return {
            "tree_index": tree_index,
            "source_component": edge["left_component"],
            "target_component": edge["right_component"],
            "canonical_face": edge["canonical_face"],
            "source_vertex": source_vertex,
            "target_vertex": target_vertex,
            "source_deleted_edge": list(source_label),
            "target_deleted_edge": list(target_label),
            "infinitesimal_forward_slope":
                edge["left_to_right_normal_slope"],
            "infinitesimal_reverse_slope":
                edge["right_to_left_normal_slope"],
            "conditioning_score": edge["conditioning_score"],
            "termination": termination,
            "depth_reached": samples[-1]["depth"],
            "finite_depth_target_normal_slope": float(slope),
            "nominated_target_edge_is_minimum_at_end":
                samples[-1]["nominated_target_edge_is_minimum"],
            "samples": samples,
        }

    all_strict = "--all-strict" in sys.argv[1:]
    island_occurrences = "--island-occurrences" in sys.argv[1:]
    reverse_only = "--reverse-only" in sys.argv[1:]
    component = next((
        int(argument.split("=", 1)[1]) for argument in sys.argv[1:]
        if argument.startswith("--component=")), None)
    island_window = next((
        float(argument.split("=", 1)[1]) for argument in sys.argv[1:]
        if argument.startswith("--island-window=")), 0.05)
    if island_occurrences:
        tree = [
            {**audit, "conditioning_score": max(
                abs(audit["left_to_right_normal_slope"]+1),
                abs(audit["right_to_left_normal_slope"]+1),
                audit["left_to_right_relative_tangent_residual"],
                audit["right_to_left_relative_tangent_residual"])}
            for audit in normal["retained_audits"]
            if island_window in audit["accepted_slope_windows"]
            and (audit["left_component"] in ISLAND_COMPONENTS
                 or audit["right_component"] in ISLAND_COMPONENTS)
        ]
    else:
        tree = normal[
            "strict_best_component_edges" if all_strict
            else "strict_unit_normal_spanning_tree"]
    if reverse_only:
        tree = [{
            **edge,
            "left_vertex": edge["right_vertex"],
            "right_vertex": edge["left_vertex"],
            "left_component": edge["right_component"],
            "right_component": edge["left_component"],
            "left_deleted_edge": edge["right_deleted_edge"],
            "right_deleted_edge": edge["left_deleted_edge"],
            "left_to_right_normal_slope":
                edge["right_to_left_normal_slope"],
            "right_to_left_normal_slope":
                edge["left_to_right_normal_slope"],
        } for edge in tree]
    if component is not None:
        tree = [edge for edge in tree
                if component in (edge["left_component"],
                                 edge["right_component"])]
    with ThreadPoolExecutor(
            max_workers=24 if (all_strict or island_occurrences) else 8
            ) as executor:
        audits = list(executor.map(run, enumerate(tree)))
    audits.sort(key=lambda audit: audit["tree_index"])
    reached = [audit for audit in audits if reached_maximum_depth(audit)]
    face_tracking = [
        audit for audit in reached
        if audit["nominated_target_edge_is_minimum_at_end"]
        and abs(audit["finite_depth_target_normal_slope"]+1) < 0.25]
    surviving_edges = sorted({
        tuple(sorted((audit["source_component"],
                      audit["target_component"])))
        for audit in face_tracking})
    surviving_components = graph_components(
        len(incidence["components"]), surviving_edges)
    output = os.environ.get("MARICI_OUTPUT") or (
        "research/flavor/results/"
        f"wp10_sparse_fiber_island_occurrence_continuation_"
        f"w{int(round(100*island_window)):02d}"
        f"{'_reverse' if reverse_only else ''}.json"
        if island_occurrences else
        "research/flavor/results/"
        "wp10_sparse_fiber_all_strict_normal_continuation.json"
        if all_strict else OUTPUT)
    combined_edges = set(surviving_edges)
    if island_occurrences:
        base = json.load(open(BASE_ALL))
        combined_edges.update(
            tuple(sorted((audit["source_component"],
                          audit["target_component"])))
            for audit in base["audits"]
            if reached_maximum_depth(audit)
            and audit["nominated_target_edge_is_minimum_at_end"]
            and abs(audit["finite_depth_target_normal_slope"]+1) < 0.25)
        if reverse_only:
            forward_path = (
                "research/flavor/results/"
                f"wp10_sparse_fiber_island_occurrence_continuation_"
                f"w{int(round(100*island_window)):02d}.json")
            forward = json.load(open(forward_path))
            combined_edges.update(
                tuple(sorted((audit["source_component"],
                              audit["target_component"])))
                for audit in forward["audits"]
                if reached_maximum_depth(audit)
                and audit["nominated_target_edge_is_minimum_at_end"]
                and abs(audit["finite_depth_target_normal_slope"]+1) < 0.25)
    combined_components = graph_components(
        len(incidence["components"]), sorted(combined_edges))
    out = {
        "schema": (
            "marici.flavor.sparse_fiber_island_occurrence_continuation.v1"
            if island_occurrences else
            "marici.flavor.sparse_fiber_all_strict_normal_continuation.v1"
            if all_strict else
            "marici.flavor.sparse_fiber_strict_normal_continuation.v1"),
        "strength": "bounded_numerical_continuation_census",
        "maximum_log_depth": MAX_DEPTH,
        "source": NORMAL,
        "island_infinitesimal_slope_window": (
            island_window if island_occurrences else None),
        "reverse_only": reverse_only,
        "tree_edge_count": len(audits),
        "maximum_depth_reached_count": len(reached),
        "early_failure_count": len(audits)-len(reached),
        "nonlinear_face_tracking_count": len(face_tracking),
        "surviving_component_edge_count": len(surviving_edges),
        "surviving_component_graph_component_count":
            len(surviving_components),
        "surviving_component_graph_component_sizes":
            [len(group) for group in surviving_components],
        "combined_with_all_strict_best_edge_count": len(combined_edges),
        "combined_component_graph_component_count":
            len(combined_components),
        "combined_component_graph_component_sizes":
            [len(group) for group in combined_components],
        "readout_continuation_but_wrong_face_count":
            len(reached)-len(face_tracking),
        "maximum_final_l2_residual_among_reached": max(
            (audit["samples"][-1]["normalized_readout_l2_residual"]
             for audit in reached), default=None),
        "finite_depth_target_normal_slope_range": [
            min(audit["finite_depth_target_normal_slope"]
                for audit in audits),
            max(audit["finite_depth_target_normal_slope"]
                for audit in audits),
        ],
        "scope": (
            "finite-depth face tracking is still not an asymptotic theorem or "
            "a phase/deck coherence certificate"),
        "audits": audits,
    }
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps({key: out[key] for key in (
        "tree_edge_count", "maximum_depth_reached_count",
        "early_failure_count", "nonlinear_face_tracking_count",
        "surviving_component_edge_count",
        "surviving_component_graph_component_count",
        "surviving_component_graph_component_sizes",
        "combined_with_all_strict_best_edge_count",
        "combined_component_graph_component_count",
        "combined_component_graph_component_sizes",
        "readout_continuation_but_wrong_face_count",
        "maximum_final_l2_residual_among_reached",
        "finite_depth_target_normal_slope_range")}, indent=2))


if __name__ == "__main__":
    main()
