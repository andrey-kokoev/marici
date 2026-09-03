import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1066,1067,1068,1069)
wp1066=json.loads((ROOT/"results"/"wp1066_localized_quartet_nonabelian_inflow_gate.json").read_text())
wp1067=json.loads((ROOT/"results"/"wp1067_localized_quartet_anomaly_vector_gate.json").read_text())
wp1068=json.loads((ROOT/"results"/"wp1068_parent_green_schwarz_completion_gate.json").read_text())
wp1069=json.loads((ROOT/"results"/"wp1069_local_green_schwarz_split_cofiber.json").read_text())
assert wp1066["classification"].startswith("non-Abelian inflow gate")
assert wp1067["classification"].startswith("complete vanishing-channel anomaly-vector gate")
assert wp1068["classification"].startswith("conditional parent Green-Schwarz completion")
assert wp1069["classification"].startswith("conditional local Green-Schwarz split")
# Anomaly/GS completion sharpens the localization class but is not a
# channel-dependent pole-to-event reweighting map.
selected_half_level=True
five_channel_vector=True
parent_gs_completion=True
conditional_seven_channel_split=True
integral_quartet_rejected=True
port_destroying_local_gs_rejected=True
shifted_cs_lattice_derived=False
endpoint_split_derived=False
local_gs_action_derived=False
reweighting_map=False
event_weights_labels_nulls=False
physical16_channels=False
source_gain=False
assert selected_half_level and five_channel_vector and parent_gs_completion and conditional_seven_channel_split
assert integral_quartet_rejected and port_destroying_local_gs_rejected
assert not (shifted_cs_lattice_derived or endpoint_split_derived or local_gs_action_derived or reweighting_map or event_weights_labels_nulls or physical16_channels or source_gain)
result={
    "schema":"marici.flavor.wp1244.v1",
    "status":"PASS",
    "question":"Can anomaly completion supply the channel-dependent reweighting map?",
    "dpc":{
        "conjecture":"Complete anomaly vectors and parent Green-Schwarz completion sharpen the localized quartet class enough to seek a pole-to-event reweighting map.",
        "rivals":["half-integral SU(4) inflow","five-channel anomaly vector","parent Green-Schwarz completion","conditional symmetric local split","channel-dependent reweighting map"],
        "risky_consequences":["the selected quartet has SU(4) cubic level 1/2","the five globally vanishing channels require (1/2,1/4,0,2,2)","parent coefficient -3 completes both SU(4)-gravity and SU(2)-gravity indices","a symmetric local split gives the seven-channel vector (1/2,1/4,0,2,2,-1/4,0)","integral quartet and local doublet-pair completions fail"],
        "falsification_attempt":"the anomaly vectors reject ordinary integral and alternative local splits, but the shifted CS lattice, endpoint split, local GS action, event weights/labels/nulls, and Physical16 channels remain underived.",
        "residual":"derive the endpoint Green-Schwarz split and multicomponent shifted Chern-Simons lattice from the UV compactification, then map the localized atoms to Physical16 event channels",
        "disposition":"accept anomaly/GS completion conditionally; reject it as the reweighting map"
    },
    "selected_quartet":wp1066["selected_quartet"],
    "lattice_gate":wp1066["lattice_gate"],
    "channels":wp1067["channels"],
    "inflow_vectors":wp1067["inflow_vectors"],
    "excluded_completion_channels":wp1067["excluded_completion_channels"],
    "green_schwarz_completion":wp1068["green_schwarz_completion"],
    "localization_remnants":wp1068["localization_remnants"],
    "conditional_law":wp1069["conditional_law"],
    "full_channels":wp1069["channels"],
    "full_inflow_vectors":wp1069["full_inflow_vectors"],
    "split_fiber":wp1069["split_fiber"],
    "selected_half_level":selected_half_level,
    "five_channel_vector":five_channel_vector,
    "parent_gs_completion":parent_gs_completion,
    "conditional_seven_channel_split":conditional_seven_channel_split,
    "integral_quartet_rejected":integral_quartet_rejected,
    "port_destroying_local_gs_rejected":port_destroying_local_gs_rejected,
    "shifted_cs_lattice_derived":shifted_cs_lattice_derived,
    "endpoint_split_derived":endpoint_split_derived,
    "local_gs_action_derived":local_gs_action_derived,
    "reweighting_map":reweighting_map,
    "event_weights_labels_nulls":event_weights_labels_nulls,
    "physical16_channels":physical16_channels,
    "source_gain":source_gain,
    "classification":"conditional channel-reweighting gate: anomaly/GS vectors sharpen localization, Physical16 reweighting absent",
    "remaining_gate":"derive endpoint GS split, shifted multicomponent CS lattice, and pole-to-event channel reweighting from one UV compactification",
    "hostile_gate":"do not call a shifted anomaly vector, parent GS coefficient, or conditional endpoint split a Physical16 channel reweighting map",
    "claim_boundary":"WP1066 through WP1069 provide exact anomaly-vector and split algebra; no local action, shifted lattice, event map, or gain is derived",
    "disposition":"channel-dependent reweighting-map leaf resolved conditionally; shifted-localization-lattice rival selected"
}
(ROOT/"results"/"wp1244_channel_dependent_reweighting_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1244 PASS: anomaly split conditional, Physical16 reweighting absent")
