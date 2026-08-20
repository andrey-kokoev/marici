"""Bounded normalized-readout continuation on the 33 carrier-tree faces.

This is a depth-ten numerical pilot.  For each tree edge, concrete vertices
and deleted entries realizing its canonical support face are selected.  Both
source deleted magnitude is forced down while all ten target-chart parameters
are corrected against the source's full 17-component normalized physical
readout.  The target normal speed is derived rather than chosen.
"""
from concurrent.futures import ThreadPoolExecutor
import json
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "research/flavor/checkers")
from wp7_ensemble import SIGMA, build_texture, mask_slots, observables17

ATLAS = "research/flavor/results/wp10_sparse_fiber_face_atlas.json"
INCIDENCE = "research/flavor/results/wp10_sparse_fiber_incidence_graph.json"
ENSEMBLE = "research/flavor/results/wp7_ensemble.json"
OUTPUT = (
    "research/flavor/results/"
    "wp10_sparse_fiber_boundary_readout_pilot.json")
DEPTHS = np.linspace(0.0, 10.0, 41)


def labels(member):
    mu, md = member
    return ([('u', *slot) for slot in mask_slots(mu)]
            +[('d', *slot) for slot in mask_slots(md)])


def observable(record, theta):
    edge = record["phase_edge"]
    yu, yd = build_texture(
        *record["member"], edge[0], tuple(edge[1:]), theta)
    return observables17(yu, yd)/SIGMA


def main():
    atlas = json.load(open(ATLAS))
    incidence = json.load(open(INCIDENCE))
    ensemble = json.load(open(ENSEMBLE))
    raw = []
    for orbit in ensemble["orbits"]:
        for record in orbit["viable_minima"]:
            raw.append({"orbit": orbit["orbit_index"], **record})

    records = {}
    observations = {}
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
        records[vertex["id"]] = record
        theta = np.array(record["log_mags"]+[record["phi"]], dtype=float)
        observations[vertex["id"]] = observable(record, theta)

    component_vertices = {
        i: component["vertices"]
        for i, component in enumerate(incidence["components"])}

    jobs = []
    for tree_index, edge in enumerate(atlas["carrier_gate_spanning_tree"]):
        face = edge["canonical_face"]
        occurrences = {}
        for component_key in ("source_component", "target_component"):
            component = edge[component_key]
            found = []
            for vertex in component_vertices[component]:
                for deletion in atlas["vertex_faces"][str(vertex)]:
                    if deletion["canonical_face"] == face:
                        found.append((vertex, deletion))
            assert found, (edge, component)
            occurrences[component_key] = found
        pairs = [
            (float(np.max(np.abs(
                observations[a[0]]-observations[b[0]]))), a, b)
            for a in occurrences["source_component"]
            for b in occurrences["target_component"]
        ]
        _, source_occurrence, target_occurrence = min(
            pairs, key=lambda item: item[0])
        jobs.append((tree_index, edge, source_occurrence, target_occurrence))

    def run(job):
        tree_index, edge, source_occurrence, target_occurrence = job
        source_vertex, source_deletion = source_occurrence
        target_vertex, target_deletion = target_occurrence
        source_record = records[source_vertex]
        target_record = records[target_vertex]
        source_theta0 = np.array(
            source_record["log_mags"]+[source_record["phi"]], dtype=float)
        target_theta0 = np.array(
            target_record["log_mags"]+[target_record["phi"]], dtype=float)
        source_label = (
            source_deletion["sector"], source_deletion["row"],
            source_deletion["column"])
        target_label = (
            target_deletion["sector"], target_deletion["row"],
            target_deletion["column"])
        source_index = labels(source_record["member"]).index(source_label)
        target_index = labels(target_record["member"]).index(target_label)
        tracked = target_theta0.copy()
        samples = []
        termination = "depth_ten_reached"
        for depth in DEPTHS:
            source_theta = source_theta0.copy()
            source_theta[source_index] -= depth
            wanted = observable(source_record, source_theta)

            def residual(theta):
                return observable(target_record, theta)-wanted

            solve = least_squares(
                residual, tracked, jac="3-point", x_scale="jac",
                xtol=1e-11, ftol=1e-11, gtol=1e-11, max_nfev=400)
            tracked = solve.x
            norm = float(np.linalg.norm(solve.fun))
            target_minimum_index = int(np.argmin(tracked[:-1]))
            samples.append({
                "depth": float(depth),
                "success": bool(solve.success),
                "normalized_readout_l2_residual": norm,
                "normalized_readout_max_residual": float(
                    np.max(np.abs(solve.fun))),
                "target_parameter_norm": float(np.linalg.norm(tracked)),
                "target_phase": float(tracked[-1]),
                "target_face_log_displacement": float(
                    tracked[target_index]-target_theta0[target_index]),
                "target_minimum_edge_index": target_minimum_index,
                "nominated_target_edge_is_minimum":
                    target_minimum_index == target_index,
            })
            if not solve.success or norm > 1e-4:
                termination = "readout_mismatch_or_solver_failure"
                break
        return {
            "tree_index": tree_index,
            "source_component": edge["source_component"],
            "target_component": edge["target_component"],
            "canonical_face": edge["canonical_face"],
            "source_vertex": source_vertex,
            "target_vertex": target_vertex,
            "source_deleted_edge": list(source_label),
            "target_deleted_edge": list(target_label),
            "initial_max_observable_separation_sigma": float(np.max(np.abs(
                observations[source_vertex]-observations[target_vertex]))),
            "phase_edge_deleted": bool(
                list(source_label) == source_record["phase_edge"]
                or list(target_label) == target_record["phase_edge"]),
            "termination": termination,
            "target_face_log_slope": (
                float((samples[-1]["target_face_log_displacement"]
                       -samples[0]["target_face_log_displacement"])
                      /(samples[-1]["depth"]-samples[0]["depth"]))
                if len(samples) > 1 else None),
            "nominated_target_edge_is_minimum_at_end":
                samples[-1]["nominated_target_edge_is_minimum"],
            "samples": samples,
        }

    with ThreadPoolExecutor(max_workers=8) as executor:
        audits = list(executor.map(run, jobs))
    audits.sort(key=lambda audit: audit["tree_index"])
    passed = [
        audit for audit in audits
        if audit["termination"] == "depth_ten_reached"]
    boundary_candidates = [
        audit for audit in passed
        if audit["nominated_target_edge_is_minimum_at_end"]
        and abs(audit["target_face_log_slope"]+1) < 0.25]
    out = {
        "schema": "marici.flavor.sparse_fiber_boundary_readout_pilot.v1",
        "strength": "bounded_numerical_depth_ten_pilot",
        "source": ATLAS,
        "depths": [float(x) for x in DEPTHS],
        "tree_edge_count": len(audits),
        "depth_ten_pass_count": len(passed),
        "early_failure_count": len(audits)-len(passed),
        "boundary_tracking_candidate_count": len(boundary_candidates),
        "readout_continuation_but_wrong_face_count":
            len(passed)-len(boundary_candidates),
        "phase_edge_deleted_count": sum(
            audit["phase_edge_deleted"] for audit in audits),
        "nominated_target_edge_minimum_at_end_count": sum(
            audit["nominated_target_edge_is_minimum_at_end"]
            for audit in audits),
        "target_face_log_slope_range": [
            min(audit["target_face_log_slope"] for audit in audits),
            max(audit["target_face_log_slope"] for audit in audits),
        ],
        "maximum_final_l2_residual_among_passes": max(
            (audit["samples"][-1]["normalized_readout_l2_residual"]
             for audit in passed), default=None),
        "scope": (
            "passing depth ten is only a continuation pilot; it does not "
            "establish an asymptotic boundary incidence or deck coherence; "
            "the deterministic spanning-tree witness is not exhaustive over "
            "all vertex/deletion occurrences of a canonical face"),
        "audits": audits,
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps({key: out[key] for key in (
        "tree_edge_count", "depth_ten_pass_count", "early_failure_count",
        "boundary_tracking_candidate_count",
        "readout_continuation_but_wrong_face_count",
        "phase_edge_deleted_count",
        "nominated_target_edge_minimum_at_end_count",
        "target_face_log_slope_range",
        "maximum_final_l2_residual_among_passes")}, indent=2))


if __name__ == "__main__":
    main()
