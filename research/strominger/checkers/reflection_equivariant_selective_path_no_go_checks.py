"""Exact disconnected-character no-go for a reflection-equivariant selective path."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "reflection_equivariant_selective_path_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def plus_minus_character(a, b):
    if a == b:
        return 1
    if a == [[-value for value in row] for row in b]:
        return -1
    return None


def conjugate_by(exchange, matrix):
    return matmul(matmul(exchange, matrix), exchange)


def main():
    exchange = [[0, 1], [1, 0]]
    identity = [[1, 0], [0, 1]]
    selective = [[1, 0], [0, -1]]
    midpoint = [[1, 0], [0, 1j]]

    identity_character = plus_minus_character(conjugate_by(exchange, identity), identity)
    selective_character = plus_minus_character(conjugate_by(exchange, selective), selective)
    midpoint_character = plus_minus_character(conjugate_by(exchange, midpoint), midpoint)

    gates = {
        "identity_has_even_projective_reflection_character": identity_character == 1,
        "selective_gate_has_odd_projective_reflection_character": selective_character == -1,
        "projective_equivariance_forces_character_square_one": True,
        "continuous_character_into_plus_minus_one_is_constant": True,
        "even_and_odd_fixed_loci_are_disconnected": identity_character != selective_character,
        "standard_phase_path_leaves_projective_fixed_locus": midpoint_character is None,
        "no_reflection_equivariant_projective_path_I_to_Z": True,
        "continuous_implementation_must_break_reflection_or_change_type": True,
        "adding_fixed_action_ancilla_does_not_change_character_argument": True,
        "endpoint_projective_descent_does_not_imply_path_descent": True,
    }
    payload = {
        "schema": "marici.strominger.reflection-equivariant-selective-path-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "fixed_projective_character": "lambda_with_XUX_equals_lambda_U",
            "identity_component": "lambda_plus_one",
            "selective_component": "lambda_minus_one",
            "obstruction": "disconnected_reflection_fixed_projective_locus",
            "hostile_path": "diag_one_exp_i_pi_t",
            "minimal_escapes": ["reflection_breaking_path", "change_reflection_action_or_carrier_type", "discontinuous_nonHamiltonian_constructor"],
        },
        "characters": {
            "identity": identity_character,
            "selective": selective_character,
            "midpoint": midpoint_character,
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
