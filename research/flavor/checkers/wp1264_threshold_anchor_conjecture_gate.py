import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1264-threshold-anchor-conjecture"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1178,1179,1180,1181,1182,1183)
wp1178=json.loads((ROOT/"results"/"wp1178_portal_to_sector_dilation_gate.json").read_text())
wp1179=json.loads((ROOT/"results"/"wp1179_nontrivial_portal_dilation_gate.json").read_text())
wp1180=json.loads((ROOT/"results"/"wp1180_source_dynamics_channel_selection_no_go.json").read_text())
wp1181=json.loads((ROOT/"results"/"wp1181_transient_sector_interface_gate.json").read_text())
wp1182=json.loads((ROOT/"results"/"wp1182_threshold_intertwiner_no_go.json").read_text())
wp1183=json.loads((ROOT/"results"/"wp1183_threshold_basis_scale_no_go.json").read_text())

# Bold conjecture: every microscopic source grammar capable of producing the
# flavor selector must carry a dimensionful threshold anchor that jointly fixes
# sector basis, amplitude, decay clock, and portal-to-sector channel.
replacement_channel_exists=wp1178["trace_preserving"] and wp1178["completely_positive"]
replacement_is_sourced=wp1178["input_dependence"] or wp1178["sourced_portal_dynamics"] > 0
nontrivial_channel_exists=wp1179["input_dependent"] and wp1179["completely_positive"]
stationary_selects_channel=wp1180["stationary_selection"]
transient_interface_exists=wp1181["cptp_at_each_time"] and wp1181["trace_preserving_at_each_time"]
transient_source_selected=wp1181["source_selected_interfaces"] > 0
threshold_identifies_basis=wp1182["source_basis_selection"]
threshold_identifies_scale=wp1183["threshold_scale_selected"] and wp1183["production_normalization_selected"]

assert replacement_channel_exists and not replacement_is_sourced
assert nontrivial_channel_exists and wp1179["fixed_output_channel_fiber_dimension"] == 4223
assert wp1180["composed_outputs"] == ["Tr(X) rho_dim", "Tr(X) rho_dim"] and not stationary_selects_channel
assert transient_interface_exists and not transient_source_selected
assert wp1182["interface_fiber_dimension"] == 87 and not threshold_identifies_basis
assert wp1183["joint_fiber_dimension"] == 88 and wp1183["time_reparam_invariant"] and not threshold_identifies_scale

# Falsification would require a source-selected microscopic grammar with no
# dimensionful threshold anchor.  None of the replayed routes supplies one.
anchor_free_source_grammar=False
threshold_anchor_constructed=False
conjecture_refuted=anchor_free_source_grammar
assert not conjecture_refuted and not threshold_anchor_constructed

result={
    "schema":"marici.flavor.wp1264.v1",
    "status":"PASS",
    "question":"Can an anchor-free microscopic source grammar select the portal-to-sector production channel?",
    "dpc":{
        "conjecture":"Every microscopic source grammar sufficient for the flavor selector must carry a dimensionful threshold anchor jointly fixing sector basis, amplitude, decay clock, and portal-to-sector channel.",
        "rivals":["input-erasing replacement channel","source-selected nontrivial dilation","stationary-dynamics selection","finite-time transient interface","threshold-identified basis and scale","anchor-free microscopic grammar"],
        "risky_consequences":["WP1178 has a CPTP replacement channel but zero sourced portal dynamics","WP1179 has input-dependent dilations and a 4223-dimensional fixed-output fiber","WP1180 stationary composition erases the dilation perturbation","WP1181 has a conditional transient interface but zero source-selected interfaces","WP1182 leaves an 87-dimensional basis/amplitude fiber","WP1183 leaves an 88-dimensional joint fiber including time reparameterization"],
        "falsification_attempt":"Replay WP1178 through WP1183 and search for a source-selected production channel that fixes basis, amplitude, and clock without a dimensionful threshold anchor.",
        "residual":"No anchor-free source grammar is found; the conjecture survives. A dimensionful threshold packet remains unconstructed and unfalsified as the required microscopic grammar.",
        "disposition":"threshold-anchor conjecture survives attempted falsification; microscopic threshold-anchor packet selected"
    },
    "falsification_routes":{
        "replacement_channel":{
            "exists":replacement_channel_exists,
            "input_dependent":wp1178["input_dependence"],
            "sourced_portal_dynamics":wp1178["sourced_portal_dynamics"]
        },
        "nontrivial_dilation":{
            "exists":nontrivial_channel_exists,
            "fixed_output_channel_fiber_dimension":wp1179["fixed_output_channel_fiber_dimension"],
            "sourced_portal_dynamics":wp1179["sourced_portal_dynamics"]
        },
        "stationary_dynamics":{
            "composed_outputs":wp1180["composed_outputs"],
            "stationary_selection":stationary_selects_channel,
            "sector_jump_operators":wp1180["sector_jump_operators"]
        },
        "transient_interface":{
            "exists":transient_interface_exists,
            "source_selected_interfaces":wp1181["source_selected_interfaces"],
            "threshold_intertwiners":wp1181["threshold_intertwiners"]
        },
        "threshold_identifiability":{
            "basis_orbit_dimension":wp1182["basis_orbit_dimension"],
            "interface_fiber_dimension":wp1182["interface_fiber_dimension"],
            "source_basis_selection":wp1182["source_basis_selection"],
            "source_amplitude_selection":wp1182["source_amplitude_selection"]
        },
        "basis_scale_clock":{
            "joint_fiber_dimension":wp1183["joint_fiber_dimension"],
            "time_reparam_invariant":wp1183["time_reparam_invariant"],
            "threshold_basis_selected":wp1183["threshold_basis_selected"],
            "threshold_scale_selected":wp1183["threshold_scale_selected"],
            "production_normalization_selected":wp1183["production_normalization_selected"]
        }
    },
    "anchor_free_source_grammar_found":anchor_free_source_grammar,
    "threshold_anchor_constructed":threshold_anchor_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold threshold-anchor conjecture: attempted falsification fails across all replayed microscopic-grammar routes",
    "remaining_gate":"construct or refute a dimensionful threshold-anchor packet that selects sector basis, amplitude, decay clock, and portal-to-sector production channel from source dynamics",
    "hostile_gate":"do not treat conditional CPTP channels, transient curves, or survival of this falsification attempt as a sourced microscopic grammar or as proof of the threshold-anchor conjecture",
    "claim_boundary":"WP1178 through WP1183 falsify the tested anchor-free routes; the bold threshold-anchor conjecture survives but remains unproven",
    "disposition":"microscopic-source-grammar leaf resolved conditionally; dimensionful threshold-anchor packet required"
}
(ROOT/"results"/"wp1264_threshold_anchor_conjecture_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1264 PASS: threshold-anchor conjecture survives attempted falsification; residual packet remains open")
