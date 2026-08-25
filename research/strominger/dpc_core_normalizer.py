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
    defaults_forbidden = not contract.get("legacy_projection_audit", {}).get("permit_defaulting", True)
    return {
        "schema": "marici.dpc-core-normalizer-result.v1",
        "passed": all(item["passed"] for item in results + normalization_results + successor_audits) and all(item["covered"] for item in overlaps) and defaults_forbidden and all(item["compiled"] for item in native_audits),
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
    }
