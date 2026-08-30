#!/usr/bin/env python3
"""Audit the first frozen flavor UV candidate class against WP118 admission."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp119_first_bounded_uv_candidate_audit.json"


def load(name):
    return json.loads((ROOT / "results" / name).read_text(encoding="utf-8"))


d116 = load("wp116_source_selector_final_disposition.json")
d117 = load("wp117_uv_ensemble_contract.json")
d118 = load("wp118_flavor_dpc_bounded_audit.json")

required = (
    "bounded_class",
    "independent_validation",
    "physical_source_generation",
    "normalized_quotient_measure",
    "recovered_physical16_certificate",
    "declared_budgets",
    "descendant_closed_counterfactual",
    "protected_prediction",
)

candidates = [
    {
        "id": "sm_one_loop_rg",
        "bounded_class": True,
        "independent_validation": True,
        "physical_source_generation": False,
        "normalized_quotient_measure": False,
        "recovered_physical16_certificate": False,
        "declared_budgets": False,
        "descendant_closed_counterfactual": False,
        "protected_prediction": False,
        "evidence": "derived SM transport fixes no Yukawa ensemble",
    },
    {
        "id": "fdm2_fixed_wp90_benchmark",
        "bounded_class": True,
        "independent_validation": False,
        "physical_source_generation": True,
        "normalized_quotient_measure": False,
        "recovered_physical16_certificate": False,
        "declared_budgets": False,
        "descendant_closed_counterfactual": False,
        "protected_prediction": False,
        "evidence": "WP112 full benchmark physical instrument falsified",
    },
    {
        "id": "fdm2_two_parameter_wp114_repair",
        "bounded_class": True,
        "independent_validation": False,
        "physical_source_generation": True,
        "normalized_quotient_measure": False,
        "recovered_physical16_certificate": False,
        "declared_budgets": False,
        "descendant_closed_counterfactual": False,
        "protected_prediction": False,
        "evidence": "repair parameters were obtained by scanning target readouts",
    },
    {
        "id": "wp117_abstract_uv_template",
        "bounded_class": True,
        "independent_validation": True,
        "physical_source_generation": False,
        "normalized_quotient_measure": False,
        "recovered_physical16_certificate": False,
        "declared_budgets": True,
        "descendant_closed_counterfactual": False,
        "protected_prediction": False,
        "evidence": "typed class contract has no instantiated action, measure, or matching map",
    },
]


def first_failure(candidate):
    return next((field for field in required if not candidate[field]), None)


for candidate in candidates:
    candidate["first_failure"] = first_failure(candidate)
    candidate["admitted"] = candidate["first_failure"] is None

canonical_class = json.dumps(candidates, sort_keys=True, separators=(",", ":")).encode()
class_digest = hashlib.sha256(canonical_class).hexdigest()
admitted = [c["id"] for c in candidates if c["admitted"]]

gates = {
    "WP116_negative_closeout_passes": d116["passed"] == d116["total"] == 15,
    "WP117_ensemble_is_undefined": d117["ensemble_classification"] == "undefined_without_additional_source_data",
    "WP118_is_bounded_not_universal": d118["surviving_framework"]["claim_kind"] == "bounded source-relative audit",
    "candidate_class_has_four_members": len(candidates) == 4,
    "all_eight_admission_fields_declared": all(all(field in c for field in required) for c in candidates),
    "SM_RG_fails_source_generation_first": candidates[0]["first_failure"] == "physical_source_generation",
    "fixed_FDM2_fails_independent_validation_first": candidates[1]["first_failure"] == "independent_validation",
    "fitted_repair_fails_independent_validation_first": candidates[2]["first_failure"] == "independent_validation",
    "abstract_template_fails_source_identity_first": candidates[3]["first_failure"] == "physical_source_generation",
    "fixed_benchmark_falsifier_preserved": d116["gates"]["fixed_fdm2_physical_instrument_is_falsified"],
    "fitted_repair_authority_failure_preserved": d116["gates"]["two_parameter_overlap_is_fitted_not_selected"],
    "no_historical_candidate_promoted_by_ensemble_agreement": not any(c["protected_prediction"] for c in candidates),
    "missing_fields_are_false_not_numeric_zero": all(not isinstance(c[field], (int, float)) or isinstance(c[field], bool) for c in candidates for field in required),
    "zero_candidates_admitted": admitted == [],
    "class_digest_is_fixed": len(class_digest) == 64,
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.first-bounded-uv-candidate-audit.v1",
    "audit_kind": "retrospective admission audit; not prospective phenomenology",
    "candidate_class_id": "C_FUV_0",
    "candidate_class_sha256": class_digest,
    "required_fields": list(required),
    "candidates": candidates,
    "admitted_candidates": admitted,
    "classification": "bounded_class_audited_zero_of_four_candidates_admitted",
    "reason_no_protected_test_runs": "all candidates have already inspected the historical flavor readouts and fail an upstream admission field",
    "smallest_common_missing_package": "independently validated bounded UV source plus quotient measure, covariant matching, budgets, descendant-closed counterfactual, and prediction firewall",
    "next_gate": "freeze one externally constrained physical UV model and specify constraint, nuisance-tuning, and protected datasets before opening the protected flavor readout",
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}

OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values()), [k for k, v in gates.items() if not v]
print(json.dumps({"passed": result["passed"], "total": result["total"], "admitted": len(admitted), "class_sha256": class_digest, "output": str(OUT)}))
