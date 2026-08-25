#!/usr/bin/env python3
"""Classify the hybrid controlled-inversion gate and teleport corrections."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


def x_gate(d):
    return np.roll(np.eye(d, dtype=complex), 1, axis=0)


def z_gate(d):
    return np.diag(np.exp(2j * np.pi * np.arange(d) / d))


def pauli(d, x, z):
    return np.linalg.matrix_power(x_gate(d), x) @ np.linalg.matrix_power(z_gate(d), z)


def equal_up_to_phase(left, right, tolerance=1e-9):
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tolerance


def controlled_inversion():
    unitary = np.zeros((6, 6), dtype=complex)
    for parity in range(2):
        for rotation in range(3):
            target = (-rotation) % 3 if parity else rotation
            unitary[parity * 3 + target, parity * 3 + rotation] = 1
    return unitary


def main():
    product_paulis = []
    for a, b, c, d in itertools.product(range(2), range(2), range(3), range(3)):
        product_paulis.append(
            ((a, b, c, d), np.kron(pauli(2, a, b), pauli(3, c, d)))
        )
    generators = [
        np.kron(x_gate(2), np.eye(3)),
        np.kron(z_gate(2), np.eye(3)),
        np.kron(np.eye(2), x_gate(3)),
        np.kron(np.eye(2), z_gate(3)),
    ]

    def is_product_clifford(unitary):
        return all(
            any(
                equal_up_to_phase(unitary @ generator @ unitary.conj().T, candidate)
                for _, candidate in product_paulis
            )
            for generator in generators
        )

    unitary = controlled_inversion()
    assert np.max(np.abs(unitary @ unitary - np.eye(6))) < 1e-9
    conjugated_generator_is_pauli = [
        any(equal_up_to_phase(unitary @ generator @ unitary.conj().T, p) for _, p in product_paulis)
        for generator in generators
    ]
    assert conjugated_generator_is_pauli == [False, True, False, False]
    assert not is_product_clifford(unitary)

    correction_classes = []
    for label, product_pauli in product_paulis:
        correction = unitary @ np.linalg.inv(product_pauli.conj()) @ unitary.conj().T
        correction_classes.append(
            {"bell_outcome": list(label), "correction_is_product_clifford": is_product_clifford(correction)}
        )
    clifford = [row for row in correction_classes if row["correction_is_product_clifford"]]
    nonclifford = [row for row in correction_classes if not row["correction_is_product_clifford"]]
    assert len(clifford) == 4
    assert len(nonclifford) == 32

    result = {
        "schema": "marici.kitaev.s3-controlled-inversion-magic-obstruction.v1",
        "hybrid_system": "qubit tensor qutrit",
        "unitary": "|e,k> maps to |e,(-1)^e k>",
        "involution": True,
        "pauli_generator_conjugates_are_product_pauli": conjugated_generator_is_pauli,
        "is_product_clifford": False,
        "teleportation": {
            "bell_branches": len(correction_classes),
            "clifford_feedforward_branches": len(clifford),
            "nonclifford_feedforward_branches": len(nonclifford),
            "clifford_branch_probability": "1/9",
            "deterministic_clifford_feedforward": False,
            "correction_classes": correction_classes,
        },
        "resource_theory_consequence": "stabilizer states, product-Pauli measurements, Clifford teleportation resources, and Pauli feed-forward cannot deterministically implement this unitary",
        "minimal_new_resource_type": "a verified nonstabilizer controlled-inversion injection state or an explicit code switch to a gate set containing an equivalent hybrid non-Clifford operation",
        "verdict": "Full S3 multiplication is not executable in the frozen stabilizer resource theory. Its controlled-inversion factor is non-Clifford, and naive Choi teleportation has non-Clifford feed-forward in 32 of 36 branches. A verified magic resource or code switch is necessary.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-controlled-inversion-magic-obstruction.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
