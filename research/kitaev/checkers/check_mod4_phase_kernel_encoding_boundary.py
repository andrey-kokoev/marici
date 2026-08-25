#!/usr/bin/env python3
"""Classify K_rs=i^(rs) under native-ququart and binary pointer lenses."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
KDIR = ROOT / "research" / "kitaev"
OUT = KDIR / "results" / "mod4-phase-kernel-encoding-boundary.json"


def shift(d):
    return np.roll(np.eye(d, dtype=complex), 1, axis=0)


def clock(d):
    return np.diag(np.exp(2j * np.pi * np.arange(d) / d))


def equal_up_to_phase(left, right, tolerance=1e-9):
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tolerance


def normalizes(unitary, generators, paulis):
    return all(
        any(equal_up_to_phase(unitary @ generator @ unitary.conj().T, candidate)
            for candidate in paulis)
        for generator in generators
    )


def main() -> None:
    phases = np.array([1j ** ((r * s) % 4) for r in range(4) for s in range(4)])
    kernel = np.diag(phases)

    x4, z4, i4 = shift(4), clock(4), np.eye(4, dtype=complex)
    ququart_paulis = [
        np.kron(np.linalg.matrix_power(x4, a) @ np.linalg.matrix_power(z4, b),
                np.linalg.matrix_power(x4, c) @ np.linalg.matrix_power(z4, d))
        for a, b, c, d in itertools.product(range(4), repeat=4)
    ]
    ququart_generators = [np.kron(x4, i4), np.kron(z4, i4),
                          np.kron(i4, x4), np.kron(i4, z4)]
    native_ququart_clifford = normalizes(kernel, ququart_generators, ququart_paulis)
    assert native_ququart_clifford

    x2 = np.array([[0, 1], [1, 0]], dtype=complex)
    z2 = np.diag([1, -1]).astype(complex)
    i2 = np.eye(2, dtype=complex)
    binary_paulis = []
    for bits in itertools.product(range(2), repeat=8):
        operator = np.array([[1]], dtype=complex)
        for q in range(4):
            operator = np.kron(operator,
                               np.linalg.matrix_power(x2, bits[2 * q])
                               @ np.linalg.matrix_power(z2, bits[2 * q + 1]))
        binary_paulis.append(operator)
    binary_generators = []
    for q in range(4):
        for gate in (x2, z2):
            operator = np.array([[1]], dtype=complex)
            for j in range(4):
                operator = np.kron(operator, gate if j == q else i2)
            binary_generators.append(operator)
    binary_clifford = normalizes(kernel, binary_generators, binary_paulis)
    assert not binary_clifford

    def additive_order(vector, modulus):
        return next(k for k in range(1, modulus + 1)
                    if all((k * coordinate) % modulus == 0 for coordinate in vector))

    ququart_projective_orders = [
        additive_order(vector, 4) for vector in itertools.product(range(4), repeat=2)
    ]
    two_qubit_projective_orders = [
        additive_order(vector, 2) for vector in itertools.product(range(2), repeat=4)
    ]
    ququart_order_census = {str(k): ququart_projective_orders.count(k) for k in sorted(set(ququart_projective_orders))}
    binary_order_census = {str(k): two_qubit_projective_orders.count(k) for k in sorted(set(two_qubit_projective_orders))}
    assert ququart_order_census == {"1": 1, "2": 3, "4": 12}
    assert binary_order_census == {"1": 1, "2": 15}
    assert ququart_order_census != binary_order_census

    # Binary order |a,b,c,d> represents r=2a+b and s=2c+d in the matrix
    # enumeration. Then rs = b*d + 2*(a*d+b*c) mod 4.
    reconstructed = []
    for a, b, c, d in itertools.product(range(2), repeat=4):
        exponent = (b * d + 2 * (a * d + b * c)) % 4
        reconstructed.append(1j ** exponent)
    assert np.max(np.abs(np.array(reconstructed) - phases)) < 1e-9

    result = {
        "schema": "marici.kitaev.mod4-phase-kernel-encoding-boundary.v1",
        "kernel": "K|r,s>=i^(r*s)|r,s>",
        "operator_schmidt_rank": 4,
        "native_ququart_lens": {
            "pauli": "X4,Z4 on each pointer",
            "is_clifford": native_ququart_clifford,
            "constructor": "one generalized ququart controlled-Z",
        },
        "binary_two_qubits_per_pointer_lens": {
            "is_four_qubit_clifford": binary_clifford,
            "bit_convention": "r=2a+b, s=2c+d",
            "exact_decomposition": "CS(b,d) * CZ(a,d) * CZ(b,c)",
            "nonclifford_component": "controlled-S on the low bits b,d",
            "nonclifford_gate_count_in_clifford_plus_CS_library": 1,
            "optimality": "upper bound from exact CS*CZ*CZ decomposition; lower bound from non-Clifford Pauli-normalizer failure",
        },
        "pauli_lens_no_isomorphism": {
            "native_ququart_projective_label_group": "Z4 x Z4",
            "native_ququart_element_order_census": ququart_order_census,
            "two_qubit_projective_label_group": "Z2^4",
            "two_qubit_element_order_census": binary_order_census,
            "pauli_preserving_relabelling_exists": False,
            "reason": "the ququart label group has twelve order-four elements while the two-qubit label group has none",
        },
        "source_consequence": {
            "shared_constructor_count": 1,
            "if_native_ququart_stabilizer_hardware": "interaction kernel is Clifford",
            "in_frozen_binary_stabilizer_architecture": "requires the already-missing controlled-S-type resource",
            "new_magic_species_beyond_existing_D_S3_frontier": 0,
            "factory_reuse": "the controlled-S-type factory already required by the controlled-power-two record phase can serve this kernel",
            "does_not_supply": "coherent Wilson residue extraction into either pointer",
        },
        "verdict": "The cross-factor residue interaction is not intrinsically magic. It is one Clifford controlled-Z in the native mod-4 ququart coefficient lens, but becomes exactly one CS plus two CZ gates in the frozen binary pointer encoding. One non-Clifford gate is optimal, and its controlled-S species is already missing elsewhere in the D(S3) architecture, so this interaction adds no new magic species. The two Pauli lenses are not related by a Pauli-preserving relabelling; a ququart switch remains a genuine architectural transition.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
