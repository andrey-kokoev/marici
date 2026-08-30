#!/usr/bin/env python3
"""Exact minimal redundancy for a pre-actuation lockstep controller bit."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
LOCUS = K / "results" / "s3-lockstep-interface-fault-locus.json"
OUT = K / "results" / "s3-lockstep-controller-redundancy.json"


def flip(word: tuple[int, ...], positions: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(bit ^ int(j in positions) for j, bit in enumerate(word))


def main() -> None:
    detection_checks = 0
    correction_checks = 0
    for command in (0, 1):
        # One copy cannot distinguish a fault from the opposite valid command.
        one = (command,)
        assert flip(one, (0,)) == (command ^ 1,)

        two = (command, command)
        for position in range(2):
            corrupted = flip(two, (position,))
            assert corrupted[0] != corrupted[1]
            detection_checks += 1

        three = (command, command, command)
        for position in range(3):
            corrupted = flip(three, (position,))
            majority = int(sum(corrupted) >= 2)
            assert majority == command
            correction_checks += 1

        # A common-mode flip remains a valid unanimous codeword.
        assert len(set(flip(two, (0, 1)))) == 1
        assert len(set(flip(three, (0, 1, 2)))) == 1
        assert flip(three, (0, 1, 2))[0] == command ^ 1

    locus = json.loads(LOCUS.read_text(encoding="utf-8"))
    assert locus["fault_models"]["factorized_actuators_with_one_shared_controller"][
        "maximum_pointer_block_support"
    ] == 4
    result = {
        "schema": "marici.kitaev.s3-lockstep-controller-redundancy.v1",
        "inputs_sha256": {
            str(LOCUS.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(LOCUS.read_bytes()).hexdigest()
        },
        "fault_model": {
            "controller_command_is_classical_before_actuation": True,
            "at_most_one_independent_replica_bit_flip": True,
            "comparison_or_vote_completes_before_fanout": True,
        },
        "minimality": {
            "one_copy_detects_one_flip": False,
            "two_copy_equality_detects_one_flip": True,
            "two_copy_detection_checks": detection_checks,
            "three_copy_majority_corrects_one_flip": True,
            "three_copy_correction_checks": correction_checks,
            "minimum_copies_for_detection": 2,
            "minimum_copies_for_correction": 3,
        },
        "common_mode_boundary": {
            "all_replica_flip_detected_by_equality_or_majority": False,
            "independent_fault_domains_required": True,
            "quantum_actuator_faults_repaired_by_controller_redundancy": False,
        },
        "verdict": "For a classical command validated before actuator fanout and at most one independent replica flip, two controller copies are minimally sufficient for detection and three are minimally sufficient for correction. Common-mode replica faults remain invisible, and this redundancy does not repair quantum switch faults or price the interface.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
