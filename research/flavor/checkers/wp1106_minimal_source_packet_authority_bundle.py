import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "contracts" / "flavor-interaction-net-state.v1.json").read_text())
node_ids = {n["id"] for n in contract["nodes"]}

requirements = {
    "absolute_uv_boundary_lift": {
        "needed": "absolute seven-channel Chern-Simons lift, counterterm convention, endpoint orientation, and coset realization",
        "closed_shortcuts": ["wp1094_coset_absolute_boundary_action_fiber", "wp1098_contact_counterterm_boundary_lift_no_go"],
    },
    "integer_clock_lift": {
        "needed": "integer n, sign sigma, unit orbit B/A=6n^2, and source normalization",
        "closed_shortcuts": ["wp1095_wilson_integer_lift_clock_no_go", "wp1099_integral_lattice_clock_orientation_no_go", "wp1101_anomaly_denominator_clock_no_go", "wp1104_pairing_trace_clock_no_go"],
    },
    "oriented_second_stage_frame": {
        "needed": "oriented adjoint ray, ordered B lines, cyclic seed, and history dilation without quartet destruction",
        "closed_shortcuts": ["wp1089_oriented_adjoint_doublet_breaking_no_go", "wp1092_conditional_wilson_production_kernel_no_go"],
    },
    "independent_rho": {
        "needed": "independent weight-(-3) section with line bundle, descent law, temporal scope, and comparison node",
        "closed_shortcuts": ["wp1090_reciprocal_determinant_rho_no_go", "wp1091_source_natural_negative_weight_scalar_no_go", "wp1103_pairing_cyclic_ray_rho_no_go"],
    },
    "production_and_gain": {
        "needed": "six-row branch-to-physical16 coupling matrix, event reweighting, channel selection, and gain 3/2",
        "closed_shortcuts": ["wp1093_history_dilation_gain_no_go", "wp1097_finite_scheme_port_gain_no_go", "wp1100_alternating_cubic_production_kernel_no_go", "wp1102_bifundamental_pairing_production_kernel_no_go", "wp1105_history_pairing_gain_no_go"],
    },
    "physical16_descent": {
        "needed": "source-authorized quotient descent, comparison node, normalization, and frozen readout provenance",
        "closed_shortcuts": ["wp1096_normalization_packet_authority_audit_gate"],
    },
}
assert len(requirements) == 6
for req in requirements.values():
    assert req["closed_shortcuts"]
    assert set(req["closed_shortcuts"]) <= node_ids

closed_count = sum(len(r["closed_shortcuts"]) for r in requirements.values())
assert closed_count == 17
available_outputs = {k: False for k in requirements}
assert not any(available_outputs.values())

result = {
    "schema": "marici.flavor.wp1106.v1",
    "status": "PASS",
    "question": "What minimal authority bundle must the successful source packet supply?",
    "requirements": requirements,
    "closed_shortcut_count": closed_count,
    "available_outputs": available_outputs,
    "classification": "conditional gate: six-output source-packet interface frozen from verified negative gates",
    "remaining_gate": "construct or obtain one source packet supplying all six outputs with explicit provenance and no target fitting",
    "hostile_gate": "do not promote any subset, internal invariant, conditional constructor, normalization port, or owner silence into the full authority bundle",
    "claim_boundary": "this is an interface synthesis, not a claimed positive construction",
    "disposition": "minimal missing-authority bundle frozen",
}

(ROOT / "results" / "wp1106_minimal_source_packet_authority_bundle.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1106 PASS:", len(requirements), closed_count, len(node_ids))
