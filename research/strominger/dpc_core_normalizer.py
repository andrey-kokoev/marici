"""Bounded DPC constructor-DAG normalizer.

The normalizer preserves the full authority signature.  Equal executable
outputs are insufficient for a critical-pair join.
"""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
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


def audit_dynamic_reconfiguration_chains(contract: dict[str, Any]) -> list[dict[str, Any]]:
    audits = []
    for chain in contract.get("dynamic_reconfiguration_chain_audits", []):
        errors: list[str] = []
        current = chain.get("base_configuration", {})
        current_epoch = current.get("epoch")
        current_digest = current.get("state_sha256")
        current_members = current.get("members")
        current_quorum = current.get("quorum")
        current_authority = current.get("authority_resource")
        accumulated = set(current.get("support", []))
        consumed: set[str] = set()
        bridges = []
        bridge_states: list[tuple[set[str], dict[str, str]]] = []
        steps = chain.get("steps", [])
        if not steps or not chain.get("theorem_scope"):
            errors.append("dynamic_reconfiguration_chain_empty_or_unscoped")
        for step in steps:
            old = step.get("old_configuration", {})
            new = step.get("new_configuration", {})
            physical = step.get("physical_successor", {})
            output = step.get("output_configuration", {})
            if (old.get("epoch"), old.get("state_sha256"), old.get("members"), old.get("quorum"), old.get("authority_resource")) != (current_epoch, current_digest, current_members, current_quorum, current_authority):
                errors.append("dynamic_reconfiguration_predecessor_link_failure")
            if set(old.get("support", [])) != accumulated:
                errors.append("dynamic_reconfiguration_predecessor_support_failure")
            if not step.get("source_authority_root"):
                errors.append("dynamic_reconfiguration_constructor_untyped")
            old_offset = old.get("epoch", {}).get("offset")
            if (new.get("epoch", {}).get("parameter") != old.get("epoch", {}).get("parameter") or not isinstance(old_offset, int) or new.get("epoch", {}).get("offset") != old_offset + 1):
                errors.append("dynamic_reconfiguration_nonadjacent_epoch")
            if not physical.get("realized") or physical.get("predecessor_state_sha256") != old.get("state_sha256") or physical.get("successor_state_sha256") != new.get("state_sha256"):
                errors.append("dynamic_reconfiguration_physical_correspondence_failure")
            old_q, new_q = set(old.get("quorum", [])), set(new.get("quorum", []))
            bridge = old_q & new_q
            if not bridge or not old_q <= set(old.get("members", [])) or not new_q <= set(new.get("members", [])) or len(old.get("members", [])) != len(set(old.get("members", []))) or len(new.get("members", [])) != len(set(new.get("members", []))):
                errors.append("dynamic_reconfiguration_invalid_configuration_bridge")
            if set(step.get("old_quorum_endorsement", [])) != old_q or set(step.get("new_quorum_endorsement", [])) != new_q or not step.get("joint_consensus_required"):
                errors.append("dynamic_reconfiguration_joint_endorsement_failure")
            if set(step.get("bridge_witness", [])) != bridge:
                errors.append("dynamic_reconfiguration_bridge_mismatch")
            roots = step.get("bridge_authority_roots", {})
            faults = [set(fault) for fault in step.get("admissible_bridge_fault_sets", [])]
            if set(roots) != bridge:
                errors.append("dynamic_reconfiguration_bridge_roots_incomplete")
            root_fibers = [{node for node, root in roots.items() if root == authority_root} for authority_root in set(roots.values())]
            if any(fiber not in faults for fiber in root_fibers):
                errors.append("dynamic_reconfiguration_common_cause_omitted")
            if any(not (bridge - fault) for fault in faults):
                errors.append("dynamic_reconfiguration_bridge_fault_unsafe")
            output_authority = output.get("authority_resource")
            if step.get("consumes_authority_resource") != current_authority or current_authority in consumed or not output_authority or output_authority == current_authority or output_authority in consumed or step.get("old_authority_retained") is not False or step.get("live_authority_count_after") != 1:
                errors.append("dynamic_reconfiguration_linear_replacement_failure")
            consumed.add(current_authority)
            expected_support = accumulated | set(new.get("support", [])) | set(physical.get("support", [])) | {step.get("source_authority_root")}
            if set(output.get("support", [])) != expected_support:
                errors.append("dynamic_reconfiguration_support_not_monotone")
            if (output.get("epoch"), output.get("state_sha256"), output.get("members"), output.get("quorum")) != (new.get("epoch"), new.get("state_sha256"), new.get("members"), new.get("quorum")):
                errors.append("dynamic_reconfiguration_output_mismatch")
            bridges.append({"step": step.get("id"), "bridge": sorted(bridge), "authority_roots": roots, "fault_sets": [sorted(fault) for fault in faults]})
            bridge_states.append((bridge, roots))
            accumulated = expected_support
            current_epoch, current_digest = output.get("epoch"), output.get("state_sha256")
            current_members, current_quorum = output.get("members"), output.get("quorum")
            current_authority = output_authority
        global_root_faults = [set(fault) for fault in chain.get("admissible_authority_root_fault_sets", [])]
        all_roots = {root for _, roots in bridge_states for root in roots.values()}
        if any({root} not in global_root_faults for root in all_roots):
            errors.append("dynamic_reconfiguration_global_root_fault_omitted")
        for root_fault in global_root_faults:
            for bridge, roots in bridge_states:
                failed_nodes = {node for node in bridge if roots.get(node) in root_fault}
                if not (bridge - failed_nodes):
                    errors.append("dynamic_reconfiguration_global_fault_unsafe")
        terminal = chain.get("expected_terminal_configuration", {})
        if (current_epoch, current_digest, current_members, current_quorum, current_authority) != (terminal.get("epoch"), terminal.get("state_sha256"), terminal.get("members"), terminal.get("quorum"), terminal.get("authority_resource")):
            errors.append("dynamic_reconfiguration_terminal_mismatch")
        if accumulated != set(terminal.get("support", [])):
            errors.append("dynamic_reconfiguration_support_not_monotone")
        audits.append({"id": chain["id"], "passed": not errors, "errors": sorted(set(errors)), "step_count": len(steps), "terminal_epoch": current_epoch, "live_authority_resource": current_authority, "consumed_authority_resources": sorted(consumed), "accumulated_support": sorted(accumulated), "bridge_audits": bridges, "global_authority_root_fault_sets": [sorted(fault) for fault in global_root_faults], "induction_rule": "a valid prefix extends iff the adjacent realized joint transition consumes its sole live configuration authority, emits one replacement, accumulates support, and every admitted local or chain-wide authority-root fault leaves every affected bridge with a survivor"})
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
    dynamic_reconfiguration_audits = audit_dynamic_reconfiguration_chains(contract)
    defaults_forbidden = not contract.get("legacy_projection_audit", {}).get("permit_defaulting", True)
    return {
        "schema": "marici.dpc-core-normalizer-result.v1",
        "passed": all(item["passed"] for item in results + normalization_results + successor_audits + execution_audits + cocircuit_audits + resource_ssa_audits + projection_audits + chain_audits + reconfiguration_audits + dynamic_reconfiguration_audits) and all(item["covered"] for item in overlaps) and defaults_forbidden and all(item["compiled"] for item in native_audits),
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
        "dynamic_reconfiguration_chains": dynamic_reconfiguration_audits,
    }
