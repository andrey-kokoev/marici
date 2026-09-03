import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1262-boundary-instrument-falsification"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1160,1177))
wp1160=json.loads((ROOT/"results"/"wp1160_phase_lift_no_go.json").read_text())
wp1161=json.loads((ROOT/"results"/"wp1161_phase_compatible_constraint_census.json").read_text())
wp1162=json.loads((ROOT/"results"/"wp1162_split_minimal_amplitude_no_go.json").read_text())
wp1163=json.loads((ROOT/"results"/"wp1163_connected_minimal_amplitude_no_go.json").read_text())
wp1164=json.loads((ROOT/"results"/"wp1164_higher_constraint_amplitude_classification.json").read_text())
wp1165=json.loads((ROOT/"results"/"wp1165_three_c4_amplitude_no_go.json").read_text())
wp1166=json.loads((ROOT/"results"/"wp1166_c4c8_amplitude_no_go.json").read_text())
wp1167=json.loads((ROOT/"results"/"wp1167_boundary_unistochastic_inventory.json").read_text())
wp1168=json.loads((ROOT/"results"/"wp1168_support_five_graph_search.json").read_text())
wp1169=json.loads((ROOT/"results"/"wp1169_support_five_phase_obstruction.json").read_text())
wp1170=json.loads((ROOT/"results"/"wp1170_support_five_unistochastic_candidate.json").read_text())
wp1171=json.loads((ROOT/"results"/"wp1171_exact_unistochastic_certificate.json").read_text())
wp1172=json.loads((ROOT/"results"/"wp1172_production_realization_no_go.json").read_text())
wp1173=json.loads((ROOT/"results"/"wp1173_phase_gauge_production_law.json").read_text())
wp1174=json.loads((ROOT/"results"/"wp1174_physical16_channel_map_no_go.json").read_text())
wp1175=json.loads((ROOT/"results"/"wp1175_source_production_kernel_gate.json").read_text())
wp1176=json.loads((ROOT/"results"/"wp1176_uv_ensemble_matching_no_go.json").read_text())

# Support four cannot refute the one-boundary-instrument conjecture: the exact
# interior point and every regular or known boundary/irregular class fail the
# phase gate.
support_four_first_lift=False
support_four_constraint_census=True
support_four_split_consistent=wp1162["consistent_split_carriers"]
support_four_connected_interior=wp1163["phase_compatible_connected_interior_points"]
support_four_three_c4_interior=wp1165["phase_compatible_three_c4_interior_points"]
support_four_c4c8_interior=wp1166["phase_compatible_c4c8_interior_points"]
boundary_irregular_unistochastic=wp1167["unistochastic_candidates"]
assert not wp1160["phase_compatible"] and wp1160["phase_lift_certificates"] == 0
assert support_four_constraint_census and wp1161["minimum_total_two_overlap_constraints"] >= 18
assert support_four_split_consistent == 0
assert support_four_connected_interior == 0
assert support_four_three_c4_interior == 0
assert support_four_c4c8_interior == 0
assert boundary_irregular_unistochastic == 0

# Support five is the strongest algebraic survivor: it has graph-compatible
# fixed-q carriers and a rigorous exact real orthogonal solution.  Push that
# survivor through every production gate without adding boundary source data.
support_five_carriers=wp1168["linearly_feasible_derangement_carriers"] == 720
support_five_first_witness_lift=wp1169["phase_lift_certificates"]
support_five_numerical_candidate=wp1170["maximum_fixed_q_error"] < wp1170["tolerance"]
exact_support_five_unistochastic=wp1171["exact_real_orthogonal_solution_certified"]
assert support_five_carriers and support_five_first_witness_lift == 0
assert support_five_numerical_candidate and exact_support_five_unistochastic

physical_production_maps=wp1172["physical_production_maps"]
phase_quotient_constructed=wp1173["phase_gauge_law_constructed"]
sourced_channel_maps=wp1174["sourced_channel_maps"]
source_certificates=wp1175["source_certificates"]
boundary_state_available=wp1176["boundary_state_available"]
assert physical_production_maps == 0
assert phase_quotient_constructed and wp1173["physical_production_maps"] == 0
assert sourced_channel_maps == 0 and wp1174["explicit_nonidentifiability"]["channels_distinct"]
assert source_certificates == 0 and wp1175["kernel_rank"] == 1
assert not boundary_state_available and not wp1176["microstate_uniformity_forced"]

# The attempted refutation fails: the exact algebraic survivor does not supply
# a production map, selected channel, sourced kernel, or boundary state.  This
# is evidence for the conjecture's survival, not proof of the conjecture.
conjecture_refuted=False
boundary_packet_constructed=False
assert not conjecture_refuted and not boundary_packet_constructed

result={
    "schema":"marici.flavor.wp1262.v1",
    "status":"PASS",
    "question":"Can the strongest algebraic survivors falsify the one-boundary-instrument conjecture without new boundary source data?",
    "dpc":{
        "conjecture":"A support-four or exact support-five algebraic survivor can supply phase and physical production independently of the missing boundary instrument.",
        "rivals":["support-four interior phase lift","regular support-four carrier class","boundary or irregular candidate","exact support-five unistochastic survivor","modulus-to-production route","phase-gauge quotient","fitted physical16 channel","minimum-rank kernel","UV ensemble matching"],
        "risky_consequences":["WP1160 gives unequal two-overlap products 1/1764 and 83/5292","WP1161 imposes at least 18 two-overlap constraints on every support-four carrier","WP1162, WP1163, WP1165, and WP1166 leave no regular support-four interior class","WP1167 rejects all six known boundary or irregular candidates","WP1171 certifies an exact real orthogonal support-five fixed-q solution","WP1172 leaves 11 unobserved phase parameters and no production components","WP1174 leaves a 69-dimensional generic channel fiber","WP1175 and WP1176 supply no source certificate or boundary state"],
        "falsification_attempt":"Replay WP1160 through WP1176 and force the strongest exact support-five survivor through production, phase-gauge, channel, kernel, and UV-state gates without adding boundary source data.",
        "residual":"The conjecture survives this attempt; a boundary density/instrument packet or an independent lawful composition remains required.",
        "disposition":"attempted refutation fails conditionally; boundary-density instrument rival selected"
    },
    "support_four_phase_test":{
        "first_point_phase_compatible":support_four_first_lift,
        "blocking_row_pair":wp1160["blocking_row_pair"],
        "shared_columns":wp1160["shared_columns"],
        "amplitude_products":wp1160["amplitude_products"],
        "minimum_total_two_overlap_constraints":wp1161["minimum_total_two_overlap_constraints"],
        "split_consistent_carriers":support_four_split_consistent,
        "connected_interior_points":support_four_connected_interior,
        "three_c4_interior_points":support_four_three_c4_interior,
        "c4c8_interior_points":support_four_c4c8_interior,
        "boundary_irregular_unistochastic_candidates":boundary_irregular_unistochastic
    },
    "support_five_strongest_survivor":{
        "linearly_feasible_derangement_carriers":wp1168["linearly_feasible_derangement_carriers"],
        "first_witness_phase_lift_certificates":support_five_first_witness_lift,
        "numerical_candidate_maximum_fixed_q_error":wp1170["maximum_fixed_q_error"],
        "exact_real_orthogonal_solution_certified":exact_support_five_unistochastic,
        "krawczyk_contraction_infinity_norm":wp1171["krawczyk_contraction_infinity_norm"]
    },
    "production_admission":{
        "phase_orbit_dimension":wp1172["phase_orbit_dimension"],
        "production_components":wp1172["production_components"],
        "physical_production_maps":physical_production_maps,
        "phase_quotient_constructed":phase_quotient_constructed,
        "sourced_channel_maps":sourced_channel_maps,
        "generic_channel_fiber_dimension":wp1174["generic_fiber_dimension"],
        "minimum_rank_kernel":wp1175["kernel"],
        "kernel_source_certificates":source_certificates,
        "boundary_state_available":boundary_state_available,
        "density_fiber_dimension":wp1176["density_fiber_dimension"]
    },
    "one_boundary_instrument_conjecture_refuted":conjecture_refuted,
    "boundary_packet_constructed":boundary_packet_constructed,
    "classification":"falsification gate: strongest algebraic survivor does not refute the one-boundary-instrument conjecture",
    "remaining_gate":"derive a boundary density/instrument packet, or refute the conjecture by independently composing production, clock, channel, matching, and calibrated physical16 descent",
    "hostile_gate":"do not treat survival of this falsification attempt as proof of the conjecture, and do not promote the exact support-five modulus to a boundary packet",
    "claim_boundary":"WP1160 through WP1176 establish exact algebraic and production no-go facts; the one-boundary-instrument conjecture remains a surviving research hypothesis, not a theorem",
    "disposition":"one-boundary-instrument falsification gate resolved conditionally; boundary-density instrument rival selected"
}
(ROOT/"results"/"wp1262_boundary_instrument_falsification_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1262 PASS: strongest algebraic survivor fails to refute boundary-instrument conjecture")
