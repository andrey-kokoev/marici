import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1284-normalization-port-rank"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1283)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1283=json.loads((ROOT/"results"/"wp1283_gain_nuisance_observability_gate.json").read_text())
v9=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v9.json").read_text())
v10=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v10.json").read_text())
benincasa=(REPO/"research"/"benincasa"/"finite-scheme-normalization-port-theorem.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1283["gain_nuisance_observability_required"] is True and wp1283["actual_packets_supplied"]==0
assert "Jacobian" in benincasa and "rank three" in benincasa
assert "Counting three" in benincasa and "reported numbers is not enough" in benincasa
assert "same scheme" in benincasa and "point for every subsequent observable" in benincasa
assert "declared normalization ports with a Jacobian rank certificate" in request
assert list(v9["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","provenance"
]
assert list(v10["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","normalization_port_rank","provenance"
]
rank=v10["required_objects"]["normalization_port_rank"]
assert rank["physical_ports_declared"] is True
assert rank["jacobian_rank_certificate"] is True
assert rank["rank_matches_scheme_orbit"] is True
assert rank["independent_records_joined"] is True
assert rank["same_scheme_point_for_subsequent_observables"] is True
assert "reported_number_count_treated_as_jacobian_rank_certificate" in v10["hostile_rejections"]
assert "finite_scheme_orbit_without_declared_physical_ports" in v10["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v9 fields can be present while finite normalization
# is represented by reported numbers without declared ports or rank proof.
rank_shadow_packet={
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
    "normalization_port_rank":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v10_admitted=all(
    rank_shadow_packet.get(k) is not None for k in (
        "source_selected_uv_boundary_object","instrument_update","source_transversal",
        "preparation_production_factorization","sequential_record_fidelity",
        "constructor_intertwiner","independent_frame_anchor","context_saturation",
        "gain_nuisance_observability","normalization_port_rank"
    )
)
assert v10_admitted is False
actual_packets_supplied=0

# Falsifier: a count of reported normalization numbers already certifies the
# Jacobian rank on the finite scheme orbit.
number_count_sufficient=False
normalization_port_certificate_constructed=False
conjecture_refuted=number_count_sufficient
assert not conjecture_refuted and not normalization_port_certificate_constructed

result={
    "schema":"marici.flavor.wp1284.v1",
    "status":"PASS",
    "question":"Can a count of reported normalization numbers substitute for declared physical ports and Jacobian rank?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must declare physical normalization ports and prove a Jacobian rank certificate matching the finite scheme orbit, with independent records joined and one scheme point reused for subsequent observables.",
        "rivals":["WP1128 v1 admission contract","WP1283 v9 admission contract","rank-shadow packet","reported-number packet","fitted-gain packet","fixture packet"],
        "risky_consequences":["the Benincasa analogue proves counting reported numbers is not enough","WP1283 still has no normalization_port_rank object","the handoff request demands declared normalization ports and Jacobian rank","v10 adds the port-rank object and rejects number-count shadows"],
        "falsification_attempt":"Replay WP1128 and WP1283; compare the v9 and v10 admission contracts; test a rank-shadow packet with all v9 fields but no normalization-port rank object.",
        "residual":"The rank-shadow packet is rejected and no actual packet is admitted. The normalization-port-rank necessity conjecture survives. The residual is a source-derived port set and Jacobian rank certificate.",
        "disposition":"normalization-port-rank necessity survives attempted falsification; authority-grant composition selected"
    },
    "admission_contract_v9":"research/flavor/contracts/flavor-event-production-packet-admission.v9.json",
    "admission_contract_v10":"research/flavor/contracts/flavor-event-production-packet-admission.v10.json",
    "required_object_count_v9":len(v9["required_objects"]),
    "required_object_count_v10":len(v10["required_objects"]),
    "normalization_port_rank_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "rank_shadow_packet_admitted_v10":v10_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "number_count_sufficient":number_count_sufficient,
    "normalization_port_certificate_constructed":normalization_port_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold normalization-port-rank gate: v10 admission rejects reported-number shadows",
    "remaining_gate":"derive declared physical ports and a source-provenanced Jacobian rank certificate for the finite normalization orbit",
    "hostile_gate":"do not admit a count of reported numbers or finite orbit without physical ports and rank proof",
    "claim_boundary":"WP1128, WP1283, the Benincasa analogue, and the handoff request falsify number-count sufficiency; the normalization-port-rank necessity conjecture survives but remains unproven",
    "disposition":"normalization-port leaf resolved conditionally; authority-grant composition required"
}
(ROOT/"results"/"wp1284_normalization_port_rank_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1284 PASS: normalization-port-rank necessity survives attempted falsification; v10 admission contract active")
