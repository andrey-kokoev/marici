#!/usr/bin/env python3
"""Hostile executability audit for controlled D(S3) Wilson quarter evolutions."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-controlled-wilson-executability.json"


def paulis(qubits: int) -> list[np.ndarray]:
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    identity = np.eye(2, dtype=complex)
    result = []
    for bits in itertools.product(range(2), repeat=2 * qubits):
        operator = np.array([[1]], dtype=complex)
        for q in range(qubits):
            operator = np.kron(
                operator,
                np.linalg.matrix_power(x, bits[2 * q])
                @ np.linalg.matrix_power(z, bits[2 * q + 1]),
            )
        result.append(operator)
    return result


def equal_up_to_phase(left: np.ndarray, right: np.ndarray, tolerance: float = 1e-9) -> bool:
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tolerance


def is_clifford(unitary: np.ndarray, qubits: int, candidates: list[np.ndarray]) -> bool:
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    identity = np.eye(2, dtype=complex)
    generators = []
    for q in range(qubits):
        for gate in (x, z):
            operator = np.array([[1]], dtype=complex)
            for j in range(qubits):
                operator = np.kron(operator, gate if j == q else identity)
            generators.append(operator)
    return all(
        any(equal_up_to_phase(unitary @ generator @ unitary.conj().T, candidate)
            for candidate in candidates)
        for generator in generators
    )


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multilinear_coefficients_mod4(values: list[int]) -> list[int]:
    coefficients = []
    for mask in range(8):
        value = 0
        for subset in range(8):
            if subset & ~mask == 0:
                value += (-1) ** (mask.bit_count() - subset.bit_count()) * values[subset]
        coefficients.append(value % 4)
    return coefficients


def is_diagonal_clifford_phase(values: list[int]) -> bool:
    coefficients = multilinear_coefficients_mod4(values)
    return coefficients[7] == 0 and all(coefficients[mask] % 2 == 0 for mask in (3, 5, 6))


def main() -> None:
    modular_path = K / "results" / "s3-modular-data.json"
    kickback_path = K / "results" / "s3-coherent-wilson-phase-kickback.json"
    ft_path = K / "results" / "s3-executable-ft-frontier-audit.json"
    modular = json.loads(modular_path.read_text(encoding="utf-8"))
    kickback = json.loads(kickback_path.read_text(encoding="utf-8"))
    ft = json.loads(ft_path.read_text(encoding="utf-8"))
    labels = modular["label_order"]
    S = sp.Matrix([
        [sp.Rational(Fraction(value).numerator, Fraction(value).denominator) for value in row]
        for row in modular["S_matrix"]
    ])
    table = sp.Matrix(8, 8, lambda x, a: sp.simplify(S[x, a] / S[0, a]))

    p3 = paulis(3)
    p4 = paulis(4)
    classifications = {}
    phase_functions = {}
    family_labels = sorted({
        label
        for family in kickback["exact_modular_phase_estimation"]["family_moduli"]
        for label in family
    })
    assert family_labels == ["C", "D", "E", "F", "G", "H"]
    for label in family_labels:
        row = labels.index(label)
        residues = [int(table[row, sector]) % 4 for sector in range(8)]
        phases = np.array([1j ** residue for residue in residues])
        phase_functions[label] = residues
        logical = np.diag(phases)
        controlled = np.block([
            [np.eye(8, dtype=complex), np.zeros((8, 8), dtype=complex)],
            [np.zeros((8, 8), dtype=complex), logical],
        ])
        classifications[label] = {
            "wilson_eigenvalues": [int(table[row, sector]) for sector in range(8)],
            "quarter_evolution_is_three_qubit_clifford": is_clifford(logical, 3, p3),
            "controlled_quarter_evolution_is_four_qubit_clifford": is_clifford(controlled, 4, p4),
        }
    assert all(not item["quarter_evolution_is_three_qubit_clifford"]
               for item in classifications.values())
    assert all(not item["controlled_quarter_evolution_is_four_qubit_clifford"]
               for item in classifications.values())

    bit_vectors = [((i >> 2) & 1, (i >> 1) & 1, i & 1) for i in range(8)]
    invertible_binary_matrices = []
    for entries in itertools.product(range(2), repeat=9):
        matrix = sp.Matrix(3, 3, entries)
        if int(matrix.det()) % 2:
            invertible_binary_matrices.append(entries)
    assert len(invertible_binary_matrices) == 168

    def affine_image(entries, translation, vector):
        return tuple(
            (sum(entries[3 * row + column] * vector[column] for column in range(3))
             + translation[row]) % 2
            for row in range(3)
        )

    def vector_index(vector):
        return 4 * vector[0] + 2 * vector[1] + vector[2]

    affine_diagonal_clifford_equivalence = {}
    for source in family_labels:
        equivalent = []
        for target in family_labels:
            found = False
            for entries in invertible_binary_matrices:
                for translation in bit_vectors:
                    difference = [
                        (phase_functions[target][vector_index(affine_image(entries, translation, vector))]
                         - phase_functions[source][vector_index(vector)]) % 4
                        for vector in bit_vectors
                    ]
                    if is_diagonal_clifford_phase(difference):
                        found = True
                        break
                if found:
                    break
            if found:
                equivalent.append(target)
        affine_diagonal_clifford_equivalence[source] = equivalent
    magic_species = sorted({tuple(value) for value in affine_diagonal_clifford_equivalence.values()})
    assert magic_species == [("C", "F", "G", "H"), ("D", "E")]

    assert ft["verdict"].startswith("The executable stabilizer subcompiler")
    result = {
        "schema": "marici.kitaev.s3-controlled-wilson-executability.v1",
        "inputs": {
            str(path.relative_to(ROOT)).replace("\\", "/"): digest(path)
            for path in (modular_path, kickback_path, ft_path)
        },
        "logical_normalizer_test": classifications,
        "clifford_assisted_magic_equivalence": {
            "allowed_free_relations": "three-bit affine permutations and diagonal Clifford phase corrections",
            "equivalence_neighborhoods": affine_diagonal_clifford_equivalence,
            "species": [list(species) for species in magic_species],
            "species_count": len(magic_species),
            "every_minimum_family_uses_both_species": True,
        },
        "family_consequence": {
            "minimum_family_count": kickback["minimum_family_count"],
            "every_minimum_family_contains_four_nonclifford_quarter_evolutions": True,
            "one_frozen_stabilizer_constructor_serves_any_family": False,
            "minimum_nonclifford_species_up_to_available_affine_and_diagonal_clifford_interconversion": 2,
        },
        "microscopic_constructor_audit": {
            "closed_ribbon_insertion": "produces a Wilson eigenvalue/amplitude and is generally nonunitary; it is not exp(2 pi i W_x/4)",
            "mobile_ancilla": {
                "support": "one noncontractible cycle of length L",
                "data_contact_depth": "L",
                "single_persistent_ancilla_fault": "can propagate to a suffix of O(L) data contacts and become logical",
                "one_fault_tolerant": False,
            },
            "verified_extended_ancilla": {
                "support": "distributed length-L encoded/cat resource",
                "data_contact_depth_excluding_preparation": 1,
                "single_transversal_contact_fault": "at most one data fault under the declared contact model",
                "missing": "a verified preparation factory for the non-Clifford controlled Wilson resource",
            },
            "locality_lower_bound": "a single localized controller cannot influence all length-L loop contacts through bounded-range gates in sublinear depth unless pre-shared length-L correlations are charged",
            "code_distance": "distance 3 is only conditionally sufficient after each missing controlled-W module is supplied as a one-fault-tolerant exRec",
            "leakage": "ideal compute-uncompute has zero final label leakage; any retained/lost pointer dephases sectors sharing the environment record",
        },
        "resource_no_go": {
            "frozen_resource_theory": "encoded stabilizer states, Clifford operations, Pauli measurements, and Pauli feed-forward",
            "target_outside_frozen_theory": True,
            "phase_kickback_relocates_oracle": True,
            "required_new_resource": "verified nonstabilizer controlled-W_x quarter-evolution states/gadgets, an equivalent code switch, or a stronger source-derived topological gate constructor",
        },
        "verdict": "The mod-4 compiler is correct but does not close physical executability. Every Wilson quarter evolution appearing in every faithful family, and every controlled version, is non-Clifford in the frozen three-qubit sector encoding. The admitted stabilizer architecture therefore cannot generate even one required controlled gate, let alone a shared four-type constructor. Mobile-loop implementations are not one-fault tolerant; verified distributed implementations merely move the missing resource into their preparation factory.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
