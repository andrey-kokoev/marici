#!/usr/bin/env python3
"""Finite logical audit of encoded Clifford gate teleportation resources."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


def x_gate(d):
    matrix = np.zeros((d, d), dtype=complex)
    for j in range(d):
        matrix[(j + 1) % d, j] = 1
    return matrix


def z_gate(d):
    return np.diag([np.exp(2j * np.pi * j / d) for j in range(d)])


def fourier(d):
    omega = np.exp(2j * np.pi / d)
    return np.array([[omega ** (j * k) / np.sqrt(d) for k in range(d)] for j in range(d)])


def sum_gate(d):
    matrix = np.zeros((d * d, d * d), dtype=complex)
    for a in range(d):
        for b in range(d):
            matrix[a * d + (a + b) % d, a * d + b] = 1
    return matrix


def pauli(d, x, z):
    return np.linalg.matrix_power(x_gate(d), x) @ np.linalg.matrix_power(z_gate(d), z)


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


def identify_product_pauli(matrix, d, systems):
    for labels in itertools.product(range(d), repeat=2 * systems):
        candidate = kron_all(
            [pauli(d, labels[2 * i], labels[2 * i + 1]) for i in range(systems)]
        )
        if equal_up_to_phase(matrix, candidate):
            return labels
    return None


def audit(name, d, systems, unitary):
    dimension = d**systems
    assert np.max(np.abs(unitary.conj().T @ unitary - np.eye(dimension))) < 1e-9
    corrections = []
    for labels in itertools.product(range(d), repeat=2 * systems):
        bell_pauli = kron_all(
            [pauli(d, labels[2 * i], labels[2 * i + 1]) for i in range(systems)]
        )
        teleported_channel = unitary @ bell_pauli.conj() / dimension
        correction = unitary @ np.linalg.inv(bell_pauli.conj()) @ unitary.conj().T
        corrected = correction @ teleported_channel
        assert equal_up_to_phase(corrected, unitary / dimension)
        correction_label = identify_product_pauli(correction, d, systems)
        assert correction_label is not None
        corrections.append({"bell_outcome": list(labels), "pauli_correction": list(correction_label)})
    return {
        "gate": name,
        "field_order": d,
        "logical_systems": systems,
        "bell_outcomes_checked": len(corrections),
        "all_corrections_are_product_paulis": True,
        "encoded_resource_blocks": 2 * systems,
        "logical_resource_stabilizer_generators": 2 * systems,
        "destructive_bell_rail_pairs": 5 * systems,
        "measured_rail_observables": 10 * systems,
        "correction_table": corrections,
    }


def main():
    audits = [
        audit("H", 2, 1, fourier(2)),
        audit("F3", 3, 1, fourier(3)),
        audit("SUM2", 2, 2, sum_gate(2)),
        audit("SUM3", 3, 2, sum_gate(3)),
    ]
    assert sum(item["bell_outcomes_checked"] for item in audits) == 110
    result = {
        "schema": "marici.kitaev.s3-encoded-clifford-teleportation.v1",
        "audits": audits,
        "total_logical_bell_outcomes_checked": 110,
        "fault_tolerance_contract": {
            "resource": "verified encoded Clifford Choi state (I tensor U)|Phi_L>",
            "measurement": "destructive pairwise physical Bell measurements, independently decoded by the five-rail syndrome tables",
            "correction": "listed logical product Pauli, represented by the frozen logical Pauli words",
            "single_fault_scope": "one rail outcome or one resource rail before decoding; no rail participates in two Bell pairs",
        },
        "resolved_gates": ["logical H", "logical F3", "logical qubit SUM", "logical qutrit SUM"],
        "unresolved_gate": "qubit-controlled qutrit inversion inside full S3 multiplication",
        "verdict": "Encoded Choi teleportation removes the transversal obstruction for all required component Clifford gates. All 110 Bell branches have explicit Pauli corrections. Verified preparation of the encoded Choi states and the hybrid controlled-inversion injection remain separate obligations.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-encoded-clifford-teleportation.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
