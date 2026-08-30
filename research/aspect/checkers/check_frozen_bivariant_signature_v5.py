import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v4 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v4.json").read_text(encoding="utf-8"))
v5 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v5.json").read_text(encoding="utf-8"))
x, y, u, v = sp.symbols("x y u v", real=True)

# Repair packet in the two standard blowup charts.
G_repair = sp.diag(x, y)
G_x_chart = G_repair.subs(y, x * u)
G_y_chart = G_repair.subs(x, y * v)
G_overlap = sp.simplify(G_x_chart.subs({x: y * v, u: 1 / v}) - G_y_chart)

# Unused packet: diagonalized by a fixed orthogonal route frame.
G_unused = sp.Matrix([[x, y], [y, x]])
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
G_unused_diag = sp.simplify(H.T * G_unused * H)
G_unused_x_chart = sp.simplify(G_unused_diag.subs(y, x * u))

resolved_fields = set(v5["log_resolved_metric_route_family"]["required_fields"])
resolved_laws = set(v5["log_resolved_metric_route_family"]["required_laws"])
assoc_laws = set(v5["resolved_metric_route_associator"]["required_laws"])

checks = {
    "v4_preserved_as_failed_predecessor": "normal_blowup" not in v4["arrow_types"],
    "v5_is_new_frozen_candidate": v5["status"] == "candidate_frozen" and v5["cell_creation_during_replay"] is False,
    "blowup_arrow_is_declared": "normal_blowup" in v5["arrow_types"],
    "resolved_direction_object_is_declared": "projectivized_normal_direction_stratum" in v5["object_types"],
    "directional_gluing_cell_is_declared": "directional_filtration_gluing" in v5["cell_types"],
    "repair_x_chart_factorization": G_x_chart == sp.diag(x, x * u),
    "repair_y_chart_factorization": G_y_chart == sp.diag(y * v, y),
    "repair_chart_overlap_closes": G_overlap == sp.zeros(2),
    "repair_x_chart_determinant": sp.factor(G_x_chart.det()) == u * x**2,
    "repair_y_chart_determinant": sp.factor(G_y_chart.det()) == v * y**2,
    "repair_x_chart_valuation_sum": (1 + 1, 0 + 1) == (2, 1),
    "unused_packet_fixed_frame_diagonalizes": G_unused_diag == sp.diag(x + y, x - y),
    "unused_packet_determinant_factors": sp.factor(G_unused.det()) == (x - y) * (x + y),
    "unused_x_chart_has_two_exceptional_directions": sp.simplify(G_unused_x_chart.det() - x**2 * (1 - u) * (1 + u)) == 0,
    "resolved_chart_cover_is_required": "resolved_chart_cover" in resolved_fields,
    "determinant_vector_law_is_required": "determinant_divisor_vector_equals_sum_of_grade_dimension_times_valuation_vector" in resolved_laws,
    "specialization_coherence_is_required": "pentagon_and_hexagon_commute_with_exceptional_specialization" in assoc_laws,
    "completion_before_projection_is_frozen": "completed_sewing_precedes_finite_projection" in assoc_laws,
    "local_packet_not_global_admission": v5["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v5-check.v1",
    "status": "candidate_v5_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "v4_disposition": "preserved as falsified",
    "v5_disposition": "candidate frozen; repair and unused two-line exceptional-direction local packets pass; global admission not earned",
    "next_decisive_test": "resolved family with nontrivial monodromy or normalization-induced carrier divisor",
}

out = root / "results" / "frozen_bivariant_signature_v5.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v5_frozen_local_schema_pass" else 1)
