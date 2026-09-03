import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1272-sourced-boundary-character-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1249,1254))
wp1249=json.loads((ROOT/"results"/"wp1249_oriented_adjoint_direction_gate.json").read_text())
wp1250=json.loads((ROOT/"results"/"wp1250_normalized_dual_cycle_orientation_gate.json").read_text())
wp1251=json.loads((ROOT/"results"/"wp1251_fused_defect_analytic_constraints_gate.json").read_text())
wp1252=json.loads((ROOT/"results"/"wp1252_orientation_odd_boundary_datum_gate.json").read_text())
wp1253=json.loads((ROOT/"results"/"wp1253_sourced_boundary_character_gate.json").read_text())

oriented_ray_routes={
    "admitted_selectors":{
        "reciprocal_rho_closed":wp1249["reciprocal_rho_closed"],
        "natural_scalar_rho_closed":wp1249["natural_scalar_rho_closed"],
        "wilson_kernel_closed":wp1249["wilson_kernel_closed"],
        "history_gain_closed":wp1249["history_gain_closed"],
        "bare_lattice_orientation_closed":wp1249["bare_lattice_orientation_closed"],
        "normalized_dual_cycle":wp1249["normalized_dual_cycle"],
        "oriented_generator":wp1249["oriented_generator"],
        "integer_lift":wp1249["integer_lift"],
        "clock_orientation":wp1249["clock_orientation"],
        "independent_rho":wp1249["independent_rho"],
        "production_kernel":wp1249["production_kernel"],
        "gain_3_over_2":wp1249["gain_3_over_2"],
        "physical16_descent":wp1249["physical16_descent"]
    },
    "dual_cycle":{
        "six_output_interface":wp1250["six_output_interface"],
        "packet_classes_classified":wp1250["packet_classes_classified"],
        "existing_defect_excluded":wp1250["existing_defect_excluded"],
        "field_fiber_23":wp1250["field_fiber_23"],
        "normalized_dual_cycle":wp1250["normalized_dual_cycle"],
        "oriented_generator":wp1250["oriented_generator"],
        "integer_clock_lift":wp1250["integer_clock_lift"],
        "absolute_boundary_lift":wp1250["absolute_boundary_lift"],
        "independent_rho":wp1250["independent_rho"],
        "production_and_gain":wp1250["production_and_gain"],
        "physical16_descent":wp1250["physical16_descent"],
        "fused_packet_constructed":wp1250["fused_packet_constructed"]
    },
    "fused_defect_constraints":{
        "constraint_fiber":wp1251["constraint_fiber"],
        "local_split_fiber":wp1251["local_split_fiber"],
        "endpoint_exchange_closed":wp1251["endpoint_exchange_closed"],
        "wilson_orientation_closed":wp1251["wilson_orientation_closed"],
        "extended_rho_closed":wp1251["extended_rho_closed"],
        "quotient_production_closed":wp1251["quotient_production_closed"],
        "orientation_odd_datum":wp1251["orientation_odd_datum"],
        "selected_split":wp1251["selected_split"],
        "independent_rho":wp1251["independent_rho"],
        "production_kernel":wp1251["production_kernel"],
        "physical16_descent":wp1251["physical16_descent"],
        "source_values":wp1251["source_values"]
    },
    "orientation_odd_boundary":{
        "hadamard_classification":wp1252["hadamard_classification"],
        "kronecker_algebra":wp1252["kronecker_algebra"],
        "complete_mixing_sourced":wp1252["complete_mixing_sourced"],
        "irreversible_mixing_sourced":wp1252["irreversible_mixing_sourced"],
        "c6_generator_sourced":wp1252["c6_generator_sourced"],
        "endpoint_symmetry":wp1252["endpoint_symmetry"],
        "anomaly_phase_provenance":wp1252["anomaly_phase_provenance"],
        "residue_channels":wp1252["residue_channels"],
        "orientation_odd_datum":wp1252["orientation_odd_datum"],
        "selected_split":wp1252["selected_split"],
        "clock_orientation":wp1252["clock_orientation"],
        "physical16_channels":wp1252["physical16_channels"],
        "source_values":wp1252["source_values"]
    },
    "sourced_boundary_character":{
        "closure_audit_complete":wp1253["closure_audit_complete"],
        "admission_contract_constructed":wp1253["admission_contract_constructed"],
        "corpus_scan_complete":wp1253["corpus_scan_complete"],
        "current_source_passes":wp1253["current_source_passes"],
        "actual_packets_supplied":wp1253["actual_packets_supplied"],
        "admissible_corpus_packets":wp1253["admissible_corpus_packets"],
        "sourced_character":wp1253["sourced_character"],
        "six_channels":wp1253["six_channels"],
        "phase_observable":wp1253["phase_observable"],
        "production_kernel":wp1253["production_kernel"],
        "event_map":wp1253["event_map"],
        "physical16_descent":wp1253["physical16_descent"]
    }
}
assert oriented_ray_routes["admitted_selectors"]["reciprocal_rho_closed"]
assert oriented_ray_routes["admitted_selectors"]["natural_scalar_rho_closed"]
assert oriented_ray_routes["admitted_selectors"]["bare_lattice_orientation_closed"]
assert oriented_ray_routes["dual_cycle"]["six_output_interface"] and oriented_ray_routes["dual_cycle"]["field_fiber_23"]
assert oriented_ray_routes["fused_defect_constraints"]["constraint_fiber"] and oriented_ray_routes["fused_defect_constraints"]["local_split_fiber"]
assert oriented_ray_routes["orientation_odd_boundary"]["hadamard_classification"] and oriented_ray_routes["orientation_odd_boundary"]["kronecker_algebra"]
assert oriented_ray_routes["sourced_boundary_character"]["closure_audit_complete"]
assert oriented_ray_routes["sourced_boundary_character"]["admission_contract_constructed"]
assert oriented_ray_routes["sourced_boundary_character"]["corpus_scan_complete"]
assert oriented_ray_routes["sourced_boundary_character"]["current_source_passes"]==0
assert oriented_ray_routes["sourced_boundary_character"]["actual_packets_supplied"]==0
assert oriented_ray_routes["sourced_boundary_character"]["admissible_corpus_packets"]==0
for section in oriented_ray_routes.values():
    for key,value in section.items():
        if key in {
            "normalized_dual_cycle","oriented_generator","integer_lift","clock_orientation","independent_rho",
            "production_kernel","gain_3_over_2","physical16_descent","integer_clock_lift","absolute_boundary_lift",
            "production_and_gain","fused_packet_constructed","orientation_odd_datum","selected_split",
            "source_values","complete_mixing_sourced","irreversible_mixing_sourced","c6_generator_sourced",
            "endpoint_symmetry","anomaly_phase_provenance","residue_channels","physical16_channels",
            "sourced_character","six_channels","phase_observable","event_map"
        }:
            assert value is False, key

# Falsifier: the current source or existing corpus supplies an oriented adjoint
# ray while bypassing a sourced boundary character carrying channels, phases,
# production kernel, event map, and Physical16 descent.
current_corpus_bypass_found=False
sourced_boundary_character_derived=False
conjecture_refuted=current_corpus_bypass_found
assert not conjecture_refuted and not sourced_boundary_character_derived

result={
    "schema":"marici.flavor.wp1272.v1",
    "status":"PASS",
    "question":"Can the current source or existing corpus supply an oriented adjoint ray while bypassing a sourced boundary character?",
    "dpc":{
        "conjecture":"Every source-derived oriented adjoint ray sufficient for the common UV packet must be carried by a sourced boundary character with six channels, a selected-packet-preserving phase observable, a production kernel, an event/readout map, and calibrated Physical16 descent.",
        "rivals":["reciprocal determinant rho","natural scalar rho","Wilson production kernel","history gain","absolute coset lift","integer clock lift","finite-scheme ports","contact counterterm","bare integral lattice","fused defect constraints","endpoint exchange","extended line","quotient descent","Hadamard algebra","anomaly phases","Green residues","existing corpus"],
        "risky_consequences":["WP1249 closes all admitted selectors","WP1250 gives the 23-field fused-defect fiber but no constructed values","WP1251 gives exact constraints and split fibers but no orientation-odd datum","WP1252 classifies H6/F3 tensor F2 but no sourced generator, phase provenance, or channels","WP1253 finds zero current-source passes and zero admissible corpus packets"],
        "falsification_attempt":"Replay WP1249 through WP1253 and search the current source and corpus for an oriented ray that bypasses the sourced boundary character.",
        "residual":"No current or corpus route supplies the oriented adjoint ray; the sourced-boundary-character necessity conjecture survives. The residual is an external or newly derived UV event-production packet admitted by the WP1128 contract.",
        "disposition":"sourced-boundary-character necessity survives attempted falsification; external/new UV event-production packet selected"
    },
    "oriented_ray_routes":oriented_ray_routes,
    "current_corpus_bypass_found":current_corpus_bypass_found,
    "sourced_boundary_character_derived":sourced_boundary_character_derived,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold sourced-boundary-character necessity gate: current source and corpus do not bypass the event-production packet",
    "remaining_gate":"obtain an external or newly derived UV event-production packet with six channels, phase observable, production kernel, event map, and calibrated Physical16 descent",
    "hostile_gate":"do not treat determinant scalars, Wilson/history constructors, coset lifts, finite ports, fused-defect constraints, Hadamard algebra, anomaly integers, Green residues, or corpus mentions as a sourced boundary character",
    "claim_boundary":"WP1249 through WP1253 falsify the tested current-source and corpus routes; the sourced-boundary-character necessity conjecture survives but remains unproven",
    "disposition":"oriented-adjoint-ray leaf resolved conditionally; external/new UV event-production packet required"
}
(ROOT/"results"/"wp1272_sourced_boundary_character_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1272 PASS: sourced-boundary-character necessity survives attempted falsification; external/new UV packet remains open")
