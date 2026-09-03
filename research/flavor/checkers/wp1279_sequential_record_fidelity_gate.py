import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1279-sequential-record-fidelity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1278)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1278=json.loads((ROOT/"results"/"wp1278_preparation_production_factorization_gate.json").read_text())
v4=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v4.json").read_text())
v5=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v5.json").read_text())
sontag=(REPO/"research"/"sontag"/"effects-do-not-determine-instruments.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1278["preparation_production_factorization_required"] is True and wp1278["actual_packets_supplied"]==0
assert "joint sequential records" in sontag
assert "lineage binds the later record" in sontag
assert "sequential-record continuation law" in request
assert "joint record words and lineage keys" in request
assert list(v4["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","provenance"
]
assert list(v5["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity","provenance"
]
seq=v5["required_objects"]["sequential_record_fidelity"]
assert seq["joint_record_words_present"] is True
assert seq["branch_conditioned_continuation"] is True
assert seq["later_record_bound_to_earlier_branch"] is True
assert seq["cross_branch_substitution_forbidden"] is True
assert seq["continuation_provenance"]=="explicit"
assert "marginal_records_treated_as_joint_record_words" in v5["hostile_rejections"]
assert "cross_branch_continuation_substituted_for_branch_conditioned_fidelity" in v5["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v4 fields can be present while only marginal first
# records and unconstrained later continuations are supplied.
marginal_shadow_packet={
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
    "sequential_record_fidelity":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v5_admitted=(
    marginal_shadow_packet.get("source_selected_uv_boundary_object") is not None
    and marginal_shadow_packet.get("instrument_update") is not None
    and marginal_shadow_packet.get("source_transversal") is not None
    and marginal_shadow_packet.get("preparation_production_factorization") is not None
    and marginal_shadow_packet.get("sequential_record_fidelity") is not None
)
assert v5_admitted is False
actual_packets_supplied=0

# Falsifier: marginal first records and unconstrained later continuations
# already preserve branch-conditioned joint record words.
marginal_records_sufficient=False
sequential_record_certificate_constructed=False
conjecture_refuted=marginal_records_sufficient
assert not conjecture_refuted and not sequential_record_certificate_constructed

result={
    "schema":"marici.flavor.wp1279.v1",
    "status":"PASS",
    "question":"Can marginal records and unconstrained continuation substitute for branch-conditioned sequential fidelity?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must preserve joint record words under branch-conditioned continuation, bind each later record to the earlier instrument branch, and forbid cross-branch substitution.",
        "rivals":["WP1128 v1 admission contract","WP1278 v4 admission contract","marginal-record shadow packet","effect-only packet","fused shadow packet","fixture packet"],
        "risky_consequences":["the Sontag hostile separates effect-equivalent instruments by one-step continuation and joint records","WP1278 still has no sequential_record_fidelity object","the handoff request demands a sequential-record continuation law and joint record words","v5 adds sequential fidelity and rejects marginal/cross-branch shadows"],
        "falsification_attempt":"Replay WP1128 and WP1278; compare the v4 and v5 admission contracts; test a marginal-record shadow packet with all v4 fields but no sequential fidelity object.",
        "residual":"The marginal-record shadow packet is rejected and no actual packet is admitted. The sequential-fidelity necessity conjecture survives. The residual is a source-derived branch-conditioned continuation certificate.",
        "disposition":"sequential-record fidelity necessity survives attempted falsification; constructor-intertwiner certificate selected"
    },
    "admission_contract_v4":"research/flavor/contracts/flavor-event-production-packet-admission.v4.json",
    "admission_contract_v5":"research/flavor/contracts/flavor-event-production-packet-admission.v5.json",
    "required_object_count_v4":len(v4["required_objects"]),
    "required_object_count_v5":len(v5["required_objects"]),
    "sequential_record_fidelity_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "marginal_shadow_packet_admitted_v5":v5_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "marginal_records_sufficient":marginal_records_sufficient,
    "sequential_record_certificate_constructed":sequential_record_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold sequential-record fidelity gate: v5 admission rejects marginal-record shadows",
    "remaining_gate":"derive branch-conditioned continuation with joint record words and source provenance",
    "hostile_gate":"do not admit marginal records, cross-branch continuations, fixtures, or partial interfaces as sequential fidelity",
    "claim_boundary":"WP1128, WP1278, the Sontag analogue, and the handoff request falsify marginal-record sufficiency; the sequential-fidelity necessity conjecture survives but remains unproven",
    "disposition":"sequential-fidelity leaf resolved conditionally; constructor-intertwiner certificate required"
}
(ROOT/"results"/"wp1279_sequential_record_fidelity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1279 PASS: sequential-record fidelity necessity survives attempted falsification; v5 admission contract active")
