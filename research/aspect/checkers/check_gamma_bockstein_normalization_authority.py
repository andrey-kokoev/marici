import json
from pathlib import Path


root = Path(__file__).parents[1]
marici = root.parents[1]
benincasa = marici / "research" / "benincasa"

cone = json.loads((benincasa / "rank26-conductor-specialization-cone.json").read_text(encoding="utf-8"))
generator = json.loads((benincasa / "rank26-conductor-cone-gradezero-horizontality.json").read_text(encoding="utf-8"))
transition = json.loads((benincasa / "g12-g31-residue-chart-transition.json").read_text(encoding="utf-8"))
common = json.loads((benincasa / "results" / "rank26-two-conductor-common-descent-line.json").read_text(encoding="utf-8"))
gamma = json.loads((benincasa / "results" / "rank26-conductor-gamma-bockstein.json").read_text(encoding="utf-8"))

transition_claims = json.dumps(transition).lower()
dual_gamma_naturality_declared = "dual gamma" in transition_claims or "dual_gamma" in transition_claims or "epsilon derivative" in transition_claims

checks = {
    "epsilon_is_source_declared_with_unit_slope": cone["physical_exponent"] == "-1/2 + epsilon" and cone["single_branch_character"]["epsilon_slope"] == "1",
    "source_normalization_pairs_with_simple_pole": cone["normalization_order"] == 1 and cone["conductor_pole_order"] == -1 and cone["normalized_grade"] == 0,
    "target_milnor_line_has_primitive_unit": generator["milnor_rank"] == 1 and generator["milnor_basis"] == ["1"] and generator["normalized_universal_grade_zero_scaling"] == "1",
    "ordinary_labelled_chart_transition_is_exact": transition["checks"]["passed"] and transition["checks"]["mapped_relation_failures"] == 0 and transition["checks"]["roundtrip_failures"] == 0,
    "residue_orientation_unit_is_fixed": transition["transition"]["orientation_sign"] == -1,
    "both_conductors_share_one_target_line": common["passed"] and common["ranks"]["absolute_plus_both"] == common["ranks"]["absolute_plus_g1"],
    "gamma_checker_identifies_transition_as_remaining_gate": gamma["passed"] and "labelled chart transition" in gamma["conclusion"],
    "dual_gamma_chart_naturality_is_not_yet_declared": not dual_gamma_naturality_declared,
}

result = {
    "schema": "marici.aspect.gamma-bockstein-normalization-authority.v1",
    "status": "classified_one_open_gate" if all(checks.values()) else "audit_failure",
    "checks": checks,
    "closed_authority": [
        "unit epsilon normal coordinate",
        "simple-pole pairing to grade zero",
        "primitive Milnor target generator",
        "ordinary signed residue-chart isomorphism",
        "one common target line for both conductors",
    ],
    "open_gate": "extend the labelled residue-chart transition to dual epsilon and prove that the gamma-Bockstein naturality square commutes with the fixed orientation sign",
    "absolute_uniqueness_disposition": "not yet established across conductor charts",
}

out = root / "results" / "gamma_bockstein_normalization_authority.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "classified_one_open_gate" else 1)
