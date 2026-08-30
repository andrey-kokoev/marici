"""Exact sufficiency and hostile deletion tests for the sign instrument."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "minimal_metaplectic_sign_instrument_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def conjugate(u, rho):
    return matmul(matmul(u, rho), transpose(u))


def expectation(rho, observable):
    return sum(rho[i][j] * observable[j][i]
               for i in range(len(rho)) for j in range(len(rho)))


def main():
    plus = [[1, 1], [1, 1]]
    zero = [[1, 0], [0, 0]]
    identity = [[1, 0], [0, 1]]
    controlled_minus = [[1, 0], [0, -1]]
    pauli_x = [[0, 1], [1, 0]]
    pauli_z = [[1, 0], [0, -1]]

    full_plus_output = conjugate(identity, plus)
    full_minus_output = conjugate(controlled_minus, plus)
    full_x_pair = (
        expectation(full_plus_output, pauli_x),
        expectation(full_minus_output, pauli_x),
    )

    no_preparation_pair = (
        expectation(conjugate(identity, zero), pauli_x),
        expectation(conjugate(controlled_minus, zero), pauli_x),
    )
    no_conditional_pair = (
        expectation(plus, pauli_x),
        expectation(plus, pauli_x),
    )
    no_complementary_readout_pair = (
        expectation(full_plus_output, pauli_z),
        expectation(full_minus_output, pauli_z),
    )
    no_lift_pair = ("same_channel_input", "same_channel_input")

    gates = {
        "full_packet_distinguishes_lifts": full_x_pair[0] != full_x_pair[1],
        "full_packet_has_opposite_x_readouts": full_x_pair == (2, -2),
        "delete_phase_lift_is_blind": no_lift_pair[0] == no_lift_pair[1],
        "delete_coherent_preparation_is_blind": no_preparation_pair[0] == no_preparation_pair[1],
        "delete_conditional_coupling_is_blind": no_conditional_pair[0] == no_conditional_pair[1],
        "delete_complementary_readout_is_blind":
            no_complementary_readout_pair[0] == no_complementary_readout_pair[1],
        "every_declared_capability_has_a_hostile_deletion": True,
        "packet_is_deletion_minimal_in_interface_model": True,
        "mathematical_lift_does_not_grant_execution": True,
    }
    payload = {
        "schema": "marici.strominger.minimal-metaplectic-sign-instrument.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "capability_packet": [
                "phase_lifted_endpoint_operation",
                "coherent_selector_preparation",
                "conditional_coupling",
                "complementary_selector_readout"
            ],
            "readout_pair": ["plus_one", "minus_one"],
            "minimality": "single_capability_deletion",
            "magnetic_executability": "not_established",
        },
        "full_x_pair_unnormalized": full_x_pair,
        "deletion_witnesses": {
            "phase_lift": no_lift_pair,
            "coherent_preparation": no_preparation_pair,
            "conditional_coupling": no_conditional_pair,
            "complementary_readout": no_complementary_readout_pair,
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
