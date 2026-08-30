#!/usr/bin/env python3
"""Joint selector and fault-domain gate for four CDFG pointer interfaces."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
NIMA = ROOT / "research" / "nima" / "joint-selector-correlation-and-orbit-product-gate.md"
INTERFACE = K / "results" / "s3-hybrid-z4-binary-interface.json"
POINTER = K / "results" / "s3-shared-predicate-pointer-typing.json"
OUT = K / "results" / "s3-joint-interface-selector-fault-gate.json"


def main() -> None:
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    pointer = json.loads(POINTER.read_text(encoding="utf-8"))
    ports = ("C", "D", "F", "G")
    configurations = set(itertools.product((0, 1), repeat=len(ports)))
    shared_image = {(0, 0, 0, 0), (1, 1, 1, 1)}
    missing = sorted(configurations - shared_image)
    marginals = [{state[j] for state in shared_image} for j in range(len(ports))]
    assert all(marginal == {0, 1} for marginal in marginals)
    assert len(configurations) == 16 and len(shared_image) == 2 and len(missing) == 14
    independent_bits = math.ceil(math.log2(len(configurations)))
    lockstep_bits = math.ceil(math.log2(len(shared_image)))
    assert independent_bits == 4 and lockstep_bits == 1

    budget = interface["conditional_CDFG_accounting"][
        "available_total_lens_switch_budget_for_strict_improvement"
    ]
    assert budget == 83
    assert pointer["frozen_pointer_statement"] == "one four-level coherent pointer per Wilson observable"
    result = {
        "schema": "marici.kitaev.s3-joint-interface-selector-fault-gate.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (NIMA, INTERFACE, POINTER)
        },
        "ports": list(ports),
        "independent_interface_contract": {
            "required_joint_configurations": len(configurations),
            "minimum_selector_bits": independent_bits,
            "one_shared_bit_marginals_complete": True,
            "one_shared_bit_joint_image_size": len(shared_image),
            "missing_joint_configurations": ["".join(map(str, state)) for state in missing],
            "missing_count": len(missing),
            "verdict": "joint_selector_correlation_deficit",
        },
        "authorized_lockstep_contract": {
            "admissible_configurations": ["0000", "1111"],
            "minimum_selector_bits": lockstep_bits,
            "selector_sufficient": True,
            "single_authority_root_spans_pointer_blocks": len(ports),
            "independent_pointer_fault_domains_certified": False,
            "required_additional_typing": [
                "source-authorized lockstep coherence law",
                "common-cause fault set",
                "epoch and replay identity",
                "one-fault output contract across all four pointer blocks",
            ],
        },
        "resource_boundary": {
            "previous_total_interface_budget_for_strict_improvement_T_equivalent": budget,
            "marginal_interface_costs_may_be_summed_without_joint_constructor": False,
            "reason": "shared selection can change both reachable joint configurations and common-cause fault structure",
            "numerical_joint_switch_cost_derived": False,
        },
        "verdict": "Four marginally complete pointer interfaces do not compose automatically. Independent per-port switching needs a 16-state joint image and at least four selector bits; one shared bit reaches only the two lockstep configurations and misses fourteen. Lockstep can instead be authorized, but then its single selector is a common-cause root spanning all four pointers. Hence the conditional <83T interface budget is not yet a compositional executable bound.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
