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

    path_by_order = {tuple(path["order"]): path for path in legal_paths}
    swap_cells = []
    adjacency = {tuple(path["order"]): set() for path in legal_paths}
    for order, left_path in path_by_order.items():
        for index in range(len(order) - 1):
            left, right = order[index], order[index + 1]
            if left in closure[right] or right in closure[left] or frozenset({left, right}) not in declared_commutes:
                continue
            swapped = order[:index] + (right, left) + order[index + 2:]
            right_path = path_by_order.get(swapped)
            if right_path is None:
                continue
            left_endpoint, right_endpoint = left_path["endpoint"], right_path["endpoint"]
            packet_equal = left_endpoint["boundary_packet"] == right_endpoint["boundary_packet"]
            domain_equal = left_endpoint["domain_signature"] == right_endpoint["domain_signature"]
            norm_equal = left_endpoint["graph_norm_signature"] == right_endpoint["graph_norm_signature"]
            support_equal = left_endpoint["support"] == right_endpoint["support"]
            defects_equal = left_endpoint["defects"] == right_endpoint["defects"]
            capability_equal = left_endpoint["capabilities"] == right_endpoint["capabilities"]
            generated = packet_equal and domain_equal and norm_equal and support_equal and defects_equal and capability_equal
            code = None if generated else ("repair_swap_domain_failure" if not domain_equal or not norm_equal else "repair_swap_packet_failure")
            swap_cells.append({"left_path": list(order), "right_path": list(swapped), "generated": generated, "code": code, "complete_boundary_packet_equal": packet_equal, "graph_domain_equivalent": domain_equal, "graph_norm_equivalent": norm_equal, "support_union_equal": support_equal, "remaining_defects_equal": defects_equal, "reconstruction_capability_equal": capability_equal, "scalar_endpoint_bytes_equal": left_endpoint["scalar_output"] == right_endpoint["scalar_output"]})
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
    expected = model.get("expected", {})
    observed = {"linear_extension_count": len(extensions), "legal_completed_path_count": len(legal_paths), "swap_component_count": len(components), "typed_endpoint_count": len(typed_endpoints)}
    for key, value in expected.items():
        if observed.get(key) != value:
            errors.append("model_expectation_mismatch:" + key)
    return {"id": model["id"], "passed": not errors, "errors": sorted(set(errors)), "dependency_acyclic": acyclic, "dependency_closure": {key: sorted(value) for key, value in closure.items()}, "observed": observed, "linear_extensions": [list(order) for order in extensions], "paths": paths, "swap_cells": swap_cells, "swap_components": components, "all_legal_paths_one_typed_endpoint": len(typed_endpoints) == 1, "scalar_bytes_do_not_define_typed_endpoint": any(cell["scalar_endpoint_bytes_equal"] and not cell["generated"] for cell in swap_cells)}


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
    models = [compile_model(model) for model in contract.get("models", [])]
    return {"schema": "marici.dependency-aware-partial-repair-result.v1", "passed": bool(models) and all(model["passed"] for model in models), "models": models}
