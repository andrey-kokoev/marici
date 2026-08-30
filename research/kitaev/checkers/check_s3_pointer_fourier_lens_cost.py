#!/usr/bin/env python3
"""Exact F4 cost and pointer lens/block decomposition separation."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SHARING = K / "results" / "s3-cross-port-conjunction-sharing.json"
CS_FACTORY = K / "results" / "controlled-s-from-t-factory.json"
ENCODING = K / "results" / "mod4-phase-kernel-encoding-boundary.json"
OUT = K / "results" / "s3-pointer-fourier-lens-cost.json"


def equal_phase(left: np.ndarray, right: np.ndarray, tol: float = 1e-12) -> bool:
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tol:
        return False
    phase = overlap / abs(overlap)
    return np.max(np.abs(left - phase * right)) < tol


def paulis(qubits: int) -> list[np.ndarray]:
    x = np.array([[0, 1], [1, 0]], complex)
    z = np.diag([1, -1]).astype(complex)
    result = []
    for bits in itertools.product(range(2), repeat=2 * qubits):
        op = np.array([[1]], complex)
        for q in range(qubits):
            op = np.kron(op, np.linalg.matrix_power(x, bits[2*q]) @ np.linalg.matrix_power(z, bits[2*q+1]))
        result.append(op)
    return result


def is_binary_clifford(unitary: np.ndarray) -> bool:
    x = np.array([[0, 1], [1, 0]], complex)
    z = np.diag([1, -1]).astype(complex)
    identity = np.eye(2)
    candidates = paulis(2)
    generators = [np.kron(x, identity), np.kron(z, identity),
                  np.kron(identity, x), np.kron(identity, z)]
    return all(any(equal_phase(unitary @ generator @ unitary.conj().T, candidate)
                   for candidate in candidates) for generator in generators)


def main() -> None:
    omega = 1j
    f4 = np.array([[omega ** (j * k) for k in range(4)] for j in range(4)], complex) / 2
    h = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
    h0, h1 = np.kron(h, np.eye(2)), np.kron(np.eye(2), h)
    cs = np.diag([1, 1, 1, 1j]).astype(complex)
    swap = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], complex)
    circuit = swap @ h1 @ cs @ h0
    residual = float(np.max(np.abs(circuit - f4)))
    assert residual < 1e-12
    assert not is_binary_clifford(f4)

    x4 = np.roll(np.eye(4, dtype=complex), 1, axis=0)
    z4 = np.diag([omega ** j for j in range(4)])
    native_residuals = {
        "F4_X4_F4dagger_vs_Z4": float(np.max(np.abs(f4 @ x4 @ f4.conj().T - z4))),
        "F4_Z4_F4dagger_vs_X4inverse": float(np.max(np.abs(f4 @ z4 @ f4.conj().T - np.linalg.matrix_power(x4, 3)))),
    }
    assert max(native_residuals.values()) < 1e-12

    sharing = json.loads(SHARING.read_text(encoding="utf-8"))
    cs_factory = json.loads(CS_FACTORY.read_text(encoding="utf-8"))
    encoding = json.loads(ENCODING.read_text(encoding="utf-8"))
    assert cs_factory["resources"]["T_or_T_dagger_injections"] == 3
    assert encoding["pauli_lens_no_isomorphism"]["pauli_preserving_relabelling_exists"] is False
    cdfg = sharing["families"]["CDFG"]["T_count_upper_bound"]
    binary_fourier_cs = 4 * 2  # four pointers, inverse extraction and forward unextraction
    result = {
        "schema": "marici.kitaev.s3-pointer-fourier-lens-cost.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SHARING, CS_FACTORY, ENCODING)
        },
        "exact_F4_decomposition": "F4 = SWAP (I tensor H) CS (H tensor I)",
        "matrix_max_residual": residual,
        "binary_lens": {
            "F4_is_binary_Clifford": False,
            "CS_invocations_per_F4": 1,
            "F4_per_pointer_full_extract_lookup_unextract_cycle": 2,
            "pointers": 4,
            "total_CS_invocations": binary_fourier_cs,
            "T_upper_bound_from_three_T_CS_factory": 3 * binary_fourier_cs,
            "CDFG_upper_bound_including_pointer_Fouriers": cdfg + 3 * binary_fourier_cs,
        },
        "native_ququart_lens": {
            "F4_is_ququart_Clifford": True,
            "normalizer_residuals": native_residuals,
            "binary_193T_compiler_transports_unchanged": False,
            "reason": "the native ququart and two-qubit Pauli label groups are not Pauli-preservingly isomorphic; controlled-phase primitives must be recompiled in the native lens",
        },
        "independent_axes": {
            "correction_block_decomposition": ["one monolithic block", "two independently protected component blocks"],
            "coefficient_Pauli_lens": ["binary two-qubit", "native ququart"],
            "rule": "block decomposition does not determine the Pauli lens and the two costs may not be mixed without an explicit transport compiler",
        },
        "verdict": "In the binary pointer lens the full coherent CDFG cycle adds exactly eight CS invocations, giving a 24T upper-bound increment and 217T total ideal bound. F4 is Clifford in the native ququart lens, but the binary 193T controlled-phase compiler cannot be imported unchanged. Pointer block typing and coefficient lens are independent architectural choices.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
