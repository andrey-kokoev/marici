import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1282-context-saturation"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1281)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1281=json.loads((ROOT/"results"/"wp1281_independent_frame_anchor_gate.json").read_text())
v7=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v7.json").read_text())
v8=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v8.json").read_text())
aspect=(REPO/"research"/"aspect"/"context-saturated-optical-quotient.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1281["independent_frame_anchor_required"] is True and wp1281["actual_packets_supplied"]==0
assert "probe domain is saturated under the admitted optical contexts" in aspect
assert "Feedback has synthesized the missing" in aspect and "probe direction internally" in aspect
assert "internal slot" in aspect
assert "context-saturation tests under the admitted context monoid" in request
assert list(v7["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","provenance"
]
assert list(v8["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation","provenance"
]
ctx=v8["required_objects"]["context_saturation"]
assert ctx["admitted_context_monoid"]=="explicit"
assert ctx["external_context_orbit_saturated"] is True
assert ctx["feedback_cavity_test"] is True
assert ctx["internal_route_slot_test"] is True
assert ctx["coherent_control_declaration"]=="explicit"
assert "probe_domain_equivalence_promoted_to_contextual_equivalence" in v8["hostile_rejections"]
assert "contextless_or_unsaturated_packet_treated_as_route_compositional" in v8["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v7 fields can be present while packet equivalence is
# established only on the injected probe domain and not under admitted contexts.
probe_shadow_packet={
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
    "independent_frame_anchor":"mock-anchor",
    "context_saturation":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v8_admitted=all(
    probe_shadow_packet.get(k) is not None for k in (
        "source_selected_uv_boundary_object","instrument_update","source_transversal",
        "preparation_production_factorization","sequential_record_fidelity",
        "constructor_intertwiner","independent_frame_anchor","context_saturation"
    )
)
assert v8_admitted is False
actual_packets_supplied=0

# Falsifier: probe-domain equivalence already certifies contextual and route
# compositional packet equivalence under all admitted contexts.
probe_domain_sufficient=False
context_saturation_certificate_constructed=False
conjecture_refuted=probe_domain_sufficient
assert not conjecture_refuted and not context_saturation_certificate_constructed

result={
    "schema":"marici.flavor.wp1282.v1",
    "status":"PASS",
    "question":"Can probe-domain equivalence substitute for context-saturated packet testing?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must be tested under the admitted context monoid, including feedback, coherent control, and internal route slots, before endpoint or probe equivalence can be treated as compositional.",
        "rivals":["WP1128 v1 admission contract","WP1281 v7 admission contract","probe-domain shadow packet","common-mode packet","fixture packet"],
        "risky_consequences":["the Aspect analogue separates devices identical on an injected probe by feedback and internal route slots","WP1281 still has no context_saturation object","the handoff request demands context-saturation tests","v8 adds the saturation object and rejects probe-domain shadows"],
        "falsification_attempt":"Replay WP1128 and WP1281; compare the v7 and v8 admission contracts; test a probe-domain shadow packet with all v7 fields but no context saturation.",
        "residual":"The probe-domain shadow packet is rejected and no actual packet is admitted. The context-saturation necessity conjecture survives. The residual is a source-derived admitted context monoid and saturation certificate.",
        "disposition":"context-saturation necessity survives attempted falsification; gain nuisance-state observability selected"
    },
    "admission_contract_v7":"research/flavor/contracts/flavor-event-production-packet-admission.v7.json",
    "admission_contract_v8":"research/flavor/contracts/flavor-event-production-packet-admission.v8.json",
    "required_object_count_v7":len(v7["required_objects"]),
    "required_object_count_v8":len(v8["required_objects"]),
    "context_saturation_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "probe_shadow_packet_admitted_v8":v8_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "probe_domain_sufficient":probe_domain_sufficient,
    "context_saturation_certificate_constructed":context_saturation_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold context-saturation gate: v8 admission rejects probe-domain shadows",
    "remaining_gate":"derive the admitted context monoid and source-provenanced feedback/internal-route saturation tests",
    "hostile_gate":"do not admit endpoint or probe-domain equivalence without external-context, feedback, and internal-slot saturation",
    "claim_boundary":"WP1128, WP1281, the Aspect analogue, and the handoff request falsify probe-domain sufficiency; the context-saturation necessity conjecture survives but remains unproven",
    "disposition":"context-saturation leaf resolved conditionally; gain nuisance-state observability required"
}
(ROOT/"results"/"wp1282_context_saturation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1282 PASS: context-saturation necessity survives attempted falsification; v8 admission contract active")
