#!/usr/bin/env python3
"""Persistent-fault audit for reusable Wilson compiler work ancillas."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-wilson-phase-native-compression.json"
CONTRACT = K / "contracts" / "d-s3-resource-relative-capability.v2.json"
OUT = K / "results" / "s3-wilson-work-ancilla-hygiene.json"


def support(mask: int) -> set[int]:
    return {bit for bit in range(4) if mask & (1 << bit)}


def audit_target(record: dict) -> dict:
    work_terms = [term for term in record["terms"] if term["clean_ancillas"] > 0]
    supports = [support(term["mask"]) for term in work_terms]
    overlap_table = []
    for left, right in itertools.combinations(range(len(supports)), 2):
        overlap = sorted(supports[left] & supports[right])
        overlap_table.append({"left": left, "right": right, "overlap_blocks": overlap})

    # For serial reuse in the frozen order, a segment without a hygiene
    # barrier is safe only if no encoded block is revisited by the persistent
    # work fault. Dynamic programming finds the minimum barriers.
    count = len(supports)
    best = [10**9] * (count + 1)
    best[0] = 0
    for end in range(1, count + 1):
        seen: set[int] = set()
        for start in range(end - 1, -1, -1):
            if seen & supports[start]:
                break
            seen |= supports[start]
            barriers = best[start] + (0 if start == 0 else 1)
            best[end] = min(best[end], barriers)
    minimum = best[count] if count else 0
    no_barrier_multiplicity = {
        str(block): sum(block in term_support for term_support in supports)
        for block in range(4)
    }
    max_multiplicity = max(no_barrier_multiplicity.values(), default=0)
    return {
        "work_using_monomial_gadgets": count,
        "supports_by_gadget": [sorted(item) for item in supports],
        "pairwise_overlap_table": overlap_table,
        "no_barrier_error_multiplicity_by_block": no_barrier_multiplicity,
        "no_barrier_max_errors_in_one_block": max_multiplicity,
        "minimum_inter_gadget_hygiene_barriers": minimum,
        "barrier_action": "recover, verify-clean, or discard-and-replace every reusable work block before its next overlapping gadget",
        "final_recovery_required_for_one_error_output_contract": False,
        "final_recovery_note": "one last-gadget fault may leave one rail error per incident block, which is allowed by the frozen output contract",
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    future = next(item for item in contract["capabilities"]
                  if item["id"] == "complete_compiler_future_magic")
    preserved = future["status"]["preserved_contract"]
    assert preserved["id"] == "one_fault_output_contract" and preserved["preserved"]
    controlled = {label: audit_target(record) for label, record in source["controlled"].items()}
    logical = {label: audit_target(record) for label, record in source["logical"].items()}

    # Every controlled work gadget contains control block 3. Hence every pair
    # overlaps and serial reuse needs a barrier after each nonfinal gadget.
    for record in controlled.values():
        count = record["work_using_monomial_gadgets"]
        assert all(3 in item for item in record["supports_by_gadget"])
        assert record["minimum_inter_gadget_hygiene_barriers"] == max(0, count - 1)
        if count > 1:
            assert record["no_barrier_max_errors_in_one_block"] > 1

    result = {
        "schema": "marici.kitaev.s3-wilson-work-ancilla-hygiene.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SOURCE, CONTRACT)
        },
        "fault_model": {
            "fault": "one persistent rail fault in a reusable encoded work block",
            "contact_effect": "adds at most one rail error to each incident encoded data block per gadget",
            "failure_condition": "the same data block receives two propagated rail errors before work-block hygiene",
            "scope": "support automaton only; no stochastic rate or microscopic exRec claim",
        },
        "logical": logical,
        "controlled": controlled,
        "verdict": "Serial work-ancilla reuse is conditionally compatible with the frozen one-fault output contract only when a recover/verify-or-replace hygiene barrier separates every pair of overlapping work-using gadgets. All controlled work gadgets overlap on the control block, so each controlled target needs exactly k-1 inter-gadget barriers for k work gadgets. Parallel fresh work blocks avoid reuse propagation but do not remove their own verification obligation.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
