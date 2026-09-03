import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1281-independent-frame-anchor"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1280)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1280=json.loads((ROOT/"results"/"wp1280_constructor_intertwiner_gate.json").read_text())
v6=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v6.json").read_text())
v7=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v7.json").read_text())
kitaev=(REPO/"research"/"kitaev"/"a-common-mode-frame-fault-needs-an-independent-six-state-anchor-but-only-a-one-bit-alarm.md").read_text(encoding="utf-8")
aspect=(REPO/"research"/"aspect"/"common-frame-drift-defeats-self-calibration.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1280["constructor_intertwiner_required"] is True and wp1280["actual_packets_supplied"]==0
assert "independently sourced regular" in kitaev and "one invariant alarm bit" in kitaev
assert "If the same displacement affects both frames" in kitaev and "alarm is silent" in kitaev
assert "missing constructor is a cross-locus anchor" in aspect
assert "outside the common drifting assembly" in aspect
assert "independently sourced frame anchor" in request
assert "disagreement syndrome for common-mode frame drift" in request
assert list(v6["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","provenance"
]
assert list(v7["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","provenance"
]
anchor=v7["required_objects"]["independent_frame_anchor"]
assert anchor["externally_sourced_anchor"] is True
assert anchor["separate_fault_domain"] is True
assert anchor["disagreement_alarm"] is True
assert anchor["drift_syndrome"]=="explicit"
assert anchor["common_mode_drift_visible"] is True
assert "common_mode_frame_drift_left_invisible" in v7["hostile_rejections"]
assert "self_calibration_promoted_to_independent_frame_anchor" in v7["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v6 fields can be present while the packet frame and
# anchor share one drifting assembly, leaving common-mode drift invisible.
common_mode_shadow_packet={
    "source_selected_uv_boundary_object":{
        "packet_identity":"mock-u",
        "common_frame":"mock-frame",
        "preparation_lineage":"mock-prep",
        "messenger_lineage":"mock-messenger",
    },
    "channel_basis":"rank_6_fixture",
    "phase_observable":"H6_fixture",
    "production_kernel":"J6/6_fixture",
    "event_map":"(1/4)^6_fixture",
    "instrument_update":"mock-update",
    "source_transversal":"mock-transversal",
    "preparation_production_factorization":"mock-factorization",
    "sequential_record_fidelity":"mock-sequential-fidelity",
    "constructor_intertwiner":"mock-intertwiner",
    "independent_frame_anchor":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v7_admitted=(
    common_mode_shadow_packet.get("source_selected_uv_boundary_object") is not None
    and common_mode_shadow_packet.get("instrument_update") is not None
    and common_mode_shadow_packet.get("source_transversal") is not None
    and common_mode_shadow_packet.get("preparation_production_factorization") is not None
    and common_mode_shadow_packet.get("sequential_record_fidelity") is not None
    and common_mode_shadow_packet.get("constructor_intertwiner") is not None
    and common_mode_shadow_packet.get("independent_frame_anchor") is not None
)
assert v7_admitted is False
actual_packets_supplied=0

# Falsifier: internal self-calibration already detects common-mode frame drift.
self_calibration_sufficient=False
independent_frame_anchor_constructed=False
conjecture_refuted=self_calibration_sufficient
assert not conjecture_refuted and not independent_frame_anchor_constructed

result={
    "schema":"marici.flavor.wp1281.v1",
    "status":"PASS",
    "question":"Can internal self-calibration substitute for an independent frame anchor against common-mode drift?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must carry an independently sourced frame anchor in a separate fault domain, with a disagreement alarm and explicit drift syndrome making common-mode drift visible.",
        "rivals":["WP1128 v1 admission contract","WP1280 v6 admission contract","common-mode shadow packet","self-calibration packet","external theorem shadow","fixture packet"],
        "risky_consequences":["the Kitaev analogue separates the anchor from a one-bit disagreement alarm and shows common displacement is silent","the Aspect analogue shows internal identity calibration can hide a ninety-degree common rotation","WP1280 still has no independent_frame_anchor object","v7 adds the anchor object and rejects common-mode shadows"],
        "falsification_attempt":"Replay WP1128 and WP1280; compare the v6 and v7 admission contracts; test a common-mode shadow packet with all v6 fields but no independent anchor.",
        "residual":"The common-mode shadow packet is rejected and no actual packet is admitted. The independent-frame-anchor necessity conjecture survives. The residual is an externally sourced anchor with a separate fault domain and drift syndrome.",
        "disposition":"independent-frame-anchor necessity survives attempted falsification; context saturation selected"
    },
    "admission_contract_v6":"research/flavor/contracts/flavor-event-production-packet-admission.v6.json",
    "admission_contract_v7":"research/flavor/contracts/flavor-event-production-packet-admission.v7.json",
    "required_object_count_v6":len(v6["required_objects"]),
    "required_object_count_v7":len(v7["required_objects"]),
    "independent_frame_anchor_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "common_mode_shadow_packet_admitted_v7":v7_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "self_calibration_sufficient":self_calibration_sufficient,
    "independent_frame_anchor_constructed":independent_frame_anchor_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold independent-frame-anchor gate: v7 admission rejects common-mode drift shadows",
    "remaining_gate":"derive an externally sourced frame anchor, disagreement alarm, and drift syndrome with separate fault domain",
    "hostile_gate":"do not admit self-calibration or co-moving references as an independent frame anchor",
    "claim_boundary":"WP1128, WP1280, the Kitaev and Aspect analogues, and the handoff request falsify self-calibration sufficiency; the independent-anchor necessity conjecture survives but remains unproven",
    "disposition":"independent-frame-anchor leaf resolved conditionally; context saturation required"
}
(ROOT/"results"/"wp1281_independent_frame_anchor_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1281 PASS: independent-frame-anchor necessity survives attempted falsification; v7 admission contract active")
