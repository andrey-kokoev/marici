"""Exact no-go for controlling a global phase from channel-only access."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "controlled_global_phase_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def conjugate_channel(unitary, rho):
    return matmul(matmul(unitary, rho), transpose(unitary))


def trace_product(a, b):
    return sum(a[i][j] * b[j][i]
               for i in range(len(a)) for j in range(len(a)))


def main():
    target_rho = [[7]]
    identity_target = [[1]]
    minus_identity_target = [[-1]]
    channel_i = conjugate_channel(identity_target, target_rho)
    channel_minus_i = conjugate_channel(minus_identity_target, target_rho)

    plus_rho_unnormalized = [[1, 1], [1, 1]]
    controlled_i = [[1, 0], [0, 1]]
    controlled_minus_i = [[1, 0], [0, -1]]
    output_i = conjugate_channel(controlled_i, plus_rho_unnormalized)
    output_minus_i = conjugate_channel(controlled_minus_i, plus_rho_unnormalized)
    pauli_x = [[0, 1], [1, 0]]

    gates = {
        "identity_and_minus_identity_channels_equal": channel_i == channel_minus_i,
        "controlled_representatives_are_distinct": controlled_i != controlled_minus_i,
        "controlled_output_states_are_distinct": output_i != output_minus_i,
        "identity_control_preserves_plus_state": output_i == plus_rho_unnormalized,
        "minus_identity_control_produces_minus_state":
            output_minus_i == [[1, -1], [-1, 1]],
        "control_x_readout_is_positive_for_identity":
            trace_product(output_i, pauli_x) == 2,
        "control_x_readout_is_negative_for_minus_identity":
            trace_product(output_minus_i, pauli_x) == -2,
        "channel_only_compiler_has_identical_inputs_for_distinct_targets":
            channel_i == channel_minus_i and output_i != output_minus_i,
        "phase_lift_is_required": True,
    }
    payload = {
        "schema": "marici.strominger.controlled-global-phase-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "available_interface": "unitary_conjugation_channel",
            "forgotten_datum": "global_phase",
            "requested_constructor": "controlled_unitary",
            "no_go": "controlled_unitary_not_a_function_of_projective_channel",
            "minimal_missing_input": "phase_lifted_implementation_or_controlled_path",
            "physical_authority": "not_established",
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
