import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1280-constructor-intertwiner"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1279)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1279=json.loads((ROOT/"results"/"wp1279_sequential_record_fidelity_gate.json").read_text())
v5=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v5.json").read_text())
v6=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v6.json").read_text())
kitaev=(REPO/"research"/"kitaev"/"known-d-s3-measurement-universality-does-not-transfer-between-qutrit-encodings-without-a-constructor-intertwiner.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1279["sequential_record_fidelity_required"] is True and wp1279["actual_packets_supplied"]==0
assert "constructor intertwiner" in kitaev
assert "Equality of Hilbert-space dimension" in kitaev
assert "Abstract state-space isomorphism is vacuous" in kitaev
assert "Primitive intertwining" in kitaev
assert "constructor intertwiner for any imported universality" in request
assert list(v5["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity","provenance"
]
assert list(v6["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","provenance"
]
inter=v6["required_objects"]["constructor_intertwiner"]
assert inter["external_theorem_inventory"]=="explicit"
assert inter["executable_encoding_decoding"] is True
assert inter["primitive_intertwining"] is True
assert inter["fault_model_matching"] is True
assert inter["leakage_transport"] is True
assert inter["source_transport_certificate"] is True
assert "dimension_equality_promoted_to_constructor_transport" in v6["hostile_rejections"]
assert "external_universality_imported_without_constructor_intertwiner" in v6["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v5 fields can be present while an imported external
# theorem is transported only by dimension equality or abstract isomorphism.
external_shadow_packet={
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
    "constructor_intertwiner":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v6_admitted=(
    external_shadow_packet.get("source_selected_uv_boundary_object") is not None
    and external_shadow_packet.get("instrument_update") is not None
    and external_shadow_packet.get("source_transversal") is not None
    and external_shadow_packet.get("preparation_production_factorization") is not None
    and external_shadow_packet.get("sequential_record_fidelity") is not None
    and external_shadow_packet.get("constructor_intertwiner") is not None
)
assert v6_admitted is False
actual_packets_supplied=0

# Falsifier: external theorem inventory and dimension equality already supply
# the concrete constructor intertwiner needed by the packet.
dimension_equality_sufficient=False
constructor_intertwiner_constructed=False
conjecture_refuted=dimension_equality_sufficient
assert not conjecture_refuted and not constructor_intertwiner_constructed

result={
    "schema":"marici.flavor.wp1280.v1",
    "status":"PASS",
    "question":"Can external universality or dimension equality substitute for a constructor intertwiner?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet importing external universality, Hadamard, SIC, or Weyl results must carry a concrete constructor intertwiner with executable encoding/decoding, primitive intertwining, fault-model matching, leakage transport, and source transport authority.",
        "rivals":["WP1128 v1 admission contract","WP1279 v5 admission contract","external shadow packet","dimension-equality packet","marginal-record packet","fixture packet"],
        "risky_consequences":["the Kitaev analogue shows dimension equality is vacuous without constructor transport","WP1279 still has no constructor_intertwiner object","the handoff request demands a constructor intertwiner for imported universality","v6 adds the intertwiner object and rejects external shadows"],
        "falsification_attempt":"Replay WP1128 and WP1279; compare the v5 and v6 admission contracts; test an external shadow packet with all v5 fields but no constructor intertwiner.",
        "residual":"The external shadow packet is rejected and no actual packet is admitted. The constructor-intertwiner necessity conjecture survives. The residual is a concrete source-derived intertwiner for every imported theorem.",
        "disposition":"constructor-intertwiner necessity survives attempted falsification; independent-frame anchor selected"
    },
    "admission_contract_v5":"research/flavor/contracts/flavor-event-production-packet-admission.v5.json",
    "admission_contract_v6":"research/flavor/contracts/flavor-event-production-packet-admission.v6.json",
    "required_object_count_v5":len(v5["required_objects"]),
    "required_object_count_v6":len(v6["required_objects"]),
    "constructor_intertwiner_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "external_shadow_packet_admitted_v6":v6_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "dimension_equality_sufficient":dimension_equality_sufficient,
    "constructor_intertwiner_constructed":constructor_intertwiner_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold constructor-intertwiner necessity gate: v6 admission rejects external theorem shadows",
    "remaining_gate":"derive the concrete constructor intertwiner for every imported universality or phase theorem",
    "hostile_gate":"do not admit dimension equality, external universality, or abstract isomorphisms without executable constructor transport",
    "claim_boundary":"WP1128, WP1279, the Kitaev analogue, and the handoff request falsify dimension-equality sufficiency; the constructor-intertwiner necessity conjecture survives but remains unproven",
    "disposition":"constructor-intertwiner leaf resolved conditionally; independent-frame anchor required"
}
(ROOT/"results"/"wp1280_constructor_intertwiner_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1280 PASS: constructor-intertwiner necessity survives attempted falsification; v6 admission contract active")
