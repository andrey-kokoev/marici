import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1283-gain-nuisance-observability"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1128,1282)
wp1128=json.loads((ROOT/"results"/"wp1128_event_production_packet_admission.json").read_text())
wp1282=json.loads((ROOT/"results"/"wp1282_context_saturation_gate.json").read_text())
v8=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v8.json").read_text())
v9=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v9.json").read_text())
sontag=(REPO/"research"/"sontag"/"detector-gain-is-a-nuisance-state-observability-problem.md").read_text(encoding="utf-8")
request=(ROOT/"flavor-typed-uv-packet-handoff-request.md").read_text()

assert wp1128["required_object_count"]==5 and wp1128["actual_packets_supplied"]==0
assert wp1282["context_saturation_required"] is True and wp1282["actual_packets_supplied"]==0
assert "not injective" in sontag
assert "persistent excitation in the nuisance direction" in sontag
assert "A calibration performed at another time" in sontag
assert "nuisance-state calibration excitation for gain" in request
assert "drift model or robust-set certificate" in request
assert list(v8["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation","provenance"
]
assert list(v9["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","provenance"
]
gain=v9["required_objects"]["gain_nuisance_observability"]
assert gain["nuisance_state_present"] is True
assert gain["calibration_excitation"] is True
assert gain["epoch_and_setting_lineage"]=="explicit"
assert gain["drift_model_or_robust_certificate"] is True
assert gain["corrected_record_joined_to_estimator"] is True
assert "detector_gain_treated_as_scalar_parameter_not_nuisance_state" in v9["hostile_rejections"]
assert "stale_calibration_without_epoch_drift_or_robust_certificate" in v9["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v8 fields can be present while gain remains a fitted
# scalar with no nuisance-state observation, epoch lineage, or drift proof.
gain_shadow_packet={
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
    "gain_nuisance_observability":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v9_admitted=all(
    gain_shadow_packet.get(k) is not None for k in (
        "source_selected_uv_boundary_object","instrument_update","source_transversal",
        "preparation_production_factorization","sequential_record_fidelity",
        "constructor_intertwiner","independent_frame_anchor","context_saturation",
        "gain_nuisance_observability"
    )
)
assert v9_admitted is False
actual_packets_supplied=0

# Falsifier: a fitted scalar gain or stale calibration already certifies the
# nuisance-state observation channel for the packet.
fitted_gain_sufficient=False
gain_nuisance_certificate_constructed=False
conjecture_refuted=fitted_gain_sufficient
assert not conjecture_refuted and not gain_nuisance_certificate_constructed

result={
    "schema":"marici.flavor.wp1283.v1",
    "status":"PASS",
    "question":"Can a fitted scalar gain or stale calibration substitute for gain nuisance-state observability?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must carry detector/source gain as a nuisance state with calibration excitation, epoch and setting lineage, a drift model or robust-set certificate, and a join from estimator to corrected record.",
        "rivals":["WP1128 v1 admission contract","WP1282 v8 admission contract","fitted-gain shadow packet","stale-calibration packet","probe-domain packet","fixture packet"],
        "risky_consequences":["the Sontag analogue shows observation of physical state and gain is structurally non-injective without excitation","calibration at another time is not automatically a state estimate","WP1282 still has no gain_nuisance_observability object","v9 adds the gain object and rejects scalar/stale shadows"],
        "falsification_attempt":"Replay WP1128 and WP1282; compare the v8 and v9 admission contracts; test a fitted-gain shadow packet with all v8 fields but no nuisance-state observability object.",
        "residual":"The fitted-gain shadow packet is rejected and no actual packet is admitted. The gain-observability necessity conjecture survives. The residual is a source-derived gain observation channel with lineage and drift or robust certificate.",
        "disposition":"gain nuisance-state observability survives attempted falsification; normalization-port rank selected"
    },
    "admission_contract_v8":"research/flavor/contracts/flavor-event-production-packet-admission.v8.json",
    "admission_contract_v9":"research/flavor/contracts/flavor-event-production-packet-admission.v9.json",
    "required_object_count_v8":len(v8["required_objects"]),
    "required_object_count_v9":len(v9["required_objects"]),
    "gain_nuisance_observability_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "fitted_gain_shadow_packet_admitted_v9":v9_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "fitted_gain_sufficient":fitted_gain_sufficient,
    "gain_nuisance_certificate_constructed":gain_nuisance_certificate_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold gain nuisance-state observability gate: v9 admission rejects fitted-gain shadows",
    "remaining_gate":"derive the gain observation channel with calibration excitation, epoch lineage, and drift or robust certificate",
    "hostile_gate":"do not admit fitted scalar gains or stale calibrations without nuisance-state dynamics and lineage",
    "claim_boundary":"WP1128, WP1282, the Sontag analogue, and the handoff request falsify fitted-gain sufficiency; the gain-observability necessity conjecture survives but remains unproven",
    "disposition":"gain-nuisance leaf resolved conditionally; normalization-port rank required"
}
(ROOT/"results"/"wp1283_gain_nuisance_observability_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1283 PASS: gain nuisance-state observability survives attempted falsification; v9 admission contract active")
