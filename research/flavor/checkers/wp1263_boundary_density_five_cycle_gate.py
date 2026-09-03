import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1263-five-cycle-boundary-density"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1177,1246,1254,1255,1256,1257,1258)
wp1177=json.loads((ROOT/"results"/"wp1177_uv_boundary_density_no_go.json").read_text())
wp1246=json.loads((ROOT/"results"/"wp1246_common_uv_boundary_action_packet_gate.json").read_text())
wp1254=json.loads((ROOT/"results"/"wp1254_six_branch_preparation_gate.json").read_text())
wp1255=json.loads((ROOT/"results"/"wp1255_mass_clock_gate.json").read_text())
wp1256=json.loads((ROOT/"results"/"wp1256_channel_gain_gate.json").read_text())
wp1257=json.loads((ROOT/"results"/"wp1257_kernel_classification_gate.json").read_text())
wp1258=json.loads((ROOT/"results"/"wp1258_matching_selection_gate.json").read_text())

cycles=[
    {
        "cycle":1,
        "conjecture":"The sourced dark-state attractor directly supplies the 23-dimensional UV boundary density matrix.",
        "falsification":{
            "source_dimension":wp1177["source_state"]["dimension"],
            "target_dimension":wp1177["target_state"]["dimension"],
            "source_rank":wp1177["source_state"]["rank"],
            "target_rank":wp1177["target_state"]["rank"],
            "portal_to_sector_dilations":wp1177["portal_to_sector_dilations"],
            "boundary_density_matrices":wp1177["boundary_density_matrices"]
        },
        "falsified":wp1177["boundary_density_matrices"] == 0 and wp1177["portal_to_sector_dilations"] == 0,
        "residual":"derive a portal-to-sector dilation or independent UV boundary state with the required spectrum and sector weights"
    },
    {
        "cycle":2,
        "conjecture":"The exact dimension-trace state and sector weights already constitute the physical six-branch preparation law.",
        "falsification":{
            "dimension_trace_state_constructed":wp1254["dimension_trace_state_constructed"],
            "normalized_boundary_state":wp1254["normalized_boundary_state"],
            "preparation_operator":wp1254["preparation_operator"],
            "source_measure":wp1254["source_measure"],
            "physical_preparation":wp1254["physical_preparation"]
        },
        "falsified":wp1254["dimension_trace_state_constructed"] and not wp1254["physical_preparation"],
        "residual":"obtain a UV preparation packet carrying a sourced 23-dimensional state, sector projections q, a preparation operator, and measure provenance"
    },
    {
        "cycle":3,
        "conjecture":"Common-twist equality plus the radius law selects the absolute localized mass clock.",
        "falsification":{
            "radius_law_exact":wp1255["radius_law_exact"],
            "unique_flux_sector":wp1255["unique_flux_sector"],
            "gauge_gravity_ratio":wp1255["gauge_gravity_ratio"],
            "localized_descent":wp1255["localized_descent"],
            "physical_momentum_frame":wp1255["physical_momentum_frame"],
            "absolute_clock":wp1255["absolute_clock"]
        },
        "falsified":wp1255["radius_law_exact"] and not wp1255["absolute_clock"],
        "residual":"materialize a compactification clock packet selecting n and B/A, proving localized descent, and fixing the physical momentum frame"
    },
    {
        "cycle":4,
        "conjecture":"Exact two-port rows, support/rank/orbit algebra, and anomaly invariance select the physical16 channel and production kernel.",
        "falsification":{
            "realized_physical16_channels":wp1256["realized_physical16_channels"],
            "common_gain_compatible":wp1256["common_gain_compatible"],
            "cascade_certificate":wp1256["cascade_certificate"],
            "low_rank_local_maps":wp1257["rank_two_search"]["low_rank_local_maps"],
            "selected_matching_class":wp1258["selected_matching_class"],
            "selected_kernel":wp1258["selected_kernel"]
        },
        "falsified":wp1256["realized_physical16_channels"] == 0 and not wp1258["selected_matching_class"] and not wp1258["selected_kernel"],
        "residual":"materialize physical16 channel and gain-cascade packets plus a production-matching packet with couplings, gain, and localization certificate"
    },
    {
        "cycle":5,
        "conjecture":"Calibrated acquisition and the existing Nima candidate packets construct the common UV boundary-action instrument.",
        "falsification":{
            "four_state_calibration":wp1246["four_state_calibration"],
            "aspect_composition_calibrated":wp1246["aspect_composition_calibrated"],
            "nima_candidates_fill_none":wp1246["nima_candidates_fill_none"],
            "common_uv_packet":wp1246["common_uv_packet"],
            "production_kernel":wp1246["production_kernel"],
            "gain_3_over_2_derived":wp1246["gain_3_over_2_derived"],
            "flux_sector_orientation":wp1246["flux_sector_orientation"],
            "endpoint_action":wp1246["endpoint_action"],
            "physical16_channel":wp1246["physical16_channel"]
        },
        "falsified":wp1246["four_state_calibration"] and wp1246["nima_candidates_fill_none"] and not wp1246["common_uv_packet"],
        "residual":"obtain an owner-supplied microscopic source grammar or Nima construction/no-go carrying production kernel, mixing, gain, flux sector, endpoint action, and physical16 channel map"
    }
]
assert len(cycles) == 5
assert all(cycle["falsified"] for cycle in cycles)

result={
    "schema":"marici.flavor.wp1263.v1",
    "status":"PASS",
    "question":"Do five conjecture-falsification-residual cycles produce the boundary-density instrument from existing source data?",
    "dpc":{
        "conjecture":"Five independent existing-source routes can jointly construct or eliminate the need for the boundary-density instrument.",
        "rivals":["direct attractor density","dimension-trace preparation","common-twist radius clock","rows/support/anomaly kernel and channel","calibrated Nima candidate composition"],
        "risky_consequences":["WP1177 has zero dilations and zero boundary density matrices","WP1254 constructs rho_dim but no physical preparation","WP1255 has the radius law but no absolute clock","WP1256 through WP1258 have rows, map classifications, and anomaly invariance but no selected channel, matching, or kernel","WP1246 has calibrated acquisition but no common UV packet"],
        "falsification_attempt":"Replay WP1177, WP1246, and WP1254 through WP1258, then run five independent conjecture-falsification-residual cycles against their exact outputs.",
        "residual":"All five cycles are falsified; the remaining object is a source-derived boundary-density instrument packet or an owner-side microscopic grammar/no-go.",
        "disposition":"five-cycle gate resolved conditionally; boundary-density instrument remains selected"
    },
    "cycles":cycles,
    "five_cycles_completed":True,
    "all_cycles_falsified":True,
    "boundary_density_instrument_constructed":False,
    "one_boundary_instrument_conjecture_status":"survived_not_proven",
    "classification":"five-cycle DPC gate: every existing-source shortcut to the boundary-density instrument is falsified",
    "remaining_gate":"derive the boundary-density instrument packet, or an owner-side microscopic grammar/no-go, with state, preparation, clock, channel, matching, gain, and calibrated descent in one source packet",
    "hostile_gate":"do not treat the five failed shortcuts as proof of the one-boundary-instrument conjecture or as construction of the boundary packet",
    "claim_boundary":"the result establishes five replayed falsification cycles and their residuals; the one-boundary-instrument conjecture survives but remains unproven",
    "disposition":"boundary-density five-cycle gate resolved conditionally; source-derived boundary instrument construction remains required"
}
(ROOT/"results"/"wp1263_boundary_density_five_cycle_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1263 PASS: 5 conjecture-falsification-residual cycles completed; boundary-density instrument remains open")
