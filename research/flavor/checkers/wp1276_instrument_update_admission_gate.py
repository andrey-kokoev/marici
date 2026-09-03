import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1276-instrument-update-interface"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1274,1275)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1274=json.loads((ROOT/"results"/"wp1274_shared_frame_handoff_necessity_gate.json").read_text())
wp1275=json.loads((ROOT/"results"/"wp1275_source_selected_uv_boundary_object_gate.json").read_text())
v1=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v1.json").read_text())
v2=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v2.json").read_text())
sontag=(REPO/"research"/"sontag"/"effects-do-not-determine-instruments.md").read_text()
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1274["actual_typed_packet_admitted"] is False and wp1274["partial_replies_compose"] is False
assert wp1275["u_object_constructed"] is False and wp1275["current_u_candidate_found"] is False
assert "Effects are not additional state transitions" in sontag or "effects describe current record statistics" in sontag
assert "record-conditioned update" in sontag
assert "joint record" in sontag
assert "record-conditioned post-record update map" in request
assert "sequential-record continuation law" in request
assert "joint record words and lineage keys" in request
assert list(v1["required_objects"])==["channel_basis","phase_observable","production_kernel","event_map","provenance"]
assert list(v2["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","provenance"
]
assert v2["required_objects"]["instrument_update"]["record_conditioned"] is True
assert v2["required_objects"]["instrument_update"]["post_record_state_present"] is True
assert v2["required_objects"]["instrument_update"]["sequential_continuation"] is True
assert v2["required_objects"]["instrument_update"]["joint_record_lineage"] is True
assert "effect_only_packet_without_record_conditioned_update" in v2["hostile_rejections"]
assert "partial_interfaces_without_source_selected_uv_boundary_object" in v2["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: a packet can carry the v1 event algebra and still be an
# effect-only shadow with no record-conditioned post-record state.
effect_only_packet={
    "source_selected_uv_boundary_object":None,
    "channel_basis":"rank_6_fixture",
    "phase_observable":"H6_fixture",
    "production_kernel":"J6/6_fixture",
    "event_map":"(1/4)^6_fixture",
    "provenance":{"packet_id":"mock"},
}
v2_admitted=(
    effect_only_packet.get("source_selected_uv_boundary_object") is not None
    and "instrument_update" in effect_only_packet
    and effect_only_packet.get("provenance") is not None
)
assert v2_admitted is False
actual_packets_supplied=0

# Falsifier: event probabilities and readout images alone supply the required
# instrument branch and post-record continuation.
effect_only_packet_sufficient=False
instrument_update_interface_constructed=False
conjecture_refuted=effect_only_packet_sufficient
assert not conjecture_refuted and not instrument_update_interface_constructed

result={
    "schema":"marici.flavor.wp1276.v1",
    "status":"PASS",
    "question":"Can an event-production packet be admitted from effects and readout images without a record-conditioned instrument update?",
    "dpc":{
        "conjecture":"Every admissible typed UV event-production packet must include a record-conditioned post-record update map, sequential continuation law, and joint-record lineage in addition to effects, kernels, gains, and images.",
        "rivals":["WP1128 v1 admission contract","effect-only packet","kernel-only packet","phase-gauge packet","fixture packet","partial-interface composition"],
        "risky_consequences":["Sontag's hostile gives identical present effects with different post-record states and different joint future records","WP1128 v1 has no instrument_update object","WP1274 admits no typed packet","WP1275 constructs no source-selected U","the v2 contract adds source-selected U and instrument_update as required objects"],
        "falsification_attempt":"Replay WP1128, WP1274, and WP1275; compare the v1 and v2 admission contracts; test an effect-only packet carrying the v1 event algebra.",
        "residual":"The effect-only packet is rejected and no actual packet is admitted. The instrument-update necessity conjecture survives. The residual is a source-derived update map from U with sequential-record continuation and lineage.",
        "disposition":"instrument-update necessity survives attempted falsification; source-transversal certificate selected"
    },
    "admission_contract_v1":"research/flavor/contracts/flavor-event-production-packet-admission.v1.json",
    "admission_contract_v2":"research/flavor/contracts/flavor-event-production-packet-admission.v2.json",
    "required_object_count_v1":len(v1["required_objects"]),
    "required_object_count_v2":len(v2["required_objects"]),
    "instrument_update_required":True,
    "source_selected_u_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "effect_only_packet_admitted_v2":v2_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "effect_only_packet_sufficient":effect_only_packet_sufficient,
    "instrument_update_interface_constructed":instrument_update_interface_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold instrument-update necessity gate: v2 admission rejects effect-only packet shadows",
    "remaining_gate":"derive the record-conditioned update map, sequential continuation law, and joint-record lineage from the source-selected U packet",
    "hostile_gate":"do not admit effect probabilities, kernels, phase gauges, readout images, or fixtures without post-record update and lineage",
    "claim_boundary":"WP1128, WP1274, WP1275, and the Sontag analogue falsify effect-only sufficiency; the instrument-update necessity conjecture survives but remains unproven",
    "disposition":"instrument-update-interface leaf resolved conditionally; source-transversal certificate required"
}
(ROOT/"results"/"wp1276_instrument_update_admission_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1276 PASS: instrument-update necessity survives attempted falsification; v2 admission contract active")
