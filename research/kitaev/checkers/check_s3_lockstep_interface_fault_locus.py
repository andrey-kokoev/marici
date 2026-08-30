#!/usr/bin/env python3
"""Finite fault-locus separation for the four-port lockstep interface."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
LOCKSTEP = K / "results" / "s3-lockstep-interface-normal-form.json"
JOINT = K / "results" / "s3-joint-interface-selector-fault-gate.json"
OUT = K / "results" / "s3-lockstep-interface-fault-locus.json"


def weight(pattern: tuple[int, ...]) -> int:
    return sum(pattern)


def main() -> None:
    ports = ("C", "D", "F", "G")
    ideal_truth_table = {0: (0, 0, 0, 0), 1: (1, 1, 1, 1)}

    # Same ideal lockstep map, three distinct single-fault loci.
    factorized_actuator_faults = {
        tuple(int(j == port) for j in range(4)) for port in range(4)
    }
    monolithic_channel_faults = set(itertools.product((0, 1), repeat=4)) - {(0, 0, 0, 0)}
    shared_controller_faults = {(1, 1, 1, 1)}

    assert max(map(weight, factorized_actuator_faults)) == 1
    assert max(map(weight, monolithic_channel_faults)) == 4
    assert max(map(weight, shared_controller_faults)) == 4
    assert (1, 1, 1, 1) not in factorized_actuator_faults
    assert (1, 1, 1, 1) in monolithic_channel_faults
    assert (1, 1, 1, 1) in shared_controller_faults

    lockstep = json.loads(LOCKSTEP.read_text(encoding="utf-8"))
    joint = json.loads(JOINT.read_text(encoding="utf-8"))
    assert lockstep["selector_refinement"]["two_state_lockstep_contract_sufficient_for_ideal_interaction_order"] is True
    assert joint["authorized_lockstep_contract"]["single_authority_root_spans_pointer_blocks"] == 4
    result = {
        "schema": "marici.kitaev.s3-lockstep-interface-fault-locus.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (LOCKSTEP, JOINT)
        },
        "ideal_lockstep_truth_table": {str(key): "".join(map(str, value))
                                        for key, value in ideal_truth_table.items()},
        "fault_models": {
            "four_factorized_quantum_actuators": {
                "single_fault_patterns": ["".join(map(str, p)) for p in sorted(factorized_actuator_faults)],
                "maximum_pointer_block_support": 1,
                "block_local_quantum_fault_containment_passes": True,
                "shared_controller_fault_included": False,
            },
            "one_monolithic_four_block_channel": {
                "single_fault_pattern_count": len(monolithic_channel_faults),
                "maximum_pointer_block_support": 4,
                "contains_1111": True,
                "block_local_quantum_fault_containment_passes": False,
            },
            "factorized_actuators_with_one_shared_controller": {
                "shared_controller_fault_patterns": ["1111"],
                "maximum_pointer_block_support": 4,
                "quantum_actuator_locality_alone_proves_global_one_fault_contract": False,
                "required_repair": "harden, duplicate-and-compare, or make controller faults detectable/benign",
            },
        },
        "typing_consequence": {
            "ideal_lockstep_unitary_determines_fault_locus": False,
            "shared_schedule_implies_monolithic_quantum_channel": False,
            "factorized_quantum_switches_imply_independent_total_fault_domains": False,
            "required_fields": [
                "quantum actuator decomposition",
                "controller authority roots",
                "controller-to-actuator fanout",
                "fault detection and recovery boundary",
            ],
        },
        "verdict": "The ideal lockstep truth table does not determine fault locality. Four synchronized but factorized quantum actuators limit an actuator fault to one pointer block, whereas a monolithic quantum channel permits four-block support. Yet even factorized actuators inherit a four-block common-cause mode from an unhardened shared controller. The compiler must type controller and quantum-channel loci separately.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
