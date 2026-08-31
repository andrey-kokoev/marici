import copy
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
CONTRACT = ROOT / "contracts" / "g4-linking-fourier-poisson-candidate.v1.json"
RESULT = ROOT / "results" / "g4-linking-fourier-poisson-conformance.json"
REQUIRED_LABELS = {"prime", "grade", "shell", "ordered_pair"}
REQUIRED_PRESENTATIONS = {
    "multiplication",
    "convolution",
    "reflected_multiplication",
    "reflected_convolution",
}
REQUIRED_STRATA = {"primitive", "square", "connected", "wall", "archimedean"}


def complex_value(value):
    if isinstance(value, list) and len(value) == 2:
        return complex(value[0], value[1])
    return complex(value)


def matrix(value):
    return [[complex_value(entry) for entry in row] for row in value]


def determinant(cell):
    return cell[0][0] * cell[1][1] - cell[0][1] * cell[1][0]


def validate(candidate):
    errors = []
    if "linking_cell" not in candidate or "fourier_poisson_comparison" not in candidate:
        return ["missing_linking_or_fourier_poisson_cell"]

    linking = candidate["linking_cell"]
    fp = candidate["fourier_poisson_comparison"]
    alpha = linking.get("alpha")
    lam = linking.get("lambda")
    try:
        gw = matrix(linking["G_W"])
        gs = matrix(linking["G_S"])
    except (KeyError, TypeError, ValueError):
        return ["invalid_or_missing_full_polarized_matrices"]

    if linking.get("alpha_source_derived") is not True:
        errors.append("alpha_fitted_not_source_derived")
    if linking.get("lambda_formula") != "-kappa_p/(2*s_p)" or linking.get("lambda_positive") is not True:
        errors.append("forced_lambda_not_preserved")
    if linking.get("full_output_linking_gram") is not True or linking.get("summed_pauli_frame") is True:
        errors.append("summed_pauli_frame_substituted_for_full_gram")

    expected = [
        [alpha * alpha * gw[0][0], alpha * lam * gw[0][1]],
        [alpha * lam * gw[1][0], lam * lam * gw[1][1]],
    ]
    if gs != expected:
        if gs[0][0] == expected[0][0] and gs[1][1] == expected[1][1] and gs[0][1] != expected[0][1]:
            errors.append("mixed_block_identity_failed")
        else:
            errors.append("full_polarized_pullback_identity_failed")
    if determinant(gs) == (alpha * lam) ** 2 * determinant(gw) and gs != expected:
        errors.append("determinant_equality_does_not_imply_matrix_equality")
    if linking.get("mixed_block_globally_closable") is not True:
        errors.append("primewise_mixed_block_not_globally_closable")
    if linking.get("all_four_blocks_projectively_continuous") is not True:
        errors.append("four_block_projective_continuity_missing")
    if linking.get("reciprocal_compatible") is not True:
        errors.append("linking_cell_not_reciprocal_compatible")

    if fp.get("source_carrier") != "retained_horizontal_response_graph":
        errors.append("retained_response_source_not_identified")
    if not fp.get("target_carrier") or not fp.get("comparison_map"):
        errors.append("g4_target_or_comparison_map_missing")
    if fp.get("intertwining_identity") != "C_FP W_FP = W_G4 C_FP":
        errors.append("fourier_poisson_intertwining_identity_missing")
    if fp.get("response_dual_action") != "contragredient":
        errors.append("response_dual_not_contragredient")
    if set(fp.get("response_presentations", [])) != REQUIRED_PRESENTATIONS:
        errors.append("four_presentation_response_packet_incomplete")
    if fp.get("descent") != "horizontal_equalizer":
        errors.append("orbit_sum_substituted_for_horizontal_descent")
    if fp.get("scalarization_stage") != "after_response_sewing":
        errors.append("response_scalarized_before_sewing")
    if not REQUIRED_LABELS.issubset(set(fp.get("retained_labels", []))):
        errors.append("prime_grade_shell_or_pair_labels_erased")
    if fp.get("vacuum_fixed") is not True or fp.get("valuation_length_preserved") is not True:
        errors.append("restricted_product_source_law_failed")
    if fp.get("wall_jump_coordinates_retained") is not True:
        errors.append("output_only_tate_data_substituted_for_boundary_graph")
    if fp.get("reciprocal_odd_sign_retained") is not True:
        errors.append("reciprocal_odd_sign_lost")
    if set(fp.get("response_strata", [])) != REQUIRED_STRATA:
        errors.append("response_strata_incomplete")
    if fp.get("maximal_isotropic_form_preserved") is not True:
        errors.append("maximal_isotropic_form_not_preserved")
    if fp.get("presentation_dependent_euler_phase") is not False:
        errors.append("presentation_dependent_euler_phase")
    if fp.get("prime_current_endomorphism_substitution") is not False:
        errors.append("prime_current_endomorphism_substituted_for_adelic_transition")
    if not fp.get("evans_state_placement_map"):
        errors.append("evans_state_placement_missing")
    if fp.get("evans_trace_before_arithmetic_codiagonalization") is not True:
        errors.append("evans_trace_evaluated_after_arithmetic_codiagonalization")
    return errors


def hostile_cases(baseline):
    cases = {}

    case = copy.deepcopy(baseline)
    case["linking_cell"]["G_W"][0][1] = [1, -2]
    case["linking_cell"]["G_W"][1][0] = [1, 2]
    cases["reversed_oriented_mixed_sign"] = case

    case = copy.deepcopy(baseline)
    case["linking_cell"]["G_S"][0][1] = [0, 0]
    case["linking_cell"]["G_S"][1][0] = [0, 0]
    cases["mixed_blocks_erased"] = case

    case = copy.deepcopy(baseline)
    case["linking_cell"]["G_S"] = [[10, [0, 0]], [[0, 0], 36]]
    cases["determinant_only_match"] = case

    case = copy.deepcopy(baseline)
    case["linking_cell"]["alpha_source_derived"] = False
    cases["fitted_alpha"] = case

    case = copy.deepcopy(baseline)
    case["linking_cell"]["mixed_block_globally_closable"] = False
    cases["primewise_not_globally_closable"] = case

    case = copy.deepcopy(baseline)
    case["linking_cell"]["full_output_linking_gram"] = False
    case["linking_cell"]["summed_pauli_frame"] = True
    cases["summed_pauli_frame"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["response_presentations"] = ["multiplication"]
    cases["multiplication_only_response"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["descent"] = "fourfold_orbit_direct_sum"
    cases["four_orbit_copies_as_independent_states"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["scalarization_stage"] = "before_response_sewing"
    cases["scalarization_before_sewing"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["wall_jump_coordinates_retained"] = False
    cases["output_only_tate_substitution"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["presentation_dependent_euler_phase"] = True
    cases["presentation_dependent_euler_phase"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["prime_current_endomorphism_substitution"] = True
    cases["prime_current_endomorphism_substitution"] = case

    case = copy.deepcopy(baseline)
    case["fourier_poisson_comparison"]["evans_state_placement_map"] = ""
    cases["missing_evans_placement"] = case
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
    "schema": "marici.nima.g4-linking-fourier-poisson-conformance.v1",
    "contract": str(CONTRACT.relative_to(ROOT.parents[1])).replace("\\", "/"),
    "passed": True,
    "claim_boundary": "Pass certifies only synthetic interface identities and hostile rejection; it does not identify G4, prove global closability for the physical carrier, Xi cancellation, or RH.",
    "baseline_errors": baseline_errors,
    "hostile_count": len(hostile_results),
    "hostile_results": hostile_results,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
