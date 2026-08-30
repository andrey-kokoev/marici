#!/usr/bin/env python3
"""Exact controlled-S magic-state injection and feed-forward classification."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "controlled-s-magic-injection.json"


X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
I2 = np.eye(2, dtype=complex)


def equal_up_to_phase(left, right, tolerance=1e-9):
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tolerance


def main() -> None:
    paulis = []
    for bits in itertools.product(range(2), repeat=4):
        paulis.append((bits, np.kron(np.linalg.matrix_power(X, bits[0]) @ np.linalg.matrix_power(Z, bits[1]),
                                    np.linalg.matrix_power(X, bits[2]) @ np.linalg.matrix_power(Z, bits[3]))))
    generators = [np.kron(X, I2), np.kron(Z, I2), np.kron(I2, X), np.kron(I2, Z)]

    def is_pauli(operator):
        return any(equal_up_to_phase(operator, candidate) for _, candidate in paulis)

    def is_clifford(operator):
        return all(is_pauli(operator @ generator @ operator.conj().T) for generator in generators)

    cs = np.diag([1, 1, 1, 1j]).astype(complex)
    assert not is_clifford(cs)
    corrections = []
    for outcome, pauli in paulis:
        correction = cs @ pauli @ cs.conj().T
        corrections.append({
            "bell_outcome": list(outcome),
            "correction_is_pauli": is_pauli(correction),
            "correction_is_clifford": is_clifford(correction),
        })
    assert all(row["correction_is_clifford"] for row in corrections)
    pauli_count = int(sum(row["correction_is_pauli"] for row in corrections))
    assert pauli_count == 4

    plus_plus = np.ones(4, dtype=complex) / 2
    magic_state = cs @ plus_plus
    pauli_expectations = [
        (bits, np.vdot(magic_state, pauli @ magic_state)) for bits, pauli in paulis
    ]
    unit_expectation_count = int(sum(abs(abs(value) - 1) < 1e-9 for _, value in pauli_expectations))
    # A pure two-qubit stabilizer state has four unit Pauli expectations,
    # including identity. This state has only identity.
    assert unit_expectation_count == 1

    result = {
        "schema": "marici.kitaev.controlled-s-magic-injection.v1",
        "gate": "CS=diag(1,1,1,i)",
        "gate_is_clifford": False,
        "resource_state": {
            "state": "CS|++>=(|00>+|01>+|10>+i|11>)/2",
            "unit_magnitude_pauli_expectations_including_identity": unit_expectation_count,
            "is_stabilizer_state": False,
        },
        "teleportation": {
            "bell_branches": len(corrections),
            "pauli_correction_branches": pauli_count,
            "nonpauli_clifford_correction_branches": len(corrections) - pauli_count,
            "nonclifford_correction_branches": 0,
            "deterministic_with_clifford_feedforward": True,
            "corrections": corrections,
        },
        "shared_factory_contract": {
            "consumed_resource_per_kernel_invocation": "one verified encoded CS|++> state",
            "online_nonclifford_gates_after_resource_preparation": 0,
            "online_requirements": "two logical Bell measurements plus branch-dependent two-qubit Clifford correction",
            "consumers": ["mod-four product residue kernel", "D(S3) controlled-power-two record phase"],
            "still_missing": "a source-derived verified encoded CS|++> preparation/distillation factory and its fault-tolerant exRec",
        },
        "verdict": "Controlled-S consumption is executable conditionally from one verified nonstabilizer CS|++> resource: all 16 teleportation branches have Clifford corrections, four Pauli and twelve non-Pauli Clifford. The online gadget introduces no further magic species. Physical executability remains blocked solely at verified resource-state production and encoded scheduling.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
