import json
from pathlib import Path


root = Path(__file__).parents[1]
marici = root.parents[1]
candidate = marici / "research" / "benincasa" / "checkers" / "check_rank26_conductor_specialization_cone_homology.py"
source = candidate.read_text(encoding="utf-8")

findings = {
    "source_two_term_complex_is_constructed": 'source_complex"' in source and "rank_dC" in source,
    "target_two_term_complex_is_constructed": 'target_complex"' in source and "rank_dD" in source,
    "chain_identity_is_checked": "chain_map_identity_holds" in source and "chain_residuals" in source,
    "target_boundary_rank_is_checked": "one_and_only_one_sheet_direction_becomes_exact" in source,
    "block_mapping_cone_differential_is_absent": "cone_differential" not in source and "mapping_cone" not in source,
    "mapping_cone_square_zero_check_is_absent": "cone_square" not in source and "d_squared" not in source,
    "mapping_cone_homology_dimensions_are_absent": "cone_homology" not in source,
    "explicit_primitive_field_is_absent": '"primitive"' not in source,
}

result = {
    "schema": "marici.aspect.specialization-cone-checker-scope.v1",
    "status": "target_complex_validity_tested_but_mapping_cone_unconstructed" if all(findings.values()) else "audit_inconclusive",
    "candidate": str(candidate.relative_to(marici)).replace("\\", "/"),
    "findings": findings,
    "admissible_claim_if_current_checker_passes": "the gamma-Bockstein line defines an injective target differential whose image is the rank-one sheet defect and the displayed chain square commutes",
    "inadmissible_claim": "specialization mapping-cone cohomology is computed or vanishes",
    "required_successor": [
        "export the full block mapping-cone differential in each relevant grade",
        "verify consecutive cone differentials compose to zero",
        "compute cone kernels, images, and homology dimensions",
        "export the target primitive and its transported chart representatives",
    ],
}

out = root / "results" / "specialization_cone_checker_scope.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "target_complex_validity_tested_but_mapping_cone_unconstructed" else 1)
