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


def canonical_signature(node: dict[str, Any]) -> dict[str, Any]:
    sig = {key: deepcopy(node[key]) for key in SIGNATURE_FIELDS}
    sig["scope"] = sorted(set(sig["scope"]))
    sig["support"] = sorted(set(sig["support"]))
    sig["resource"] = {key: sig["resource"][key] for key in sorted(sig["resource"])}
    return sig


def normalize(node: dict[str, Any]) -> dict[str, Any]:
    current = deepcopy(node)
    while True:
        before = json.dumps(current, sort_keys=True, separators=(",", ":"))
        current["scope"] = sorted(set(current["scope"]))
        current["support"] = sorted(set(current["support"]))
        current["resource"] = {key: current["resource"][key] for key in sorted(current["resource"])}
        operations = current.get("operations", [])
        fused_operations: list[dict[str, Any]] = []
        index = 0
        while index < len(operations):
            first = operations[index]
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
                if current.get("epoch", 0) < operation["minimum_epoch"]:
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
            reduced.append(operation)
        current["operations"] = reduced
        after = json.dumps(current, sort_keys=True, separators=(",", ":"))
        if before == after:
            return current


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


def compile_contract(contract: dict[str, Any]) -> dict[str, Any]:
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
    return {
        "schema": "marici.dpc-core-normalizer-result.v1",
        "passed": all(item["passed"] for item in results + normalization_results) and all(item["covered"] for item in overlaps),
        "rule_count": len(contract["rewrite_rules"]),
        "critical_pair_count": len(results),
        "critical_pairs": results,
        "normalization_cases": normalization_results,
        "generated_overlaps": overlaps,
        "normal_form_digests": {item["id"]: digest(item["left"]) for item in contract["critical_pairs"]},
    }
