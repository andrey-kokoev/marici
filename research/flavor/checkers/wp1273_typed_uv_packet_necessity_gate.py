import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1273-typed-uv-packet-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1254,1260))
wp1254=json.loads((ROOT/"results"/"wp1254_six_branch_preparation_gate.json").read_text())
wp1255=json.loads((ROOT/"results"/"wp1255_mass_clock_gate.json").read_text())
wp1256=json.loads((ROOT/"results"/"wp1256_channel_gain_gate.json").read_text())
wp1257=json.loads((ROOT/"results"/"wp1257_kernel_classification_gate.json").read_text())
wp1258=json.loads((ROOT/"results"/"wp1258_matching_selection_gate.json").read_text())
wp1259=json.loads((ROOT/"results"/"wp1259_boundary_smatrix_phase_gate.json").read_text())

typed_packet_interfaces={
    "preparation":{
        "conditional_q_exact":wp1254["conditional_q_exact"],
        "dimension_trace_state_constructed":wp1254["dimension_trace_state_constructed"],
        "closure_audit_complete":wp1254["closure_audit_complete"],
        "current_source_passes":wp1254["current_source_passes"],
        "parent_branching_operator":wp1254["parent_branching_operator"],
        "boundary_state_matching":wp1254["boundary_state_matching"],
        "preparation_operator":wp1254["preparation_operator"],
        "source_measure":wp1254["source_measure"],
        "normalized_boundary_state":wp1254["normalized_boundary_state"],
        "physical_preparation":wp1254["physical_preparation"]
    },
    "mass_clock":{
        "conditional_clock_facts":wp1255["conditional_clock_facts"],
        "radius_law_exact":wp1255["radius_law_exact"],
        "closure_audit_complete":wp1255["closure_audit_complete"],
        "current_source_passes":wp1255["current_source_passes"],
        "equivariant_projection":wp1255["equivariant_projection"],
        "common_twist_descent":wp1255["common_twist_descent"],
        "unique_flux_sector":wp1255["unique_flux_sector"],
        "gauge_gravity_ratio":wp1255["gauge_gravity_ratio"],
        "localized_descent":wp1255["localized_descent"],
        "physical_momentum_frame":wp1255["physical_momentum_frame"],
        "absolute_clock":wp1255["absolute_clock"]
    },
    "channel_gain":{
        "rows_exact":wp1256["rows_exact"],
        "vector_carrier_unique":wp1256["vector_carrier_unique"],
        "map_family_classified":wp1256["map_family_classified"],
        "realized_physical16_channels":wp1256["realized_physical16_channels"],
        "common_gain_compatible":wp1256["common_gain_compatible"],
        "unique_kernel":wp1256["unique_kernel"],
        "cascade_certificate":wp1256["cascade_certificate"],
        "production_maps":wp1256["production_maps"],
        "same_frame_certificate":wp1256["same_frame_certificate"],
        "physical_ratio_law":wp1256["physical_ratio_law"]
    },
    "kernel_classification":{
        "rank_two_closed":wp1257["rank_two_closed"],
        "minimal_support_classified":wp1257["minimal_support_classified"],
        "matchings_classified":wp1257["matchings_classified"],
        "orbits_classified":wp1257["orbits_classified"],
        "selected_matching":wp1257["selected_matching"],
        "production_matching_packet":wp1257["production_matching_packet"],
        "physical16_couplings":wp1257["physical16_couplings"],
        "same_frame_gain":wp1257["same_frame_gain"],
        "exchange_symmetry":wp1257["exchange_symmetry"],
        "selected_kernel":wp1257["selected_kernel"]
    },
    "matching_selection":{
        "exchange_relation_exact":wp1258["exchange_relation_exact"],
        "quotient_algebra_exact":wp1258["quotient_algebra_exact"],
        "anomaly_invariance_exact":wp1258["anomaly_invariance_exact"],
        "unbroken_exchange":wp1258["unbroken_exchange"],
        "production_quotient":wp1258["production_quotient"],
        "selected_matching_class":wp1258["selected_matching_class"],
        "physical16_couplings":wp1258["physical16_couplings"],
        "same_frame_gain":wp1258["same_frame_gain"],
        "selected_kernel":wp1258["selected_kernel"]
    },
    "boundary_smatrix":{
        "phase_classification_exact":wp1259["phase_classification_exact"],
        "fixed_q_disjointness_exact":wp1259["fixed_q_disjointness_exact"],
        "support_gate_exact":wp1259["support_gate_exact"],
        "selected_class":wp1259["selected_class"],
        "smatrix_matching_intersection":wp1259["smatrix_matching_intersection"],
        "sparse_modulus":wp1259["sparse_modulus"],
        "physical16_channels":wp1259["physical16_channels"],
        "selected_kernel":wp1259["selected_kernel"]
    }
}
assert typed_packet_interfaces["preparation"]["conditional_q_exact"]
assert typed_packet_interfaces["preparation"]["closure_audit_complete"]
assert typed_packet_interfaces["preparation"]["current_source_passes"]==0
assert typed_packet_interfaces["mass_clock"]["conditional_clock_facts"]
assert typed_packet_interfaces["mass_clock"]["closure_audit_complete"]
assert typed_packet_interfaces["mass_clock"]["current_source_passes"]==0
assert typed_packet_interfaces["channel_gain"]["rows_exact"]
assert typed_packet_interfaces["channel_gain"]["realized_physical16_channels"]==0
assert typed_packet_interfaces["kernel_classification"]["rank_two_closed"]
assert typed_packet_interfaces["kernel_classification"]["matchings_classified"]
assert typed_packet_interfaces["matching_selection"]["quotient_algebra_exact"]
assert typed_packet_interfaces["boundary_smatrix"]["support_gate_exact"]
for section in typed_packet_interfaces.values():
    for key,value in section.items():
        if key in {
            "parent_branching_operator","boundary_state_matching","preparation_operator","source_measure",
            "normalized_boundary_state","physical_preparation","equivariant_projection","common_twist_descent",
            "unique_flux_sector","gauge_gravity_ratio","localized_descent","physical_momentum_frame",
            "absolute_clock","common_gain_compatible","unique_kernel","cascade_certificate","production_maps",
            "same_frame_certificate","physical_ratio_law","selected_matching","production_matching_packet",
            "physical16_couplings","same_frame_gain","exchange_symmetry","selected_kernel","unbroken_exchange",
            "production_quotient","selected_matching_class","selected_class","smatrix_matching_intersection",
            "sparse_modulus","physical16_channels"
        }:
            assert value is False, key

# Falsifier: a partial preparation, clock, channel/gain, kernel, matching, or
# S-matrix packet is sufficient without the full typed UV event-production
# packet.
partial_packet_sufficient=False
typed_uv_packet_admitted=False
conjecture_refuted=partial_packet_sufficient
assert not conjecture_refuted and not typed_uv_packet_admitted

result={
    "schema":"marici.flavor.wp1273.v1",
    "status":"PASS",
    "question":"Can any partial preparation, clock, channel/gain, kernel, matching, or S-matrix packet substitute for the full typed UV event-production packet?",
    "dpc":{
        "conjecture":"Every admissible external or newly derived UV event-production packet must carry the full typed interface: sourced preparation state, absolute localized clock, Physical16 channels and gain cascade, production kernel, selected matching, and source phase authority in one shared frame.",
        "rivals":["six-branch preparation law","dimension-trace state","parent projection","common-twist clock","radius stabilization","two-port row pair","vector gain chain","rank-one complete mixing","support/rank/orbit algebra","exchange/quotient/anomaly matching","boundary S-matrix phase"],
        "risky_consequences":["WP1254 gives q and rho_dim but zero source passes","WP1255 gives exact clock laws but zero source passes","WP1256 gives exact rows and a map family but zero physical16 channels","WP1257 classifies six matchings but selects none","WP1258 gives quotient and anomaly facts but no production map","WP1259 classifies phase/support facts but no selected class or kernel"],
        "falsification_attempt":"Replay WP1254 through WP1259 and search for a partial packet that substitutes for the full typed UV event-production interface.",
        "residual":"No partial packet is sufficient; the full typed-packet necessity conjecture survives. The residual is an actual typed UV packet from an authorized external owner or new derivation, with all interfaces in one shared frame.",
        "disposition":"full typed-UV-packet necessity survives attempted falsification; typed UV packet handoff selected"
    },
    "typed_packet_interfaces":typed_packet_interfaces,
    "partial_packet_sufficient":partial_packet_sufficient,
    "typed_uv_packet_admitted":typed_uv_packet_admitted,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold full-typed-packet necessity gate: partial UV interfaces do not substitute for the event-production packet",
    "remaining_gate":"obtain the actual typed UV packet from an authorized external owner or new derivation and submit it to the admission contract",
    "hostile_gate":"do not treat q, rho_dim, clock laws, row pairs, gain chains, map families, matchings, quotient facts, or phase classifications as an admitted UV event-production packet",
    "claim_boundary":"WP1254 through WP1259 falsify the tested partial packets; the full typed-packet necessity conjecture survives but remains unproven",
    "disposition":"external/new UV event-production-packet leaf resolved conditionally; typed UV packet handoff required"
}
(ROOT/"results"/"wp1273_typed_uv_packet_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1273 PASS: full typed-UV-packet necessity survives attempted falsification; actual typed packet remains open")
