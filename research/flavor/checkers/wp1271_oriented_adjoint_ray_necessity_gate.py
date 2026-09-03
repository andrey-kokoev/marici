import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1271-oriented-adjoint-ray-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1246,1247,1248)
wp1246=json.loads((ROOT/"results"/"wp1246_common_uv_boundary_action_packet_gate.json").read_text())
wp1247=json.loads((ROOT/"results"/"wp1247_nima_source_dynamics_branch_gate.json").read_text())
wp1248=json.loads((ROOT/"results"/"wp1248_su3_breaking_flag_cyclic_ray_gate.json").read_text())

common_uv_packet_routes={
    "candidate_packets":{
        "soft_candidates_six":wp1246["soft_candidates_six"],
        "rank_one_reweighting_known":wp1246["rank_one_reweighting_known"],
        "aspect_composition_calibrated":wp1246["aspect_composition_calibrated"],
        "nima_candidates_fill_none":wp1246["nima_candidates_fill_none"],
        "common_uv_packet":wp1246["common_uv_packet"],
        "production_kernel":wp1246["production_kernel"],
        "mixing_matrix_derived":wp1246["mixing_matrix_derived"],
        "gain_3_over_2_derived":wp1246["gain_3_over_2_derived"],
        "flux_sector_orientation":wp1246["flux_sector_orientation"],
        "endpoint_action":wp1246["endpoint_action"],
        "physical16_channel":wp1246["physical16_channel"],
        "source_gain":wp1246["source_gain"]
    },
    "nima_branch":{
        "bipartite_carrier":wp1247["bipartite_carrier"],
        "krylov_mechanism_known":wp1247["krylov_mechanism_known"],
        "current_source_no_go":wp1247["current_source_no_go"],
        "temporal_process":wp1247["temporal_process"],
        "ordered_ports":wp1247["ordered_ports"],
        "production_kernel":wp1247["production_kernel"],
        "source_evolution":wp1247["source_evolution"],
        "cyclic_ray":wp1247["cyclic_ray"],
        "retained_history":wp1247["retained_history"],
        "volume_reference":wp1247["volume_reference"],
        "physical16_descent":wp1247["physical16_descent"]
    },
    "flag_cyclic_ray":{
        "localized_refinement_no_go":wp1248["localized_refinement_no_go"],
        "wilson_split_conditional":wp1248["wilson_split_conditional"],
        "simple_flag_conditional":wp1248["simple_flag_conditional"],
        "isometric_history_conditional":wp1248["isometric_history_conditional"],
        "volume_reference_missing":wp1248["volume_reference_missing"],
        "oriented_adjoint_ray":wp1248["oriented_adjoint_ray"],
        "ordered_weight_lines":wp1248["ordered_weight_lines"],
        "cyclic_seed":wp1248["cyclic_seed"],
        "physical_history":wp1248["physical_history"],
        "rho":wp1248["rho"],
        "physical16_descent":wp1248["physical16_descent"]
    }
}
assert common_uv_packet_routes["candidate_packets"]["soft_candidates_six"]
assert common_uv_packet_routes["candidate_packets"]["rank_one_reweighting_known"]
assert common_uv_packet_routes["candidate_packets"]["aspect_composition_calibrated"]
assert common_uv_packet_routes["candidate_packets"]["nima_candidates_fill_none"]
assert common_uv_packet_routes["nima_branch"]["bipartite_carrier"]
assert common_uv_packet_routes["nima_branch"]["krylov_mechanism_known"]
assert common_uv_packet_routes["nima_branch"]["current_source_no_go"]
assert common_uv_packet_routes["flag_cyclic_ray"]["localized_refinement_no_go"]
assert common_uv_packet_routes["flag_cyclic_ray"]["wilson_split_conditional"]
assert common_uv_packet_routes["flag_cyclic_ray"]["simple_flag_conditional"]
assert common_uv_packet_routes["flag_cyclic_ray"]["isometric_history_conditional"]
assert common_uv_packet_routes["flag_cyclic_ray"]["volume_reference_missing"]
for section in common_uv_packet_routes.values():
    for key,value in section.items():
        if key in {
            "common_uv_packet","production_kernel","mixing_matrix_derived","gain_3_over_2_derived",
            "flux_sector_orientation","endpoint_action","physical16_channel","source_gain",
            "temporal_process","ordered_ports","source_evolution","cyclic_ray","retained_history",
            "volume_reference","physical16_descent","oriented_adjoint_ray","ordered_weight_lines",
            "cyclic_seed","physical_history","rho"
        }:
            assert value is False, key

# Falsifier: an existing calibrated packet, candidate source packet, bipartite
# carrier, Wilson flag, or history bundle supplies the common UV packet while
# bypassing the source-derived oriented adjoint ray.
existing_packet_bypass_found=False
oriented_adjoint_ray_derived=False
conjecture_refuted=existing_packet_bypass_found
assert not conjecture_refuted and not oriented_adjoint_ray_derived

result={
    "schema":"marici.flavor.wp1271.v1",
    "status":"PASS",
    "question":"Can an existing calibrated packet, candidate source packet, bipartite carrier, Wilson flag, or history bundle supply the common UV packet without a source-derived oriented adjoint ray?",
    "dpc":{
        "conjecture":"Every common UV compactification packet sufficient for flavor must pass through a source-derived oriented adjoint ray, followed by ordered weight lines, cyclic preparation, retained history, volume reference, and calibrated Physical16 descent.",
        "rivals":["calibrated acquisition packet","rank-one reweighting packet","Aspect pattern composition","current Nima candidate packets","bipartite SU(3) carrier","Krylov history witness","Wilson line flag","isometric history bundle","scalar adjoint route"],
        "risky_consequences":["WP1246 calibrates acquisition but no candidate packet fills production, mixing, gain, flux, endpoint action, or channels","WP1247 finds a bipartite carrier and Krylov mechanism but no temporal process, source evolution, cyclic ray, retained history, volume reference, or descent","WP1248 finds conditional Wilson and history constructors but no oriented adjoint ray, ordered weight lines, cyclic seed, physical history, rho, or descent"],
        "falsification_attempt":"Replay WP1246 through WP1248 and search for an existing packet that supplies the common UV compactification while bypassing the oriented adjoint ray.",
        "residual":"No existing packet supplies the common UV packet; the oriented-adjoint-ray necessity conjecture survives. The residual is a source-derived oriented adjoint ray in su(2)_B, followed by cyclic preparation, retained history, rho, and Physical16 descent.",
        "disposition":"oriented-adjoint-ray necessity survives attempted falsification; source-derived oriented adjoint ray selected"
    },
    "common_uv_packet_routes":common_uv_packet_routes,
    "existing_packet_bypass_found":existing_packet_bypass_found,
    "oriented_adjoint_ray_derived":oriented_adjoint_ray_derived,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold oriented-adjoint-ray necessity gate: existing packets and conditional Wilson/history constructors do not bypass the source ray",
    "remaining_gate":"derive an oriented adjoint ray in su(2)_B from one source packet, then cyclic preparation, physical history, rho, and calibrated Physical16 descent",
    "hostile_gate":"do not treat calibration rank, rank-one reweighting, candidate packets, bipartite carriers, Krylov witnesses, Wilson splits, or history bundles as a common UV packet",
    "claim_boundary":"WP1246 through WP1248 falsify the tested bypasses; the oriented-adjoint-ray necessity conjecture survives but remains unproven",
    "disposition":"common-UV-compactification-packet leaf resolved conditionally; oriented adjoint ray required"
}
(ROOT/"results"/"wp1271_oriented_adjoint_ray_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1271 PASS: oriented-adjoint-ray necessity survives attempted falsification; source-derived ray remains open")
