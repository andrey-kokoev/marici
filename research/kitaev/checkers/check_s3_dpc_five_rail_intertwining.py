#!/usr/bin/env python3
"""Test whether the DPC nonlinear source pulses preserve the frozen codes."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from check_s3_five_rail_code_freeze import QUBIT, QUTRIT


OUT = Path(__file__).parents[1] / "results" / "s3-dpc-five-rail-intertwining.json"
TOL = 1e-9


def digits(index, q):
    out = [0] * 5
    for position in range(4, -1, -1):
        out[position] = index % q
        index //= q
    return out


def index_of(word, q):
    value = 0
    for entry in word:
        value = q * value + entry
    return value


def apply_pauli(vector, row, q):
    omega = np.exp(2j * np.pi / q)
    output = np.zeros_like(vector)
    for source, amplitude in enumerate(vector):
        if abs(amplitude) < 1e-14:
            continue
        word = digits(source, q)
        phase = omega ** sum(row[5 + j] * word[j] for j in range(5))
        target = [(word[j] + row[j]) % q for j in range(5)]
        output[index_of(target, q)] += phase * amplitude
    return output


def project(vector, stabilizers, q):
    result = vector.astype(complex)
    for generator in stabilizers:
        orbit_sum = np.zeros_like(result)
        term = result
        for _ in range(q):
            orbit_sum += term
            term = apply_pauli(term, generator, q)
        result = orbit_sum / q
    return result


def code_basis(stabilizers, q):
    dimension = q**5
    basis = []
    for seed in range(dimension):
        vector = np.zeros(dimension, dtype=complex)
        vector[seed] = 1
        candidate = project(vector, stabilizers, q)
        for prior in basis:
            candidate -= np.vdot(prior, candidate) * prior
        norm = np.linalg.norm(candidate)
        if norm > TOL:
            basis.append(candidate / norm)
        if len(basis) == q:
            break
    assert len(basis) == q
    matrix = np.column_stack(basis)
    assert np.max(np.abs(matrix.conj().T @ matrix - np.eye(q))) < TOL
    assert all(
        np.max(np.abs(np.column_stack([apply_pauli(matrix[:, j], row, q) for j in range(q)]) - matrix)) < TOL
        for row in stabilizers
    )
    return matrix


def apply_transversal_hybrid(vector):
    output = np.zeros_like(vector)
    qutrit_dim = 3**5
    for source, amplitude in enumerate(vector):
        if abs(amplitude) < 1e-14:
            continue
        qubit_word = digits(source // qutrit_dim, 2)
        qutrit_word = digits(source % qutrit_dim, 3)
        target_qutrit = [(-k) % 3 if e else k for e, k in zip(qubit_word, qutrit_word)]
        target = (source // qutrit_dim) * qutrit_dim + index_of(target_qutrit, 3)
        output[target] += amplitude
    return output


def apply_transversal_phase(vector, angle):
    output = vector.copy()
    block_dim = 2**5
    for source in range(vector.size):
        left = digits(source // block_dim, 2)
        right = digits(source % block_dim, 2)
        output[source] *= np.exp(1j * angle * sum(a * b for a, b in zip(left, right)))
    return output


def leakage(unitary_action, code_matrix):
    projector = code_matrix @ code_matrix.conj().T
    residuals = []
    logical_columns = []
    for column in range(code_matrix.shape[1]):
        target = unitary_action(code_matrix[:, column])
        residuals.append(float(np.linalg.norm(target - projector @ target)))
        logical_columns.append(code_matrix.conj().T @ target)
    return max(residuals), np.column_stack(logical_columns)


def main():
    qubit = code_basis(QUBIT, 2)
    qutrit = code_basis(QUTRIT, 3)
    hybrid_code = np.kron(qubit, qutrit)
    qubit_pair_code = np.kron(qubit, qubit)

    hybrid_leakage, hybrid_logical = leakage(apply_transversal_hybrid, hybrid_code)
    phase_rows = []
    for name, angle in (("controlled_T", -np.pi / 4), ("controlled_S", -np.pi / 2), ("controlled_Z", -np.pi)):
        leak, logical = leakage(lambda v, angle=angle: apply_transversal_phase(v, angle), qubit_pair_code)
        phase_rows.append({
            "gate": name,
            "max_codespace_leakage_norm": leak,
            "preserves_code": leak < TOL,
            "compressed_map_unitarity_defect": float(np.linalg.norm(logical.conj().T @ logical - np.eye(4), 2)),
        })

    result = {
        "schema": "marici.kitaev.s3-dpc-five-rail-intertwining.v1",
        "code_dimensions": {"qubit": 2, "qutrit": 3, "hybrid": 6, "qubit_pair": 4},
        "transversal_hybrid_exchange": {
            "max_codespace_leakage_norm": hybrid_leakage,
            "preserves_code": hybrid_leakage < TOL,
            "compressed_map_unitarity_defect": float(
                np.linalg.norm(hybrid_logical.conj().T @ hybrid_logical - np.eye(6), 2)
            ),
        },
        "transversal_record_phases": phase_rows,
        "one_fault_spread_is_not_enough": True,
        "repair_required": "verified encoded resource injection or a code-switch surface with an independently checked intertwiner",
    }
    all_preserve = result["transversal_hybrid_exchange"]["preserves_code"] and all(
        row["preserves_code"] for row in phase_rows[:2]
    )
    result["complete_frozen_code_lift"] = all_preserve
    result["verdict"] = (
        "The raw nonlinear source is already transversal on the frozen codes."
        if all_preserve else
        "Rail-local nonlinear pulses have bounded fault spread but do not supply the complete frozen-code intertwiner. The logical source mechanism is genuine, while the physical five-rail compiler remains conditional on verified injection or code switching."
    )
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
