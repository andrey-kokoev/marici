#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S = ROOT / "research" / "strominger"
sys.path.insert(0, str(S))

from partial_repair_compiler import compile_contract  # noqa: E402


contract_path = S / "contracts" / "dependency-aware-partial-repairs.v1.json"
result_path = S / "results" / "dependency_aware_partial_repairs.json"
contract = json.loads(contract_path.read_text(encoding="ascii"))
result = compile_contract(contract)
models = {model["id"]: model for model in result["models"]}
semantic_gates = {
    "all_poset_linear_extension_graphs_connected": all(model["poset_extension_graph_connected"] for model in result["models"]),
    "discrete_poset_recovers_six_path_permutohedron": models["independent_three_repairs"]["observed"] == {"linear_extension_count":6,"legal_completed_path_count":6,"swap_component_count":1,"typed_endpoint_count":1,"first_braid_class":"zero"},
    "precedence_reduces_to_three_connected_paths": models["one_precedence_relation"]["observed"]["linear_extension_count"] == 3 and models["one_precedence_relation"]["observed"]["swap_component_count"] == 1,
    "equal_bytes_do_not_hide_graph_norm_failure": models["equal_bytes_inequivalent_graph_norms"]["scalar_bytes_do_not_define_typed_endpoint"] and any(cell["code"] == "repair_swap_domain_failure" and not cell["graph_norm_equivalent"] for cell in models["equal_bytes_inequivalent_graph_norms"]["swap_cells"]),
    "pairwise_diamonds_can_fail_braid": all(cell["generated"] for cell in models["pairwise_diamonds_failed_braid"]["swap_cells"]) and models["pairwise_diamonds_failed_braid"]["braid_audits"][0]["classification"] == "untyped_residual",
    "central_phase_retained_as_anomaly_candidate": models["central_phase_anomaly"]["braid_audits"][0]["classification"] == "central_phase" and not models["central_phase_anomaly"]["braid_audits"][0]["coherent"],
    "capability_deletion_blocks_one_order": models["residual_capability_deleted_before_consumption"]["observed"]["legal_completed_path_count"] == 1 and any(cell["code"] == "repair_residual_capability_failure" for cell in models["residual_capability_deleted_before_consumption"]["swap_cells"]),
    "theta_tate_remains_declaration_blocked": result["theta_tate_fixture"]["status"] == "source_declarations_required" and len(result["theta_tate_fixture"]["missing_source_declarations"]) == 7 and not result["theta_tate_fixture"]["enumeration_performed"],
    "theta_triangle_classifies_all_six_orders": result["theta_repair_triangle"]["observed"]["formal_order_count"] == 6 and len(result["theta_repair_triangle"]["paths"]) == 6,
    "theta_triangle_current_source_has_no_completed_path": result["theta_repair_triangle"]["observed"]["admissible_order_count"] == 0 and result["theta_repair_triangle"]["same_completed_typed_endpoint"] is None,
    "theta_triangle_first_illegal_nodes_are_typed": {path["first_rejection"]["code"] for path in result["theta_repair_triangle"]["paths"]} == {"distinction_erased_before_required_repair","theta_pro_gram_instantiation_blocked_missing_incidence","valuation_completion_not_source_authorized"},
    "theta_triangle_hostile_witness_is_irrecoverable": result["theta_repair_triangle"]["principal_hostile_rejection"]["code"] == "distinction_erased_before_required_repair" and result["theta_repair_triangle"]["principal_hostile_rejection"]["recovery_possible"] is False,
    "finite_clark_positivity_does_not_authorize_completion": result["theta_repair_triangle"]["clark_finite_bulk_identity"].startswith("2||G+f||") and not result["theta_repair_triangle"]["clark_completion_continuity_authorized"],
    "native_q_flow_endpoint_control_kept_separate": result["theta_repair_triangle"]["native_q_flow_endpoint_certificate"]["authorizes_clark_z_completion"] is False,
}
result["semantic_gates"] = semantic_gates

hostiles = {}
for name, mutate, expected in (
    ("missing_authority_root", lambda c: c["models"][0]["repairs"][0].update({"authority_root":None}), "repair_constructor_authority_untyped"),
    ("dependency_cycle", lambda c: (c["models"][1]["repairs"][0].update({"prerequisites":["B"]}), c["models"][1]["repairs"][1].update({"prerequisites":["A"]})), "repair_dependency_cycle"),
    ("wrong_independent_path_count", lambda c: c["models"][0]["expected"].update({"linear_extension_count":5}), "model_expectation_mismatch:linear_extension_count"),
    ("wrong_precedence_path_count", lambda c: c["models"][1]["expected"].update({"linear_extension_count":6}), "model_expectation_mismatch:linear_extension_count"),
    ("scalar_bytes_claim_typed_coherence", lambda c: c["models"][2]["expected"].update({"swap_component_count":1}), "model_expectation_mismatch:swap_component_count"),
    ("graph_norm_difference_hidden", lambda c: c["models"][2]["expected"].update({"typed_endpoint_count":1}), "model_expectation_mismatch:typed_endpoint_count"),
    ("failed_braid_forced_zero", lambda c: c["models"][3].update({"swap_cell_witnesses":{}}), "model_expectation_mismatch:first_braid_class"),
    ("pairwise_cell_source_deleted", lambda c: c["models"][3]["swap_cell_witnesses"]["A,B,C|0"].update({"source_authority_root":None}), "repair_swap_cell_value_untyped:A,B,C|0"),
    ("central_phase_root_deleted", lambda c: c["models"][4]["braid_checks"][0]["residual_policy"].update({"source_authority_root":None}), "model_expectation_mismatch:first_braid_class"),
    ("capability_deletion_hidden", lambda c: c["models"][5]["repairs"][1].update({"produces_capabilities":["residual_k"]}), "model_expectation_mismatch:legal_completed_path_count"),
    ("theta_dependencies_invented", lambda c: c["theta_tate_fixture"].update({"assume_discrete_poset":True}), "theta_tate_dependencies_invented"),
    ("theta_enumerated_while_incomplete", lambda c: c["theta_tate_fixture"].update({"compilation_mode":"enumerate"}), "theta_tate_enumeration_without_source_declarations"),
    ("theta_question_deleted", lambda c: c["theta_tate_fixture"].update({"open_source_questions":c["theta_tate_fixture"]["open_source_questions"][:-1]}), "theta_tate_open_questions_incomplete"),
    ("triangle_seam_contract_weakened", lambda c: c["theta_repair_triangle"]["operations"][2].update({"required_distinctions":["raw_arithmetic_label"]}), "theta_triangle_completion_distinction_contract_weakened"),
    ("triangle_uniform_family_self_asserted", lambda c: c["theta_repair_triangle"].update({"clark_uniform_constructor_family":{"family_id":"F","source_authority_root":None,"fixed_finite":True,"uniformly_dominates_current_matrices":True}}), "theta_triangle_uniform_family_unauthorized"),
    ("triangle_swap_authority_fitted", lambda c: c["theta_repair_triangle"]["commutation_declarations"][0].update({"authorized":True}), "theta_triangle_swap_authority_untyped"),
    ("triangle_closure_claimed", lambda c: c["theta_repair_triangle"]["expected"].update({"admissible_order_count":1}), "theta_triangle_expectation_mismatch:admissible_order_count"),
    ("triangle_clark_source_deleted", lambda c: c["theta_repair_triangle"]["operations"][1].update({"source_authority":None}), "theta_triangle_source_authority_missing:C"),
):
    candidate = deepcopy(contract)
    mutate(candidate)
    candidate_result = compile_contract(candidate)
    errors = {error for model in candidate_result["models"] for error in model["errors"]} | set(candidate_result["theta_tate_fixture"]["errors"]) | set(candidate_result["theta_repair_triangle"]["errors"])
    hostiles[name] = not candidate_result["passed"] and expected in errors

result["hostiles"] = hostiles
result["all_hostiles_rejected"] = all(hostiles.values())
result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")

for model in result["models"]:
    print(("PASS" if model["passed"] else "FAIL") + " model." + model["id"])
for name, passed in hostiles.items():
    print(("PASS" if passed else "FAIL") + " hostile." + name)
for name, passed in semantic_gates.items():
    print(("PASS" if passed else "FAIL") + " gate." + name)
print(f"SUMMARY {sum(model['passed'] for model in result['models'])}/{len(result['models'])}; HOSTILE {sum(hostiles.values())}/{len(hostiles)}")
raise SystemExit(0 if result["passed"] and result["all_hostiles_rejected"] and all(semantic_gates.values()) else 1)
