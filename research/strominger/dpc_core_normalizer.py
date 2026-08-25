"""Bounded DPC constructor-DAG normalizer.

The normalizer preserves the full authority signature.  Equal executable
outputs are insufficient for a critical-pair join.
"""

from __future__ import annotations

import hashlib
import json
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
        reduced: list[dict[str, Any]] = []
        for operation in operations:
            if operation["kind"] == "identity":
                if operation["signature"] != canonical_signature(current):
                    raise ValueError("identity_signature_mismatch")
                continue
            if operation["kind"] == "attenuate":
                current["scope"] = sorted(set(current["scope"]) & set(operation["scope"]))
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
    return {
        "schema": "marici.dpc-core-normalizer-result.v1",
        "passed": all(item["passed"] for item in results),
        "rule_count": len(contract["rewrite_rules"]),
        "critical_pair_count": len(results),
        "critical_pairs": results,
        "normal_form_digests": {item["id"]: digest(item["left"]) for item in contract["critical_pairs"]},
    }
