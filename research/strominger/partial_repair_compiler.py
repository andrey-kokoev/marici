"""Dependency-aware compiler for finite authority-bearing partial repairs."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from itertools import permutations
from typing import Any


REPAIR_FIELDS = {
    "repair_id", "input_defect_signature", "output_defect_signature",
    "domain_signature", "graph_norm_signature", "boundary_current_delta",
    "support_delta", "authority_root", "prerequisites",
    "residual_certificate_type", "domain_after", "graph_norm_after",
    "consumes_capabilities", "produces_capabilities",
}


def stable_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def validate_repair(repair: dict[str, Any], repair_ids: set[str]) -> list[str]:
    errors = []
    missing = sorted(REPAIR_FIELDS - set(repair))
    if missing:
        errors.append("repair_constructor_fields_missing:" + ",".join(missing))
        return errors
    if not repair["repair_id"] or not repair["authority_root"] or not repair["residual_certificate_type"]:
        errors.append("repair_constructor_authority_untyped")
    if not set(repair["prerequisites"]) <= repair_ids or repair["repair_id"] in repair["prerequisites"]:
        errors.append("repair_prerequisites_invalid")
    if not isinstance(repair["boundary_current_delta"], dict) or not isinstance(repair["support_delta"], list):
        errors.append("repair_packet_delta_untyped")
    if not isinstance(repair["domain_after"], dict) or not isinstance(repair["graph_norm_after"], dict):
        errors.append("repair_domain_transition_untyped")
    return errors


def dependency_closure(repairs: dict[str, dict[str, Any]]) -> tuple[dict[str, set[str]], bool]:
    closure = {repair_id: set(repair["prerequisites"]) for repair_id, repair in repairs.items()}
    changed = True
    while changed:
        changed = False
        for repair_id in closure:
            expanded = set().union(*(closure[item] for item in closure[repair_id])) if closure[repair_id] else set()
            if not expanded <= closure[repair_id]:
                closure[repair_id] |= expanded
                changed = True
    acyclic = all(repair_id not in prerequisites for repair_id, prerequisites in closure.items())
    return closure, acyclic


def linear_extensions(repairs: dict[str, dict[str, Any]], closure: dict[str, set[str]]) -> list[tuple[str, ...]]:
    ids = sorted(repairs)
    return [order for order in permutations(ids) if all(closure[repair_id] <= set(order[:index]) for index, repair_id in enumerate(order))]


def apply_repair(state: dict[str, Any], repair: dict[str, Any], applied: set[str]) -> tuple[dict[str, Any] | None, str | None]:
    repair_id = repair["repair_id"]
    if not set(repair["prerequisites"]) <= applied:
        return None, "repair_prerequisite_failure"
    defects = set(state["defects"])
    required_defects = set(repair["input_defect_signature"])
    if not required_defects <= defects:
        return None, "repair_input_defect_failure"
    accepted_domains = repair["domain_signature"] if isinstance(repair["domain_signature"], list) else [repair["domain_signature"]]
    if state["domain_signature"] not in accepted_domains:
        return None, "repair_domain_failure"
    accepted_norms = repair["graph_norm_signature"] if isinstance(repair["graph_norm_signature"], list) else [repair["graph_norm_signature"]]
    if state["graph_norm_signature"] not in accepted_norms:
        return None, "repair_graph_norm_input_failure"
    required_capabilities = set(repair["consumes_capabilities"])
    if not required_capabilities <= set(state["capabilities"]):
        return None, "repair_residual_capability_failure"
    result = deepcopy(state)
    result["defects"] = sorted((defects - required_defects) | set(repair["output_defect_signature"]))
    result["domain_signature"] = repair["domain_after"].get(state["domain_signature"])
    result["graph_norm_signature"] = repair["graph_norm_after"].get(state["graph_norm_signature"])
    if result["domain_signature"] is None:
        return None, "repair_domain_transition_failure"
    if result["graph_norm_signature"] is None:
        return None, "repair_graph_norm_transition_failure"
    boundary = dict(result["boundary_packet"])
    for key, value in repair["boundary_current_delta"].items():
        boundary[key] = boundary.get(key, 0) + value
    result["boundary_packet"] = {key: boundary[key] for key in sorted(boundary)}
    result["support"] = sorted(set(result["support"]) | set(repair["support_delta"]))
    result["capabilities"] = sorted((set(result["capabilities"]) - required_capabilities) | set(repair["produces_capabilities"]))
    result["applied"] = sorted(applied | {repair_id})
    return result, None


def execute_path(initial: dict[str, Any], order: tuple[str, ...], repairs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    state = deepcopy(initial)
    states = []
    applied: set[str] = set()
    for repair_id in order:
        next_state, error = apply_repair(state, repairs[repair_id], applied)
        if error:
            return {"order": list(order), "legal": False, "error": error, "failed_repair": repair_id, "states": states}
        state = next_state
        applied.add(repair_id)
        unresolved = sorted(state["defects"])
        states.append({"after": repair_id, "state": deepcopy(state), "unsafe_repair_in_progress": bool(unresolved), "unresolved_defects": unresolved, "next_admissible_repairs": sorted(candidate for candidate, repair in repairs.items() if candidate not in applied and set(repair["prerequisites"]) <= applied), "residual_capability": sorted(state["capabilities"])})
    endpoint_packet = {key: state[key] for key in ("defects", "domain_signature", "graph_norm_signature", "boundary_packet", "support", "capabilities", "scalar_output")}
    return {"order": list(order), "legal": True, "states": states, "endpoint": endpoint_packet, "endpoint_digest": stable_digest(endpoint_packet)}


def compile_model(model: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    repairs_list = model.get("repairs", [])
    repairs = {repair.get("repair_id"): repair for repair in repairs_list if repair.get("repair_id")}
    if len(repairs) != len(repairs_list):
        errors.append("repair_ids_duplicate_or_missing")
    repair_ids = set(repairs)
    for repair in repairs.values():
        errors.extend(validate_repair(repair, repair_ids))
    closure, acyclic = dependency_closure(repairs) if repairs else ({}, False)
    if not acyclic:
        errors.append("repair_dependency_cycle")
    declared_commutes = {frozenset(pair) for pair in model.get("commutes_with", []) if len(pair) == 2}
    extensions = linear_extensions(repairs, closure) if acyclic else []
    paths = [execute_path(model["initial_state"], order, repairs) for order in extensions]
    legal_paths = [path for path in paths if path["legal"]]

    extension_set = set(extensions)
    extension_adjacency = {order: set() for order in extensions}
    for order in extensions:
        for index in range(len(order) - 1):
            left, right = order[index], order[index + 1]
            if left in closure[right] or right in closure[left]:
                continue
            target = order[:index] + (right, left) + order[index + 2:]
            if target in extension_set:
                extension_adjacency[order].add(target)
    reached = set()
    if extensions:
        reached, frontier = {extensions[0]}, [extensions[0]]
        while frontier:
            current = frontier.pop()
            for target in extension_adjacency[current]:
                if target not in reached:
                    reached.add(target)
                    frontier.append(target)
    poset_extension_graph_connected = bool(extensions) and reached == extension_set

    all_path_by_order = {tuple(path["order"]): path for path in paths}
    path_by_order = {tuple(path["order"]): path for path in legal_paths}
    swap_cells = []
    adjacency = {tuple(path["order"]): set() for path in legal_paths}
    for order, left_path in path_by_order.items():
        for index in range(len(order) - 1):
            left, right = order[index], order[index + 1]
            if left in closure[right] or right in closure[left]:
                continue
            swapped = order[:index] + (right, left) + order[index + 2:]
            if frozenset({left, right}) not in declared_commutes:
                if swapped in all_path_by_order:
                    swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": False, "code": "repair_swap_authority_missing", "complete_boundary_packet_equal": False, "graph_domain_equivalent": False, "graph_norm_equivalent": False, "support_union_equal": False, "remaining_defects_equal": False, "reconstruction_capability_equal": False, "scalar_endpoint_bytes_equal": False, "missing_swap_cell": True, "left_domain": None, "right_domain": None, "boundary_residual": None})
                continue
            right_path = path_by_order.get(swapped)
            if right_path is None:
                rejected_path = all_path_by_order.get(swapped)
                if rejected_path is not None:
                    swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": False, "code": rejected_path.get("error", "repair_swap_domain_failure"), "complete_boundary_packet_equal": False, "graph_domain_equivalent": False, "graph_norm_equivalent": False, "support_union_equal": False, "remaining_defects_equal": False, "reconstruction_capability_equal": False, "scalar_endpoint_bytes_equal": False, "missing_swap_cell": True, "left_domain": left_path["states"][index + 1]["state"]["domain_signature"], "right_domain": None, "boundary_residual": None})
                continue
            left_local = left_path["states"][index + 1]["state"]
            right_local = right_path["states"][index + 1]["state"]
            packet_equal = left_local["boundary_packet"] == right_local["boundary_packet"]
            domain_equal = left_local["domain_signature"] == right_local["domain_signature"]
            norm_equal = left_local["graph_norm_signature"] == right_local["graph_norm_signature"]
            support_equal = left_local["support"] == right_local["support"]
            defects_equal = left_local["defects"] == right_local["defects"]
            capability_equal = left_local["capabilities"] == right_local["capabilities"]
            boundary_keys = set(left_local["boundary_packet"]) | set(right_local["boundary_packet"])
            boundary_residual = {key: left_local["boundary_packet"].get(key, 0) - right_local["boundary_packet"].get(key, 0) for key in sorted(boundary_keys)}
            boundary_residual = {key: value for key, value in boundary_residual.items() if value}
            generated = packet_equal and domain_equal and norm_equal and support_equal and defects_equal and capability_equal
            code = None if generated else ("repair_swap_domain_failure" if not domain_equal or not norm_equal else "repair_swap_packet_failure")
            swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": generated, "code": code, "complete_boundary_packet_equal": packet_equal, "graph_domain_equivalent": domain_equal, "graph_norm_equivalent": norm_equal, "support_union_equal": support_equal, "remaining_defects_equal": defects_equal, "reconstruction_capability_equal": capability_equal, "scalar_endpoint_bytes_equal": left_local["scalar_output"] == right_local["scalar_output"], "missing_swap_cell": not generated, "left_domain": left_local["domain_signature"], "right_domain": right_local["domain_signature"], "left_graph_norm": left_local["graph_norm_signature"], "right_graph_norm": right_local["graph_norm_signature"], "boundary_residual": boundary_residual})
            if generated:
                adjacency[order].add(swapped)
                adjacency[swapped].add(order)
    components = []
    remaining = set(adjacency)
    while remaining:
        seed = min(remaining)
        component, frontier = {seed}, [seed]
        while frontier:
            current = frontier.pop()
            for target in adjacency[current]:
                if target not in component:
                    component.add(target)
                    frontier.append(target)
        components.append([list(order) for order in sorted(component)])
        remaining -= component
    typed_endpoints = {path["endpoint_digest"] for path in legal_paths}
    swap_witnesses = model.get("swap_cell_witnesses", {})
    for key, witness in swap_witnesses.items():
        if not isinstance(witness.get("value"), int) or not witness.get("source_authority_root") or witness.get("derivation") != "source_comparison_current":
            errors.append("repair_swap_cell_value_untyped:" + key)

    def edge_value(order: tuple[str, ...], position: int) -> int:
        return swap_witnesses.get(",".join(order) + "|" + str(position), {}).get("value", 0)

    braid_audits = []
    for braid in model.get("braid_checks", []):
        start = tuple(braid.get("start_order", []))
        position = braid.get("position")
        comparable = start in path_by_order and isinstance(position, int) and 0 <= position < len(start) - 2
        left_word = [position, position + 1, position]
        right_word = [position + 1, position, position + 1]

        def follow(order: tuple[str, ...], word: list[int]) -> tuple[tuple[str, ...], int, bool]:
            total = 0
            for swap_position in word:
                target = order[:swap_position] + (order[swap_position + 1], order[swap_position]) + order[swap_position + 2:]
                cell = next((item for item in swap_cells if item["left_path"] == list(order) and item["right_path"] == list(target)), None)
                if cell is None or not cell["generated"]:
                    return order, total, False
                total += edge_value(order, swap_position)
                order = target
            return order, total, True

        left_endpoint, left_value, left_exists = follow(start, left_word) if comparable else (start, 0, False)
        right_endpoint, right_value, right_exists = follow(start, right_word) if comparable else (start, 0, False)
        residual = left_value - right_value
        policy = braid.get("residual_policy", {})
        if not left_exists or not right_exists or left_endpoint != right_endpoint:
            classification = "domain_mismatch"
        elif residual == 0:
            classification = "zero"
        elif policy.get("class") == "exact_boundary" and policy.get("source_authority_root") and policy.get("comparison_cell"):
            classification = "exact_boundary"
        elif policy.get("class") == "central_phase" and policy.get("source_authority_root"):
            classification = "central_phase"
        else:
            classification = "untyped_residual"
        coherent = classification in {"zero", "exact_boundary"}
        braid_audits.append({"id": braid.get("id"), "left_exists": left_exists, "right_exists": right_exists, "common_endpoint": left_endpoint == right_endpoint, "left_comparison_value": left_value, "right_comparison_value": right_value, "residual": residual, "classification": classification, "coherent": coherent, "fitted_cell_forbidden": classification == "untyped_residual"})
    expected = model.get("expected", {})
    observed = {"linear_extension_count": len(extensions), "legal_completed_path_count": len(legal_paths), "swap_component_count": len(components), "typed_endpoint_count": len(typed_endpoints), "first_braid_class": braid_audits[0]["classification"] if braid_audits else None}
    for key, value in expected.items():
        if observed.get(key) != value:
            errors.append("model_expectation_mismatch:" + key)
    return {"id": model["id"], "passed": not errors, "errors": sorted(set(errors)), "dependency_acyclic": acyclic, "dependency_closure": {key: sorted(value) for key, value in closure.items()}, "poset_extension_graph_connected": poset_extension_graph_connected, "observed": observed, "linear_extensions": [list(order) for order in extensions], "paths": paths, "swap_cells": swap_cells, "swap_components": components, "braid_audits": braid_audits, "all_legal_paths_one_typed_endpoint": len(typed_endpoints) == 1, "scalar_bytes_do_not_define_typed_endpoint": any(cell["scalar_endpoint_bytes_equal"] and not cell["generated"] for cell in swap_cells)}


def compile_theta_tate_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    expected_ids = {"S", "P", "Q", "A", "L", "C", "D"}
    declaration_fields = {"precedes", "commutes_with", "domain_after", "boundary_delta", "completion_scope"}
    stages = fixture.get("stages", [])
    stage_ids = {stage.get("repair_id") for stage in stages}
    errors = []
    if stage_ids != expected_ids or len(stages) != len(expected_ids):
        errors.append("theta_tate_stage_inventory_mismatch")
    missing = {}
    for stage in stages:
        absent = sorted(field for field in declaration_fields if field not in stage or stage.get(field) is None)
        if absent:
            missing[stage.get("repair_id")] = absent
    if fixture.get("assume_discrete_poset") is not False:
        errors.append("theta_tate_dependencies_invented")
    ready = not missing and not errors
    if fixture.get("compilation_mode") == "enumerate" and not ready:
        errors.append("theta_tate_enumeration_without_source_declarations")
    status = "ready" if ready else "source_declarations_required"
    if fixture.get("expected_status") != status:
        errors.append("theta_tate_declaration_status_mismatch")
    questions = fixture.get("open_source_questions", [])
    required_questions = {"P<->Q?", "S<->P?", "L<C?", "(P,Q,S,A)<D?"}
    if set(questions) != required_questions:
        errors.append("theta_tate_open_questions_incomplete")
    return {"passed": not errors, "errors": sorted(set(errors)), "status": status, "stage_ids": sorted(stage_ids - {None}), "missing_source_declarations": missing, "open_source_questions": questions, "enumeration_performed": ready and fixture.get("compilation_mode") == "enumerate", "legal_factorization_paths": [], "swap_components": [], "missing_swap_cells": [], "first_braid_residual": None, "unsafe_intermediate_states": [], "one_typed_endpoint": None}


def compile_theta_repair_triangle(triangle: dict[str, Any]) -> dict[str, Any]:
    required_fields = {"input_state_type", "output_state_type", "domain_before", "domain_after", "graph_norm_before", "graph_norm_after", "boundary_delta", "completion_scope", "residual_capability", "source_authority"}
    expected_ids = {"S", "C", "L"}
    stages = {stage.get("repair_id"): stage for stage in triangle.get("operations", [])}
    errors = []
    if set(stages) != expected_ids or len(triangle.get("operations", [])) != 3:
        errors.append("theta_triangle_operation_inventory_mismatch")
    for repair_id, stage in stages.items():
        if not required_fields <= set(stage):
            errors.append("theta_triangle_constructor_fields_missing:" + str(repair_id))
        if not stage.get("source_authority"):
            errors.append("theta_triangle_source_authority_missing:" + str(repair_id))
    if set(stages.get("L", {}).get("required_distinctions", [])) != {"seam_translation_norm", "raw_arithmetic_label"}:
        errors.append("theta_triangle_completion_distinction_contract_weakened")
    family = triangle.get("clark_uniform_constructor_family")
    family_authorized = bool(family and family.get("family_id") and family.get("source_authority_root") and family.get("fixed_finite") is True and family.get("uniformly_dominates_current_matrices") is True)
    if family is not None and not family_authorized:
        errors.append("theta_triangle_uniform_family_unauthorized")
    commutations = triangle.get("commutation_declarations", [])
    for declaration in commutations:
        if declaration.get("authorized") and (not declaration.get("source_authority_root") or not declaration.get("comparison_cell")):
            errors.append("theta_triangle_swap_authority_untyped")

    initial = {"state_components": {"finite_theta_source"}, "domain": {"finite_support"}, "graph_norm": {"tail_analytic_gram"}, "distinctions": {"tail_translation_norm", "raw_arithmetic_label"}, "capabilities": {"raw_label_port"}, "completion_scope": "uncompleted_finite_packet"}

    def apply(stage_id: str, state: dict[str, Any], path: tuple[str, ...]) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        result = deepcopy(state)
        if stage_id == "S":
            result["state_components"].add("independent_seam_state")
            result["domain"].add("tail_seam_domain")
            result["graph_norm"].add("seam_translation_norm")
            result["distinctions"].add("seam_translation_norm")
            result["capabilities"].add("seam_state_port")
        elif stage_id == "C":
            if "pro_gram_completion" in result["state_components"] and not family_authorized:
                return None, {"code":"clark_current_not_continuous_after_completion", "path":list(path), "failed_operation":"C", "missing_certificate":"fixed_finite_uniform_constructor_family_F", "recovery_possible":False}
            result["state_components"].add("clark_differentiated_bulk")
            result["domain"].add("clark_finite_current_domain")
            result["graph_norm"].add("clark_z_derivative_finite_bulk")
            result["capabilities"].add("clark_current_matrix")
        elif stage_id == "L":
            missing_distinctions = set(stages["L"].get("required_distinctions", [])) - result["distinctions"]
            if missing_distinctions:
                lost = sorted(missing_distinctions)[0]
                return None, {"code":"distinction_erased_before_required_repair", "path":list(path), "failed_operation":"L", "lost_capability":lost, "recovery_possible":False}
            if "independent_seam_state" not in result["state_components"]:
                return None, {"code":"distinction_erased_before_required_repair", "path":list(path), "failed_operation":"L", "lost_capability":"seam_translation_norm", "recovery_possible":False}
            if "clark_differentiated_bulk" in result["state_components"] and not family_authorized:
                return None, {"code":"theta_pro_gram_instantiation_blocked_missing_incidence", "path":list(path), "failed_operation":"L", "missing_source_maps":["valuation/Fock -> boundary", "Clark current -> common finite module"], "required_family":"fixed_finite_authorized_F", "recovery_possible":False}
            if stages["L"].get("completion_scope") == "completion_stability_unproved":
                return None, {"code":"valuation_completion_not_source_authorized", "path":list(path), "failed_operation":"L", "missing_constructor":stages["L"].get("missing_source_constructor"), "recovery_possible":False}
            result["state_components"] |= {"valuation_constructor_port", "pro_gram_completion"}
            result["domain"].add("constructor_generated_pro_gram_domain")
            result["graph_norm"].add("valuation_pro_gram_topology")
            result["distinctions"].add("prime_valuation_label")
            result["capabilities"].add("valuation_projector_family")
            result["completion_scope"] = "constructor_generated_pro_gram_completion"
        return result, None

    path_results = []
    for order in permutations(sorted(expected_ids)):
        state = deepcopy(initial)
        prefixes = []
        rejection = None
        for stage_id in order:
            state, rejection = apply(stage_id, state, order[:order.index(stage_id) + 1])
            if rejection:
                break
            prefixes.append({"after":stage_id, "state_components":sorted(state["state_components"]), "domain":sorted(state["domain"]), "graph_norm":sorted(state["graph_norm"]), "distinctions":sorted(state["distinctions"]), "completion_scope":state["completion_scope"], "unsafe_repair_in_progress":stage_id != order[-1]})
        endpoint = None
        if rejection is None:
            endpoint = {key: sorted(state[key]) if isinstance(state[key], set) else state[key] for key in ("state_components", "domain", "graph_norm", "distinctions", "capabilities", "completion_scope")}
        path_results.append({"order":list(order), "dynamically_admissible":rejection is None, "first_rejection":rejection, "prefixes":prefixes, "typed_endpoint":endpoint, "endpoint_digest":stable_digest(endpoint) if endpoint else None})
    admissible = [path for path in path_results if path["dynamically_admissible"]]
    endpoints = {path["endpoint_digest"] for path in admissible}
    authorized_swaps = [declaration for declaration in commutations if declaration.get("authorized")]
    hostile = triangle.get("principal_hostile_fixture", {})
    hostile_witness = {"code":"distinction_erased_before_required_repair", "path":["complete_tail_quotient","retain_seam"], "lost_capability":"seam_translation_norm", "recovery_possible":False, "tail_norm":hostile.get("tail_norm"), "seam_norm":hostile.get("seam_norm"), "adjacent_label_collapse":hostile.get("adjacent_label_collapse")}
    expected = triangle.get("expected", {})
    observed = {"formal_order_count":len(path_results), "admissible_order_count":len(admissible), "typed_endpoint_count":len(endpoints), "authorized_adjacent_swap_count":len(authorized_swaps), "first_braid_class":"illegal_factorization" if len(admissible) < 6 else "not_computed"}
    for key, value in expected.items():
        if observed.get(key) != value:
            errors.append("theta_triangle_expectation_mismatch:" + key)
    return {"passed":not errors, "errors":sorted(set(errors)), "source_status":"blocked_on_valuation_incidence_completion_and_clark_uniform_F" if not family_authorized else "blocked_on_valuation_incidence_completion", "clark_finite_bulk_identity":"2||G+f||^2+2a^2||partial_z G||^2", "clark_completion_continuity_authorized":family_authorized, "native_q_flow_endpoint_certificate":triangle.get("native_q_flow_endpoint_certificate"), "observed":observed, "paths":path_results, "authorized_adjacent_swaps":authorized_swaps, "same_completed_typed_endpoint":len(endpoints) == 1 if admissible else None, "braid_residual_class":observed["first_braid_class"], "principal_hostile_rejection":hostile_witness}


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
    models = [compile_model(model) for model in contract.get("models", [])]
    theta_tate = compile_theta_tate_fixture(contract.get("theta_tate_fixture", {}))
    theta_triangle = compile_theta_repair_triangle(contract.get("theta_repair_triangle", {}))
    return {"schema": "marici.dependency-aware-partial-repair-result.v1", "passed": bool(models) and all(model["passed"] for model in models) and theta_tate["passed"] and theta_triangle["passed"], "models": models, "theta_tate_fixture": theta_tate, "theta_repair_triangle": theta_triangle}
