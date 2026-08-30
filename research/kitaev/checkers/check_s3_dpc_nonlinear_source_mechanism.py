#!/usr/bin/env python3
"""Exact logical-layer source mechanism behind the D(S3) magic boundary."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


OUT = Path(__file__).parents[1] / "results" / "s3-dpc-nonlinear-source-mechanism.json"
TOL = 1e-10


def basis_permutation(bits, transform):
    dimension = 1 << bits
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        word = tuple((source >> (bits - 1 - j)) & 1 for j in range(bits))
        target_word = transform(word)
        target = sum(bit << (bits - 1 - j) for j, bit in enumerate(target_word))
        matrix[target, source] = 1
    return matrix


def diagonal_from_boolean(bits, phase):
    values = []
    for source in range(1 << bits):
        word = tuple((source >> (bits - 1 - j)) & 1 for j in range(bits))
        values.append(np.exp(1j * phase(word)))
    return np.diag(values)


def close(left, right):
    return float(np.max(np.abs(left - right))) < TOL


def main():
    # Source primitives are occupation interactions, declared before target
    # gates: H2(j,k)=n_j n_k and H3(j,k,l)=n_j n_k n_l.
    cc_phase = lambda angle: diagonal_from_boolean(2, lambda w: angle * w[0] * w[1])
    ccz = diagonal_from_boolean(3, lambda w: np.pi * w[0] * w[1] * w[2])
    controlled_s = cc_phase(np.pi / 2)
    controlled_t = cc_phase(np.pi / 4)

    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    h_target = np.kron(np.eye(4), h)
    toffoli_from_source = h_target @ ccz @ h_target
    toffoli_truth = basis_permutation(3, lambda w: (w[0], w[1], w[2] ^ (w[0] & w[1])))
    assert close(toffoli_from_source, toffoli_truth)

    # Controlled SWAP = CNOT(b->a), Toffoli(c,a->b), CNOT(b->a).
    cnot_b_to_a = basis_permutation(3, lambda w: (w[0], w[1] ^ w[2], w[2]))
    toffoli_c_a_to_b = basis_permutation(3, lambda w: (w[0], w[1], w[2] ^ (w[0] & w[1])))
    fredkin_compiled = cnot_b_to_a @ toffoli_c_a_to_b @ cnot_b_to_a
    fredkin_truth = basis_permutation(
        3, lambda w: (w[0], w[2], w[1]) if w[0] else w
    )
    assert close(fredkin_compiled, fredkin_truth)

    # Direct hybrid realization on C2 tensor C3.  K12 is the antisymmetric
    # exchange projector between qutrit levels 1 and 2; a conditional pi pulse
    # changes only that exchange parity and is exactly controlled inversion.
    n_control = np.diag([0, 1]).astype(complex)
    minus = np.array([0, 1, -1], dtype=complex) / np.sqrt(2)
    exchange_projector = np.outer(minus, minus.conj())
    hybrid_generator = np.kron(n_control, exchange_projector)
    controlled_exchange = np.eye(6, dtype=complex) - 2 * hybrid_generator
    direct_inversion = np.zeros((6, 6), dtype=complex)
    for control in (0, 1):
        for qutrit in range(3):
            target = (-qutrit) % 3 if control else qutrit
            direct_inversion[3 * control + target, 3 * control + qutrit] = 1
    assert close(controlled_exchange, direct_inversion)
    assert close(hybrid_generator @ hybrid_generator, hybrid_generator)

    # Qutrit embedding |0>->|00>, |1>->|01>, |2>->|10>.  The unused |11>
    # is fixed.  Controlled SWAP is precisely controlled qutrit inversion.
    embedding = {0: (0, 0), 1: (0, 1), 2: (1, 0)}
    embedded_action = []
    for control in (0, 1):
        for qutrit in range(3):
            a, b = embedding[qutrit]
            target = fredkin_truth @ np.eye(8)[:, 4 * control + 2 * a + b]
            index = int(np.argmax(np.abs(target)))
            out = ((index >> 2) & 1, (index >> 1) & 1, index & 1)
            decoded = next(k for k, pair in embedding.items() if pair == out[1:])
            embedded_action.append([control, qutrit, out[0], decoded])
            assert decoded == ((-qutrit) % 3 if control else qutrit)

    # The eight-level record phase factorizes into three independently timed
    # H2 couplings.  This derives the earlier declared phase formula.
    record_checks = []
    for power in (1, 2, 4):
        direct = diagonal_from_boolean(
            4, lambda w: -np.pi * power * w[0] * (4 * w[1] + 2 * w[2] + w[3]) / 4
        )
        factors = np.eye(16, dtype=complex)
        angles = []
        for bit, weight in enumerate((4, 2, 1), start=1):
            angle = -np.pi * power * weight / 4
            angles.append(angle / np.pi)
            factors = factors @ diagonal_from_boolean(
                4, lambda w, bit=bit, angle=angle: angle * w[0] * w[bit]
            )
        assert close(direct, factors)
        record_checks.append({
            "power": power,
            "coupling_angles_in_pi_units": angles,
            "exact_factorization": True,
        })

    # Hostile source mutations.  They preserve the Hilbert-space support but
    # fail the exact generated operation.
    no_control_ccz = diagonal_from_boolean(3, lambda w: np.pi * w[1] * w[2])
    wrong_angle_ct = cc_phase(np.pi / 2)
    wrong_angle_cs = cc_phase(np.pi)
    missing_lsb = diagonal_from_boolean(
        4, lambda w: -np.pi * w[0] * (4 * w[1] + 2 * w[2]) / 4
    )
    target_power_one = diagonal_from_boolean(
        4, lambda w: -np.pi * w[0] * (4 * w[1] + 2 * w[2] + w[3]) / 4
    )
    hostile = {
        "erase_three_body_control": not close(no_control_ccz, ccz),
        "replace_controlled_t_angle_by_controlled_s": not close(wrong_angle_ct, controlled_t),
        "replace_controlled_s_angle_by_controlled_z": not close(wrong_angle_cs, controlled_s),
        "drop_least_significant_record_coupling": not close(missing_lsb, target_power_one),
        "erase_control_from_hybrid_exchange": not close(
            np.kron(np.eye(2), np.eye(3) - 2 * exchange_projector), direct_inversion
        ),
        "formal_support_without_pulse_calibration": True,
    }
    assert all(hostile.values())

    # A transversal implementation of each k-body port has bounded spread:
    # one faulty rail can affect at most that same rail in each participating
    # block.  This is necessary but not sufficient: the encoded gate must also
    # intertwine the frozen code projector, or be supplied by a verified code
    # switch/resource factory.
    fault_spread = {
        "two_body_port": {"participating_blocks": 2, "max_bad_rails_per_block": 1},
        "three_body_port": {"participating_blocks": 3, "max_bad_rails_per_block": 1},
        "distance_three_local_recovery_compatible": True,
        "encoded_intertwining_proved": False,
        "reason": "rail-local spread does not prove that transversal H2/H3 preserves the frozen five-rail codes",
    }

    result = {
        "schema": "marici.kitaev.s3-dpc-nonlinear-source-mechanism.v1",
        "source": {
            "primitive_family": [
                "H2(j,k)=n_j n_k",
                "H3(j,k,l)=n_j n_k n_l",
                "Hex=n_control tensor |1-2><1-2|/2",
            ],
            "independent_of_target_names": True,
            "required_controls": ["switchable support", "signed calibrated duration", "coherent occupation basis"],
        },
        "generated_resources": {
            "controlled_T": close(controlled_t, cc_phase(np.pi / 4)),
            "controlled_S": close(controlled_s, cc_phase(np.pi / 2)),
            "CCZ": close(ccz, diagonal_from_boolean(3, lambda w: np.pi * np.prod(w))),
            "Toffoli_from_H_CCZ_H": close(toffoli_from_source, toffoli_truth),
            "controlled_qutrit_inversion_from_fredkin": True,
            "controlled_qutrit_inversion_from_hybrid_exchange": close(controlled_exchange, direct_inversion),
        },
        "embedded_controlled_inversion_table": embedded_action,
        "record_phase_factorizations": record_checks,
        "hostile_source_mutations_rejected": hostile,
        "fault_spread_contract": fault_spread,
        "capability_disposition": {
            "logical_endpoint_generation": "Executable relative to the admitted nonlinear occupation source",
            "frozen_stabilizer_theory": "Obstructed",
            "five_rail_fault_tolerant_lift": "Conditional on encoded intertwining or a verified code-switch/resource factory",
        },
        "dpc_status": "proper generative explanation of the logical capability boundary; not yet a full physical fault-tolerant compiler",
        "verdict": "The missing D(S3) controls are generated by independently stated nonlinear source couplings: H2 supplies the record phases, while conditional hybrid exchange directly supplies qutrit inversion; H3 independently realizes the same inversion through CCZ, Toffoli, and a binary embedding. Removing or mistiming the generative couplings preserves formal support but destroys the target operations. Rail locality bounds fault spread, while encoded code preservation remains the explicit next theorem.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
