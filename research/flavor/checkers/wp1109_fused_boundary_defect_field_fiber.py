import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

fields = {
    "absolute_uv_boundary_lift": ["integer_exponents7", "counterterm_basis", "evaluation_law"],
    "integer_clock_lift": ["n", "sigma", "unit_orbit", "source_normalization"],
    "oriented_second_stage_frame": ["adjoint_ray", "ordered_lines", "cyclic_seed", "history_dilation"],
    "independent_rho": ["section", "line_bundle", "descent_law", "temporal_scope", "comparison_node"],
    "production_and_gain": ["six_row_kernel", "event_weights", "channel_selection", "gain_three_halves"],
    "physical16_descent": ["quotient_map", "comparison_normalization", "frozen_readout_provenance"],
}
assert len(fields) == 6
field_arity = {k: len(v) for k,v in fields.items()}
assert field_arity == {
    "absolute_uv_boundary_lift": 3,
    "integer_clock_lift": 4,
    "oriented_second_stage_frame": 4,
    "independent_rho": 5,
    "production_and_gain": 4,
    "physical16_descent": 3,
}
total_fields = sum(field_arity.values())
assert total_fields == 23

constraints = {
    "exponents_are_integer_vector": {"length": 7},
    "unit_orbit_is_6n_squared": True,
    "sigma_is_sign": True,
    "rho_weight_is_minus_3": True,
    "kernel_shape_is_6_by_6": True,
    "gain_is_three_halves": True,
}
n_type = "integer_unspecified"
sigma_type = "sign_unspecified"
unit_orbit_law = "6*n*n"
rho_weight = -3
kernel_shape = (6,6)
gain = Fraction(3,2)
assert constraints["exponents_are_integer_vector"]["length"] == 7
assert unit_orbit_law == "6*n*n"
assert rho_weight == -3
assert kernel_shape == (6,6)
assert gain == Fraction(3,2)

constructed_values = {k: False for k in fields}
assert not any(constructed_values.values())

result = {
    "schema": "marici.flavor.wp1109.v1",
    "status": "PASS",
    "question": "What fields must a genuinely new fused UV boundary defect add?",
    "fields": fields,
    "field_arity": field_arity,
    "total_fields": total_fields,
    "constraints": constraints,
    "n_type": n_type,
    "sigma_type": sigma_type,
    "unit_orbit_law": unit_orbit_law,
    "rho_weight": rho_weight,
    "kernel_shape": list(kernel_shape),
    "gain": str(gain),
    "constructed_values": constructed_values,
    "classification": "conditional gate: 23-field constructor fiber for the six-output defect packet",
    "remaining_gate": "derive anomaly/analytic constraints on these fields and then construct source-authorized values",
    "hostile_gate": "do not treat field names, placeholder variables, or arity bookkeeping as a constructed source packet",
    "claim_boundary": "this is the missing-data fiber for G3a, not a positive defect construction",
    "disposition": "new fused-defect field specification completed",
}

(ROOT / "results" / "wp1109_fused_boundary_defect_field_fiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1109 PASS:", len(fields), total_fields, kernel_shape, gain)
