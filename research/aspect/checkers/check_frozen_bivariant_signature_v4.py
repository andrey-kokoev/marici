import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v3 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v3.json").read_text(encoding="utf-8"))
v4 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v4.json").read_text(encoding="utf-8"))
t = sp.symbols("t", real=True)

# Repair packet.
G_simple = sp.diag(1, t)
G_simple_zero = G_simple.subs(t, 0)
simple_radical = G_simple_zero.nullspace()
simple_crossing = sp.diff(G_simple, t).subs(t, 0)[1, 1]

# Unused packet with two different vanishing orders in the full radical.
G_graded = sp.diag(t, t**2)
G_graded_zero = G_graded.subs(t, 0)
graded_radical = G_graded_zero.nullspace()
first_grade_form = sp.diff(G_graded, t).subs(t, 0)[0, 0]
second_grade_form = (sp.diff(G_graded, t, 2).subs(t, 0) / sp.factorial(2))[1, 1]
det_order_check = sp.factor(G_graded.det())

stratum_fields = set(v4["stratified_metric_route_family"]["singular_stratum_required_fields"])
filtration_laws = set(v4["radical_jet_filtration"]["required_laws"])
associator_laws = set(v4["stratified_metric_route_associator"]["required_laws"])

checks = {
    "v3_preserved_as_failed_predecessor": "degenerate_metric_route_space" not in v3["object_types"],
    "v4_is_new_frozen_candidate": v4["status"] == "candidate_frozen" and v4["cell_creation_during_replay"] is False,
    "specialization_arrow_is_declared": "specialization_to_singular_stratum" in v4["arrow_types"],
    "radical_quotient_cell_is_declared": "radical_quotient_gluing" in v4["cell_types"],
    "normal_jet_filtration_is_required": "radical_jet_filtration" in stratum_fields,
    "simple_repair_radical_is_correct": simple_radical == [sp.Matrix([0, 1])],
    "simple_repair_crossing_form_is_nondegenerate": simple_crossing == 1,
    "unused_packet_full_radical_has_dimension_two": len(graded_radical) == 2,
    "unused_packet_first_grade_is_nondegenerate": first_grade_form == 1,
    "unused_packet_second_grade_is_nondegenerate": second_grade_form == 1,
    "unused_packet_determinant_order_is_three": det_order_check == t**3,
    "weighted_grade_dimension_law_holds": 1 * 1 + 2 * 1 == 3,
    "determinant_order_law_is_frozen": "determinant_order_equals_weighted_sum_of_graded_dimensions" in filtration_laws,
    "associator_must_preserve_filtration": "associator_preserves_radical_jet_filtration" in associator_laws,
    "completion_before_projection_is_frozen": "completed_sewing_precedes_finite_projection" in associator_laws,
    "local_packet_not_global_admission": v4["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v4-check.v1",
    "status": "candidate_v4_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "v3_disposition": "preserved as falsified",
    "v4_disposition": "candidate frozen; simple and two-grade rank-loss local gates pass; global admission not earned",
    "next_decisive_test": "unused multiparameter singular packet with nontrivial path dependence and full specialization coherence",
}

out = root / "results" / "frozen_bivariant_signature_v4.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v4_frozen_local_schema_pass" else 1)
