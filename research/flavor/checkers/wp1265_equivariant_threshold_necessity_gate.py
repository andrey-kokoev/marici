import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1265-equivariant-threshold-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1184,1190,1192,1193,1200,1201,1205)
wp1184=json.loads((ROOT/"results"/"wp1184_dimensionful_threshold_anchor_no_go.json").read_text())
wp1190=json.loads((ROOT/"results"/"wp1190_spectral_flow_clock_no_go.json").read_text())
wp1192=json.loads((ROOT/"results"/"wp1192_rg_event_anchor_gate.json").read_text())
wp1193=json.loads((ROOT/"results"/"wp1193_physical_running_observable_gate.json").read_text())
wp1200=json.loads((ROOT/"results"/"wp1200_equivariant_index_source_gate.json").read_text())
wp1201=json.loads((ROOT/"results"/"wp1201_spurion_alignment_source_gate.json").read_text())
wp1205=json.loads((ROOT/"results"/"wp1205_threshold_intertwiner_gate.json").read_text())

# Bold necessity conjecture: no dimensionful threshold anchor can be sourced
# without a protected equivariant-index/character-transport packet.
non_equivariant_candidates={
    "rg_transmutation":{
        "conditional_rg_scale_available":wp1184["conditional_rg_scale_available"],
        "threshold_anchor_selected":wp1184["threshold_anchor_selected"],
        "physical_threshold_packet":wp1184["physical_threshold_packet"],
        "combined_threshold_fiber_dimension":wp1184["combined_threshold_fiber_dimension"]
    },
    "spectral_flow_clock":{
        "spectral_flow_orientation_selected":wp1190["spectral_flow_orientation_selected"],
        "spectral_flow_clock_law":wp1190["spectral_flow_clock_law"],
        "common_clock_selected":wp1190["common_clock_selected"]
    },
    "intrinsic_rg_event_anchor":{
        "translation_fiber_repaired":wp1192["translation_fiber_repaired"],
        "scheme_descent":wp1192["scheme_descent"],
        "physical_running_observable":wp1192["physical_running_observable"]
    },
    "canonical_effective_charge":{
        "physical_running_records_exist":wp1193["physical_running_records_exist"],
        "canonical_running_observable":wp1193["canonical_running_observable"],
        "common_gain_instrument":wp1193["common_gain_instrument"]
    }
}
non_equivariant_anchor_found=any(
    route.get("threshold_anchor_selected",False)
    or route.get("physical_threshold_packet",False)
    or route.get("common_clock_selected",False)
    or route.get("physical_running_observable",False)
    or route.get("canonical_running_observable",False)
    for route in non_equivariant_candidates.values()
)
assert not non_equivariant_anchor_found
assert wp1184["combined_threshold_fiber_dimension"] == 89
assert wp1190["clock_fiber_dimensions"] == 2
assert wp1192["scheme_resultant"] == "110592"
assert wp1193["portal_records"] == ["1/2","9/16"]

# The proposed protected equivariant route also remains incomplete, so the
# necessity conjecture survives without being proved or constructed.
equivariant_route={
    "incidence_equivariant_index":wp1200["incidence_equivariant_index"],
    "spurion_equivariant_lift":wp1200["spurion_equivariant_lift"],
    "primitive_character_transport":wp1200["primitive_character_transport"],
    "spurion_alignment_in_model":wp1201["alignment_selected_in_model"],
    "source_completion_authority":wp1201["source_completion_authority"],
    "index_transport":wp1201["index_transport"],
    "isometric_marked_threshold":wp1205["isometric_marked_threshold"],
    "calibrated_readout":wp1205["calibrated_readout"]
}
assert equivariant_route["spurion_equivariant_lift"]
assert not equivariant_route["incidence_equivariant_index"]
assert not equivariant_route["primitive_character_transport"]
assert equivariant_route["spurion_alignment_in_model"] and not equivariant_route["source_completion_authority"]
assert not equivariant_route["index_transport"]
assert not equivariant_route["isometric_marked_threshold"] and not equivariant_route["calibrated_readout"]

protected_equivariant_anchor_constructed=False
conjecture_refuted=non_equivariant_anchor_found
assert not protected_equivariant_anchor_constructed and not conjecture_refuted

result={
    "schema":"marici.flavor.wp1265.v1",
    "status":"PASS",
    "question":"Can a replayed non-equivariant route source the dimensionful threshold anchor without protected equivariant-index transport?",
    "dpc":{
        "conjecture":"Every source-derived dimensionful threshold anchor for the flavor selector must pass through a protected equivariant-index or character-transport packet.",
        "rivals":["RG dimensional transmutation","spectral-flow clock","intrinsic RG event anchor","canonical effective charge","protected equivariant spurion index","non-equivariant threshold anchor"],
        "risky_consequences":["WP1184 leaves an 89-dimensional threshold fiber","WP1190 leaves two clock-fiber dimensions","WP1192's intrinsic anchor fails scheme descent with resultant 110592","WP1193 has distinct portal records 1/2 and 9/16","WP1200 incidence fails equivariance and primitive character transport","WP1201 selects the ray only in a declared model","WP1205 requires identity marked-port transport and lacks calibrated readout"],
        "falsification_attempt":"Replay the non-equivariant RG, spectral, event-anchor, and effective-charge routes and search for any sourced dimensionful threshold anchor that bypasses protected equivariant transport.",
        "residual":"No non-equivariant anchor is found, so the necessity conjecture survives. The protected equivariant-index packet itself remains unconstructed, so the conjecture is not proven.",
        "disposition":"equivariant-threshold necessity survives attempted falsification; protected index-transport packet selected"
    },
    "non_equivariant_candidates":non_equivariant_candidates,
    "equivariant_route_status":equivariant_route,
    "non_equivariant_anchor_found":non_equivariant_anchor_found,
    "protected_equivariant_anchor_constructed":protected_equivariant_anchor_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold equivariant-threshold necessity gate: all replayed bypass routes fail to source the threshold anchor",
    "remaining_gate":"construct a protected equivariant-index/character-transport packet, or refute necessity by sourcing a dimensionful threshold anchor without one",
    "hostile_gate":"do not treat failure of bypass routes as proof of necessity, and do not treat conditional spurion alignment or character sewing as a sourced threshold anchor",
    "claim_boundary":"WP1184, WP1190, WP1192, WP1193, WP1200, WP1201, and WP1205 support the attempted falsification; the conjecture survives only over those replayed routes",
    "disposition":"dimensionful-threshold-anchor leaf resolved conditionally; protected equivariant-index transport required"
}
(ROOT/"results"/"wp1265_equivariant_threshold_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1265 PASS: equivariant-threshold necessity survives attempted falsification; protected index transport remains open")
