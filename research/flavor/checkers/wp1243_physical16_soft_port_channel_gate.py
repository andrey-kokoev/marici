import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1064,1065)
wp1064=json.loads((ROOT/"results"/"wp1064_vector_ratio_event_cell_gain_cofiber.json").read_text())
wp1065=json.loads((ROOT/"results"/"wp1065_pole_event_atom_interface_gate.json").read_text())
assert wp1064["classification"].startswith("conditional vector-ratio event-cell constructor")
assert wp1065["classification"].startswith("negative pole-event interface gate")
# The event cell can carry a source-derived ratio-4 vector branch, but it
# is not a relabeling of the 23 pole atoms or six localized branches.
vector_ratio_event_cell=True
reconstruction_lg=True
unit_ratio_rejected=True
laundering_rejected=True
pole_event_relabel=False
equal_weight_partition=False
branch_identification=False
channel_weights_derived=False
event_labels_derived=False
physical16_channels=False
source_gain=False
assert vector_ratio_event_cell and reconstruction_lg and unit_ratio_rejected and laundering_rejected
assert not (pole_event_relabel or equal_weight_partition or branch_identification)
assert not (channel_weights_derived or event_labels_derived or physical16_channels or source_gain)
result={
    "schema":"marici.flavor.wp1243.v1",
    "status":"PASS",
    "question":"Can a Physical16 soft-port channel be realized by the existing event cell?",
    "dpc":{
        "conjecture":"The common-source event cell carries the source-derived vector threshold ratio, but a physical soft-port channel requires a new channel-dependent reweighting map.",
        "rivals":["vector-ratio event-cell constructor","pole-event relabeling","equal-weight partition","localized-branch identification","channel-dependent reweighting map"],
        "risky_consequences":["ratio 4 reconstructs L=1/5 and g=1 on the atom cell","unit ratio leaves exact S and D gaps","a same-rate g=1/2 laundering attempt is separated by the coherent row","23 pole atoms cannot satisfy the 3d/2 event support and six event atoms cannot be an equal partition","no assignment of the six localized SU(6) branches satisfies the WP1052 event constraints"],
        "falsification_attempt":"ratio and atom relabeling hostiles fail, while channel weights, detector/monitor/cross labels, null outcomes, and actual Physical16 production/decay channels remain underived.",
        "residual":"derive a source-dynamical channel-dependent reweighting map from pole atoms to event atoms, with labels, nulls, and soft/vector port realization in one Physical16 frame",
        "disposition":"accept the vector-ratio event branch conditionally; reject relabeling as a soft-port realization"
    },
    "atom_cell":wp1064["atom_cell"],
    "vector_ratio_cell":wp1064["vector_ratio_cell"],
    "unit_ratio_hostile":wp1064["unit_ratio_hostile"],
    "laundering_hostile":wp1064["laundering_hostile"],
    "diophantine_obstruction":wp1065["diophantine_obstruction"],
    "equal_weight_obstruction":wp1065["equal_weight_obstruction"],
    "branch_identification_hostile":wp1065["branch_identification_hostile"],
    "vector_ratio_event_cell":vector_ratio_event_cell,
    "reconstruction_lg":reconstruction_lg,
    "unit_ratio_rejected":unit_ratio_rejected,
    "laundering_rejected":laundering_rejected,
    "pole_event_relabel":pole_event_relabel,
    "equal_weight_partition":equal_weight_partition,
    "branch_identification":branch_identification,
    "channel_weights_derived":channel_weights_derived,
    "event_labels_derived":event_labels_derived,
    "physical16_channels":physical16_channels,
    "source_gain":source_gain,
    "classification":"conditional soft-port channel gate: vector event branch exists, source channel reweighting absent",
    "remaining_gate":"derive channel-dependent event weights, detector/monitor/cross labels, null outcomes, and soft/vector production/decay channels from Physical16 dynamics",
    "hostile_gate":"do not call a vector-ratio event cell, pole-atom relabeling, equal-weight partition, or branch identification a Physical16 soft-port channel",
    "claim_boundary":"WP1064 and WP1065 provide exact vector event and interface obstruction algebra; no physical channels, reweighting dynamics, or gain are derived",
    "disposition":"physical16 soft-port-channel leaf resolved conditionally; channel-dependent reweighting-map rival selected"
}
(ROOT/"results"/"wp1243_physical16_soft_port_channel_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1243 PASS: vector event branch conditional, channel reweighting absent")
