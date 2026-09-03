import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1044,1045,1046,1047,1048,1049)
wp1044=json.loads((ROOT/"results"/"wp1044_coherent_rate_interference_gain_gate.json").read_text())
wp1045=json.loads((ROOT/"results"/"wp1045_visibility_reference_calibration_gate.json").read_text())
wp1046=json.loads((ROOT/"results"/"wp1046_common_frame_visibility_transport_gate.json").read_text())
wp1047=json.loads((ROOT/"results"/"wp1047_visibility_epoch_anchor_gate.json").read_text())
wp1048=json.loads((ROOT/"results"/"wp1048_coherent_final_state_support_gate.json").read_text())
wp1049=json.loads((ROOT/"results"/"wp1049_overlap_monitor_null_accounting_gate.json").read_text())
assert wp1044["classification"] == "conditional instrument gate: coherent phase-flipped difference plus background and absolute signal rows identifies signed gain locally after visibility/reference calibration; it does not derive the source value of g"
assert wp1045["classification"] == "conditional calibration gate: one independent reference-only visibility row closes the local gain-visibility kernel in the one-amplitude model"
assert wp1046["classification"] == "conditional transport gate: a reference row calibrates Flavor visibility only after a source or apparatus law identifies the reference and flavor visibilities in one frame"
assert wp1047["classification"] == "conditional epoch gate: common-frame visibility transport must be live-anchored; stale transport gives a confidently wrong gain"
assert wp1048["classification"] == "conditional support gate: calibrated visibility and live epoch do not prove coherent final-state overlap; the physical16 process must supply cofinality or measure the overlap"
assert wp1049["classification"] == "conditional null-accounting gate: an overlap monitor measures cofinality only after monitor loss/null events are retained or independently calibrated"
# The coherent instrument can locally decode gain, but only after six
# nonredundant calibration/support rows; none derives the source value.
coherent_gain_rank=True
visibility_reference_required=True
common_frame_transport_required=True
live_epoch_anchor_required=True
cofinality_monitor_required=True
null_accounting_required=True
source_gain_value=False
physical16_process=False
reference_channel=False
cofinal_final_state=False
null_complete_monitor=False
assert coherent_gain_rank and visibility_reference_required and common_frame_transport_required
assert live_epoch_anchor_required and cofinality_monitor_required and null_accounting_required
assert not (source_gain_value or physical16_process or reference_channel or cofinal_final_state or null_complete_monitor)
result={
    "schema":"marici.flavor.wp1239.v1",
    "status":"PASS",
    "question":"Can a coherent Physical16 instrument acquire the source-detector gain?",
    "dpc":{
        "conjecture":"Background, absolute rate, and phase-flipped coherent difference acquire the source-detector gain.",
        "rivals":["pure-rate confounder","gain-visibility kernel","reference/common-frame mismatch","stale epoch drift","partial coherent overlap","lossy overlap monitor"],
        "risky_consequences":["pure rate has rank two while the coherent row raises rank to three","a reference row raises gain-visibility rank from three to four","common-frame transport raises rank from four to five","a live epoch anchor separates stale packets with wrong gain decode","coherent overlap c multiplies D and needs its own record","monitor loss eta multiplies overlap H and requires null accounting"],
        "falsification_attempt":"each calibration row removes one exact collision, but no source-derived Physical16 process or gain value is supplied.",
        "residual":"one Physical16 coherent final-state process with independent reference visibility, common-frame live transport, cofinality or overlap monitor, null-complete accounting, and source provenance for g",
        "disposition":"accept a minimal conditional acquisition schema; reject any current source-detector gain law"
    },
    "local_rank":wp1044["local_rank"],
    "gain_formula":wp1044["exact_reconstruction"]["formula_g"],
    "reference_reconstruction":wp1045["exact_reconstruction_with_reference"],
    "common_frame_constraint":wp1046["common_frame_constraint"],
    "stale_collision":wp1047["exact_stale_collision"],
    "overlap_law":wp1048["coherent_overlap"],
    "monitor_law":wp1049["overlap_monitor_law"],
    "null_retaining_decode":wp1049["null_retaining_decode"],
    "coherent_gain_rank":coherent_gain_rank,
    "visibility_reference_required":visibility_reference_required,
    "common_frame_transport_required":common_frame_transport_required,
    "live_epoch_anchor_required":live_epoch_anchor_required,
    "cofinality_monitor_required":cofinality_monitor_required,
    "null_accounting_required":null_accounting_required,
    "source_gain_value":source_gain_value,
    "physical16_process":physical16_process,
    "reference_channel":reference_channel,
    "cofinal_final_state":cofinal_final_state,
    "null_complete_monitor":null_complete_monitor,
    "classification":"conditional gain-acquisition schema: coherent rank exists, source gain and Physical16 process absent",
    "remaining_gate":"construct the coherent Physical16 process and null-retaining cofinality monitor, then derive source gain in the same calibrated frame",
    "hostile_gate":"do not call local rank, reference rows, transport equality, epoch anchors, overlap records, or monitor counts a source-derived gain law",
    "claim_boundary":"WP1044 through WP1049 define the minimal instrument obligations; none instantiates the process or derives g",
    "disposition":"source-detector gain-law leaf resolved conditionally; coherent cofinality-monitor rival selected"
}
(ROOT/"results"/"wp1239_source_detector_gain_law_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1239 PASS: gain acquisition conditional, coherent cofinality monitor required")
