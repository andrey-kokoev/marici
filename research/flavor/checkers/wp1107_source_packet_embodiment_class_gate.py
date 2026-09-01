import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

outputs = [
    "absolute_uv_boundary_lift",
    "integer_clock_lift",
    "oriented_second_stage_frame",
    "independent_rho",
    "production_and_gain",
    "physical16_descent",
]
classes = {
    "shifted_flux_only": {
        "status": "insufficient_current_packet",
        "outputs": {k: False for k in outputs},
        "blocking_evidence": ["wp1071_shifted_flux_cs_interface_no_go", "wp1094_coset_absolute_boundary_action_fiber"],
    },
    "conditional_wilson_krylov_only": {
        "status": "insufficient_current_packet",
        "outputs": {k: False for k in outputs},
        "blocking_evidence": ["wp1089_oriented_adjoint_doublet_breaking_no_go", "wp1090_reciprocal_determinant_rho_no_go", "wp1093_history_dilation_gain_no_go"],
    },
    "finite_scheme_normalization_only": {
        "status": "insufficient_current_packet",
        "outputs": {k: False for k in outputs},
        "blocking_evidence": ["wp1096_normalization_packet_authority_audit_gate", "wp1097_finite_scheme_port_gain_no_go", "wp1098_contact_counterterm_boundary_lift_no_go"],
    },
    "fused_uv_boundary_defect_with_line_and_production_data": {
        "status": "open_positive_class",
        "outputs": {k: True for k in outputs},
        "required_not_constructed": True,
        "blocking_evidence": ["wp1106_minimal_source_packet_authority_bundle"],
    },
}
assert len(classes) == 4
for name in ["shifted_flux_only", "conditional_wilson_krylov_only", "finite_scheme_normalization_only"]:
    assert not any(classes[name]["outputs"].values())
assert all(classes["fused_uv_boundary_defect_with_line_and_production_data"]["outputs"].values())
assert classes["fused_uv_boundary_defect_with_line_and_production_data"]["required_not_constructed"]

coverage_counts = {name: sum(c["outputs"].values()) for name,c in classes.items()}
assert coverage_counts == {
    "shifted_flux_only": 0,
    "conditional_wilson_krylov_only": 0,
    "finite_scheme_normalization_only": 0,
    "fused_uv_boundary_defect_with_line_and_production_data": 6,
}

result = {
    "schema": "marici.flavor.wp1107.v1",
    "status": "PASS",
    "question": "Which source-packet embodiments could supply the six-output WP1106 bundle?",
    "outputs": outputs,
    "candidate_classes": classes,
    "coverage_counts": coverage_counts,
    "classification": "conditional gate: three admitted packet classes are individually insufficient; one fused UV boundary-defect class remains open but unconstructed",
    "remaining_gate": "construct or obtain the fused source packet and verify all six outputs before any selector claim",
    "hostile_gate": "do not fuse conditional constructors by transport, treat class potential as construction, or omit any of the six outputs",
    "claim_boundary": "the positive class is a typed requirement, not evidence that such a packet exists",
    "disposition": "source-packet embodiment classes classified",
}

(ROOT / "results" / "wp1107_source_packet_embodiment_class_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1107 PASS:", len(classes), coverage_counts)
