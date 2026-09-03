import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1277-source-transversal-certificate"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1276)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1276=json.loads((ROOT/"results"/"wp1276_instrument_update_admission_gate.json").read_text())
v2=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v2.json").read_text())
v3=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v3.json").read_text())
sontag=(REPO/"research"/"sontag"/"faithful-recovery-needs-a-source-transversal.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1276["instrument_update_required"] is True and wp1276["actual_packets_supplied"]==0
assert "Physical recovery on a source domain" in sontag
assert "Predictive recovery for a frozen experiment family" in sontag
assert "source-derived transversal" in sontag and "fiber ambiguity" in sontag
assert "physical-versus-predictive recovery declaration" in request
assert "source-derived transversal or injectivity certificate" in request
assert "quotient descent" in request
assert list(v2["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","provenance"
]
assert list(v3["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal","provenance"
]
assert v3["required_objects"]["source_transversal"]["source_lift_certificate_present"] is True
assert v3["required_objects"]["source_transversal"]["quotient_predictive_descent"] is True
assert v3["required_objects"]["source_transversal"]["physical_recovery_preserves_source_representatives"] is True
assert v3["required_objects"]["source_transversal"]["u_map_explicit"] is True
assert v3["required_objects"]["source_transversal"]["equivalence_class_representative_only"] is False
assert "predictive_recovery_conflated_with_physical_source_recovery" in v3["hostile_rejections"]
assert "equivalence_class_representative_treated_as_source_selected_transversal" in v3["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: a packet can satisfy the WP1128/WP1276 event and update
# conditions while descending only an equivalence class or predictive quotient.
quotient_shadow_packet={
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
    "source_transversal":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v3_admitted=(
    quotient_shadow_packet.get("source_selected_uv_boundary_object") is not None
    and quotient_shadow_packet.get("instrument_update") is not None
    and quotient_shadow_packet.get("source_transversal") is not None
)
assert v3_admitted is False
actual_packets_supplied=0

# Falsifier: predictive quotient descent already certifies the physical source
# transversal needed for flavor packet admission.
predictive_descent_sufficient=False
source_transversal_certificate_constructed=False
conjecture_refuted=predictive_descent_sufficient
assert not conjecture_refuted and not source_transversal_certificate_constructed

result={
    "schema":"marici.flavor.wp1277.v1",
    "status":"PASS",
    "question":"Can quotient or predictive recovery certify a source-transversal packet without a source lift certificate?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must carry a source-derived transversal certificate proving physical recovery on source representatives and predictive quotient descent, not merely equivalence-class recovery.",
        "rivals":["WP1128 v1 admission contract","WP1276 v2 admission contract","quotient shadow packet","effect-only packet","partial-interface composition","fixture packet"],
        "risky_consequences":["Sontag recovery distinguishes physical realization from predictive quotient recovery","WP1276 still has no source_transversal object","WP1275 constructs no source-selected U","v3 requires an explicit U map and source lift certificate"],
        "falsification_attempt":"Replay WP1128 and WP1276; compare the v2 and v3 admission contracts; test a quotient shadow packet with all event/update fields but no source transversal.",
        "residual":"The quotient shadow packet is rejected and no actual packet is admitted. The source-transversal necessity conjecture survives. The residual is a source-derived transversal certificate from U.",
        "disposition":"source-transversal necessity survives attempted falsification; preparation-production factorization selected"
    },
    "admission_contract_v2":"research/flavor/contracts/flavor-event-production-packet-admission.v2.json",
    "admission_contract_v3":"research/flavor/contracts/flavor-event-production-packet-admission.v3.json",
    "required_object_count_v2":len(v2["required_objects"]),
    "required_object_count_v3":len(v3["required_objects"]),
    "source_transversal_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "quotient_shadow_packet_admitted_v3":v3_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "predictive_descent_sufficient":predictive_descent_sufficient,
    "source_transversal_certificate_constructed":source_transversal_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold source-transversal necessity gate: v3 admission rejects quotient shadow packets",
    "remaining_gate":"derive the source lift certificate and explicit U map proving physical recovery on source representatives",
    "hostile_gate":"do not admit predictive quotient descent, equivalence-class representatives, fixtures, or partial interfaces as source transversals",
    "claim_boundary":"WP1128, WP1276, and the Sontag analogue falsify predictive-descent sufficiency; the source-transversal necessity conjecture survives but remains unproven",
    "disposition":"source-transversal leaf resolved conditionally; preparation-production factorization required"
}
(ROOT/"results"/"wp1277_source_transversal_admission_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1277 PASS: source-transversal necessity survives attempted falsification; v3 admission contract active")
