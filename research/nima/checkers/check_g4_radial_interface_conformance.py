import copy
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
CONTRACT = ROOT / "contracts" / "g4-radial-interface-candidate.v1.json"
RESULT = ROOT / "results" / "g4-radial-interface-conformance.json"

REQUIRED_FIELDS = {
    "radial_carrier",
    "radial_source_map",
    "radial_feature_map",
    "radial_codiagonal",
    "radial_recovery",
    "cycle_policy",
    "green_form",
    "green_radical",
    "return_map",
    "laws",
}
REQUIRED_LABELS = {"prime", "grade", "shell", "ordered_pair"}
REQUIRED_FEATURES = {
    "-rho_plus_0",
    "E_plus",
    "W_plus",
    "+rho_minus_0",
    "E_minus",
    "W_minus",
}


def validate(candidate):
    errors = []
    missing = sorted(REQUIRED_FIELDS - candidate.keys())
    if missing:
        errors.append(f"missing_fields:{','.join(missing)}")
        return errors

    carrier = candidate["radial_carrier"]
    source = candidate["radial_source_map"]
    feature = candidate["radial_feature_map"]
    codiagonal = candidate["radial_codiagonal"]
    recovery = candidate["radial_recovery"]
    cycle = candidate["cycle_policy"]
    form = candidate["green_form"]
    radical = candidate["green_radical"]
    return_map = candidate["return_map"]
    laws = candidate["laws"]

    if not REQUIRED_LABELS.issubset(set(carrier.get("labels", []))):
        errors.append("labels_not_retained")
    if carrier.get("polarized") is not True:
        errors.append("polarized_carrier_not_declared")
    if not REQUIRED_FEATURES.issubset(set(feature.get("coordinates", []))):
        errors.append("full_six_coordinate_feature_missing")
    if codiagonal.get("endpoint_coefficients") != [1, 1]:
        errors.append("endpoint_codiagonal_coefficients_wrong")
    if codiagonal.get("wronskian_coefficients") != [-0.5, -0.5]:
        errors.append("wronskian_codiagonal_coefficients_wrong")

    retains = set(carrier.get("retains", []))
    full_state = {"rho_plus", "rho_minus"}.issubset(retains)
    if recovery.get("mode") == "full_state_retained" and not full_state:
        errors.append("readout_only_carrier_claims_full_state_recovery")
    if recovery.get("identity_on_range") is not True:
        errors.append("range_recovery_identity_missing")
    if recovery.get("continuous") is not True:
        errors.append("range_recovery_continuity_missing")

    if cycle.get("mode") == "quotient_by_Z1":
        if source.get("kernel") != cycle.get("cycle_space"):
            errors.append("cycle_quotient_does_not_match_source_kernel")
        if cycle.get("chosen_independently_of_source_coefficients") is not True:
            errors.append("adaptive_cycle_observer_or_quotient")
        if cycle.get("reciprocal_equivariant") is not True:
            errors.append("cycle_policy_not_reciprocal_equivariant")
        if cycle.get("cutoff_natural") is not True:
            errors.append("cycle_policy_not_cutoff_natural")

    if radical.get("definition") != "form_radical_on_declared_feature_range":
        errors.append("green_radical_not_form_defined")
    if not form.get("metric") or form.get("metric") == "one_real_return_scalar":
        errors.append("full_green_metric_missing")
    if radical.get("equals_cycle_space") is True and not radical.get(
        "range_nondegeneracy_witness"
    ):
        errors.append("cycle_space_renamed_radical_without_nondegeneracy_witness")

    placement = set(return_map.get("placement", []))
    if return_map.get("prime_diagonality_stage") != "before_label_codiagonalization":
        errors.append("prime_diagonality_inferred_after_codiagonalization")
    if "before_label_codiagonalization" not in placement:
        errors.append("return_placement_erases_labels_before_test")

    covariance = set(laws.get("reciprocal_covariance", []))
    if not {"U", "radial_codiagonal", "cycle_policy", "return_map"}.issubset(covariance):
        errors.append("reciprocal_covariance_incomplete")
    if laws.get("kernel_sequence") != (
        "0 -> ker(U) -> ker(DU) -> ran(U) intersect N_bal -> 0"
    ):
        errors.append("kernel_sequence_missing_or_changed")
    if not REQUIRED_LABELS.issubset(
        set(laws.get("quotient_projection_compatibility", []))
    ):
        errors.append("quotient_projection_compatibility_incomplete")
    return errors


def hostile_cases(baseline):
    cases = {}

    cases["all_interfaces_checked_only"] = {"all_interfaces_checked": True}

    case = copy.deepcopy(baseline)
    case["radial_carrier"]["retains"] = ["endpoint_plus", "endpoint_minus"]
    cases["readout_only_claims_full_state"] = case

    case = copy.deepcopy(baseline)
    case["radial_carrier"]["polarized"] = False
    case["radial_feature_map"]["faithfulness_scope"] = "pairwise_collision_free"
    cases["pairwise_collision_promoted_to_polarized_faithfulness"] = case

    case = copy.deepcopy(baseline)
    case["green_radical"]["definition"] = "interval_cycle_space_Z1"
    cases["interval_cycles_renamed_green_radical"] = case

    case = copy.deepcopy(baseline)
    case["radial_feature_map"]["coordinates"] = ["source_fixed_theta_ray"]
    cases["source_ray_promoted_to_polarized_carrier"] = case

    case = copy.deepcopy(baseline)
    case["radial_source_map"]["kernel"] = "endpoint_wronskian_balance_space"
    cases["endpoint_balance_identified_with_interval_cycles"] = case

    case = copy.deepcopy(baseline)
    case["cycle_policy"]["chosen_independently_of_source_coefficients"] = False
    cases["adaptive_forest_observer"] = case

    case = copy.deepcopy(baseline)
    case["green_form"]["metric"] = "one_real_return_scalar"
    cases["one_scalar_promoted_to_metric"] = case

    case = copy.deepcopy(baseline)
    case["return_map"]["placement"] = ["after_label_codiagonalization"]
    case["return_map"]["prime_diagonality_stage"] = "after_label_codiagonalization"
    cases["prime_diagonality_after_codiagonalization"] = case

    return cases


baseline = json.loads(CONTRACT.read_text(encoding="utf-8"))
baseline_errors = validate(baseline)
assert not baseline_errors, baseline_errors

hostile_results = {}
for name, hostile in hostile_cases(baseline).items():
    errors = validate(hostile)
    assert errors, f"hostile fixture passed: {name}"
    hostile_results[name] = errors

result = {
    "schema": "marici.nima.g4-radial-interface-conformance.v1",
    "contract": str(CONTRACT.relative_to(ROOT.parents[1])).replace("\\", "/"),
    "passed": True,
    "claim_boundary": (
        "Pass certifies only that the synthetic candidate exposes the required interface "
        "shape and that declared hostile fixtures are rejected; it does not identify G4, "
        "prove a Green theorem, Xi cancellation, or RH."
    ),
    "baseline_errors": baseline_errors,
    "hostile_results": hostile_results,
    "hostile_count": len(hostile_results),
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
