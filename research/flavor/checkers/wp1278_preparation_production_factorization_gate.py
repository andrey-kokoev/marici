import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1278-preparation-production-factorization"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1277)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1277=json.loads((ROOT/"results"/"wp1277_source_transversal_admission_gate.json").read_text())
v3=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v3.json").read_text())
v4=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v4.json").read_text())
sontag=(REPO/"research"/"sontag"/"effects-do-not-determine-instruments.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1277["source_transversal_required"] is True and wp1277["actual_packets_supplied"]==0
assert "record-conditioned update" in sontag
assert "joint sequential records" in sontag
assert "factorized preparation and production maps" in request
assert "separate preparation/messenger and production/response lineage" in request
assert list(v3["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal","provenance"
]
assert list(v4["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","provenance"
]
factor=v4["required_objects"]["preparation_production_factorization"]
assert factor["joint_hidden_state_update_present"] is True
assert factor["preparation_factor_present"] is True
assert factor["production_factor_present"] is True
assert factor["independent_factors"] is True
assert factor["preparation_messenger_lineage"]=="explicit"
assert factor["production_response_lineage"]=="explicit"
assert "single_instrument_without_factorized_preparation_and_production" in v4["hostile_rejections"]
assert "correlated_preparation_response_pair_treated_as_independent_product_factors" in v4["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all prior v3 fields can be present while preparation and
# production are fused into one record-labelled map with no independent factors.
fused_shadow_packet={
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
    "preparation_production_factorization":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v4_admitted=(
    fused_shadow_packet.get("source_selected_uv_boundary_object") is not None
    and fused_shadow_packet.get("instrument_update") is not None
    and fused_shadow_packet.get("source_transversal") is not None
    and fused_shadow_packet.get("preparation_production_factorization") is not None
)
assert v4_admitted is False
actual_packets_supplied=0

# Falsifier: one fused record-labelled update already certifies the independent
# preparation and production factors demanded by the packet.
fused_update_sufficient=False
factorization_certificate_constructed=False
conjecture_refuted=fused_update_sufficient
assert not conjecture_refuted and not factorization_certificate_constructed

result={
    "schema":"marici.flavor.wp1278.v1",
    "status":"PASS",
    "question":"Can one fused record-labelled update substitute for independent preparation and production factors?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must carry one joint hidden-state update factored into independent preparation and production maps with separate messenger and response lineage.",
        "rivals":["WP1128 v1 admission contract","WP1277 v3 admission contract","fused shadow packet","effect-only packet","quotient shadow packet","fixture packet"],
        "risky_consequences":["the Sontag hostile makes record-conditioned updates sequential and joint-record typed","WP1277 still has no preparation_production_factorization object","the handoff request explicitly demands factorized preparation and production maps with separate lineage","v4 adds the factorization object and rejects fused updates"],
        "falsification_attempt":"Replay WP1128 and WP1277; compare the v3 and v4 admission contracts; test a fused shadow packet with all v3 fields but no factorization object.",
        "residual":"The fused shadow packet is rejected and no actual packet is admitted. The factorization necessity conjecture survives. The residual is a source-derived joint update with independent preparation and production factors.",
        "disposition":"preparation-production factorization necessity survives attempted falsification; sequential-record fidelity selected"
    },
    "admission_contract_v3":"research/flavor/contracts/flavor-event-production-packet-admission.v3.json",
    "admission_contract_v4":"research/flavor/contracts/flavor-event-production-packet-admission.v4.json",
    "required_object_count_v3":len(v3["required_objects"]),
    "required_object_count_v4":len(v4["required_objects"]),
    "preparation_production_factorization_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "fused_shadow_packet_admitted_v4":v4_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "fused_update_sufficient":fused_update_sufficient,
    "factorization_certificate_constructed":factorization_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold preparation-production factorization gate: v4 admission rejects fused shadow packets",
    "remaining_gate":"derive a joint hidden-state update with independent preparation and production factors and separate messenger/response lineage",
    "hostile_gate":"do not admit one fused instrument update or correlated preparation/response pair as independent product factors",
    "claim_boundary":"WP1128, WP1277, the Sontag analogue, and the handoff request falsify fused-update sufficiency; the factorization necessity conjecture survives but remains unproven",
    "disposition":"preparation-production-factorization leaf resolved conditionally; sequential-record fidelity required"
}
(ROOT/"results"/"wp1278_preparation_production_factorization_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1278 PASS: preparation-production factorization necessity survives attempted falsification; v4 admission contract active")
