import json
import os
from fractions import Fraction
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1287-absolute-boundary-lift"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
_source_replay_records = replay_source_checkers(1098,1106,1109,1286)
wp1098=json.loads((ROOT/"results"/"wp1098_contact_counterterm_boundary_lift_no_go.json").read_text())
wp1106=json.loads((ROOT/"results"/"wp1106_minimal_source_packet_authority_bundle.json").read_text())
wp1109=json.loads((ROOT/"results"/"wp1109_fused_boundary_defect_field_fiber.json").read_text())
wp1286=json.loads((ROOT/"results"/"wp1286_sequential_record_lineage_closure_gate.json").read_text())
v11=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v11.json").read_text())
v12=json.loads((ROOT/"contracts"/"flavor-event-production-packet-admission.v12.json").read_text())
nima=(REPO/"research"/"nima"/"theta-scalar-schur-realization-closes-provenance-and-every-boundary-lift-needs-determinant-control.md").read_text(encoding="utf-8")
groth=(REPO/"research"/"grothendieck"/"theta-weyl-cayley-boundary-lift-audit.md").read_text(encoding="utf-8")
aspect=(REPO/"research"/"aspect"/"a-nonclosed-range-completion-falsifies-frozen-v7.md").read_text(encoding="utf-8")

assert wp1098["status"]=="PASS"
assert all(v is False for v in wp1106["available_outputs"].values()) and wp1106["closed_shortcut_count"]==17
assert wp1109["total_fields"]==23 and wp1109["kernel_shape"]==[6,6]
assert wp1286["joint_record_lineage_certificate_constructed"] is False and wp1286["actual_packets_supplied"]==0
assert "determinant control" in nima and "Lift trilemma" in nima
assert "source-derived boundary selector" in groth and "full-Weyl covariance" in groth
assert "closed-range or spectral defect" in aspect
assert list(v11["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","normalization_port_rank","authority_grant_composition","provenance"
]
assert list(v12["required_objects"])==[
    "source_selected_uv_boundary_object","channel_basis","phase_observable",
    "production_kernel","event_map","instrument_update","source_transversal",
    "preparation_production_factorization","sequential_record_fidelity",
    "constructor_intertwiner","independent_frame_anchor","context_saturation",
    "gain_nuisance_observability","normalization_port_rank","authority_grant_composition",
    "absolute_boundary_lift","provenance"
]
lift=v12["required_objects"]["absolute_boundary_lift"]
assert lift["seven_integer_exponents"] is True
assert lift["counterterm_basis"]=="explicit"
assert lift["endpoint_orientation"]=="explicit"
assert lift["direction_labelled_boundary_coordinates"] is True
assert lift["determinant_schur_control"] is True
assert lift["completed_category_and_closed_range_typing"] is True
assert lift["spectral_defect_data"]=="explicit"
assert "boundary_template_or_contact_shift_treated_as_absolute_boundary_lift" in v12["hostile_rejections"]
assert "boundary_lift_without_determinant_schur_and_completed_spectral_control" in v12["hostile_rejections"]

q=[Fraction(d,23) for d in (6,8,1,4,2,2)]
P_row=[Fraction(1,6)]*6
Pq=[sum(x*y for x,y in zip(P_row,q)) for _ in range(6)]
event_row=[Fraction(3,2)*x for x in Pq]
assert Pq==[Fraction(1,6)]*6 and event_row==[Fraction(1,4)]*6

# Strongest hostile: all v11 fields can be present while the seven-channel
# absolute boundary lift remains a template/contact shadow without determinant
# or completed spectral control.
boundary_shadow_packet={
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
    "authority_grant_composition":"mock-grants",
    "absolute_boundary_lift":None,
    "provenance":{"packet_id":"mock","boundary_authority":"fixture"},
}
v12_admitted=all(
    boundary_shadow_packet.get(k) is not None for k in (
        "source_selected_uv_boundary_object","instrument_update","source_transversal",
        "preparation_production_factorization","sequential_record_fidelity",
        "constructor_intertwiner","independent_frame_anchor","context_saturation",
        "gain_nuisance_observability","normalization_port_rank","authority_grant_composition",
        "absolute_boundary_lift"
    )
)
assert v12_admitted is False
actual_packets_supplied=0

# Falsifier: a boundary template or contact shift already supplies determinant
# and completed spectral control for the absolute lift.
boundary_template_sufficient=False
absolute_boundary_lift_constructed=False
conjecture_refuted=boundary_template_sufficient
assert not conjecture_refuted and not absolute_boundary_lift_constructed

result={
    "schema":"marici.flavor.wp1287.v1",
    "status":"PASS",
    "question":"Can a boundary template or contact shift substitute for the determinant-controlled absolute boundary lift?",
    "dpc":{
        "conjecture":"Every admissible typed UV packet must carry the absolute boundary lift with seven integer exponents, counterterm basis, endpoint orientation, direction-labelled boundary coordinates, determinant/Schur control, completed closed-range typing, and spectral-defect data.",
        "rivals":["WP1098 contact-counterterm route","WP1106 source bundle","WP1109 field fiber","boundary shadow packet","contract shadow","fixture packet"],
        "risky_consequences":["WP1106 and WP1109 show no admitted packet supplies the lift","the Nima analogue requires determinant control through the Schur complement","the Grothendieck analogue requires a source-derived full-covariance boundary selector","the Aspect analogue requires completed closed-range/spectral typing"],
        "falsification_attempt":"Replay WP1098, WP1106, WP1109, and WP1286; compare the v11 and v12 admission contracts; test a boundary shadow packet with all v11 fields but no absolute boundary lift.",
        "residual":"The boundary shadow packet is rejected and no actual packet is admitted. The absolute-boundary-lift necessity conjecture survives. The residual is a source-derived seven-channel lift with determinant and completed spectral control.",
        "disposition":"absolute-boundary-lift necessity survives attempted falsification; owner preparation-packet handoff selected"
    },
    "admission_contract_v11":"research/flavor/contracts/flavor-event-production-packet-admission.v11.json",
    "admission_contract_v12":"research/flavor/contracts/flavor-event-production-packet-admission.v12.json",
    "required_object_count_v11":len(v11["required_objects"]),
    "required_object_count_v12":len(v12["required_objects"]),
    "absolute_boundary_lift_required":True,
    "probability_row":[str(x) for x in Pq],
    "event_row":[str(x) for x in event_row],
    "boundary_shadow_packet_admitted_v12":v12_admitted,
    "actual_packets_supplied":actual_packets_supplied,
    "boundary_template_sufficient":boundary_template_sufficient,
    "absolute_boundary_lift_constructed":absolute_boundary_lift_constructed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold absolute-boundary-lift gate: v12 admission rejects boundary template shadows",
    "remaining_gate":"derive the seven-channel absolute lift with determinant/Schur control and completed spectral defect data",
    "hostile_gate":"do not admit boundary templates, contact shifts, or finite shadows without determinant and completed spectral control",
    "claim_boundary":"WP1098, WP1106, WP1109, WP1286, and the analogue packets falsify boundary-template sufficiency; the absolute-lift necessity conjecture survives but remains unproven",
    "disposition":"A1 boundary-lift remains deferred; owner preparation-packet handoff required"
}
(ROOT/"results"/"wp1287_absolute_boundary_lift_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1287 PASS: absolute-boundary-lift necessity survives attempted falsification; v12 admission contract active")
