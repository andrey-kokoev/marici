#!/usr/bin/env python3
"""Pointer-block typing audit for shared CDFG predicate faults."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-cross-port-conjunction-sharing.json"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
OUT = K / "results" / "s3-shared-predicate-pointer-typing.json"


def multiplicities(uses: list[dict], split_power_components: bool) -> dict:
    keys = [f"{item['port']}:power{item['power']}" if split_power_components else item["port"]
            for item in uses]
    counts = Counter(keys)
    return {"contact_multiplicity_by_encoded_pointer_block": dict(sorted(counts.items())),
            "maximum_multiplicity": max(counts.values(), default=0),
            "one_persistent_fault_can_exceed_one_error_per_pointer_block": any(v > 1 for v in counts.values())}


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    pointer_text = kickback["exact_modular_phase_estimation"]["pointer"]
    assert pointer_text == "one four-level coherent pointer per Wilson observable"
    uses = source["families"]["CDFG"]["uses_by_shared_data_predicate"]
    models = {}
    for model, split in (("monolithic_encoded_ququart_per_port", False),
                         ("two_independently_protected_binary_components_per_port", True)):
        predicates = {predicate: multiplicities(items, split) for predicate, items in uses.items()}
        models[model] = {
            "predicates": predicates,
            "one_fault_output_contract_preserved_by_contact_multiplicity_alone":
                not any(item["one_persistent_fault_can_exceed_one_error_per_pointer_block"]
                        for item in predicates.values()),
        }
    mono = models["monolithic_encoded_ququart_per_port"]
    split = models["two_independently_protected_binary_components_per_port"]
    assert mono["predicates"]["111"]["contact_multiplicity_by_encoded_pointer_block"] == {"C": 2, "F": 2, "G": 2}
    assert mono["one_fault_output_contract_preserved_by_contact_multiplicity_alone"] is False
    assert split["one_fault_output_contract_preserved_by_contact_multiplicity_alone"] is True
    result = {
        "schema": "marici.kitaev.s3-shared-predicate-pointer-typing.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SOURCE, KICKBACK)
        },
        "frozen_pointer_statement": pointer_text,
        "models": models,
        "monolithic_repair": {
            "minimum_power_layer_boundary_for_predicate_111": 1,
            "required_action": "hygiene or discard-and-recompute the 111 predicate workspace between controlled-power layers",
            "ideal_shared_episode_count_no_longer_fault_safe": 4,
            "recomputed_conjunction_episode_upper_bound": 6,
            "derivation": "011 base and 111 extension are each instantiated once in the power-1 layer and again in the power-2 layer; 101 and 110 remain power-1 only",
        },
        "typing_blocker": "The phrase 'one four-level coherent pointer' does not state whether fault correction treats the two phase-estimation controls as one encoded block or two independently protected component blocks.",
        "scope_boundary": "This checker audits pointer contact multiplicity only. Compute/uncompute propagation into sector data and microscopic controlled-phase faults remain outside the model.",
        "verdict": "The fault-safe status of ideal four-episode cross-port sharing depends on an unresolved pointer-block decomposition. It fails contact multiplicity for a monolithic ququart but survives that particular test for two independently protected binary components. No unconditional fault-tolerant sharing theorem follows until the encoding is frozen.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
