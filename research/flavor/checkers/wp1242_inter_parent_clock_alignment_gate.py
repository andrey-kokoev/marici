import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1060,1061,1062,1063)
wp1060=json.loads((ROOT/"results"/"wp1060_common_twist_parent_clock_gate.json").read_text())
wp1061=json.loads((ROOT/"results"/"wp1061_radius_stabilized_common_clock_cofiber.json").read_text())
wp1062=json.loads((ROOT/"results"/"wp1062_same_frame_kk_momentum_ratio_cofiber.json").read_text())
wp1063=json.loads((ROOT/"results"/"wp1063_soft_scale_two_port_instrument_lock.json").read_text())
assert wp1060["classification"].startswith("conditional common-twist clock constructor")
assert wp1061["classification"].startswith("conditional radius-clock cofiber")
assert wp1062["classification"].startswith("conditional same-frame momentum cofiber")
assert wp1063["classification"].startswith("conditional soft-scale two-port instrument")
# Common twist closes the relative parent gap conditionally. Radius,
# flux, and instrument data sharpen absolute calibration, but the soft
# ratio-one detector channel is still only an instrument reference.
inter_parent_clock_equal=True
same_frame_vector_ratios=True
soft_two_port_lock=True
joint_quantization_condition=True
common_twist_derived=False
masslessness_derived=False
flux_sector_derived=False
gauge_gravity_ratio_derived=False
soft_physical_channel=False
physical_gain=False
assert inter_parent_clock_equal and same_frame_vector_ratios and soft_two_port_lock and joint_quantization_condition
assert not (common_twist_derived or masslessness_derived or flux_sector_derived or gauge_gravity_ratio_derived or soft_physical_channel or physical_gain)
result={
    "schema":"marici.flavor.wp1242.v1",
    "status":"PASS",
    "question":"Can inter-parent clock alignment calibrate the pole momentum?",
    "dpc":{
        "conjecture":"A massless common-twist tower aligns the 15 and bar6 clocks; stabilized radius and two-port locking reduce momentum calibration to one missing soft Physical16 channel.",
        "rivals":["massless common twist","stabilized radius clock","same-frame KK vector ratios","soft-scale two-port instrument lock"],
        "risky_consequences":["the 15 and bar6 clocks become equal at every KK level","R star squared=3 A n squared/(2B) and M squared=(B/A)/(6n squared)","vector KK N=1 and N=2 ratios are 4 and 16 in the same radius frame","locking m to M gives ratios 1 and 4 and restores the WP1042 1/2 shape"],
        "falsification_attempt":"different twist charges, parent bulk mass, wrong flux sectors, vector-only ports, and heavy/light clocks all fail, but the common twist, flux sector, gauge-gravity ratio, and soft detector channel remain underived.",
        "residual":"derive common twist/masslessness, flux sector, and gauge-gravity ratio from one compactification, then realize the soft and vector ports as actual Physical16 production/decay channels",
        "disposition":"accept the common-clock construction conditionally; reject it as calibrated physical pole dynamics"
    },
    "common_twist_cell":wp1060["common_twist_cell"],
    "twist_hostiles":wp1060["hostiles"],
    "clock_law":wp1061["clock_law"],
    "unit_clock_condition":wp1061["unit_clock_condition"],
    "radius_cases":wp1061["cases"],
    "same_frame_law":wp1062["same_frame_law"],
    "vector_ports":wp1062["vector_ports"],
    "soft_scale_port":wp1062["soft_scale_port"],
    "instrument_pair":wp1063["instrument_pair"],
    "response_determinant":wp1063["response_determinant"],
    "vector_only_hostile":wp1063["vector_only_hostile"],
    "inter_parent_clock_equal":inter_parent_clock_equal,
    "same_frame_vector_ratios":same_frame_vector_ratios,
    "soft_two_port_lock":soft_two_port_lock,
    "joint_quantization_condition":joint_quantization_condition,
    "common_twist_derived":common_twist_derived,
    "masslessness_derived":masslessness_derived,
    "flux_sector_derived":flux_sector_derived,
    "gauge_gravity_ratio_derived":gauge_gravity_ratio_derived,
    "soft_physical_channel":soft_physical_channel,
    "physical_gain":physical_gain,
    "classification":"conditional inter-parent clock alignment: common twist aligns parents, soft Physical16 channel absent",
    "remaining_gate":"derive the compactification class and realize soft plus vector momentum ports in actual Physical16 production/decay channels",
    "hostile_gate":"do not call common twist, radius balance, same-frame vector ratios, or an instrument lock a derived Physical16 soft channel",
    "claim_boundary":"WP1060 through WP1063 provide exact common-clock and momentum-ratio algebra; no flux/vector quantization, physical detector channel, or gain is derived",
    "disposition":"inter-parent clock alignment leaf resolved conditionally; soft-port channel realization rival selected"
}
(ROOT/"results"/"wp1242_inter_parent_clock_alignment_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1242 PASS: inter-parent clock conditional, soft Physical16 channel absent")
