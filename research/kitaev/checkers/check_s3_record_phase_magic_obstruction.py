#!/usr/bin/env python3
"""Classify the three record-controlled label phases on binary label rails."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


def x_gate():
    return np.array([[0, 1], [1, 0]], dtype=complex)


def z_gate():
    return np.diag([1, -1]).astype(complex)


def kron_all(matrices):
    result = np.array([[1]], dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def equal_up_to_phase(left, right, tolerance=1e-9):
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tolerance


def paulis(registers):
    one = np.eye(2)
    local = [one, x_gate(), z_gate(), x_gate() @ z_gate()]
    return [kron_all(choice) for choice in itertools.product(local, repeat=registers)]


def controlled_label_phase(power):
    diagonal = []
    for record in range(2):
        for residue in range(8):
            diagonal.append(np.exp(-1j * np.pi * power * record * residue / 4))
    return np.diag(diagonal)


def is_clifford(unitary, product_paulis, generators):
    return all(
        any(equal_up_to_phase(unitary @ generator @ unitary.conj().T, p) for p in product_paulis)
        for generator in generators
    )


def main():
    product_paulis = paulis(4)
    generators = []
    for register in range(4):
        for local in (x_gate(), z_gate()):
            factors = [np.eye(2)] * 4
            factors[register] = local
            generators.append(kron_all(factors))

    audits = []
    expected = {1: False, 2: False, 4: True}
    for power in (1, 2, 4):
        unitary = controlled_label_phase(power)
        clifford = is_clifford(unitary, product_paulis, generators)
        assert clifford == expected[power]
        factors = {
            "most_significant_label_bit": f"controlled phase exp(-i*pi*{power})",
            "middle_label_bit": f"controlled phase exp(-i*pi*{power}/2)",
            "least_significant_label_bit": f"controlled phase exp(-i*pi*{power}/4)",
        }
        audits.append(
            {
                "controlled_power": power,
                "is_four_qubit_clifford": clifford,
                "binary_phase_factorization": factors,
            }
        )

    result = {
        "schema": "marici.kitaev.s3-record-phase-magic-obstruction.v1",
        "label_encoding": "residue r = 4 b2 + 2 b1 + b0",
        "audits": audits,
        "clifford_controlled_powers": [4],
        "nonclifford_controlled_powers": [1, 2],
        "stabilizer_resource_consequence": "the U and U^2 record-label phases cannot be implemented deterministically using only encoded Clifford Choi states, Pauli measurements, and Pauli feed-forward",
        "minimal_new_resource_types": [
            "verified controlled-T-type phase resource for power 1",
            "verified controlled-S-type phase resource for power 2",
        ],
        "verdict": "Binary label encoding makes the phase inventory exact: power 4 is Clifford, while powers 1 and 2 are non-Clifford and require verified magic resources in addition to the controlled-inversion resource.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-record-phase-magic-obstruction.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
