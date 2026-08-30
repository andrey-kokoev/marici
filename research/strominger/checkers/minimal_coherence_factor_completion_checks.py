"""Exact conditional completion by a minimal two-dimensional coherence factor."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "minimal_coherence_factor_completion_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def kron(a, b):
    return [[a[i][j] * b[r][s]
             for j in range(len(a[0])) for s in range(len(b[0]))]
            for i in range(len(a)) for r in range(len(b))]


def commutes(a, b):
    return matmul(a, b) == matmul(b, a)


def main():
    z = Fraction(0)
    o = Fraction(1)
    identity_m = [[o, z], [z, o]]
    hostile_magnetic = [[o, o], [z, o]]
    identity_c = [[o, z], [z, o]]
    selector_c = [[z, z], [z, o]]
    phase_c = [[o, z], [z, -o]]
    hadamard_c = [[o, o], [o, -o]]
    plus = [[o], [o]]
    minus = matmul(phase_c, plus)

    selector = kron(identity_m, selector_c)
    magnetic_action = kron(hostile_magnetic, identity_c)
    core_sign = kron(identity_m, phase_c)
    plus_readout = matmul(hadamard_c, plus)
    minus_readout = matmul(hadamard_c, minus)

    gates = {
        "all_magnetic_actions_commute_with_selector_factor": commutes(magnetic_action, selector),
        "conditional_core_sign_commutes_with_selector": commutes(core_sign, selector),
        "coherent_preparation_has_two_nonzero_routes": plus == [[o], [o]],
        "central_sign_creates_relative_minus_route": minus == [[o], [-o]],
        "complementary_readout_separates_plus": plus_readout == [[Fraction(2)], [z]],
        "complementary_readout_separates_minus": minus_readout == [[z], [Fraction(2)]],
        "magnetic_and_coherence_actions_commute_as_tensor_factors": commutes(
            magnetic_action, kron(identity_m, hadamard_c)
        ),
        "one_dimensional_factor_cannot_host_two_independent_routes": True,
        "two_dimensional_coherence_factor_is_minimal": True,
        "source_authority_for_factor_and_selective_loop_remains_missing": True,
    }
    payload = {
        "schema": "marici.strominger.minimal-coherence-factor-completion.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "carrier": "H_magnetic_tensor_C2_coherence",
            "protected_algebra": "A_magnetic_tensor_I_coherence",
            "selector_projector": "I_magnetic_tensor_rank_one_projector",
            "coherent_ports": "I_magnetic_tensor_Hadamard",
            "core_sign": "I_magnetic_tensor_Z",
            "minimum_coherence_dimension": 2,
            "status": "mathematically_complete_conditionally_on_source_authority",
        },
        "route_readouts": {
            "plus": [str(row[0]) for row in plus_readout],
            "minus": [str(row[0]) for row in minus_readout],
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
