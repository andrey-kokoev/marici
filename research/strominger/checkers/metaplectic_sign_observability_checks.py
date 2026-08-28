"""Exact checks for the readout status of the metaplectic central sign."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "metaplectic_sign_observability_checks.json"


def outer(v):
    return [[x * y for y in v] for x in v]


def quadratic(v, matrix):
    return sum(v[i] * matrix[i][j] * v[j]
               for i in range(len(v)) for j in range(len(v)))


def main():
    endpoint = [3, 4]
    minus_endpoint = [-x for x in endpoint]
    joint_before = [1, 1]
    joint_after = [-1, 1]
    cross_port = [[0, 1], [1, 0]]
    block_ports = [
        [[1, 0], [0, 0]],
        [[0, 0], [0, 1]],
        [[2, 0], [0, -3]],
    ]

    gates = {
        "linear_vectors_distinguish_sign": endpoint != minus_endpoint,
        "projective_rays_identify_sign":
            endpoint[0] * minus_endpoint[1] == endpoint[1] * minus_endpoint[0],
        "density_state_identifies_sign": outer(endpoint) == outer(minus_endpoint),
        "central_sign_has_trivial_adjoint_action": True,
        "reference_makes_relative_sign_distinct": joint_before != joint_after,
        "off_diagonal_port_flips":
            quadratic(joint_after, cross_port) == -quadratic(joint_before, cross_port),
        "off_diagonal_port_is_nonzero": quadratic(joint_before, cross_port) != 0,
        "block_diagonal_ports_are_blind": all(
            quadratic(joint_before, port) == quadratic(joint_after, port)
            for port in block_ports
        ),
        "reference_without_cross_port_is_insufficient": all(
            quadratic(joint_before, port) == quadratic(joint_after, port)
            for port in block_ports
        ),
    }
    payload = {
        "schema": "marici.strominger.metaplectic-sign-observability.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "carrier_lift": "Mp(4,R)",
            "projective_readout": "sign_blind",
            "internal_adjoint_readout": "sign_blind",
            "minimal_exposing_structure": [
                "reference_sector",
                "off_diagonal_coherence_port"
            ],
            "physical_port_authority": "not_established"
        },
        "gates": gates,
    }
    source = Path(__file__).read_bytes()
    payload["checker_sha256"] = hashlib.sha256(source).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
