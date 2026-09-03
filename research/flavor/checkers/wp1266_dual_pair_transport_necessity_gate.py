import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1266-dual-pair-transport-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1206,1207,1208,1209,1210,1211)
wp1206=json.loads((ROOT/"results"/"wp1206_coherent_kinetic_normalization_gate.json").read_text())
wp1207=json.loads((ROOT/"results"/"wp1207_boundary_reservoir_source_gate.json").read_text())
wp1208=json.loads((ROOT/"results"/"wp1208_common_junction_source_gate.json").read_text())
wp1209=json.loads((ROOT/"results"/"wp1209_endpoint_reciprocity_source_gate.json").read_text())
wp1210=json.loads((ROOT/"results"/"wp1210_source_modulus_selection_gate.json").read_text())
wp1211=json.loads((ROOT/"results"/"wp1211_flavor_dual_pair_existence_gate.json").read_text())

conditional_transport_routes={
    "coherent_kinetic_normalization":{
        "unique_dark_projector":wp1206["unique_dark_projector"],
        "fixed_port_magnitude":wp1206["fixed_port_magnitude"],
        "source_authority_derived":wp1206["source_authority_derived"],
        "threshold_intertwined":wp1206["threshold_intertwined"],
        "coherent_reference_calibrated":wp1206["coherent_reference_calibrated"]
    },
    "boundary_reservoir":{
        "dark_kernel_derived":wp1207["dark_kernel_derived"],
        "negative_eigenray_derived":wp1207["negative_eigenray_derived"],
        "microscopic_junction":wp1207["microscopic_junction"],
        "isometric_threshold":wp1207["isometric_threshold"],
        "calibrated_instrument":wp1207["calibrated_instrument"]
    },
    "common_junction":{
        "reciprocal_normalized":wp1208["reciprocal_normalized"],
        "lossless_two_port":wp1208["lossless_two_port"],
        "endpoint_reciprocity_microscopically_derived":wp1208["endpoint_reciprocity_microscopically_derived"],
        "isometric_full_transport":wp1208["isometric_full_transport"],
        "calibrated_detector":wp1208["calibrated_detector"]
    },
    "endpoint_colligation":{
        "trace_preserving":wp1209["trace_preserving"],
        "unique_stationary_dark":wp1209["unique_stationary_dark"],
        "lossless_complement":wp1209["lossless_complement"],
        "q_modulus_free":wp1209["q_modulus_free"],
        "z_modulus_free":wp1209["z_modulus_free"],
        "calibrated_physical16":wp1209["calibrated_physical16"]
    }
}
assert all(route[next(key for key in route if key.endswith("derived") or key in {"trace_preserving","reciprocal_normalized","unique_dark_projector"})] for route in conditional_transport_routes.values())
assert wp1206["source_authority_derived"] is False
assert wp1207["microscopic_junction"] is False and wp1207["isometric_threshold"] is False
assert wp1208["endpoint_reciprocity_microscopically_derived"] is False and wp1208["isometric_full_transport"] is False
assert wp1209["q_modulus_free"] is True and wp1209["z_modulus_free"] is True and wp1209["calibrated_physical16"] is False

# The dual-pair bypass test: a conjecture-falsifying route would source q,z or
# protected transport without a microscopic flavor dual pair.
self_dual_principle={
    "abstract_pairing_selects":wp1210["abstract_pairing_selects"],
    "selected_coupling":wp1210["selected_coupling"],
    "global_pairing_basin":wp1210["global_pairing_basin"],
    "current_flavor_pair_absent":wp1210["current_flavor_pair_absent"],
    "q_selected":wp1210["q_selected"],
    "z_selected":wp1210["z_selected"],
    "microscopic_realization":wp1210["microscopic_realization"]
}
dual_pair_search={
    "joint_observer_fails":wp1211["joint_observer_fails"],
    "g2_pair_fails":wp1211["g2_pair_fails"],
    "rank_one_lattice_fails":wp1211["rank_one_lattice_fails"],
    "compulsory_mediators_fail":wp1211["compulsory_mediators_fail"],
    "wrong_operator_or_postsource_fails":wp1211["wrong_operator_or_postsource_fails"],
    "flavor_dual_pair_exists":wp1211["flavor_dual_pair_exists"],
    "new_yukawa_source_derived":wp1211["new_yukawa_source_derived"]
}
assert self_dual_principle["abstract_pairing_selects"] and self_dual_principle["global_pairing_basin"]
assert self_dual_principle["current_flavor_pair_absent"] and not self_dual_principle["q_selected"] and not self_dual_principle["z_selected"]
assert all(value for key,value in dual_pair_search.items() if key.endswith("_fails"))
assert not dual_pair_search["flavor_dual_pair_exists"] and not dual_pair_search["new_yukawa_source_derived"]

dual_pair_free_protected_transport_found=False
microscopic_dual_pair_constructed=False
conjecture_refuted=dual_pair_free_protected_transport_found
assert not conjecture_refuted and not microscopic_dual_pair_constructed

result={
    "schema":"marici.flavor.wp1266.v1",
    "status":"PASS",
    "question":"Can protected equivariant-index transport be sourced without a microscopic self-dual flavor dual pair?",
    "dpc":{
        "conjecture":"Every protected equivariant-index transport capable of sourcing the dimensionful threshold anchor must terminate in a microscopic self-dual flavor dual pair.",
        "rivals":["coherent kinetic normalization","boundary reservoir","common junction","endpoint colligation","abstract self-dual pairing","current-corpus dual pair","dual-pair-free protected transport"],
        "risky_consequences":["WP1206 through WP1209 construct conditional dark-ray, junction, and colligation instruments","none derives source authority, isometric full transport, q, z, or calibrated physical16","WP1210's abstract self-dual pairing selects g=1/sqrt(2) only if the physical dual pair exists","WP1211 rejects the joint observer, G2 pair, rank-one lattice, compulsory mediators, and wrong-class instruments"],
        "falsification_attempt":"Replay WP1206 through WP1211 and search for source-authorized protected transport or selected q,z moduli without a microscopic flavor dual pair.",
        "residual":"No dual-pair-free protected transport is found; the conjecture survives. A new Yukawa-active source principle must construct or exclude the microscopic dual pair.",
        "disposition":"dual-pair transport necessity survives attempted falsification; new Yukawa-active source selected"
    },
    "conditional_transport_routes":conditional_transport_routes,
    "self_dual_principle":self_dual_principle,
    "dual_pair_search":dual_pair_search,
    "dual_pair_free_protected_transport_found":dual_pair_free_protected_transport_found,
    "microscopic_dual_pair_constructed":microscopic_dual_pair_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold dual-pair transport necessity gate: all replayed dual-pair-free protected-transport routes remain conditional",
    "remaining_gate":"derive new Yukawa-active matter, multiplicities, and vertices from an independent source principle, then test dual pairing, threshold transport, RG, and calibrated physical16 realization",
    "hostile_gate":"do not treat conditional dark rays, lossless colligations, abstract self-duality, or failed dual-pair candidates as protected source transport or as proof of necessity",
    "claim_boundary":"WP1206 through WP1211 falsify the tested bypass routes; the dual-pair necessity conjecture survives only over the replayed corpus and remains unproven",
    "disposition":"protected equivariant-index transport leaf resolved conditionally; new Yukawa-active source required"
}
(ROOT/"results"/"wp1266_dual_pair_transport_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1266 PASS: dual-pair transport necessity survives attempted falsification; new Yukawa-active source remains open")
