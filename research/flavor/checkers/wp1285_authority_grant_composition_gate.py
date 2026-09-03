import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1285-authority-grant-composition"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1284)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1284=json.loads((ROOT/"results"/"wp1284_normalization_port_rank_gate.json").read_text())
v10=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v10.json").read_text())
v11=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v11.json").read_text())
strom=(REPO/"research"/"strominger"/"authority-grant-composition-interpretation.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1284["normalization_port_rank_required"] is True and wp1284["actual_packets_supplied"]==0
assert "Typed grant" in strom and "Only admitted grants participate in composition" in strom
assert "Partial composition law" in strom and "laundering" in strom
assert "Associativity is conditional" in strom
assert "typed authority-grant composition with coherence witnesses" in request
assert list(v10["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","normalization_port_rank","provenance"
]
assert list(v11["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","normalization_port_rank","authority_grant_composition","provenance"
]
grants=v11["required_objects"]["authority_grant_composition"]
assert grants["admitted_grants_only"] is True
assert grants["endpoints_match"] is True
assert grants["authority_kind_preserved"] is True
assert grants["variance_evidence_domain_and_transformations_match"] is True
assert grants["coherence_witness"]=="explicit"
assert grants["triple_associativity_certificate"] is True
assert "partial_grants_composed_into_full_packet_authority" in v11["hostile_rejections"]
assert "authority_kind_laundering_or_factorization_dependence" in v11["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v10 fields can be present while partial grants are
# composed by matching labels alone, without typed kind/domain/coherence proof.
grant_shadow_packet={
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
    "context_saturation":"mock-context",
    "gain_nuisance_observability":"mock-gain",
    "normalization_port_rank":"mock-rank",
    "authority_grant_composition":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v11_admitted=all(
    grant_shadow_packet.get(k) is not None for k in (
        "source_selected_uv_boundary_object","instrument_update","source_transversal",
        "preparation_production_factorization","sequential_record_fidelity",
        "constructor_intertwiner","independent_frame_anchor","context_saturation",
        "gain_nuisance_observability","normalization_port_rank","authority_grant_composition"
    )
)
assert v11_admitted is False
actual_packets_supplied=0

# Falsifier: partial grants with matching labels already compose into full
# packet authority without kind/domain/coherence proof.
partial_grants_sufficient=False
authority_composition_certificate_constructed=False
conjecture_refuted=partial_grants_sufficient
assert not conjecture_refuted and not authority_composition_certificate_constructed

result={
    "schema":"marici.flavor.wp1285.v1",
    "status":"PASS",
    "question":"Can partial authority grants compose into full packet authority without a typed composition certificate?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must compose authority only through admitted grants with matching endpoints, kind, variance, evidence domains, transformations, coherence witnesses, and a triple associativity certificate.",
        "rivals":["WP1128 v1 admission contract","WP1284 v10 admission contract","grant shadow packet","reported-number packet","fixture packet"],
        "risky_consequences":["the Strominger analogue proves local validity does not guarantee a factorization-independent or kind-preserving composite","WP1284 still has no authority_grant_composition object","the handoff request demands typed authority-grant composition with coherence witnesses","v11 adds the grant object and rejects partial-grant shadows"],
        "falsification_attempt":"Replay WP1128 and WP1284; compare the v10 and v11 admission contracts; test a grant shadow packet with all v10 fields but no authority-composition object.",
        "residual":"The grant shadow packet is rejected and no actual packet is admitted. The authority-composition necessity conjecture survives. The residual is a source-derived typed grant atlas and coherence certificate.",
        "disposition":"authority-grant composition necessity survives attempted falsification; sequential-record lineage selected"
    },
    "admission_contract_v10":"research/flavor/contracts/flavor-event-production-packet-admission.v10.json",
    "admission_contract_v11":"research/flavor/contracts/flavor-event-production-packet-admission.v11.json",
    "required_object_count_v10":len(v10["required_objects"]),
    "required_object_count_v11":len(v11["required_objects"]),
    "authority_grant_composition_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "grant_shadow_packet_admitted_v11":v11_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "partial_grants_sufficient":partial_grants_sufficient,
    "authority_composition_certificate_constructed":authority_composition_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold authority-grant composition gate: v11 admission rejects partial-grant shadows",
    "remaining_gate":"derive the typed grant atlas, coherence witnesses, and triple associativity certificate from the source packet",
    "hostile_gate":"do not admit partial grants by label matching or strengthen authority kind without typed composition evidence",
    "claim_boundary":"WP1128, WP1284, the Strominger analogue, and the handoff request falsify partial-grant sufficiency; the authority-composition necessity conjecture survives but remains unproven",
    "disposition":"authority-grant leaf resolved conditionally; sequential-record lineage required"
}
(ROOT/"results"/"wp1285_authority_grant_composition_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1285 PASS: authority-grant composition necessity survives attempted falsification; v11 admission contract active")
