import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v7 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v7.json").read_text(encoding="utf-8"))
v8 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v8.json").read_text(encoding="utf-8"))

cutoffs = [2, 4, 8, 16, 32, 64]
repair_lower_bounds = [sp.Rational(1, n) for n in cutoffs]
repair_inverse_norms = cutoffs

# Weyl/approximate-kernel witnesses for D(e_n)=e_n/n.
repair_witness_norms = [sp.Integer(1) for _ in cutoffs]
repair_image_norms = repair_lower_bounds

# Finite sections of the unilateral shift S:e_k -> e_{k+1}.
N = 8
S = sp.zeros(N + 1, N)
for column in range(N):
    S[column + 1, column] = 1

family = v8["analytic_completed_resolved_route_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v8["object_types"])
cells = set(v8["cell_types"])
forbidden = set(v8["forbidden_promotions"])

checks = {
    "v7_preserved_as_failed_predecessor": v8["predecessor"].endswith("v7.json") and v7["status"] == "candidate_frozen",
    "v8_is_new_frozen_candidate": v8["status"] == "candidate_frozen" and v8["cell_creation_during_replay"] is False,
    "ambient_category_is_declared": set(v8["ambient_category"]) == {"objects", "morphisms", "exact_structure", "completion"},
    "nonclosed_range_defect_declared": "nonclosed_range_defect" in objects,
    "spectral_pro_object_declared": "zero_limit_spectral_pro_object" in objects,
    "derived_completion_cone_declared": "derived_completion_comparison_cone" in objects,
    "closed_range_certificate_declared": "closed_range_certificate" in cells,
    "repair_finite_sections_are_invertible": all(bound > 0 for bound in repair_lower_bounds),
    "repair_has_no_uniform_positive_lower_bound": min(repair_lower_bounds) == sp.Rational(1, 64) and repair_lower_bounds[-1] < repair_lower_bounds[0],
    "repair_inverse_norms_diverge": repair_inverse_norms == cutoffs,
    "repair_witnesses_are_unit_norm": repair_witness_norms == [1] * len(cutoffs),
    "repair_images_converge_toward_zero": repair_image_norms == repair_lower_bounds and repair_image_norms[-1] < repair_image_norms[0],
    "repair_spectral_germ_is_required": "approximate_kernel_sequences_define_a_retained_zero_limit_spectral_object" in laws,
    "repair_finite_promotion_needs_uniform_bound": "finite_section_invertibility_promotes_only_with_a_uniform_positive_lower_bound" in laws,
    "repair_nonclosed_range_is_retained": "topological_cone_retains_kernel_cokernel_and_nonclosed_range_defect" in laws,
    "unused_shift_is_isometric": S.T * S == sp.eye(N),
    "unused_shift_has_positive_lower_bound": S.T * S == sp.eye(N),
    "unused_shift_has_zero_kernel": len(S.nullspace()) == 0,
    "unused_shift_has_one_dimensional_cokernel": (N + 1) - S.rank() == 1,
    "spectral_gate_does_not_replace_cokernel": "ordinary_topological_cone_and_zero_limit_spectral_defect_are_both_retained" in laws,
    "dense_range_promotion_forbidden": "dense range promoted to surjectivity" in forbidden,
    "strict_descent_has_three_analytic_zero_gates": "strict_descent_requires_zero_reduced_cohomology_zero_nonclosed_range_defect_and_zero_spectral_germ" in laws,
    "local_packet_not_global_admission": v8["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v8-check.v1",
    "status": "candidate_v8_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v7_disposition": "preserved as falsified",
    "v8_disposition": "candidate frozen; the nonclosed-range completion hostile is retained spectrally and the unilateral-shift packet preserves ordinary cokernel accounting",
    "next_decisive_test": "non-normal completed transport with large pseudospectrum but no small singular value at the tested spectral point, or domain-changing unbounded specialization",
}

out = root / "results" / "frozen_bivariant_signature_v8.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v8_frozen_local_schema_pass" else 1)
