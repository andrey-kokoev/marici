"""Bounded DPC constructor-DAG normalizer.

The normalizer preserves the full authority signature.  Equal executable
outputs are insufficient for a critical-pair join.
"""

from __future__ import annotations

import hashlib
import json
import math
from itertools import combinations, permutations
from copy import deepcopy
from typing import Any


SIGNATURE_FIELDS = ("authority_kind", "scope", "modality", "support", "resource")
LEGACY_IMPORT_FIELDS = {
    "nominal_identity": "nominal capability identity",
    "scope": "operation scope",
    "modality": "resource modality",
    "resource": "conserved resource measure",
    "physical_support_roots": "physical support-root inventory",
    "epoch": "temporal validity epoch",
}


def _epoch_less(left: Any, right: Any) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        return left < right
    if isinstance(left, dict) and isinstance(right, dict):
        if left.get("parameter") != right.get("parameter"):
            raise ValueError("incomparable_epoch_parameters")
        left_offset, right_offset = left.get("offset"), right.get("offset")
        if not isinstance(left_offset, int) or not isinstance(right_offset, int):
            raise ValueError("invalid_affine_epoch")
        return left_offset < right_offset
    raise ValueError("mixed_epoch_representations")


def canonical_signature(node: dict[str, Any]) -> dict[str, Any]:
    sig = {key: deepcopy(node[key]) for key in SIGNATURE_FIELDS}
    sig["scope"] = sorted(set(sig["scope"]))
    sig["support"] = sorted(set(sig["support"]))
    sig["resource"] = {key: sig["resource"][key] for key in sorted(sig["resource"])}
    return sig


def normalize(node: dict[str, Any]) -> dict[str, Any]:
    current = deepcopy(node)
    seen: set[str] = set()
    while True:
        before = json.dumps(current, sort_keys=True, separators=(",", ":"))
        if before in seen:
            raise ValueError("normalization_cycle")
        seen.add(before)
        current["scope"] = sorted(set(current["scope"]))
        current["support"] = sorted(set(current["support"]))
        current["resource"] = {key: current["resource"][key] for key in sorted(current["resource"])}
        operations = current.get("operations", [])
        fused_operations: list[dict[str, Any]] = []
        index = 0
        while index < len(operations):
            first = operations[index]
            if index + 1 < len(operations) and first["kind"] == "coherence" and operations[index + 1]["kind"] == "coherence":
                second = operations[index + 1]
                inverse_pair = first.get("cell") == second.get("inverse_of") and second.get("cell") == first.get("inverse_of")
                if inverse_pair:
                    if not first.get("invertible") or not second.get("invertible"):
                        raise ValueError("coherence_inverse_not_invertible")
                    if not first.get("preserves_full_signature") or not second.get("preserves_full_signature"):
                        raise ValueError("coherence_inverse_changes_authority_signature")
                    index += 2
                    continue
            if index + 1 < len(operations) and first["kind"] == "transport" and operations[index + 1]["kind"] == "transport":
                second = operations[index + 1]
                if first["target"] != second["source"]:
                    raise ValueError("transport_endpoint_mismatch")
                if not first.get("preserves_authority") or not second.get("preserves_authority"):
                    raise ValueError("transport_fusion_loses_authority")
                fusion_cell = second.get("fusion_cell") or first.get("fusion_cell")
                if not fusion_cell:
                    raise ValueError("transport_fusion_missing_cell")
                fused_operations.append({
                    "kind": "transport",
                    "source": first["source"],
                    "target": second["target"],
                    "preserves_authority": True,
                    "normal_form_cell": fusion_cell,
                })
                index += 2
                continue
            fused_operations.append(first)
            index += 1
        operations = fused_operations
        reduced: list[dict[str, Any]] = []
        for operation in operations:
            if operation["kind"] == "identity":
                if operation["signature"] != canonical_signature(current):
                    raise ValueError("identity_signature_mismatch")
                continue
            if operation["kind"] == "attenuate":
                current["scope"] = sorted(set(current["scope"]) & set(operation["scope"]))
                continue
            if operation["kind"] == "support_union":
                current["support"] = sorted(set(current["support"]) | set(operation["support"]))
                continue
            if operation["kind"] == "partition":
                source = operation["source"]
                amount = current["resource"].get(source)
                children = operation["children"]
                if amount is None:
                    raise ValueError("partition_source_missing")
                if sum(children.values()) > amount:
                    raise ValueError("resource_partition_inflation")
                del current["resource"][source]
                for child, child_amount in children.items():
                    if child in current["resource"]:
                        raise ValueError("partition_child_collision")
                    current["resource"][child] = child_amount
                continue
            if operation["kind"] == "epoch_fence":
                if _epoch_less(current.get("epoch", 0), operation["minimum_epoch"]):
                    current["status"] = "rejected_stale_epoch"
                    current["executable_output"] = "REJECT:stale_epoch"
                    current["operations"] = []
                    return current
                continue
            if operation["kind"] == "transport":
                if not operation.get("preserves_authority"):
                    raise ValueError("transport_loses_authority")
                reduced.append(operation)
                continue
            if operation["kind"] == "coherence":
                if not operation.get("invertible"):
                    raise ValueError("noninvertible_coherence_cannot_normalize")
                reduced.append(operation)
                continue
            reduced.append(operation)
        current["operations"] = reduced
        after = json.dumps(current, sort_keys=True, separators=(",", ":"))
        if before == after:
            return current
        if after in seen:
            raise ValueError("normalization_cycle")


def digest(node: dict[str, Any]) -> str:
    payload = json.dumps(normalize(node), sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def check_pair(pair: dict[str, Any]) -> dict[str, Any]:
    left, right = normalize(pair["left"]), normalize(pair["right"])
    same_output = left["executable_output"] == right["executable_output"]
    same_signature = canonical_signature(left) == canonical_signature(right)
    joined = same_output and same_signature and pair.get("coherence_cell") is not None
    return {
        "id": pair["id"],
        "same_output": same_output,
        "same_full_signature": same_signature,
        "joined": joined,
        "expected_joined": pair["expected_joined"],
        "passed": joined == pair["expected_joined"],
        "failure_code": None if joined else (
            "executable_output_mismatch" if not same_output else
            "full_signature_mismatch" if not same_signature else
            "missing_authority_coherence_cell"
        ),
    }


def audit_legacy_grants(legacy: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for grant in legacy.get("authority_grants", []):
        missing = [field for field in LEGACY_IMPORT_FIELDS if field not in grant]
        audits.append({
            "id": grant["id"],
            "importable": not missing,
            "missing_core_fields": missing,
            "missing_constructors": [LEGACY_IMPORT_FIELDS[field] for field in missing],
        })
    return audits


def audit_native_capabilities(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for capability in contract.get("native_capabilities", []):
        missing = [field for field in LEGACY_IMPORT_FIELDS if field not in capability]
        error = None
        normalized = None
        if not missing:
            if len(capability.get("bound_state_sha256", "")) != 64:
                error = "native_capability_missing_bound_state"
            node = {
                "authority_kind": capability["authority_kind"],
                "scope": capability["scope"],
                "modality": capability["modality"],
                "support": capability["physical_support_roots"],
                "resource": capability["resource"],
                "epoch": capability["epoch"],
                "status": "active",
                "executable_output": capability["executable_output"],
                "operations": capability.get("operations", []),
            }
            if error is None:
                try:
                    normalized = normalize(node)
                except ValueError as exc:
                    error = str(exc)
        audits.append({
            "id": capability.get("id", "<missing-id>"),
            "missing_core_fields": missing,
            "error": error,
            "compiled": not missing and error is None,
            "normalized": normalized,
        })
    return audits


def audit_epoch_successors(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for event in contract.get("epoch_successor_events", []):
        predecessor, successor = event.get("predecessor_epoch", {}), event.get("successor_epoch", {})
        same_family = predecessor.get("parameter") == successor.get("parameter")
        adjacent = same_family and isinstance(predecessor.get("offset"), int) and successor.get("offset") == predecessor["offset"] + 1
        digests_bound = all(len(event.get(field, "")) == 64 for field in ("predecessor_state_sha256", "successor_state_sha256"))
        roots = set(event.get("configuration_authority_roots", []))
        quorum = set(event.get("certificate_quorum", []))
        signers = event.get("authorized_signers", {})
        authority = bool(roots) and event.get("joint_configuration_certificate") and quorum == roots and set(signers) == roots
        unique = event.get("durable_non_equivocation") and not event.get("competing_successor_constructible")
        fault_sets = [set(item) for item in event.get("admissible_signer_fault_sets", [])]
        signer_roots = [item.get("independence_root") for item in signers.values()]
        fault_safe = all(bool(quorum - fault) for fault in fault_sets) and len(signer_roots) == len(set(signer_roots))
        attestation_raw = event.get("physical_state_correspondence", {})
        attestation = attestation_raw if isinstance(attestation_raw, dict) else {}
        tcb = attestation.get("trusted_physical_base", {}) if isinstance(attestation, dict) else {}
        signer_independence_roots = set(signer_roots)
        physical = (
            isinstance(attestation_raw, dict)
            and attestation.get("measured_state_sha256") == event.get("successor_state_sha256")
            and bool(attestation.get("executor_id"))
            and bool(attestation.get("verifier_authority_root"))
            and bool(attestation.get("measurement_constructor"))
            and attestation.get("signature_verified")
            and attestation.get("verified_before_epoch_acceptance")
        )
        fresh = (
            attestation.get("certificate_nonce") == event.get("certificate_nonce")
            and attestation.get("attested_epoch") == successor
            and isinstance(attestation.get("monotone_boot_counter"), int)
            and attestation.get("monotone_boot_counter") >= attestation.get("accepted_counter_floor", 0)
            and attestation.get("verifier_independence_root") not in signer_independence_roots
        )
        physical_base = (
            bool(tcb.get("hardware_root_id"))
            and set(tcb.get("required_ports", [])) <= set(tcb.get("measured_ports", []))
            and bool(tcb.get("anti_rollback_storage"))
            and bool(tcb.get("bounded_threat_model"))
            and not tcb.get("claims_absolute_unclonability")
            and not tcb.get("claims_universal_port_coverage")
            and bool(tcb.get("challenge_interface"))
        )
        errors = []
        if not adjacent:
            errors.append("nonadjacent_or_cross_family_epoch_successor")
        if not digests_bound:
            errors.append("epoch_successor_does_not_bind_states")
        if not authority:
            errors.append("epoch_successor_lacks_configuration_authority")
        if not fault_safe:
            errors.append("epoch_successor_signer_fault_model_unsafe")
        if not unique:
            errors.append("epoch_successor_fork_constructible")
        if not physical:
            errors.append("epoch_successor_lacks_physical_correspondence")
        if not fresh:
            errors.append("epoch_successor_attestation_stale_or_correlated")
        if not physical_base:
            errors.append("epoch_successor_attestation_tcb_unbounded")
        audits.append({"id": event["id"], "passed": not errors, "errors": errors})
    return audits


def audit_native_execution_traces(contract: dict[str, Any]) -> list[dict[str, Any]]:
    capabilities = {item["id"]: item for item in contract.get("native_capabilities", [])}
    audits = []
    for trace in contract.get("native_execution_traces", []):
        capability = capabilities.get(trace.get("capability_id"))
        errors = []
        if capability is None or trace.get("nominal_identity") != capability.get("nominal_identity"):
            errors.append("execution_trace_identity_mismatch")
        if capability is not None and trace.get("epoch") != capability.get("epoch"):
            errors.append("execution_trace_epoch_mismatch")
        issuance, consumption = trace.get("issuance", {}), trace.get("consumption", {})
        if not issuance.get("source_authorized") or issuance.get("resource_amount") != 1:
            errors.append("execution_trace_invalid_issuance")
        if not consumption.get("atomic_compare_and_set") or consumption.get("prior_state") != "unspent" or consumption.get("post_state") != "spent":
            errors.append("execution_trace_nonatomic_consumption")
        nonce = consumption.get("nonce")
        if not nonce or not consumption.get("nonce_durably_recorded"):
            errors.append("execution_trace_replayable_nonce")
        execution, receipt = trace.get("execution", {}), trace.get("receipt", {})
        if (
            not execution.get("executor_id")
            or capability is None
            or execution.get("attested_epoch") != capability.get("epoch")
            or execution.get("attested_state_sha256") != capability.get("bound_state_sha256")
            or not execution.get("effect_committed_atomically_with_fence")
        ):
            errors.append("execution_trace_unattested_effect")
        effect_digest = execution.get("effect_sha256", "")
        if len(effect_digest) != 64 or receipt.get("effect_sha256") != effect_digest or receipt.get("nonce") != nonce or not receipt.get("receiver_signature_verified"):
            errors.append("execution_trace_receipt_mismatch")
        history = trace.get("history", {})
        kinds = [item.get("kind") for item in history.get("entries", [])]
        if not history.get("append_only") or kinds != ["issued", "consumed", "effect_committed", "receipt_recorded"]:
            errors.append("execution_trace_history_not_append_only")
        if not history.get("execution_fact_retained") or history.get("compensation_erases_history"):
            errors.append("execution_trace_erases_irreversible_history")
        audits.append({"id": trace["id"], "passed": not errors, "errors": errors})
    return audits


def _delete_tcb_assumption(contract: dict[str, Any], assumption: str) -> None:
    event = contract["epoch_successor_events"][0]
    attestation = event.get("physical_state_correspondence")
    if not isinstance(attestation, dict) or not isinstance(attestation.get("trusted_physical_base"), dict):
        raise ValueError("cocircuit_baseline_attestation_missing")
    tcb = attestation["trusted_physical_base"]
    if assumption == "anti_rollback_storage":
        tcb["anti_rollback_storage"] = False
    elif assumption == "measured_ports_cover_required_ports":
        tcb["measured_ports"] = [item for item in tcb["measured_ports"] if item != "configuration_state"]
    elif assumption == "bounded_noncloned_hardware_root":
        tcb["bounded_threat_model"] = None
    elif assumption == "independent_configuration_signer_roots":
        event["authorized_signers"]["config_root_B"]["independence_root"] = "admin_A"
    elif assumption == "transition_nonce_binding":
        attestation["certificate_nonce"] = "nonce:replayed"
    else:
        raise ValueError("unknown_tcb_assumption")


def audit_trusted_base_cocircuits(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    expected_classes = {"rollback", "hidden_port", "clone", "signer_fork", "attestation_replay"}
    for item in contract.get("trusted_base_cocircuit_audits", []):
        candidate = deepcopy(contract)
        try:
            _delete_tcb_assumption(candidate, item["assumption"])
        except ValueError as exc:
            audits.append({"id": item["id"], "assumption": item["assumption"], "primitive_failure_class": item.get("primitive_failure_class"), "singleton_deletion_rejected": False, "observed_errors": [str(exc)], "passed": False})
            continue
        successor = audit_epoch_successors(candidate)[0]
        expected_error = item["singleton_deletion_error"]
        primitive = item.get("primitive_failure_class")
        passed = not successor["passed"] and expected_error in successor["errors"] and primitive in expected_classes
        audits.append({
            "id": item["id"],
            "assumption": item["assumption"],
            "primitive_failure_class": primitive,
            "singleton_deletion_rejected": not successor["passed"],
            "observed_errors": successor["errors"],
            "passed": passed,
        })
    return audits


def audit_resource_ssa_programs(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for program in contract.get("resource_ssa_programs", []):
        live: dict[str, dict[str, Any]] = {}
        defined: set[str] = set()
        consumed: set[str] = set()
        errors: list[str] = []
        prefix_balances: list[int] = []
        nodes_by_id = {item["id"]: item for item in program.get("nodes", [])}

        def define(name: str, amount: int, state: str = "available") -> None:
            if name in defined:
                errors.append("ssa_resource_redefined")
                return
            defined.add(name)
            live[name] = {"amount": amount, "state": state}

        def take(name: str, required_state: str | None = None) -> dict[str, Any] | None:
            item = live.get(name)
            if item is None:
                errors.append("linear_resource_reused_or_undefined")
                return None
            if required_state is not None and item["state"] != required_state:
                errors.append("resource_state_mismatch")
                return None
            del live[name]
            consumed.add(name)
            return item

        for node in program.get("nodes", []):
            kind = node.get("kind")
            if kind == "issue":
                if not node.get("source_authorized") or node.get("amount", 0) <= 0:
                    errors.append("unauthorized_or_nonpositive_issue")
                else:
                    define(node["output"], node["amount"])
            elif kind == "partition":
                parent = take(node["input"], "available")
                outputs = node.get("outputs", {})
                if parent is not None:
                    if sum(outputs.values()) > parent["amount"]:
                        errors.append("ssa_partition_inflation")
                    else:
                        for name, amount in outputs.items():
                            define(name, amount)
            elif kind == "reserve":
                item = take(node["input"], "available")
                if item is not None:
                    define(node["output"], item["amount"], "reserved")
            elif kind == "release":
                item = take(node["input"], "reserved")
                if not node.get("release_authority"):
                    errors.append("release_without_authority")
                elif item is not None:
                    define(node["output"], item["amount"], "available")
            elif kind == "consume":
                item = take(node["input"])
                if item is not None and item["state"] not in {"available", "reserved"}:
                    errors.append("invalid_consumption_state")
                if item is not None and node.get("effect_output"):
                    define(node["effect_output"], item["amount"], "effect")
            elif kind == "compensate":
                effect = take(node["input"], "effect")
                if not node.get("compensation_authority"):
                    errors.append("compensation_without_authority")
                elif effect is not None:
                    define(node["settlement_output"], effect["amount"], "settled")
                    if node.get("restores_original_capability"):
                        errors.append("compensation_remints_consumed_capability")
            else:
                errors.append("unknown_resource_ssa_node")
            prefix_balance = sum(item["amount"] for item in live.values() if item["state"] in {"available", "reserved"})
            prefix_balances.append(prefix_balance)
            if prefix_balance < 0:
                errors.append("negative_resource_prefix")
        expected_terminal = program.get("expected_terminal_states", {})
        actual_terminal = {name: item["state"] for name, item in sorted(live.items())}
        if actual_terminal != expected_terminal:
            errors.append("resource_ssa_terminal_state_mismatch")
        for pair in program.get("concurrency_pairs", []):
            left, right = nodes_by_id.get(pair.get("left")), nodes_by_id.get(pair.get("right"))
            if left is None or right is None:
                errors.append("unknown_concurrent_resource_node")
                continue
            left_region, right_region = left.get("resource_region"), right.get("resource_region")
            overlap = bool(left_region and right_region and (left_region == right_region or left_region == "global" or right_region == "global"))
            if overlap and not pair.get("linearization_witness"):
                errors.append("concurrent_resource_overlap_without_linearizer")
        audits.append({"id": program["id"], "passed": not errors, "errors": sorted(set(errors)), "prefix_balances": prefix_balances, "terminal_states": actual_terminal})
    return audits


def _forget_core_capability(capability: dict[str, Any], fields: list[str]) -> dict[str, Any]:
    evidence = {
        "target_operation": capability.get("scope", [None])[0],
        "authority_kind": capability.get("authority_kind"),
        "source_authority_evidence": capability.get("source_constructor_evidence"),
    }
    return {field: evidence.get(field) for field in fields}


def audit_forgetful_projections(contract: dict[str, Any]) -> list[dict[str, Any]]:
    capabilities = {item["id"]: item for item in contract.get("native_capabilities", [])}
    audits = []
    for item in contract.get("forgetful_projection_audits", []):
        source = capabilities.get(item.get("native_capability"))
        alternate = item.get("alternate_core_preimage", {})
        fields = item.get("legacy_fields", [])
        left = _forget_core_capability(source or {}, fields)
        right = _forget_core_capability(alternate, fields)
        source_core = {field: (source or {}).get(field) for field in LEGACY_IMPORT_FIELDS}
        alternate_core = {field: alternate.get(field) for field in LEGACY_IMPORT_FIELDS}
        errors = []
        if source is None or not item.get("projection_constructor"):
            errors.append("forgetful_projection_untyped")
        if left != right or source_core == alternate_core:
            errors.append("forgetful_projection_noninjectivity_unwitnessed")
        if item.get("claims_canonical_reverse_lift") or item.get("reverse_lift_constructor") is not None:
            errors.append("canonical_reverse_lift_laundered")
        if set(fields) != {"target_operation", "authority_kind", "source_authority_evidence"}:
            errors.append("forgetful_projection_wrong_legacy_signature")
        audits.append({"id": item["id"], "passed": not errors, "errors": errors, "legacy_projection": left, "distinct_core_preimages": source_core != alternate_core, "canonical_reverse_exists": False})
    return audits


def audit_epoch_successor_chains(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for chain in contract.get("epoch_successor_chain_audits", []):
        errors: list[str] = []
        current_epoch = chain.get("base_epoch")
        current_digest = chain.get("base_state_sha256")
        accumulated = set(chain.get("base_support", []))
        seen_step_ids: set[str] = set()
        seen_successors: set[tuple[Any, Any]] = set()
        steps = chain.get("steps", [])
        if not steps or not chain.get("theorem_scope"):
            errors.append("successor_chain_empty_or_unscoped")
        for step in steps:
            successor = step.get("successor", {})
            predecessor = step.get("predecessor", {})
            successor_key = (successor.get("parameter"), successor.get("offset"))
            adjacent = (
                predecessor == current_epoch
                and successor.get("parameter") == chain.get("parameter")
                and predecessor.get("parameter") == chain.get("parameter")
                and isinstance(predecessor.get("offset"), int)
                and successor.get("offset") == predecessor["offset"] + 1
            )
            if not adjacent:
                errors.append("successor_chain_nonadjacent_step")
            if step.get("predecessor_state_sha256") != current_digest:
                errors.append("successor_chain_digest_link_failure")
            if step.get("id") in seen_step_ids or successor_key in seen_successors or step.get("competing_successor_constructible"):
                errors.append("successor_chain_uniqueness_failure")
            if not step.get("physical_state_correspondence"):
                errors.append("successor_chain_physical_correspondence_failure")
            support_added = set(step.get("support_added", []))
            if not support_added:
                errors.append("successor_chain_support_not_accumulated")
            accumulated |= support_added
            seen_step_ids.add(step.get("id"))
            seen_successors.add(successor_key)
            current_epoch = successor
            current_digest = step.get("successor_state_sha256")
        if current_epoch != chain.get("expected_terminal_epoch"):
            errors.append("successor_chain_terminal_epoch_mismatch")
        if accumulated != set(chain.get("expected_accumulated_support", [])):
            errors.append("successor_chain_support_not_accumulated")
        audits.append({"id": chain["id"], "passed": not errors, "errors": sorted(set(errors)), "step_count": len(steps), "terminal_epoch": current_epoch, "accumulated_support": sorted(accumulated), "induction_rule":"valid prefix plus one adjacent unique physically realized step yields a valid extended prefix"})
    return audits


def audit_native_reconfiguration_constructors(contract: dict[str, Any]) -> list[dict[str, Any]]:
    successor_ids = {item["id"] for item in contract.get("epoch_successor_events", [])}
    audits = []
    for constructor in contract.get("native_reconfiguration_constructors", []):
        errors: list[str] = []
        inputs = {item.get("role"): item for item in constructor.get("input_signatures", [])}
        old, new, physical = inputs.get("old_configuration", {}), inputs.get("new_configuration", {}), inputs.get("successor_state", {})
        if not constructor.get("constructor_id") or not constructor.get("source_authority_root") or set(inputs) != {"old_configuration", "new_configuration", "successor_state"}:
            errors.append("native_reconfiguration_constructor_untyped")
        if old.get("epoch", {}).get("parameter") != new.get("epoch", {}).get("parameter") or new.get("epoch", {}).get("offset") != old.get("epoch", {}).get("offset", -1) + 1:
            errors.append("native_reconfiguration_epoch_mismatch")
        output = constructor.get("output_signature", {})
        if output.get("epoch") != new.get("epoch") or output.get("state_sha256") != new.get("state_sha256") or output.get("members") != new.get("members"):
            errors.append("native_reconfiguration_output_mismatch")
        if physical.get("successor_event") not in successor_ids:
            errors.append("native_reconfiguration_missing_successor_correspondence")
        old_q, new_q = set(old.get("quorum", [])), set(new.get("quorum", []))
        old_endorsement, new_endorsement = set(constructor.get("old_quorum_endorsement", [])), set(constructor.get("new_quorum_endorsement", []))
        bridge = old_q & new_q
        if old_endorsement != old_q or new_endorsement != new_q or not constructor.get("joint_consensus_required"):
            errors.append("native_reconfiguration_lacks_joint_endorsement")
        if set(constructor.get("bridge_witness", [])) != bridge:
            errors.append("native_reconfiguration_bridge_mismatch")
        fault_sets = [set(item) for item in constructor.get("admissible_bridge_fault_sets", [])]
        if any(not (bridge - fault) for fault in fault_sets):
            errors.append("native_reconfiguration_bridge_fault_unsafe")
        root_map = constructor.get("bridge_authority_roots", {})
        if set(root_map) != bridge:
            errors.append("native_reconfiguration_bridge_roots_incomplete")
        root_fibers = [{node for node, root in root_map.items() if root == authority_root} for authority_root in set(root_map.values())]
        if any(fiber not in fault_sets for fiber in root_fibers):
            errors.append("native_reconfiguration_common_cause_omitted")
        if constructor.get("old_only_may_activate_successor") or constructor.get("new_only_may_self_activate"):
            errors.append("native_reconfiguration_self_authorization")
        expected_support = set(old.get("support", [])) | set(new.get("support", [])) | set(physical.get("support", [])) | {constructor.get("source_authority_root")}
        if set(output.get("support", [])) != expected_support:
            errors.append("native_reconfiguration_support_loss")
        if constructor.get("resource_law") != "configuration authority is replaced, not duplicated":
            errors.append("native_reconfiguration_duplicates_authority")
        audits.append({"id": constructor["id"], "passed": not errors, "errors": sorted(set(errors)), "bridge": sorted(bridge), "bridge_authority_roots": root_map, "fault_sets": [sorted(item) for item in fault_sets], "output_support": sorted(output.get("support", []))})
    return audits


def audit_configuration_paths(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for path in contract.get("configuration_path_audits", []):
        errors: list[str] = []
        current = path.get("source_configuration", {})
        current_vertex = current.get("vertex_id")
        current_digest = current.get("state_sha256")
        current_members = current.get("members")
        current_quorum = current.get("quorum")
        current_authority = current.get("authority_resource")
        accumulated = set(current.get("support", []))
        consumed: set[str] = set()
        bridges = []
        bridge_states: list[tuple[set[str], dict[str, str]]] = []
        edges = path.get("edges", [])
        if not edges or not path.get("theorem_scope"):
            errors.append("configuration_path_empty_or_unscoped")
        for edge in edges:
            source = edge.get("source_configuration", {})
            target = edge.get("target_configuration", {})
            correspondence = edge.get("state_correspondence", {})
            output = edge.get("output_configuration", {})
            if (source.get("vertex_id"), source.get("state_sha256"), source.get("members"), source.get("quorum"), source.get("authority_resource")) != (current_vertex, current_digest, current_members, current_quorum, current_authority):
                errors.append("configuration_path_incidence_failure")
            if set(source.get("support", [])) != accumulated:
                errors.append("configuration_path_source_support_failure")
            if not edge.get("source_authority_root") or source.get("vertex_id") == target.get("vertex_id"):
                errors.append("configuration_edge_untyped_or_identity")
            if correspondence.get("source_state_sha256") != source.get("state_sha256") or correspondence.get("target_state_sha256") != target.get("state_sha256") or not correspondence.get("source_derived"):
                errors.append("configuration_state_correspondence_failure")
            source_q, target_q = set(source.get("quorum", [])), set(target.get("quorum", []))
            bridge = source_q & target_q
            if not bridge or not source_q <= set(source.get("members", [])) or not target_q <= set(target.get("members", [])) or len(source.get("members", [])) != len(set(source.get("members", []))) or len(target.get("members", [])) != len(set(target.get("members", []))):
                errors.append("configuration_path_invalid_bridge")
            if set(edge.get("source_quorum_endorsement", [])) != source_q or set(edge.get("target_quorum_endorsement", [])) != target_q or not edge.get("joint_authorization_required"):
                errors.append("configuration_path_joint_authorization_failure")
            if set(edge.get("bridge_witness", [])) != bridge:
                errors.append("configuration_path_bridge_mismatch")
            roots = edge.get("bridge_authority_roots", {})
            faults = [set(fault) for fault in edge.get("admissible_bridge_fault_sets", [])]
            if set(roots) != bridge:
                errors.append("configuration_path_bridge_roots_incomplete")
            root_fibers = [{node for node, root in roots.items() if root == authority_root} for authority_root in set(roots.values())]
            if any(fiber not in faults for fiber in root_fibers):
                errors.append("configuration_path_common_cause_omitted")
            if any(not (bridge - fault) for fault in faults):
                errors.append("configuration_path_bridge_fault_unsafe")
            output_authority = output.get("authority_resource")
            if edge.get("input_authority_resource") != current_authority or current_authority in consumed or not output_authority or output_authority == current_authority or output_authority in consumed or edge.get("source_authority_also_output") is not False or edge.get("output_authority_count") != 1:
                errors.append("configuration_path_linear_replacement_failure")
            consumed.add(current_authority)
            expected_support = accumulated | set(target.get("support", [])) | set(correspondence.get("support", [])) | {edge.get("source_authority_root")}
            if set(output.get("support", [])) != expected_support:
                errors.append("configuration_path_support_union_failure")
            if (output.get("vertex_id"), output.get("state_sha256"), output.get("members"), output.get("quorum")) != (target.get("vertex_id"), target.get("state_sha256"), target.get("members"), target.get("quorum")):
                errors.append("configuration_path_output_mismatch")
            bridges.append({"edge": edge.get("id"), "bridge": sorted(bridge), "authority_roots": roots, "fault_sets": [sorted(fault) for fault in faults]})
            bridge_states.append((bridge, roots))
            accumulated = expected_support
            current_vertex, current_digest = output.get("vertex_id"), output.get("state_sha256")
            current_members, current_quorum = output.get("members"), output.get("quorum")
            current_authority = output_authority
        global_root_faults = [set(fault) for fault in path.get("admissible_authority_root_fault_sets", [])]
        all_roots = {root for _, roots in bridge_states for root in roots.values()}
        if any({root} not in global_root_faults for root in all_roots):
            errors.append("configuration_path_global_root_fault_omitted")
        for root_fault in global_root_faults:
            for bridge, roots in bridge_states:
                failed_nodes = {node for node in bridge if roots.get(node) in root_fault}
                if not (bridge - failed_nodes):
                    errors.append("configuration_path_global_fault_unsafe")
        endpoint = path.get("expected_endpoint_configuration", {})
        if (current_vertex, current_digest, current_members, current_quorum, current_authority) != (endpoint.get("vertex_id"), endpoint.get("state_sha256"), endpoint.get("members"), endpoint.get("quorum"), endpoint.get("authority_resource")):
            errors.append("configuration_path_endpoint_mismatch")
        if accumulated != set(endpoint.get("support", [])):
            errors.append("configuration_path_support_union_failure")
        audits.append({"id": path["id"], "passed": not errors, "errors": sorted(set(errors)), "edge_count": len(edges), "endpoint_vertex": current_vertex, "output_authority_resource": current_authority, "input_authority_resources": sorted(consumed), "support_union": sorted(accumulated), "bridge_audits": bridges, "global_authority_root_fault_sets": [sorted(fault) for fault in global_root_faults], "induction_rule": "a valid partial composite extends iff the next edge is incident at the current configuration vertex, carries a source-derived state correspondence, linearly replaces its input authority, unions support, and every admitted local or path-wide authority-root fault leaves every affected bridge with a survivor"})
    return audits


def _edge_summary(edge: dict[str, Any]) -> dict[str, Any]:
    source, output = edge.get("source_configuration", {}), edge.get("output_configuration", {})
    return {
        "source": source.get("vertex_id"), "target": output.get("vertex_id"),
        "input_authority": edge.get("input_authority_resource"), "output_authority": output.get("authority_resource"),
        "support": tuple(sorted(output.get("support", []))), "edges": (edge.get("id"),),
        "fault_obligations": ((edge.get("id"), tuple(sorted((node, root) for node, root in edge.get("bridge_authority_roots", {}).items()))),),
    }


def _compose_path_summaries(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any] | None:
    if left["target"] != right["source"] or left["output_authority"] != right["input_authority"]:
        return None
    return {
        "source": left["source"], "target": right["target"],
        "input_authority": left["input_authority"], "output_authority": right["output_authority"],
        "support": right["support"], "edges": left["edges"] + right["edges"],
        "fault_obligations": left["fault_obligations"] + right["fault_obligations"],
    }


def audit_configuration_category(contract: dict[str, Any]) -> list[dict[str, Any]]:
    paths = {path["id"]: path for path in contract.get("configuration_path_audits", [])}
    audits = []
    for item in contract.get("configuration_category_audits", []):
        errors: list[str] = []
        path = paths.get(item.get("path_id"), {})
        edges = path.get("edges", [])
        edge_ids = [edge.get("id") for edge in edges]
        if edge_ids != item.get("associativity_edge_ids") or len(edges) < 3:
            errors.append("configuration_category_associativity_witness_untyped")
        vertices: dict[str, dict[str, Any]] = {}
        for edge in edges:
            vertices[edge.get("source_configuration", {}).get("vertex_id")] = edge.get("source_configuration", {})
            vertices[edge.get("output_configuration", {}).get("vertex_id")] = edge.get("output_configuration", {})
        if set(item.get("identity_vertices", [])) != set(vertices) or not item.get("identity_preserves_full_signature") or item.get("identity_replaces_authority"):
            errors.append("configuration_category_identity_failure")
        summaries = [_edge_summary(edge) for edge in edges]
        identity_laws_hold = True
        for summary in summaries:
            source_signature, target_signature = vertices.get(summary["source"], {}), vertices.get(summary["target"], {})
            left_identity = {"source": summary["source"], "target": summary["source"], "input_authority": source_signature.get("authority_resource"), "output_authority": source_signature.get("authority_resource"), "support": tuple(sorted(source_signature.get("support", []))), "edges": (), "fault_obligations": ()}
            right_identity = {"source": summary["target"], "target": summary["target"], "input_authority": target_signature.get("authority_resource"), "output_authority": target_signature.get("authority_resource"), "support": tuple(sorted(target_signature.get("support", []))), "edges": (), "fault_obligations": ()}
            identity_laws_hold &= _compose_path_summaries(left_identity, summary) == summary and _compose_path_summaries(summary, right_identity) == summary
        if not identity_laws_hold:
            errors.append("configuration_category_identity_failure")
        associativity_holds = False
        if len(summaries) >= 3:
            left_pair = _compose_path_summaries(summaries[0], summaries[1])
            right_pair = _compose_path_summaries(summaries[1], summaries[2])
            left_composite = _compose_path_summaries(left_pair, summaries[2]) if left_pair else None
            right_composite = _compose_path_summaries(summaries[0], right_pair) if right_pair else None
            associativity_holds = left_composite is not None and left_composite == right_composite
        if not associativity_holds:
            errors.append("configuration_category_associativity_failure")
        audits.append({"id": item["id"], "passed": not errors, "errors": sorted(set(errors)), "identity_vertices": sorted(vertices), "identity_laws_hold": identity_laws_hold, "associativity_holds": associativity_holds, "composite_edge_sequence": edge_ids})
    return audits


def generate_configuration_coherence(contract: dict[str, Any], path_audits: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    paths = {path["id"]: path for path in contract.get("configuration_path_audits", [])}
    admitted = {audit["id"]: audit["passed"] for audit in path_audits}
    rewrites = contract.get("configuration_constructor_rewrites", [])
    rewrite_audits = []
    adjacency: dict[str, list[tuple[str, str]]] = {path_id: [] for path_id in paths}
    seen_pairs: set[tuple[str, str]] = set()
    boundary_fields = ("vertex_id", "state_sha256", "members", "quorum", "authority_resource")

    def semantic_signature(path: dict[str, Any]) -> dict[str, Any]:
        return {
            "source": {key: path.get("source_configuration", {}).get(key) for key in boundary_fields},
            "endpoint": {key: path.get("expected_endpoint_configuration", {}).get(key) for key in boundary_fields},
            "support": sorted(path.get("expected_endpoint_configuration", {}).get("support", [])),
            "fault_hypergraph": sorted(sorted(fault) for fault in path.get("admissible_authority_root_fault_sets", [])),
        }

    for rewrite in rewrites:
        errors: list[str] = []
        source_id, target_id = rewrite.get("source_path_id"), rewrite.get("target_path_id")
        pair = (source_id, target_id)
        if source_id == target_id or source_id not in paths or target_id not in paths or not admitted.get(source_id) or not admitted.get(target_id):
            errors.append("configuration_rewrite_endpoint_invalid")
        if not rewrite.get("source_authority_root") or rewrite.get("admissible_transformation") != "factorization_substitution":
            errors.append("configuration_rewrite_unauthorized")
        if "normal_form_id" in rewrite:
            errors.append("configuration_rewrite_target_fitted")
        if pair in seen_pairs:
            errors.append("configuration_rewrite_duplicate")
        if source_id in paths and target_id in paths and semantic_signature(paths[source_id]) != semantic_signature(paths[target_id]):
            errors.append("configuration_rewrite_changes_semantics")
        if not errors:
            adjacency[source_id].append((target_id, rewrite.get("id")))
            seen_pairs.add(pair)
        rewrite_audits.append({"id": rewrite.get("id"), "source_path_id": source_id, "target_path_id": target_id, "passed": not errors, "errors": errors})

    indegree = {node: 0 for node in paths}
    for outgoing in adjacency.values():
        for target, _ in outgoing:
            indegree[target] += 1
    frontier = sorted(node for node, degree in indegree.items() if degree == 0)
    visited = []
    while frontier:
        node = frontier.pop(0)
        visited.append(node)
        for target, _ in adjacency[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                frontier.append(target)
                frontier.sort()
    terminating = len(visited) == len(paths)

    def traces_from(node: str, active: frozenset[str] = frozenset()) -> list[tuple[str, tuple[str, ...]]]:
        if node in active:
            return []
        if not adjacency.get(node):
            return [(node, ())]
        traces = []
        for target, rule_id in adjacency[node]:
            traces.extend((sink, (rule_id,) + trace) for sink, trace in traces_from(target, active | {node}))
        return traces

    traces = {path_id: traces_from(path_id) if terminating else [] for path_id in paths}
    unique_sinks = {path_id: sorted({sink for sink, _ in path_traces}) for path_id, path_traces in traces.items()}
    confluent = terminating and all(len(sinks) == 1 for sinks in unique_sinks.values())
    required_pairs = set(contract.get("required_configuration_critical_pairs", []))
    critical_pair_audits = []
    for source_id in sorted(required_pairs | {node for node, outgoing in adjacency.items() if len(outgoing) > 1}):
        outgoing = adjacency.get(source_id, [])
        branch_sinks = [sorted({sink for sink, _ in traces.get(target, [])}) for target, _ in outgoing]
        joins = len(outgoing) > 1 and bool(branch_sinks) and len({tuple(sinks) for sinks in branch_sinks}) == 1 and len(branch_sinks[0]) == 1
        critical_pair_audits.append({"source_path_id": source_id, "passed": joins, "errors": [] if joins else ["configuration_rewrite_critical_pair_unjoined"], "branches": [target for target, _ in outgoing], "join": branch_sinks[0][0] if joins else None})
    system_errors = []
    if not terminating:
        system_errors.append("configuration_rewrite_nonterminating")
    if not confluent:
        system_errors.append("configuration_rewrite_nonconfluent")
    if any(not audit["passed"] for audit in critical_pair_audits):
        system_errors.append("configuration_rewrite_required_critical_pair_missing")
    system_audit = {"id": "configuration_constructor_rewrite_system", "passed": not system_errors, "errors": system_errors, "terminating": terminating, "confluent": confluent, "topological_order": visited, "normal_forms": unique_sinks}
    normalization_audits = [system_audit] + critical_pair_audits

    witnesses: dict[str, dict[str, Any]] = {}
    if not system_errors and all(audit["passed"] for audit in rewrite_audits):
        for path_id, path_traces in traces.items():
            sink = unique_sinks[path_id][0]
            canonical_trace = min(trace for trace_sink, trace in path_traces if trace_sink == sink)
            normal_form_payload = semantic_signature(paths[sink])
            normal_form_id = hashlib.sha256(json.dumps(normal_form_payload, sort_keys=True, separators=(",", ":")).encode("ascii")).hexdigest()
            witness_payload = {"path": path_id, "sink": sink, "trace": canonical_trace, "normal_form": normal_form_id}
            witness_id = hashlib.sha256(json.dumps(witness_payload, sort_keys=True, separators=(",", ":")).encode("ascii")).hexdigest()
            witnesses[path_id] = {"id": witness_id, "trace": list(canonical_trace), "sink_path_id": sink, "normal_form_id": normal_form_id}

    cells: dict[tuple[str, str], dict[str, Any]] = {}
    path_ids = sorted(witnesses)
    for index, left_id in enumerate(path_ids):
        for right_id in path_ids[index + 1:]:
            left_witness, right_witness = witnesses[left_id], witnesses[right_id]
            if left_witness["normal_form_id"] != right_witness["normal_form_id"]:
                continue
            roots = {root for edge in paths[left_id].get("edges", []) for root in edge.get("bridge_authority_roots", {}).values()}
            cell_payload = {"left": left_witness["id"], "right": right_witness["id"]}
            cell_id = hashlib.sha256(json.dumps(cell_payload, sort_keys=True, separators=(",", ":")).encode("ascii")).hexdigest()
            cell = {"id": cell_id, "left_path_id": left_id, "right_path_id": right_id, "left_witness": left_witness["id"], "right_witness": right_witness["id"], "left_trace": left_witness["trace"], "right_trace": right_witness["trace"], "normal_form_id": left_witness["normal_form_id"], "root_identification": {root: root for root in sorted(roots)}}
            cells[(left_id, right_id)] = cell
            cells[(right_id, left_id)] = {**cell, "left_path_id": right_id, "right_path_id": left_id, "left_witness": right_witness["id"], "right_witness": left_witness["id"], "left_trace": right_witness["trace"], "right_trace": left_witness["trace"]}
    return rewrite_audits, normalization_audits, cells


def audit_configuration_path_coherence(contract: dict[str, Any], path_audits: list[dict[str, Any]], generated_cells: dict[tuple[str, str], dict[str, Any]]) -> list[dict[str, Any]]:
    paths = {path["id"]: path for path in contract.get("configuration_path_audits", [])}
    admitted = {audit["id"]: audit["passed"] for audit in path_audits}
    audits = []
    for item in contract.get("configuration_path_coherence_audits", []):
        errors: list[str] = []
        if "coherence_cell" in item:
            errors.append("primitive_configuration_coherence_forbidden")
        left, right = paths.get(item.get("left_path_id"), {}), paths.get(item.get("right_path_id"), {})
        cell = generated_cells.get((item.get("left_path_id"), item.get("right_path_id")), {})
        if not admitted.get(item.get("left_path_id")) or not admitted.get(item.get("right_path_id")):
            errors.append("configuration_coherence_path_not_admissible")
        boundary_fields = ("vertex_id", "state_sha256", "members", "quorum", "authority_resource")
        left_boundary = ({key: left.get("source_configuration", {}).get(key) for key in boundary_fields}, {key: left.get("expected_endpoint_configuration", {}).get(key) for key in boundary_fields})
        right_boundary = ({key: right.get("source_configuration", {}).get(key) for key in boundary_fields}, {key: right.get("expected_endpoint_configuration", {}).get(key) for key in boundary_fields})
        boundary_equal = left_boundary == right_boundary
        support_equal = set(left.get("expected_endpoint_configuration", {}).get("support", [])) == set(right.get("expected_endpoint_configuration", {}).get("support", []))
        if not boundary_equal:
            errors.append("configuration_coherence_boundary_mismatch")
        if not support_equal:
            errors.append("configuration_coherence_support_mismatch")
        root_map = cell.get("root_identification", {})
        left_roots = {root for edge in left.get("edges", []) for root in edge.get("bridge_authority_roots", {}).values()}
        right_roots = {root for edge in right.get("edges", []) for root in edge.get("bridge_authority_roots", {}).values()}
        translated_faults = {tuple(sorted(root_map.get(root, "") for root in fault)) for fault in left.get("admissible_authority_root_fault_sets", [])}
        right_faults = {tuple(sorted(fault)) for fault in right.get("admissible_authority_root_fault_sets", [])}
        fault_descent = set(root_map) == left_roots and set(root_map.values()) == right_roots and translated_faults == right_faults
        if not fault_descent:
            errors.append("configuration_coherence_fault_descent_failure")
        if not cell:
            errors.append("configuration_coherence_not_generated")
        audits.append({"id": item["id"], "passed": not errors, "errors": sorted(set(errors)), "paths": [item.get("left_path_id"), item.get("right_path_id")], "raw_presentations_equal": [edge.get("id") for edge in left.get("edges", [])] == [edge.get("id") for edge in right.get("edges", [])], "boundary_equal": boundary_equal, "support_equal": support_equal, "fault_hypergraph_descends": fault_descent, "coherence_cell": cell.get("id"), "generated_from": [cell.get("left_witness"), cell.get("right_witness")], "normal_form_id": cell.get("normal_form_id")})
    return audits


def audit_configuration_coherence_triangles(contract: dict[str, Any], generated_cells: dict[tuple[str, str], dict[str, Any]]) -> list[dict[str, Any]]:
    audits = []
    for item in contract.get("configuration_coherence_triangle_audits", []):
        errors: list[str] = []
        if "normal_form_id" in item:
            errors.append("configuration_coherence_triangle_target_fitted")
        paths = item.get("paths", [])
        if len(paths) != 3 or len(set(paths)) != 3:
            errors.append("configuration_coherence_triangle_untyped")
            cells = ({}, {}, {})
        else:
            a, b, c = paths
            cells = (generated_cells.get((a, b), {}), generated_cells.get((b, c), {}), generated_cells.get((a, c), {}))
        ab, bc, ac = cells
        telescopes = bool(ab and bc and ac and ab.get("right_witness") == bc.get("left_witness") and ab.get("left_witness") == ac.get("left_witness") and bc.get("right_witness") == ac.get("right_witness"))
        if not telescopes:
            errors.append("configuration_coherence_triangle_holonomy")
        audits.append({"id": item["id"], "passed": not errors, "errors": errors, "paths": paths, "telescopes": telescopes, "loop_action": "identity" if telescopes else "underdetermined", "composite_cell": [ab.get("id"), bc.get("id")], "direct_cell": ac.get("id")})
    return audits


def audit_configuration_coherence_coverage(contract: dict[str, Any]) -> list[dict[str, Any]]:
    provided = {frozenset((item.get("left_path_id"), item.get("right_path_id"))) for item in contract.get("configuration_path_coherence_audits", [])}
    audits = []
    for required in contract.get("required_configuration_path_comparisons", []):
        pair = frozenset((required.get("left_path_id"), required.get("right_path_id")))
        covered = len(pair) == 2 and pair in provided
        audits.append({"paths": sorted(pair), "passed": covered, "errors": [] if covered else ["configuration_coherence_required_pair_uncovered"]})
    return audits


def audit_contextual_configuration_rewrites(contract: dict[str, Any], path_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    paths = {path["id"]: path for path in contract.get("configuration_path_audits", [])}
    admitted = {audit["id"]: audit["passed"] for audit in path_audits}
    rewrites = {rewrite["id"]: rewrite for rewrite in contract.get("configuration_constructor_rewrites", [])}
    required_fields = {"source_boundary", "endpoint_boundary", "support_union", "fault_hypergraph", "input_authority", "output_authority", "resource_freshness"}
    required_schemas = {"same_position_branch", "disjoint_positions_commute"}
    boundary_fields = ("vertex_id", "state_sha256", "members", "quorum", "authority_resource")

    def semantic_signature(path: dict[str, Any]) -> dict[str, Any]:
        return {"source": {key: path.get("source_configuration", {}).get(key) for key in boundary_fields}, "endpoint": {key: path.get("expected_endpoint_configuration", {}).get(key) for key in boundary_fields}, "support": sorted(path.get("expected_endpoint_configuration", {}).get("support", [])), "fault_hypergraph": sorted(sorted(fault) for fault in path.get("admissible_authority_root_fault_sets", []))}

    audits = []
    for theorem in contract.get("configuration_contextual_rewrite_theorems", []):
        errors: list[str] = []
        alphabet = set(theorem.get("alphabet", []))
        selected_ids = theorem.get("rewrite_ids", [])
        selected = [rewrites.get(rewrite_id, {}) for rewrite_id in selected_ids]
        ranks = theorem.get("rank", {})
        if alphabet != set(paths) or not all(admitted.get(path_id) for path_id in alphabet) or set(ranks) != alphabet or any(not isinstance(rank, int) or rank < 0 for rank in ranks.values()):
            errors.append("contextual_rewrite_alphabet_or_rank_untyped")
        derived_hole_types = []
        for path_id in sorted(alphabet):
            path = paths.get(path_id, {})
            source, endpoint = path.get("source_configuration", {}), path.get("expected_endpoint_configuration", {})
            derived_hole_types.append({"source_vertex": source.get("vertex_id"), "source_state_sha256": source.get("state_sha256"), "endpoint_vertex": endpoint.get("vertex_id"), "endpoint_state_sha256": endpoint.get("state_sha256")})
        hole_type = theorem.get("hole_type", {})
        declared_structural_hole = {key: hole_type.get(key) for key in ("source_vertex", "source_state_sha256", "endpoint_vertex", "endpoint_state_sha256")}
        resource_parameters_typed = hole_type.get("input_authority_parameter") == "alpha_in[i]" and hole_type.get("output_authority_parameter") == "alpha_out[i]" and hole_type.get("resource_instances_pairwise_disjoint") is True and hole_type.get("shared_authority_claimed") is False
        hole_typing_holds = bool(derived_hole_types) and all(derived == declared_structural_hole for derived in derived_hole_types) and resource_parameters_typed
        if not hole_typing_holds:
            errors.append("contextual_rewrite_hole_type_mismatch")
        product_context_typed = theorem.get("context_grammar") == "finite_typed_product_context" and theorem.get("composition_kind") == "independent_hole_substitution" and theorem.get("sequential_composition_claimed") is False
        if not product_context_typed:
            errors.append("contextual_rewrite_sequential_composition_smuggled")
        indexed_fibers_typed = theorem.get("support_lift") == "tagged_pair(i,support)" and theorem.get("authority_root_lift") == "tagged_pair(i,root)" and theorem.get("fault_hypergraph_composition") == "disjoint_coproduct" and theorem.get("cross_hole_correlations_authorized") is False
        if not indexed_fibers_typed:
            errors.append("contextual_rewrite_indexed_fiber_collision")
        if set(selected_ids) != set(rewrites) or any(not rewrite for rewrite in selected):
            errors.append("contextual_rewrite_rule_coverage_failure")
        rank_decreases = bool(selected) and all(rewrite.get("source_path_id") in ranks and rewrite.get("target_path_id") in ranks and ranks[rewrite["source_path_id"]] > ranks[rewrite["target_path_id"]] for rewrite in selected)
        if not rank_decreases:
            errors.append("contextual_rewrite_rank_not_decreasing")
        rule_semantics_preserved = all(rewrite.get("source_path_id") in paths and rewrite.get("target_path_id") in paths and semantic_signature(paths[rewrite["source_path_id"]]) == semantic_signature(paths[rewrite["target_path_id"]]) for rewrite in selected)
        context_preserved = theorem.get("context_closure") is True and product_context_typed and hole_typing_holds and indexed_fibers_typed and set(theorem.get("preserved_semantic_fields", [])) == required_fields and rule_semantics_preserved
        if not context_preserved:
            errors.append("contextual_rewrite_context_signature_not_preserved")
        schemas = set(theorem.get("critical_pair_schemas", []))
        if schemas != required_schemas:
            errors.append("contextual_rewrite_critical_schema_incomplete")
        adjacency: dict[str, set[str]] = {path_id: set() for path_id in alphabet}
        for rewrite in selected:
            if rewrite.get("source_path_id") in adjacency:
                adjacency[rewrite["source_path_id"]].add(rewrite.get("target_path_id"))

        def reachable(node: str) -> set[str]:
            seen, frontier = {node}, [node]
            while frontier:
                current = frontier.pop()
                for target in adjacency.get(current, set()):
                    if target not in seen:
                        seen.add(target)
                        frontier.append(target)
            return seen

        same_position_joins = True
        same_position_pairs = []
        for source, targets in adjacency.items():
            for left, right in combinations(sorted(targets), 2):
                common = sorted(reachable(left) & reachable(right))
                same_position_pairs.append({"source": source, "branches": [left, right], "common_reducts": common})
                same_position_joins &= bool(common)
        disjoint_positions_commute = context_preserved and "disjoint_positions_commute" in schemas
        local_confluence = same_position_joins and disjoint_positions_commute and schemas == required_schemas
        if not local_confluence:
            errors.append("contextual_rewrite_local_confluence_failure")
        terminating = rank_decreases
        newman_global_confluence = terminating and local_confluence and context_preserved
        if not newman_global_confluence:
            errors.append("contextual_rewrite_newman_gate_failure")
        if theorem.get("theorem_scope") != "arbitrary finite products of independently typed factorization holes":
            errors.append("contextual_rewrite_scope_laundered")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "context_grammar": theorem.get("context_grammar"), "composition_kind": theorem.get("composition_kind"), "sequential_composition_claimed": theorem.get("sequential_composition_claimed"), "hole_type": hole_type, "hole_typing_holds": hole_typing_holds, "resource_parameters_typed": resource_parameters_typed, "indexed_fibers_typed": indexed_fibers_typed, "rank_decreases": rank_decreases, "rewrite_semantics_preserved": rule_semantics_preserved, "context_signature_preserved": context_preserved, "same_position_critical_pairs": same_position_pairs, "same_position_joins": same_position_joins, "disjoint_positions_commute": disjoint_positions_commute, "locally_confluent": local_confluence, "terminating": terminating, "newman_global_confluence": newman_global_confluence, "scope": theorem.get("theorem_scope")})
    return audits


def audit_configuration_context_symmetry(contract: dict[str, Any], contextual_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    context_contracts = {item["id"]: item for item in contract.get("configuration_contextual_rewrite_theorems", [])}
    context_results = {item["id"]: item for item in contextual_audits}
    rewrites = contract.get("configuration_constructor_rewrites", [])
    audits = []
    for theorem in contract.get("configuration_context_symmetry_theorems", []):
        errors: list[str] = []
        context_id = theorem.get("context_theorem_id")
        context = context_contracts.get(context_id, {})
        context_result = context_results.get(context_id, {})
        if not context_result.get("passed") or not context_result.get("indexed_fibers_typed"):
            errors.append("context_symmetry_base_context_invalid")
        finite_bijection_typed = theorem.get("symmetry") == "finite_bijections_of_hole_indices" and theorem.get("theorem_scope") == "all finite bijections of every finite typed hole set"
        if not finite_bijection_typed:
            errors.append("context_symmetry_nonbijective_or_bounded")
        fiber_actions_typed = theorem.get("resource_action") == "alpha_rename_by_index_bijection" and theorem.get("support_action") == "tagged_pair(pi(i),support)" and theorem.get("authority_root_action") == "tagged_pair(pi(i),root)"
        if not fiber_actions_typed:
            errors.append("context_symmetry_fiber_action_not_faithful")
        position_independent = theorem.get("rewrite_action") == "position_independent" and all("hole_index" not in rewrite for rewrite in rewrites)
        if not position_independent:
            errors.append("context_symmetry_rewrite_depends_on_position")
        fault_coproduct_equivariant = context.get("fault_hypergraph_composition") == "disjoint_coproduct" and context.get("cross_hole_correlations_authorized") is False and theorem.get("cross_hole_fault_action") == "none_without_explicit_constructor"
        if not fault_coproduct_equivariant:
            errors.append("context_symmetry_cross_hole_fault_laundered")
        normalization_equivariant = theorem.get("normal_form_action") == "pointwise_normalization_then_permutation" and context_result.get("newman_global_confluence") and finite_bijection_typed and fiber_actions_typed and position_independent and fault_coproduct_equivariant
        if not normalization_equivariant:
            errors.append("context_symmetry_normalization_not_equivariant")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "finite_bijection_typed": finite_bijection_typed, "fiber_actions_typed": fiber_actions_typed, "rewrite_position_independent": position_independent, "fault_coproduct_equivariant": fault_coproduct_equivariant, "normalization_equivariant": normalization_equivariant, "scope": theorem.get("theorem_scope")})
    return audits


def audit_correlated_configuration_contexts(contract: dict[str, Any], contextual_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    context_results = {item["id"]: item for item in contextual_audits}
    paths = contract.get("configuration_path_audits", [])
    allowed_roots = {root for path in paths for edge in path.get("edges", []) for root in edge.get("bridge_authority_roots", {}).values()}
    local_bridge_root_sets = {frozenset(edge.get("bridge_authority_roots", {}).values()) for path in paths for edge in path.get("edges", [])}
    rewrites = contract.get("configuration_constructor_rewrites", [])
    audits = []
    for theorem in contract.get("configuration_correlated_context_theorems", []):
        errors: list[str] = []
        base = context_results.get(theorem.get("base_context_theorem_id"), {})
        if not base.get("passed") or not base.get("indexed_fibers_typed"):
            errors.append("correlated_context_base_invalid")
        constructor_typed = bool(theorem.get("constructor_id") and theorem.get("source_authority_root")) and theorem.get("authorized_effect") == "fault_hypergraph_extension_only"
        if not constructor_typed:
            errors.append("correlated_context_constructor_unauthorized")
        separation_preserved = theorem.get("support_identification") is False and theorem.get("resource_identification") is False
        if not separation_preserved:
            errors.append("correlated_context_authority_or_support_laundered")
        indices = theorem.get("hole_indices", [])
        if not indices or len(indices) != len(set(indices)):
            errors.append("correlated_context_hole_indices_invalid")
        raw_edges = theorem.get("correlation_hyperedges", [])
        hyperedges: set[frozenset[tuple[str, str]]] = set()
        hyperedges_typed = bool(raw_edges)
        for raw_edge in raw_edges:
            edge = frozenset((item[0], item[1]) for item in raw_edge if isinstance(item, list) and len(item) == 2)
            if len(edge) != len(raw_edge) or len({hole for hole, _ in edge}) < 2 or any(hole not in indices or root not in allowed_roots for hole, root in edge):
                hyperedges_typed = False
            hyperedges.add(edge)
        if not hyperedges_typed or len(hyperedges) != len(raw_edges):
            errors.append("correlated_context_hyperedge_untyped")
        bridge_safe = True
        for edge in hyperedges:
            for hole in indices:
                failed_roots = {root for edge_hole, root in edge if edge_hole == hole}
                if any(bridge_roots <= failed_roots for bridge_roots in local_bridge_root_sets):
                    bridge_safe = False
        if not bridge_safe:
            errors.append("correlated_context_exhausts_local_bridge")
        automorphisms = []
        if hyperedges_typed:
            for image in permutations(indices):
                mapping = dict(zip(indices, image))
                transformed = {frozenset((mapping[hole], root) for hole, root in edge) for edge in hyperedges}
                if transformed == hyperedges:
                    automorphisms.append(list(image))
        expected_automorphisms = theorem.get("expected_automorphisms", [])
        automorphism_group_exact = theorem.get("symmetry") == "automorphisms_of_typed_fault_hypergraph" and sorted(automorphisms) == sorted(expected_automorphisms)
        if not automorphism_group_exact:
            errors.append("correlated_context_symmetry_group_incorrect")
        rewrite_position_independent = all("hole_index" not in rewrite for rewrite in rewrites)
        normalization_equivariant = base.get("newman_global_confluence") and rewrite_position_independent and bridge_safe and separation_preserved and automorphism_group_exact and theorem.get("normalization_action") == "pointwise_rewrites_preserve_indexed_correlation_labels"
        if not normalization_equivariant:
            errors.append("correlated_context_normalization_not_equivariant")
        if theorem.get("theorem_scope") != "all finite typed fault hypergraphs constructed by the admitted correlation constructor":
            errors.append("correlated_context_scope_laundered")
        full_group_order = math.factorial(len(indices))
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "constructor_typed": constructor_typed, "separation_preserved": separation_preserved, "hyperedges_typed": hyperedges_typed, "local_bridges_survive": bridge_safe, "automorphisms": automorphisms, "automorphism_group_order": len(automorphisms), "full_symmetric_group_order": full_group_order, "symmetry_broken": bool(indices) and len(automorphisms) < full_group_order, "normalization_equivariant_under_stabilizer": normalization_equivariant, "scope": theorem.get("theorem_scope")})
    return audits


def audit_correlation_cocircuits(contract: dict[str, Any], correlated_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    correlated_contracts = {item["id"]: item for item in contract.get("configuration_correlated_context_theorems", [])}
    correlated_results = {item["id"]: item for item in correlated_audits}
    paths = contract.get("configuration_path_audits", [])
    local_bridges = sorted({tuple(sorted(edge.get("bridge_authority_roots", {}).values())) for path in paths for edge in path.get("edges", [])})
    audits = []
    for theorem in contract.get("configuration_correlation_cocircuit_theorems", []):
        errors: list[str] = []
        context_id = theorem.get("correlated_context_theorem_id")
        context = correlated_contracts.get(context_id, {})
        context_result = correlated_results.get(context_id, {})
        if not context_result.get("passed"):
            errors.append("correlation_cocircuit_base_context_invalid")
        if theorem.get("classification") != "indexed_local_bridge_root_sets":
            errors.append("correlation_cocircuit_classification_untyped")
        if theorem.get("safety_law") != "safe_iff_no_hyperedge_contains_a_primitive_cocircuit":
            errors.append("correlation_cocircuit_safety_law_untyped")
        if theorem.get("minimality_law") != "deleting_any_one_root_restores_a_bridge_survivor":
            errors.append("correlation_cocircuit_minimality_untyped")
        if theorem.get("symmetry_action") != "automorphism_orbits_of_cocircuits":
            errors.append("correlation_cocircuit_symmetry_action_untyped")
        if theorem.get("theorem_scope") != "all hyperedges over every finite typed hole set admitted by the correlation constructor":
            errors.append("correlation_cocircuit_scope_laundered")

        indices = context.get("hole_indices", [])
        cocircuits = {frozenset((hole, root) for root in bridge) for hole in indices for bridge in local_bridges}
        deletion_minimal = all(
            not frozenset((hole, root) for root in bridge) <= (cocircuit - {locus})
            for hole in indices
            for bridge in local_bridges
            for cocircuit in (frozenset((hole, root) for root in bridge),)
            for locus in cocircuit
        )
        # The bridge audit's failure predicate is exactly cocircuit containment.
        raw_hyperedges = context.get("correlation_hyperedges", [])
        hyperedges = {frozenset((item[0], item[1]) for item in edge) for edge in raw_hyperedges}
        admitted_safe = not any(cocircuit <= edge for cocircuit in cocircuits for edge in hyperedges)
        safety_agrees = admitted_safe == bool(context_result.get("local_bridges_survive"))
        if not deletion_minimal:
            errors.append("correlation_cocircuit_deletion_minimality_failure")
        if not safety_agrees:
            errors.append("correlation_cocircuit_safety_equivalence_failure")
        if not admitted_safe:
            errors.append("correlation_cocircuit_present_in_admitted_hyperedge")

        automorphisms = context_result.get("automorphisms", [])
        orbits: list[set[frozenset[tuple[str, str]]]] = []
        remaining = set(cocircuits)
        while remaining:
            seed = min(remaining, key=lambda value: sorted(value))
            orbit = {seed}
            for image in automorphisms:
                mapping = dict(zip(indices, image))
                orbit.add(frozenset((mapping[hole], root) for hole, root in seed))
            orbits.append(orbit)
            remaining -= orbit
        if theorem.get("expected_cocircuit_count") != len(cocircuits):
            errors.append("correlation_cocircuit_count_mismatch")
        if theorem.get("expected_orbit_count") != len(orbits):
            errors.append("correlation_cocircuit_orbit_mismatch")

        encode = lambda witness: [[hole, root] for hole, root in sorted(witness)]
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "local_bridge_root_sets": [list(bridge) for bridge in local_bridges], "primitive_cocircuits": [encode(item) for item in sorted(cocircuits, key=lambda value: sorted(value))], "cocircuit_count": len(cocircuits), "deletion_minimal": deletion_minimal, "safety_iff_cocircuit_avoidance": safety_agrees, "admitted_hyperedges_safe": admitted_safe, "cocircuit_orbits": [[encode(item) for item in sorted(orbit, key=lambda value: sorted(value))] for orbit in orbits], "orbit_count": len(orbits), "scope": theorem.get("theorem_scope")})
    return audits


def audit_correlation_composition(contract: dict[str, Any], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []
    for theorem in contract.get("configuration_correlation_composition_theorems", []):
        errors: list[str] = []
        base = cocircuit_results.get(theorem.get("cocircuit_theorem_id"), {})
        if not base.get("passed"):
            errors.append("correlation_composition_cocircuit_base_invalid")
        modes_typed = theorem.get("family_union_semantics") == "preserve_distinct_hyperedges" and theorem.get("synchronous_fusion_semantics") == "union_loci_into_one_hyperedge"
        if not modes_typed:
            errors.append("correlation_composition_modes_conflated")
        fusion_authorized = bool(theorem.get("fusion_constructor_id") and theorem.get("fusion_source_authority_root")) and theorem.get("family_union_authorizes_fusion") is False
        if not fusion_authorized:
            errors.append("correlation_composition_fusion_authority_laundered")
        if theorem.get("seam_law") != "fusion_safe_iff_no_primitive_cocircuit_is_split_across_inputs":
            errors.append("correlation_composition_seam_law_untyped")
        if theorem.get("theorem_scope") != "all pairs of typed correlation hyperedges over a common finite hole set":
            errors.append("correlation_composition_scope_laundered")

        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in base.get("primitive_cocircuits", [])}
        fixture_results = []
        for fixture in theorem.get("fixtures", []):
            left = frozenset(tuple(locus) for locus in fixture.get("left_hyperedge", []))
            right = frozenset(tuple(locus) for locus in fixture.get("right_hyperedge", []))
            left_safe = not any(cocircuit <= left for cocircuit in cocircuits)
            right_safe = not any(cocircuit <= right for cocircuit in cocircuits)
            family_safe = left_safe and right_safe
            fused = left | right
            blocking = sorted((cocircuit for cocircuit in cocircuits if cocircuit <= fused), key=lambda value: sorted(value))
            fused_safe = not blocking
            split_blocking = [cocircuit for cocircuit in blocking if not cocircuit <= left and not cocircuit <= right]
            seam_law_holds = fused_safe == (not split_blocking) if family_safe else True
            expected = fixture.get("expected", {})
            fixture_passed = left_safe and right_safe and family_safe and fused_safe == expected.get("fused_safe") and len(split_blocking) == expected.get("split_cocircuit_count") and seam_law_holds
            if not fixture_passed:
                errors.append("correlation_composition_fixture_mismatch")
            encode = lambda witness: [[hole, root] for hole, root in sorted(witness)]
            fixture_results.append({"id": fixture.get("id"), "passed": fixture_passed, "left_safe": left_safe, "right_safe": right_safe, "family_union_safe": family_safe, "fused_safe": fused_safe, "split_cocircuits": [encode(item) for item in split_blocking], "seam_law_holds": seam_law_holds})
        expected_fixture_kinds = {"safe_fusion", "unsafe_split_cocircuit_fusion"}
        if {item.get("kind") for item in theorem.get("fixtures", [])} != expected_fixture_kinds:
            errors.append("correlation_composition_fixture_coverage_incomplete")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "composition_modes_distinct": modes_typed, "fusion_separately_authorized": fusion_authorized, "fixtures": fixture_results, "seam_law": theorem.get("seam_law"), "scope": theorem.get("theorem_scope")})
    return audits


def audit_finite_fusion_witness_bounds(contract: dict[str, Any], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []
    for theorem in contract.get("configuration_finite_fusion_theorems", []):
        errors: list[str] = []
        base = cocircuit_results.get(theorem.get("cocircuit_theorem_id"), {})
        if not base.get("passed"):
            errors.append("finite_fusion_cocircuit_base_invalid")
        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in base.get("primitive_cocircuits", [])}
        derived_bound = max((len(cocircuit) for cocircuit in cocircuits), default=0)
        bound_typed = theorem.get("witness_bound_source") == "maximum_primitive_cocircuit_cardinality" and theorem.get("expected_witness_bound") == derived_bound
        if not bound_typed:
            errors.append("finite_fusion_witness_bound_not_source_derived")
        if theorem.get("finite_subfamily_law") != "unsafe_fusion_has_an_unsafe_subfusion_of_size_at_most_witness_bound":
            errors.append("finite_fusion_subfamily_law_untyped")
        if theorem.get("pairwise_completeness_claimed") != (derived_bound == 2):
            errors.append("finite_fusion_pairwise_completeness_mismatch")
        if theorem.get("theorem_scope") != "all finite families of typed correlation hyperedges over a common finite hole set":
            errors.append("finite_fusion_scope_laundered")

        fixtures = []
        sharp = False
        for fixture in theorem.get("fixtures", []):
            inputs = [frozenset(tuple(locus) for locus in edge) for edge in fixture.get("input_hyperedges", [])]
            individually_safe = all(not any(cocircuit <= edge for cocircuit in cocircuits) for edge in inputs)
            fused = frozenset().union(*inputs) if inputs else frozenset()
            globally_safe = not any(cocircuit <= fused for cocircuit in cocircuits)
            minimum_unsafe_arity = None
            for arity in range(1, len(inputs) + 1):
                if any(any(cocircuit <= frozenset().union(*subfamily) for cocircuit in cocircuits) for subfamily in combinations(inputs, arity)):
                    minimum_unsafe_arity = arity
                    break
            witness_bound_holds = globally_safe or (minimum_unsafe_arity is not None and minimum_unsafe_arity <= derived_bound)
            expected = fixture.get("expected", {})
            fixture_passed = individually_safe and globally_safe == expected.get("globally_safe") and minimum_unsafe_arity == expected.get("minimum_unsafe_arity") and witness_bound_holds
            sharp |= minimum_unsafe_arity == derived_bound
            if not fixture_passed:
                errors.append("finite_fusion_fixture_mismatch")
            fixtures.append({"id": fixture.get("id"), "passed": fixture_passed, "input_count": len(inputs), "individually_safe": individually_safe, "globally_safe": globally_safe, "minimum_unsafe_arity": minimum_unsafe_arity, "witness_bound_holds": witness_bound_holds})
        if theorem.get("bound_sharp_on_fixture") is not True or not sharp:
            errors.append("finite_fusion_witness_bound_not_sharp")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "derived_witness_bound": derived_bound, "pairwise_checks_complete": derived_bound == 2, "bound_sharp": sharp, "fixtures": fixtures, "scope": theorem.get("theorem_scope")})
    return audits


def audit_correlation_repairs(contract: dict[str, Any], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []
    for theorem in contract.get("configuration_correlation_repair_theorems", []):
        errors: list[str] = []
        base = cocircuit_results.get(theorem.get("cocircuit_theorem_id"), {})
        if not base.get("passed"):
            errors.append("correlation_repair_cocircuit_base_invalid")
        classification_typed = theorem.get("repair_classification") == "inclusion_minimal_transversals_of_blocking_cocircuits"
        if not classification_typed:
            errors.append("correlation_repair_classification_untyped")
        repair_authorized = bool(theorem.get("repair_constructor_id") and theorem.get("repair_source_authority_root")) and theorem.get("diagnosis_authorizes_repair") is False and theorem.get("repair_effect") == "remove_failed_loci_from_synchronous_hyperedge"
        if not repair_authorized:
            errors.append("correlation_repair_authority_laundered")
        if theorem.get("theorem_scope") != "every unsafe typed synchronous correlation hyperedge":
            errors.append("correlation_repair_scope_laundered")

        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in base.get("primitive_cocircuits", [])}
        fixture_results = []
        for fixture in theorem.get("fixtures", []):
            edge = frozenset(tuple(locus) for locus in fixture.get("unsafe_hyperedge", []))
            blocking = {cocircuit for cocircuit in cocircuits if cocircuit <= edge}
            universe = sorted(set().union(*blocking)) if blocking else []
            transversals: list[frozenset[tuple[str, str]]] = []
            for size in range(len(universe) + 1):
                for choice in combinations(universe, size):
                    candidate = frozenset(choice)
                    if all(candidate & cocircuit for cocircuit in blocking) and not any(previous < candidate for previous in transversals):
                        transversals.append(candidate)
            repaired_safe = all(not any(cocircuit <= (edge - repair) for cocircuit in cocircuits) for repair in transversals)
            deletion_minimal = all(any(cocircuit <= (edge - (repair - {locus})) for cocircuit in cocircuits) for repair in transversals for locus in repair)
            expected = fixture.get("expected", {})
            sizes = sorted(len(repair) for repair in transversals)
            fixture_passed = bool(blocking) and repaired_safe and deletion_minimal and len(transversals) == expected.get("minimal_repair_count") and sizes == expected.get("minimal_repair_sizes")
            if not fixture_passed:
                errors.append("correlation_repair_fixture_mismatch")
            encode = lambda witness: [[hole, root] for hole, root in sorted(witness)]
            fixture_results.append({"id": fixture.get("id"), "passed": fixture_passed, "blocking_cocircuits": [encode(item) for item in sorted(blocking, key=lambda value: sorted(value))], "minimal_repairs": [encode(item) for item in transversals], "minimal_repair_sizes": sizes, "all_repairs_restore_safety": repaired_safe, "deletion_minimal": deletion_minimal})
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "classification_typed": classification_typed, "repair_separately_authorized": repair_authorized, "fixtures": fixture_results, "scope": theorem.get("theorem_scope")})
    return audits


def audit_repair_selection(contract: dict[str, Any], repair_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    repair_results = {item["id"]: item for item in repair_audits}
    audits = []
    for theorem in contract.get("configuration_repair_selection_theorems", []):
        errors: list[str] = []
        base = repair_results.get(theorem.get("repair_theorem_id"), {})
        fixtures = {item["id"]: item for item in base.get("fixtures", [])}
        fixture = fixtures.get(theorem.get("repair_fixture_id"), {})
        if not base.get("passed") or not fixture.get("passed"):
            errors.append("repair_selection_repair_base_invalid")
        repairs = [frozenset(tuple(locus) for locus in repair) for repair in fixture.get("minimal_repairs", [])]
        universe = set().union(*repairs) if repairs else set()
        valuation_typed = bool(theorem.get("valuation_constructor_id")) and theorem.get("valuation_kind") == "strictly_positive_additive_locus_cost"
        selector_typed = bool(theorem.get("selector_constructor_id") and theorem.get("selector_source_authority_root")) and theorem.get("safety_authorizes_selection") is False and theorem.get("selection_authorizes_execution") is False
        if not valuation_typed:
            errors.append("repair_selection_valuation_untyped")
        if not selector_typed:
            errors.append("repair_selection_authority_laundered")
        if theorem.get("selection_law") != "argmin_total_cost_over_primitive_repairs":
            errors.append("repair_selection_law_untyped")
        if theorem.get("theorem_scope") != "finite primitive repair families with source-authorized strictly positive locus valuations":
            errors.append("repair_selection_scope_laundered")

        profile_results = []
        selections = set()
        for profile in theorem.get("valuation_profiles", []):
            weights = {tuple(item.get("locus", [])): item.get("cost") for item in profile.get("weights", [])}
            weights_typed = bool(profile.get("source_authority_root")) and set(weights) == universe and all(isinstance(cost, int) and not isinstance(cost, bool) and cost > 0 for cost in weights.values())
            costs = [sum(weights.get(locus, 0) for locus in repair) for repair in repairs]
            minimum = min(costs) if costs else None
            winners = [repair for repair, cost in zip(repairs, costs) if cost == minimum]
            unique = len(winners) == 1
            selected = winners[0] if unique else frozenset()
            expected = frozenset(tuple(locus) for locus in profile.get("expected_selected_repair", []))
            profile_passed = weights_typed and unique and selected == expected
            if not profile_passed:
                errors.append("repair_selection_profile_mismatch")
            selections.add(selected)
            encode = lambda witness: [[hole, root] for hole, root in sorted(witness)]
            profile_results.append({"id": profile.get("id"), "passed": profile_passed, "weights_typed": weights_typed, "repair_costs": costs, "minimum_cost": minimum, "unique_minimizer": unique, "selected_repair": encode(selected)})
        preference_reversal = len(profile_results) >= 2 and len(selections) >= 2
        no_canonical_selector = theorem.get("no_canonical_selector_from_safety") is True and preference_reversal
        if not no_canonical_selector:
            errors.append("repair_selection_canonical_choice_smuggled")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "valuation_typed": valuation_typed, "selector_separately_authorized": selector_typed, "preference_reversal": preference_reversal, "no_canonical_selector_from_safety": no_canonical_selector, "profiles": profile_results, "scope": theorem.get("theorem_scope")})
    return audits


def audit_repair_execution(contract: dict[str, Any], selection_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selection_results = {item["id"]: item for item in selection_audits}
    selection_contracts = {item["id"]: item for item in contract.get("configuration_repair_selection_theorems", [])}
    repair_contracts = {item["id"]: item for item in contract.get("configuration_correlation_repair_theorems", [])}
    audits = []
    required_bindings = {"unsafe_hyperedge", "primitive_repair_family", "valuation_profile", "selected_repair"}
    for theorem in contract.get("configuration_repair_execution_theorems", []):
        errors: list[str] = []
        selection_id = theorem.get("selection_theorem_id")
        selection = selection_results.get(selection_id, {})
        selection_contract = selection_contracts.get(selection_id, {})
        repair_contract = repair_contracts.get(selection_contract.get("repair_theorem_id"), {})
        repair_fixtures = {item["id"]: item for item in repair_contract.get("fixtures", [])}
        repair_fixture = repair_fixtures.get(selection_contract.get("repair_fixture_id"), {})
        if not selection.get("passed") or not repair_fixture:
            errors.append("repair_execution_selection_base_invalid")
        binding_typed = set(theorem.get("certificate_binding_fields", [])) == required_bindings and theorem.get("binding_kind") == "content_addressed_exact_configuration"
        if not binding_typed:
            errors.append("repair_execution_certificate_underbound")
        capability_typed = bool(theorem.get("executor_constructor_id") and theorem.get("executor_source_authority_root")) and theorem.get("capability_modality") == "linear" and theorem.get("capability_uses") == 1 and theorem.get("selection_record_is_nonexecuting") is True
        if not capability_typed:
            errors.append("repair_execution_authority_laundered")
        atomic_typed = theorem.get("execution_semantics") == "atomic_compare_bound_configuration_apply_and_consume" and theorem.get("postcondition") == "recompute_cocircuit_safety"
        if not atomic_typed:
            errors.append("repair_execution_nonatomic_or_unverified")
        if theorem.get("theorem_scope") != "all source-bound selected repairs with separately issued linear execution capabilities":
            errors.append("repair_execution_scope_laundered")

        unsafe_edge = frozenset(tuple(locus) for locus in repair_fixture.get("unsafe_hyperedge", []))
        profiles = {item["id"]: item for item in selection.get("profiles", [])}
        request_results = []
        for request in theorem.get("execution_requests", []):
            profile = profiles.get(request.get("valuation_profile_id"), {})
            selected = frozenset(tuple(locus) for locus in profile.get("selected_repair", []))
            observed = frozenset(tuple(locus) for locus in request.get("observed_hyperedge", []))
            requested = frozenset(tuple(locus) for locus in request.get("requested_repair", []))
            configuration_matches = observed == unsafe_edge
            selection_matches = requested == selected and bool(selected)
            linear_consumption = request.get("uses_before") == 1 and request.get("uses_after") == 0
            repaired_edge = observed - requested
            # Every declared local bridge must retain at least one authority root.
            local_bridges = {frozenset(edge.get("bridge_authority_roots", {}).values()) for path in contract.get("configuration_path_audits", []) for edge in path.get("edges", [])}
            postcondition_safe = all(not bridge <= {root for hole, root in repaired_edge if hole == index} for index in {hole for hole, _ in repaired_edge} for bridge in local_bridges)
            admitted = binding_typed and capability_typed and atomic_typed and configuration_matches and selection_matches and linear_consumption and postcondition_safe
            expected = request.get("expected_admitted")
            if admitted != expected:
                errors.append("repair_execution_request_mismatch")
            certificate = {"unsafe_hyperedge": [list(item) for item in sorted(unsafe_edge)], "valuation_profile": request.get("valuation_profile_id"), "selected_repair": [list(item) for item in sorted(selected)]}
            certificate_payload = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode("ascii")
            request_results.append({"id": request.get("id"), "passed": admitted == expected, "admitted": admitted, "configuration_matches": configuration_matches, "selection_matches": selection_matches, "linear_capability_consumed": linear_consumption, "postcondition_safe": postcondition_safe, "certificate_digest": hashlib.sha256(certificate_payload).hexdigest()})
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "certificate_fully_bound": binding_typed, "linear_executor_separately_authorized": capability_typed, "atomic_and_postverified": atomic_typed, "execution_requests": request_results, "scope": theorem.get("theorem_scope")})
    return audits


def audit_repair_execution_decomposition(contract: dict[str, Any], selection_audits: list[dict[str, Any]], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selection_results = {item["id"]: item for item in selection_audits}
    selection_contracts = {item["id"]: item for item in contract.get("configuration_repair_selection_theorems", [])}
    repair_contracts = {item["id"]: item for item in contract.get("configuration_correlation_repair_theorems", [])}
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []
    for theorem in contract.get("configuration_repair_execution_decomposition_theorems", []):
        errors: list[str] = []
        selection_id = theorem.get("selection_theorem_id")
        selection = selection_results.get(selection_id, {})
        selection_contract = selection_contracts.get(selection_id, {})
        repair_contract = repair_contracts.get(selection_contract.get("repair_theorem_id"), {})
        fixture = next((item for item in repair_contract.get("fixtures", []) if item.get("id") == selection_contract.get("repair_fixture_id")), {})
        profile = next((item for item in selection.get("profiles", []) if item.get("id") == theorem.get("valuation_profile_id")), {})
        cocircuit_base = cocircuit_results.get(repair_contract.get("cocircuit_theorem_id"), {})
        if not selection.get("passed") or not profile.get("passed") or not cocircuit_base.get("passed"):
            errors.append("repair_decomposition_base_invalid")
        law_typed = theorem.get("decomposition_law") == "proper_subrepairs_are_not_endpoint_capabilities_without_intermediate_state_authority" and theorem.get("atomic_capability_partition_authorized") is False
        if not law_typed:
            errors.append("repair_decomposition_authority_laundered")
        options_typed = set(theorem.get("authorized_options", [])) == {"joint_atomic_execution", "staged_execution_with_intermediate_state_authority"}
        if not options_typed:
            errors.append("repair_decomposition_options_untyped")
        if theorem.get("theorem_scope") != "all multi-locus primitive repairs selected from an unsafe typed correlation hyperedge":
            errors.append("repair_decomposition_scope_laundered")

        edge = frozenset(tuple(locus) for locus in fixture.get("unsafe_hyperedge", []))
        selected = frozenset(tuple(locus) for locus in profile.get("selected_repair", []))
        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in cocircuit_base.get("primitive_cocircuits", [])}
        proper_subrepairs = []
        for size in range(1, len(selected)):
            for subset in combinations(sorted(selected), size):
                part = frozenset(subset)
                safe = not any(cocircuit <= (edge - part) for cocircuit in cocircuits)
                proper_subrepairs.append({"repair": [list(item) for item in sorted(part)], "endpoint_safe": safe})
        joint_safe = bool(selected) and not any(cocircuit <= (edge - selected) for cocircuit in cocircuits)
        all_proper_unsafe = bool(proper_subrepairs) and all(not item["endpoint_safe"] for item in proper_subrepairs)
        algebraic_commutation = all((edge - first) - second == (edge - second) - first for first, second in combinations((frozenset({item}) for item in selected), 2))
        expected = theorem.get("expected", {})
        fixture_holds = len(proper_subrepairs) == expected.get("proper_subrepair_count") and all_proper_unsafe == expected.get("all_proper_subrepairs_endpoint_unsafe") and joint_safe == expected.get("joint_repair_safe") and algebraic_commutation
        if not fixture_holds:
            errors.append("repair_decomposition_fixture_mismatch")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "selected_repair_size": len(selected), "proper_subrepairs": proper_subrepairs, "all_proper_subrepairs_endpoint_unsafe": all_proper_unsafe, "joint_repair_safe": joint_safe, "deletion_effects_commute": algebraic_commutation, "authority_partition_forbidden": law_typed, "authorized_options_typed": options_typed, "scope": theorem.get("theorem_scope")})
    return audits


def audit_staged_repair_paths(contract: dict[str, Any], selection_audits: list[dict[str, Any]], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selection_results = {item["id"]: item for item in selection_audits}
    selection_contracts = {item["id"]: item for item in contract.get("configuration_repair_selection_theorems", [])}
    repair_contracts = {item["id"]: item for item in contract.get("configuration_correlation_repair_theorems", [])}
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []
    required_residual_bindings = {"source_configuration", "applied_subrepair", "remaining_subrepair", "target_configuration"}
    for theorem in contract.get("configuration_staged_repair_path_theorems", []):
        errors: list[str] = []
        selection_id = theorem.get("selection_theorem_id")
        selection = selection_results.get(selection_id, {})
        selection_contract = selection_contracts.get(selection_id, {})
        repair_contract = repair_contracts.get(selection_contract.get("repair_theorem_id"), {})
        fixture = next((item for item in repair_contract.get("fixtures", []) if item.get("id") == selection_contract.get("repair_fixture_id")), {})
        profile = next((item for item in selection.get("profiles", []) if item.get("id") == theorem.get("valuation_profile_id")), {})
        cocircuit_base = cocircuit_results.get(repair_contract.get("cocircuit_theorem_id"), {})
        if not selection.get("passed") or not profile.get("passed") or not cocircuit_base.get("passed"):
            errors.append("staged_repair_path_base_invalid")
        constructor_typed = bool(theorem.get("staged_constructor_id") and theorem.get("intermediate_state_authority_root")) and theorem.get("intermediate_authority_kind") == "unsafe_repair_in_progress" and theorem.get("intermediate_inherits_endpoint_safety") is False
        if not constructor_typed:
            errors.append("staged_repair_intermediate_authority_untyped")
        residual_typed = set(theorem.get("residual_certificate_binding_fields", [])) == required_residual_bindings and theorem.get("residual_capability_modality") == "linear"
        if not residual_typed:
            errors.append("staged_repair_residual_certificate_underbound")
        coherence_typed = theorem.get("coherence_cell_source") == "commuting_set_difference_identity" and theorem.get("primitive_or_fitted_coherence_cell") is False
        if not coherence_typed:
            errors.append("staged_repair_coherence_not_generated")
        if theorem.get("theorem_scope") != "both factorizations of every selected two-locus primitive repair":
            errors.append("staged_repair_scope_laundered")

        edge = frozenset(tuple(locus) for locus in fixture.get("unsafe_hyperedge", []))
        selected = frozenset(tuple(locus) for locus in profile.get("selected_repair", []))
        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in cocircuit_base.get("primitive_cocircuits", [])}
        raw_paths = theorem.get("factorization_paths", [])
        paths = []
        for raw_path in raw_paths:
            order = [tuple(locus) for locus in raw_path.get("order", [])]
            order_typed = len(order) == 2 and len(set(order)) == 2 and set(order) == selected
            intermediate = edge - {order[0]} if order else edge
            endpoint = intermediate - {order[1]} if len(order) > 1 else intermediate
            intermediate_safe = not any(cocircuit <= intermediate for cocircuit in cocircuits)
            endpoint_safe = not any(cocircuit <= endpoint for cocircuit in cocircuits)
            residual = {"source_configuration": [list(item) for item in sorted(edge)], "applied_subrepair": [list(order[0])] if order else [], "remaining_subrepair": [list(order[1])] if len(order) > 1 else [], "target_configuration": [list(item) for item in sorted(endpoint)]}
            residual_digest = hashlib.sha256(json.dumps(residual, sort_keys=True, separators=(",", ":")).encode("ascii")).hexdigest()
            paths.append({"id": raw_path.get("id"), "order_typed": order_typed, "intermediate_configuration": [list(item) for item in sorted(intermediate)], "intermediate_safe": intermediate_safe, "endpoint_configuration": [list(item) for item in sorted(endpoint)], "endpoint_safe": endpoint_safe, "residual_certificate_digest": residual_digest})
        distinct_intermediates = len({json.dumps(path["intermediate_configuration"]) for path in paths}) == len(paths)
        common_endpoint = len({json.dumps(path["endpoint_configuration"]) for path in paths}) == 1 if paths else False
        path_gate = len(paths) == 2 and all(path["order_typed"] and not path["intermediate_safe"] and path["endpoint_safe"] for path in paths) and distinct_intermediates and common_endpoint
        expected = theorem.get("expected", {})
        expected_holds = len(paths) == expected.get("path_count") and distinct_intermediates == expected.get("distinct_intermediates") and common_endpoint == expected.get("common_safe_endpoint")
        if not path_gate or not expected_holds:
            errors.append("staged_repair_path_fixture_mismatch")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "constructor_typed": constructor_typed, "residual_certificates_typed": residual_typed, "coherence_generated": coherence_typed, "paths": paths, "distinct_unsafe_intermediates": distinct_intermediates, "common_safe_endpoint": common_endpoint, "scope": theorem.get("theorem_scope")})
    return audits


def audit_finite_staged_coherence(contract: dict[str, Any], repair_audits: list[dict[str, Any]], cocircuit_audits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    repair_results = {item["id"]: item for item in repair_audits}
    repair_contracts = {item["id"]: item for item in contract.get("configuration_correlation_repair_theorems", [])}
    cocircuit_results = {item["id"]: item for item in cocircuit_audits}
    audits = []

    def swapped(order: tuple[Any, ...], position: int) -> tuple[Any, ...]:
        result = list(order)
        result[position], result[position + 1] = result[position + 1], result[position]
        return tuple(result)

    def acted(order: tuple[Any, ...], word: list[int]) -> tuple[Any, ...]:
        for position in word:
            order = swapped(order, position)
        return order

    for theorem in contract.get("configuration_finite_staged_coherence_theorems", []):
        errors: list[str] = []
        repair_id = theorem.get("repair_theorem_id")
        repair_result = repair_results.get(repair_id, {})
        repair_contract = repair_contracts.get(repair_id, {})
        fixture_result = next((item for item in repair_result.get("fixtures", []) if item.get("id") == theorem.get("repair_fixture_id")), {})
        fixture_contract = next((item for item in repair_contract.get("fixtures", []) if item.get("id") == theorem.get("repair_fixture_id")), {})
        cocircuit_base = cocircuit_results.get(repair_contract.get("cocircuit_theorem_id"), {})
        if not repair_result.get("passed") or not fixture_result.get("passed") or not cocircuit_base.get("passed"):
            errors.append("finite_staged_coherence_base_invalid")
        selected = frozenset(tuple(locus) for locus in theorem.get("selected_primitive_repair", []))
        primitive_repairs = {frozenset(tuple(locus) for locus in repair) for repair in fixture_result.get("minimal_repairs", [])}
        selected_typed = selected in primitive_repairs and len(selected) >= 2
        if not selected_typed:
            errors.append("finite_staged_selected_repair_not_primitive")
        generators_typed = theorem.get("path_generators") == "adjacent_transpositions_of_repair_loci"
        relations_typed = set(theorem.get("coherence_relations", [])) == {"involution", "far_commutation", "braid"} and theorem.get("coherence_completion") == "coxeter_presentation_of_finite_symmetric_group" and theorem.get("primitive_or_fitted_higher_cells") is False
        if not generators_typed:
            errors.append("finite_staged_generators_untyped")
        if not relations_typed:
            errors.append("finite_staged_coxeter_relations_incomplete")
        if theorem.get("intermediate_authority_kind") != "unsafe_repair_in_progress":
            errors.append("finite_staged_intermediate_authority_laundered")
        if theorem.get("theorem_scope") != "all finite selected repairs with constructor-authorized intermediate states":
            errors.append("finite_staged_scope_laundered")

        base_order = tuple(sorted(selected))
        orders = list(permutations(base_order))
        edge = frozenset(tuple(locus) for locus in fixture_contract.get("unsafe_hyperedge", []))
        cocircuits = {frozenset(tuple(locus) for locus in witness) for witness in cocircuit_base.get("primitive_cocircuits", [])}
        all_proper_prefixes_unsafe = True
        endpoints = set()
        for order in orders:
            for prefix_size in range(1, len(order)):
                intermediate = edge - set(order[:prefix_size])
                all_proper_prefixes_unsafe &= any(cocircuit <= intermediate for cocircuit in cocircuits)
            endpoints.add(edge - set(order))
        common_safe_endpoint = len(endpoints) == 1 and all(not any(cocircuit <= endpoint for cocircuit in cocircuits) for endpoint in endpoints)

        reachable = {base_order}
        frontier = [base_order]
        while frontier:
            current = frontier.pop()
            for position in range(max(0, len(current) - 1)):
                target = swapped(current, position)
                if target not in reachable:
                    reachable.add(target)
                    frontier.append(target)
        adjacent_graph_connected = set(orders) == reachable
        involution = all(acted(base_order, [i, i]) == base_order for i in range(max(0, len(base_order) - 1)))
        braid = all(acted(base_order, [i, i + 1, i]) == acted(base_order, [i + 1, i, i + 1]) for i in range(max(0, len(base_order) - 2)))
        four = tuple(range(4))
        far_commutation = all(acted(four, [i, j]) == acted(four, [j, i]) for i in range(3) for j in range(3) if abs(i - j) > 1)
        coxeter_holds = involution and braid and far_commutation and adjacent_graph_connected
        expected = theorem.get("expected", {})
        fixture_holds = len(selected) == expected.get("repair_size") and len(orders) == expected.get("path_count") and all_proper_prefixes_unsafe == expected.get("all_proper_prefixes_unsafe") and common_safe_endpoint == expected.get("common_safe_endpoint")
        if not coxeter_holds or not fixture_holds:
            errors.append("finite_staged_coherence_fixture_mismatch")
        audits.append({"id": theorem["id"], "passed": not errors, "errors": sorted(set(errors)), "selected_repair_primitive": selected_typed, "repair_size": len(selected), "factorization_path_count": len(orders), "all_proper_prefixes_unsafe": all_proper_prefixes_unsafe, "common_safe_endpoint": common_safe_endpoint, "adjacent_swap_graph_connected": adjacent_graph_connected, "coxeter_relations": {"involution": involution, "far_commutation": far_commutation, "braid": braid}, "coherence_generated": relations_typed and coxeter_holds, "scope": theorem.get("theorem_scope")})
    return audits


def compile_contract(contract: dict[str, Any], legacy: dict[str, Any] | None = None) -> dict[str, Any]:
    results = [check_pair(pair) for pair in contract["critical_pairs"]]
    pair_ids = {item["id"] for item in results}
    footprints = contract["active_rewrite_footprints"]
    overlaps = []
    for left, right in combinations(sorted(footprints), 2):
        shared = sorted(set(footprints[left]) & set(footprints[right]))
        if shared:
            key = f"{left}|{right}"
            witness = contract.get("critical_pair_coverage", {}).get(key)
            overlaps.append({"rules": [left, right], "shared_fields": shared, "witness": witness, "covered": witness in pair_ids})
    normalization_results = []
    for case in contract.get("normalization_cases", []):
        try:
            normalized = normalize(case["input"])
            actual = {key: normalized.get(key) for key in case["expected"]}
            passed = actual == case["expected"] and case.get("expected_error") is None
            error = None
        except ValueError as exc:
            normalized = None
            error = str(exc)
            passed = error == case.get("expected_error")
        normalization_results.append({"id": case["id"], "passed": passed, "error": error, "normalized": normalized})
    legacy_audits = audit_legacy_grants(legacy) if legacy is not None else []
    native_audits = audit_native_capabilities(contract)
    successor_audits = audit_epoch_successors(contract)
    execution_audits = audit_native_execution_traces(contract)
    cocircuit_audits = audit_trusted_base_cocircuits(contract)
    resource_ssa_audits = audit_resource_ssa_programs(contract)
    projection_audits = audit_forgetful_projections(contract)
    chain_audits = audit_epoch_successor_chains(contract)
    reconfiguration_audits = audit_native_reconfiguration_constructors(contract)
    configuration_path_audits = audit_configuration_paths(contract)
    configuration_category_audits = audit_configuration_category(contract)
    configuration_rewrite_audits, configuration_normalization_audits, generated_coherence_cells = generate_configuration_coherence(contract, configuration_path_audits)
    configuration_coherence_audits = audit_configuration_path_coherence(contract, configuration_path_audits, generated_coherence_cells)
    configuration_triangle_audits = audit_configuration_coherence_triangles(contract, generated_coherence_cells)
    configuration_coherence_coverage = audit_configuration_coherence_coverage(contract)
    contextual_rewrite_audits = audit_contextual_configuration_rewrites(contract, configuration_path_audits)
    context_symmetry_audits = audit_configuration_context_symmetry(contract, contextual_rewrite_audits)
    correlated_context_audits = audit_correlated_configuration_contexts(contract, contextual_rewrite_audits)
    correlation_cocircuit_audits = audit_correlation_cocircuits(contract, correlated_context_audits)
    correlation_composition_audits = audit_correlation_composition(contract, correlation_cocircuit_audits)
    finite_fusion_audits = audit_finite_fusion_witness_bounds(contract, correlation_cocircuit_audits)
    correlation_repair_audits = audit_correlation_repairs(contract, correlation_cocircuit_audits)
    repair_selection_audits = audit_repair_selection(contract, correlation_repair_audits)
    repair_execution_audits = audit_repair_execution(contract, repair_selection_audits)
    repair_decomposition_audits = audit_repair_execution_decomposition(contract, repair_selection_audits, correlation_cocircuit_audits)
    staged_repair_path_audits = audit_staged_repair_paths(contract, repair_selection_audits, correlation_cocircuit_audits)
    finite_staged_coherence_audits = audit_finite_staged_coherence(contract, correlation_repair_audits, correlation_cocircuit_audits)
    defaults_forbidden = not contract.get("legacy_projection_audit", {}).get("permit_defaulting", True)
    return {
        "schema": "marici.dpc-core-normalizer-result.v1",
        "passed": all(item["passed"] for item in results + normalization_results + successor_audits + execution_audits + cocircuit_audits + resource_ssa_audits + projection_audits + chain_audits + reconfiguration_audits + configuration_path_audits + configuration_category_audits + configuration_rewrite_audits + configuration_normalization_audits + configuration_coherence_audits + configuration_triangle_audits + configuration_coherence_coverage + contextual_rewrite_audits + context_symmetry_audits + correlated_context_audits + correlation_cocircuit_audits + correlation_composition_audits + finite_fusion_audits + correlation_repair_audits + repair_selection_audits + repair_execution_audits + repair_decomposition_audits + staged_repair_path_audits + finite_staged_coherence_audits) and all(item["covered"] for item in overlaps) and defaults_forbidden and all(item["compiled"] for item in native_audits),
        "rule_count": len(contract["rewrite_rules"]),
        "critical_pair_count": len(results),
        "critical_pairs": results,
        "normalization_cases": normalization_results,
        "generated_overlaps": overlaps,
        "normal_form_digests": {item["id"]: digest(item["left"]) for item in contract["critical_pairs"]},
        "legacy_projection": {
            "defaults_forbidden": defaults_forbidden,
            "grant_count": len(legacy_audits),
            "importable_count": sum(item["importable"] for item in legacy_audits),
            "grants": legacy_audits,
        },
        "native_capabilities": native_audits,
        "epoch_successor_events": successor_audits,
        "native_execution_traces": execution_audits,
        "trusted_base_cocircuits": cocircuit_audits,
        "resource_ssa_programs": resource_ssa_audits,
        "forgetful_projections": projection_audits,
        "epoch_successor_chains": chain_audits,
        "native_reconfiguration_constructors": reconfiguration_audits,
        "configuration_paths": configuration_path_audits,
        "configuration_category": configuration_category_audits,
        "configuration_constructor_rewrites": configuration_rewrite_audits,
        "configuration_normalization": configuration_normalization_audits,
        "configuration_path_coherence": configuration_coherence_audits,
        "configuration_coherence_triangles": configuration_triangle_audits,
        "configuration_coherence_coverage": configuration_coherence_coverage,
        "configuration_contextual_rewrite_theorems": contextual_rewrite_audits,
        "configuration_context_symmetry_theorems": context_symmetry_audits,
        "configuration_correlated_context_theorems": correlated_context_audits,
        "configuration_correlation_cocircuit_theorems": correlation_cocircuit_audits,
        "configuration_correlation_composition_theorems": correlation_composition_audits,
        "configuration_finite_fusion_theorems": finite_fusion_audits,
        "configuration_correlation_repair_theorems": correlation_repair_audits,
        "configuration_repair_selection_theorems": repair_selection_audits,
        "configuration_repair_execution_theorems": repair_execution_audits,
        "configuration_repair_execution_decomposition_theorems": repair_decomposition_audits,
        "configuration_staged_repair_path_theorems": staged_repair_path_audits,
        "configuration_finite_staged_coherence_theorems": finite_staged_coherence_audits,
    }
