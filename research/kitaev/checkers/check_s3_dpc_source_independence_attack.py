#!/usr/bin/env python3
"""Hostile audit: is the proposed DPC source independent of its target gates?"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s3-dpc-source-independence-attack.json"
NATIVE = K / "results" / "s3-local-source-model.json"
TOL = 1e-10


def exp_projector(projector, angle):
    return np.eye(projector.shape[0], dtype=complex) + (np.exp(-1j * angle) - 1) * projector


def main():
    n = np.diag([0, 1]).astype(complex)
    minus = np.array([0, 1, -1], dtype=complex) / np.sqrt(2)
    exchange = np.outer(minus, minus.conj())
    h_ex = np.kron(n, exchange)
    u_inv = exp_projector(h_ex, np.pi)

    # For a Hermitian involution U, the proposed generator is exactly the
    # target-derived spectral projector (I-U)/2.
    reconstructed_h_ex = (np.eye(6) - u_inv) / 2
    exchange_is_target_logarithm = bool(np.max(np.abs(h_ex - reconstructed_h_ex)) < TOL)
    assert exchange_is_target_logarithm

    p_ccz = np.zeros((8, 8), dtype=complex)
    p_ccz[-1, -1] = 1
    ccz = exp_projector(p_ccz, np.pi)
    ccz_generator_is_target_logarithm = bool(
        np.max(np.abs(p_ccz - (np.eye(8) - ccz) / 2)) < TOL
    )
    assert ccz_generator_is_target_logarithm

    # The controlled-phase occupation projector is likewise reconstructed
    # from the desired gate once its fitted angle is supplied.
    p2 = np.kron(n, n)
    angle = np.pi / 4
    controlled_t = exp_projector(p2, angle)
    reconstructed_p2 = (controlled_t - np.eye(4)) / (np.exp(-1j * angle) - 1)
    phase_generator_is_target_spectral_projector = bool(
        np.max(np.abs(p2 - reconstructed_p2)) < TOL
    )
    assert phase_generator_is_target_spectral_projector

    # Countably many inequivalent Hermitian generators have the same endpoint
    # unitary, so endpoint agreement does not select source dynamics.
    exchange_logarithms = []
    phase_logarithms = []
    for winding in range(-3, 4):
        h_variant = (1 + 2 * winding) * h_ex
        phase_variant = (angle + 2 * np.pi * winding) * p2
        assert np.max(np.abs(exp_projector(h_ex, np.pi * (1 + 2 * winding)) - u_inv)) < TOL
        assert np.max(np.abs(exp_projector(p2, angle + 2 * np.pi * winding) - controlled_t)) < TOL
        exchange_logarithms.append(float(np.linalg.norm(h_variant, 2)))
        phase_logarithms.append(float(np.linalg.norm(phase_variant, 2)))
    assert len(set(round(x, 8) for x in exchange_logarithms)) > 1
    assert len(set(round(x, 8) for x in phase_logarithms)) == 7

    native = json.loads(NATIVE.read_text(encoding="utf-8"))
    native_admits_pulse_source = not native["aggregate_gates"][
        "physical_pulse_availability_remains_a_source_assumption"
    ]
    assert not native_admits_pulse_source

    attacks = {
        "hybrid_exchange_equals_target_spectral_projector": exchange_is_target_logarithm,
        "ccz_generator_equals_target_spectral_projector": ccz_generator_is_target_logarithm,
        "controlled_t_projector_reconstructed_from_target": phase_generator_is_target_spectral_projector,
        "multiple_inequivalent_exchange_logarithms_same_gate": True,
        "multiple_inequivalent_phase_logarithms_same_gate": True,
        "pulse_angles_fitted_from_desired_character": True,
        "native_d_s3_source_does_not_admit_new_pulses": not native_admits_pulse_source,
        "frozen_code_physical_lift_already_falsified": True,
    }
    assert all(attacks.values())

    result = {
        "schema": "marici.kitaev.s3-dpc-source-independence-attack.v1",
        "native_source_sha256": hashlib.sha256(NATIVE.read_bytes()).hexdigest(),
        "attacks_succeeded": attacks,
        "finite_logarithm_witnesses": {
            "winding_numbers": list(range(-3, 4)),
            "exchange_generator_norms": exchange_logarithms,
            "controlled_t_generator_norms": phase_logarithms,
            "all_endpoint_unitaries_identical": True,
        },
        "failed_explanatory_criterion": "the proposed couplings and pulse durations are reconstructed from the target gates and are not derived from the native D(S3) Hamiltonian",
        "surviving_result": "exact conditional realization theorem: if independently admitted nonlinear couplers with the fitted calibrations exist, they generate the missing logical operations",
        "retracted_result": "proper hard-to-vary explanation of why the physical D(S3) source has those couplers",
        "stronger_dpc": "A capability is explained only when the same independently constrained microscopic source law derives the resource interaction, its calibrated parameter range, the target operation, and the encoded fault-tolerant lift without fitting those data from the target gate.",
        "next_falsifier": "derive the nonlinear couplers as controlled perturbations of the native D(S3) lattice Hamiltonian, or prove that no such gauge-compatible local perturbative gadget exists",
        "verdict": "The first DPC mechanism is an exact realization but not yet a proper Deutschian explanation. Its generators are target spectral logarithms, infinitely many inequivalent generators produce the same gates, their pulse angles are fitted to the desired characters, and the native D(S3) source does not supply them. The five-rail lift also fails. The surviving conjecture demands an independently constrained microscopic derivation and encoded lift.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
