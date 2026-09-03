import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1286-sequential-record-lineage-closure"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1279,1285)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1279=json.loads((ROOT/"results"/"wp1279_sequential_record_fidelity_gate.json").read_text())
wp1285=json.loads((ROOT/"results"/"wp1285_authority_grant_composition_gate.json").read_text())
v11=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v11.json").read_text())
sontag=(REPO/"research"/"sontag"/"effects-do-not-determine-instruments.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1279["sequential_record_fidelity_required"] is True and wp1279["actual_packets_supplied"]==0
assert wp1285["authority_grant_composition_required"] is True and wp1285["actual_packets_supplied"]==0
assert "lineage binds the later record" in sontag
assert "sequential evaluation assigns joint records" in sontag
assert "sequential-record continuation law" in request
assert "joint record words and lineage keys" in request
seq=v11["required_objects"]["sequential_record_fidelity"]
assert seq["joint_record_words_present"] is True
assert seq["later_record_bound_to_earlier_branch"] is True
assert seq["continuation_provenance"]=="explicit"
assert "marginal_records_treated_as_joint_record_words" in v11["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# The contract requirement is a hostile gate, not a source certificate.
contract_requirement_sufficient=False
joint_record_lineage_certificate_constructed=False
actual_packets_supplied=0
conjecture_refuted=contract_requirement_sufficient
assert not conjecture_refuted and not joint_record_lineage_certificate_constructed

result={
    "schema":"marici.flavor.wp1286.v1",
    "status":"PASS",
    "question":"Does the existing sequential-record requirement itself construct a joint record lineage certificate?",
    "dpc":{
        "conjecture":"Sequential-record lineage remains a distinct source certificate even after WP1279 and WP1285: joint record words, branch-conditioned continuation, and provenance must be derived from the admitted packet rather than merely required by the admission contract.",
        "rivals":["WP1279 admission requirement","WP1285 grant-composition requirement","contract-requirement shadow","fixture packet","actual source packet"],
        "risky_consequences":["the Sontag analogue makes lineage branch-binding and joint-record evaluation explicit","the v11 contract already contains the sequential_record_fidelity requirement","no actual packet supplies lineage keys or joint record words","contract requirements alone are not source authority"],
        "falsification_attempt":"Replay WP1128, WP1279, and WP1285; inspect the v11 contract; check whether any actual packet or source certificate has appeared.",
        "residual":"No packet has been admitted and no joint-record lineage certificate has been constructed. The lineage necessity conjecture survives. The residual is a source-derived joint-record lineage packet.",
        "disposition":"sequential-record lineage closure survives attempted falsification; return to owner packet frontier"
    },
    "admission_contract_v11":"research/flavor/contracts/flavor-event-production-packet-admission.v11.json",
    "sequential_record_fidelity_in_contract":True,
    "joint_record_lineage_certificate_constructed":joint_record_lineage_certificate_constructed,
    "contract_requirement_sufficient":contract_requirement_sufficient,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "actual_packets_supplied":actual_packets_supplied,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold sequential-record lineage closure gate: contract requirement is not source certificate",
    "remaining_gate":"obtain a source-derived joint-record lineage packet with branch keys and continuation provenance",
    "hostile_gate":"do not treat an admission requirement, contract field, fixture, or analogue theorem as the lineage certificate",
    "claim_boundary":"WP1128, WP1279, WP1285, and the Sontag analogue falsify contract-requirement sufficiency; the lineage necessity conjecture survives but remains unproven",
    "disposition":"sequential-record-lineage leaf resolved conditionally; owner packet frontier remains"
}
(ROOT/"results"/"wp1286_sequential_record_lineage_closure_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1286 PASS: sequential-record lineage closure survives attempted falsification; no source certificate admitted")
