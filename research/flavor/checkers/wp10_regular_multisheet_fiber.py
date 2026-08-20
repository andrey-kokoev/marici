"""Join WP8 same-chart doublets with WP10 local-rank certificates.

A pair of distinct parameter points in one declared sparse chart that has
indistinguishable physical observables demonstrates global noninjectivity.
If both endpoints have rank-ten local observable Jacobians, the multiplicity
is between distinct regular sheets, not a flat direction or singular fold.
"""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wp7_ensemble import (  # noqa: E402
    build_texture, mask_slots, observables17, SIGMA)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
fiber = json.loads((RESULTS / "wp8_fiber_classification.json").read_text())
local = json.loads((RESULTS / "wp10_local_phase_identifiability.json").read_text())
ensemble = json.loads((RESULTS / "wp7_ensemble.json").read_text())


def observable_map(record, theta):
    mu, md = record["member"]
    edge = record["phase_edge"]
    Yu, Yd = build_texture(mu, md, edge[0], tuple(edge[1:]), theta)
    return observables17(Yu, Yd)/SIGMA


def observable_jacobian(record, theta=None):
    if theta is None:
        theta = np.array(record["log_mags"]+[record["phi"]], dtype=float)
    def obs(value):
        return observable_map(record, value)
    jac = np.empty((17, 10))
    for j in range(10):
        h = 2e-6 if j < 9 else 1e-6
        plus, minus = theta.copy(), theta.copy()
        plus[j] += h; minus[j] -= h
        jac[:, j] = (obs(plus)-obs(minus))/(2*h)
    return jac


raw_minima = []
for orbit in ensemble["orbits"]:
    for rec in orbit["viable_minima"]:
        raw_minima.append({"orbit": orbit["orbit_index"], **rec})

records = local["records"]
audits = []
for pair in fiber["same_chart_doublets"]:
    chart = pair["chart"]
    endpoints = []
    endpoint_jacobians = []
    endpoint_records = []
    for phi in pair["phis"]:
        exact = [
            r for r in raw_minima
            if r["orbit"] == chart["orbit"]
            and r["member"] == chart["member"]
            and r["phase_edge"] == chart["phase_edge"]
            and abs(r["phi_folded"]-phi) < 1e-6
        ]
        assert exact, (chart, phi)
        endpoint_records.append(exact[0])
        endpoint_jacobians.append(observable_jacobian(exact[0]))
        candidates = [
            r for r in records
            if r["orientation"] == "original"
            and r["orbit"] == chart["orbit"]
            and abs(r["phi_folded"]-phi) < 1e-6
        ]
        assert candidates, (chart, phi)
        best = min(candidates, key=lambda r: abs(r["phi_folded"]-phi))
        endpoints.append({
            "phi": best["phi_folded"],
            "jacobian_rank": best["jacobian_rank"],
            "profiled_phase_information":
                best["profiled_phase_information"],
            "profiled_fraction": best["profiled_fraction"],
            "smallest_singular_value": best["smallest_singular_value"],
        })
    assert all(e["jacobian_rank"] == 10 for e in endpoints)
    q0, _ = np.linalg.qr(endpoint_jacobians[0])
    q1, _ = np.linalg.qr(endpoint_jacobians[1])
    tangent_cosines = np.linalg.svd(q0.T@q1, compute_uv=False)
    transition_01 = np.linalg.pinv(endpoint_jacobians[1])@endpoint_jacobians[0]
    transition_10 = np.linalg.pinv(endpoint_jacobians[0])@endpoint_jacobians[1]
    intertwining_residual = np.linalg.norm(
        endpoint_jacobians[1]@transition_01-endpoint_jacobians[0]
    )/np.linalg.norm(endpoint_jacobians[0])
    composition_residual = np.linalg.norm(
        transition_10@transition_01-np.eye(10))
    transition_singular_values = np.linalg.svd(
        transition_01, compute_uv=False)
    fiber_product_jacobian = np.hstack(
        (endpoint_jacobians[0], -endpoint_jacobians[1]))
    fiber_product_singular_values = np.linalg.svd(
        fiber_product_jacobian, compute_uv=False)
    fiber_product_relative_tolerance = 1e-7
    fiber_product_rank = int(np.sum(
        fiber_product_singular_values >
        fiber_product_relative_tolerance*fiber_product_singular_values[0]))
    transition_graph = np.vstack((np.eye(10), transition_01))
    graph_tangent_residual = np.linalg.norm(
        fiber_product_jacobian@transition_graph
    )/np.linalg.norm(endpoint_jacobians[0])
    theta0 = np.array(
        endpoint_records[0]["log_mags"]+[endpoint_records[0]["phi"]],
        dtype=float)
    theta1 = np.array(
        endpoint_records[1]["log_mags"]+[endpoint_records[1]["phi"]],
        dtype=float)
    _, _, vh0 = np.linalg.svd(endpoint_jacobians[0], full_matrices=False)
    loop_steps = 24
    loop_audits = []
    for loop_radius in (1e-4, 2e-4, 4e-4):
        tracked = theta1.copy()
        start_corrected = None
        loop_residuals = []
        for step in range(loop_steps+1):
            angle = 2*np.pi*step/loop_steps
            source_theta = theta0+loop_radius*(
                np.cos(angle)*vh0[0]+np.sin(angle)*vh0[1])
            target = observable_map(endpoint_records[0], source_theta)
            solve = least_squares(
                lambda value:
                    observable_map(endpoint_records[1], value)-target,
                tracked, jac="3-point", xtol=1e-12, ftol=1e-12, gtol=1e-12,
                max_nfev=200)
            assert solve.success, (chart, step, solve.message)
            tracked = solve.x
            if step == 0:
                start_corrected = tracked.copy()
            loop_residuals.append(float(np.linalg.norm(solve.fun)))
        loop_audits.append({
            "radius": loop_radius,
            "steps": loop_steps,
            "maximum_observable_residual": max(loop_residuals),
            "return_parameter_residual":
                float(np.linalg.norm(tracked-start_corrected)),
        })

    phase_continuations = []
    scan_theta0 = theta0.copy()
    scan_theta0[-1] = np.mod(scan_theta0[-1], 2*np.pi)
    scan_theta1 = theta1.copy()
    scan_theta1[-1] = scan_theta0[-1]+(
        (scan_theta1[-1]-scan_theta0[-1]+np.pi)%(2*np.pi)-np.pi)
    for direction in (-1, 1):
        phase_limit = float(np.clip(
            scan_theta0[-1]+direction*0.75, 0.05, 2*np.pi-0.05))
        tracked = scan_theta1.copy()
        current_phase = scan_theta0[-1]
        accepted = []
        termination = "phase_chart_scan_limit"
        step_size = 0.02
        while direction*(phase_limit-current_phase) > 1e-12:
            next_phase = current_phase+direction*min(
                step_size, abs(phase_limit-current_phase))
            source_theta = scan_theta0.copy()
            source_theta[-1] = next_phase
            target = observable_map(endpoint_records[0], source_theta)
            solve = least_squares(
                lambda value:
                    observable_map(endpoint_records[1], value)-target,
                tracked, jac="3-point", xtol=1e-11, ftol=1e-11, gtol=1e-11,
                max_nfev=250)
            residual = float(np.linalg.norm(solve.fun))
            if not solve.success or residual > 1e-5:
                step_size /= 2
                if step_size < 0.00125:
                    termination = "adaptive_corrector_failure"
                    break
                continue
            tracked = solve.x
            accepted.append({
                "source_phase": float(next_phase),
                "observable_residual": residual,
                "off_diagonal_parameter_distance":
                    float(np.linalg.norm(tracked-source_theta)),
                "tracked_phase": float(tracked[-1]),
                "minimum_tracked_magnitude": float(np.exp(tracked[:-1]).min()),
                "maximum_tracked_magnitude": float(np.exp(tracked[:-1]).max()),
            })
            current_phase = next_phase
            step_size = min(0.02, step_size*1.5)
        phase_continuations.append({
            "direction": direction,
            "target_phase_limit": float(phase_limit),
            "accepted_steps": len(accepted),
            "termination": termination,
            "minimum_off_diagonal_parameter_distance": min(
                (item["off_diagonal_parameter_distance"]
                 for item in accepted), default=None),
            "maximum_observable_residual": max(
                (item["observable_residual"] for item in accepted),
                default=None),
            "last": accepted[-1] if accepted else None,
        })

    face_edge = int(np.argmin(theta0[:-1]))
    face_tracked = theta1.copy()
    face_depth = 0.0
    face_step = 0.1
    face_target_depth = 10.0
    face_samples = []
    face_termination = "coordinate_face_asymptotic_limit"
    while face_depth < face_target_depth-1e-12:
        next_depth = min(face_target_depth, face_depth+face_step)
        source_theta = theta0.copy()
        source_theta[face_edge] -= next_depth
        target = observable_map(endpoint_records[0], source_theta)
        solve = least_squares(
            lambda value: observable_map(endpoint_records[1], value)-target,
            face_tracked, jac="3-point", xtol=1e-11, ftol=1e-11,
            gtol=1e-11, max_nfev=300)
        residual = float(np.linalg.norm(solve.fun))
        if not solve.success or residual > 1e-5:
            face_step /= 2
            if face_step < 0.003125:
                face_termination = "adaptive_corrector_failure"
                break
            continue
        face_tracked = solve.x
        face_depth = next_depth
        if (not face_samples or face_depth-face_samples[-1]["depth"] >= 0.95
                or face_depth >= face_target_depth-1e-12):
            face_samples.append({
                "depth": float(face_depth),
                "source_edge_ratio": float(np.exp(-face_depth)),
                "observable_residual": residual,
                "off_diagonal_parameter_distance":
                    float(np.linalg.norm(face_tracked-source_theta)),
                "minimum_partner_magnitude":
                    float(np.exp(face_tracked[:-1]).min()),
                "maximum_partner_magnitude":
                    float(np.exp(face_tracked[:-1]).max()),
            })
        face_step = min(0.1, face_step*1.5)
    face_source_magnitude = float(np.exp(
        theta0[face_edge]-face_depth))
    edge_labels = (
        [("u", *slot) for slot in mask_slots(endpoint_records[0]["member"][0])]
        +[("d", *slot) for slot in mask_slots(endpoint_records[0]["member"][1])])
    partner_face_edge = int(np.argmin(face_tracked[:-1]))
    face_partner_ratio = (
        face_samples[-1]["minimum_partner_magnitude"]/face_source_magnitude
        if face_samples else None)
    face_partner_log_slope = (
        (np.log(face_samples[-1]["minimum_partner_magnitude"])
         -np.log(face_samples[0]["minimum_partner_magnitude"]))
        /(face_samples[-1]["depth"]-face_samples[0]["depth"])
        if len(face_samples) > 1 else None)
    audits.append({
        "chart": chart,
        "phi_gap": pair["phi_gap"],
        "max_observable_separation_sigma": pair["max_obs_separation_sigma"],
        "log_magnitude_distance": pair["max_logmag_l2"],
        "endpoints": endpoints,
        "both_endpoints_regular": True,
        "tangent_principal_cosines": [float(x) for x in tangent_cosines],
        "largest_tangent_principal_angle_radians":
            float(np.arccos(np.clip(tangent_cosines[-1], -1, 1))),
        "coincident_tangent_spaces":
            bool(np.min(tangent_cosines) > 1-1e-6),
        "differential_transition_intertwining_relative_residual":
            float(intertwining_residual),
        "reverse_composition_identity_residual":
            float(composition_residual),
        "transition_determinant": float(np.linalg.det(transition_01)),
        "transition_singular_values":
            [float(x) for x in transition_singular_values],
        "equal_readout_fiber_product_rank": fiber_product_rank,
        "equal_readout_fiber_product_tangent_dimension":
            20-fiber_product_rank,
        "equal_readout_fiber_product_relative_rank_tolerance":
            fiber_product_relative_tolerance,
        "equal_readout_fiber_product_singular_values":
            [float(x) for x in fiber_product_singular_values],
        "equal_readout_fiber_product_rank_gap":
            float(fiber_product_singular_values[9]
                  /fiber_product_singular_values[10]),
        "transition_graph_tangent_relative_residual":
            float(graph_tangent_residual),
        "continuation_loop_audits": loop_audits,
        "maximum_continuation_observable_residual": max(
            item["maximum_observable_residual"] for item in loop_audits),
        "maximum_continuation_return_parameter_residual": max(
            item["return_parameter_residual"] for item in loop_audits),
        "phase_slice_continuations": phase_continuations,
        "coordinate_face_continuation": {
            "suppressed_edge_index": face_edge,
            "suppressed_edge_label": edge_labels[face_edge],
            "partner_vanishing_edge_index": partner_face_edge,
            "partner_vanishing_edge_label": edge_labels[partner_face_edge],
            "target_log_depth": face_target_depth,
            "reached_log_depth": float(face_depth),
            "termination": face_termination,
            "partner_minimum_to_source_edge_ratio_at_limit":
                face_partner_ratio,
            "partner_minimum_log_slope": face_partner_log_slope,
            "samples": face_samples,
            "last": face_samples[-1] if face_samples else None,
            "source_limit_log_parameters":
                [float(value) for value in source_theta],
            "partner_limit_log_parameters":
                [float(value) for value in face_tracked],
        },
        "regularity_transport":
            "rank and profiled information transported within the S3^3 orbit when the exact member was removed by deduplication",
    })

out = {
    "schema": "marici.flavor.regular_multisheet_fiber.v1",
    "status": "certified_join",
    "same_chart_doublet_count": len(audits),
    "all_endpoints_rank_ten": all(
        a["both_endpoints_regular"] for a in audits),
    "maximum_observable_separation_sigma": max(
        a["max_observable_separation_sigma"] for a in audits),
    "maximum_phase_gap": max(a["phi_gap"] for a in audits),
    "all_tangent_spaces_coincident":
        all(a["coincident_tangent_spaces"] for a in audits),
    "maximum_tangent_principal_angle_radians": max(
        a["largest_tangent_principal_angle_radians"] for a in audits),
    "maximum_transition_intertwining_relative_residual": max(
        a["differential_transition_intertwining_relative_residual"]
        for a in audits),
    "maximum_reverse_composition_identity_residual": max(
        a["reverse_composition_identity_residual"] for a in audits),
    "all_equal_readout_correspondence_tangents_dimension_ten": all(
        a["equal_readout_fiber_product_tangent_dimension"] == 10
        for a in audits),
    "maximum_transition_graph_tangent_relative_residual": max(
        a["transition_graph_tangent_relative_residual"] for a in audits),
    "maximum_continuation_observable_residual": max(
        a["maximum_continuation_observable_residual"] for a in audits),
    "maximum_continuation_return_parameter_residual": max(
        a["maximum_continuation_return_parameter_residual"] for a in audits),
    "phase_slice_continuation_count": sum(
        len(a["phase_slice_continuations"]) for a in audits),
    "all_phase_slice_scans_reach_declared_limits": all(
        item["termination"] == "phase_chart_scan_limit"
        for a in audits for item in a["phase_slice_continuations"]),
    "maximum_phase_slice_observable_residual": max(
        item["maximum_observable_residual"]
        for a in audits for item in a["phase_slice_continuations"]),
    "minimum_phase_slice_off_diagonal_parameter_distance": min(
        item["minimum_off_diagonal_parameter_distance"]
        for a in audits for item in a["phase_slice_continuations"]),
    "all_coordinate_face_scans_reach_asymptotic_limit": all(
        a["coordinate_face_continuation"]["termination"]
        == "coordinate_face_asymptotic_limit" for a in audits),
    "minimum_coordinate_face_source_edge_ratio": min(
        a["coordinate_face_continuation"]["last"]["source_edge_ratio"]
        for a in audits),
    "coordinate_face_partner_log_slope_range": [
        min(a["coordinate_face_continuation"]["partner_minimum_log_slope"]
            for a in audits),
        max(a["coordinate_face_continuation"]["partner_minimum_log_slope"]
            for a in audits),
    ],
    "coordinate_face_partner_to_source_ratio_range": [
        min(a["coordinate_face_continuation"]
              ["partner_minimum_to_source_edge_ratio_at_limit"]
            for a in audits),
        max(a["coordinate_face_continuation"]
              ["partner_minimum_to_source_edge_ratio_at_limit"]
            for a in audits),
    ],
    "interpretation":
        "the sparse-chart physical readout is locally immersive at both endpoints but globally noninjective; coincident physical tangent spaces give local sheet-transition maps, but do not yet establish a global deck group",
    "audits": audits,
}
(RESULTS / "wp10_regular_multisheet_fiber.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k != "audits"}, indent=2))
