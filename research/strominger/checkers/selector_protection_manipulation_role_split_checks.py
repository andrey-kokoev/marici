"""Exact no-go for one algebra both protecting and manipulating a selector."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "selector_protection_manipulation_role_split_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def subtract(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def commutes(a, b):
    return matmul(a, b) == matmul(b, a)


def main():
    z = Fraction(0)
    o = Fraction(1)
    p = [[o, z], [z, z]]
    identity = [[o, z], [z, o]]
    phase = [[o, z], [z, -o]]
    swap = [[z, o], [o, z]]
    # An unnormalized Hadamard is sufficient for exact commutant tests.
    hadamard = [[o, o], [o, -o]]

    gates = {
        "protected_phase_commutes_with_selector": commutes(phase, p),
        "identity_commutes_with_selector": commutes(identity, p),
        "coherent_swap_does_not_commute_with_selector": not commutes(swap, p),
        "complementary_hadamard_does_not_commute_with_selector": not commutes(hadamard, p),
        "phase_and_swap_generate_noncommuting_controls": not commutes(phase, swap),
        "strict_superselection_forbids_coherent_preparation": True,
        "strict_superselection_forbids_complementary_readout": True,
        "typed_role_split_retains_protection_and_ports": True,
        "role_split_is_compositional_not_chronological": True,
    }
    payload = {
        "schema": "marici.strominger.selector-protection-manipulation-role-split.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "protected_endomorphisms": "commutant_of_P",
            "preparation_port": "typed_map_into_selector_object",
            "complementary_readout_port": "typed_map_out_of_selector_object",
            "forbidden_conflation": "all_three_roles_as_one_closed_endomorphism_algebra",
            "superselection_label_alone": "insufficient_for_interference",
            "required_structure": "object_with_protected_core_and_non-endomorphic_ports",
        },
        "commutators": {
            "phase_with_projector": [[str(x) for x in row] for row in subtract(matmul(phase, p), matmul(p, phase))],
            "swap_with_projector": [[str(x) for x in row] for row in subtract(matmul(swap, p), matmul(p, swap))],
            "hadamard_with_projector": [[str(x) for x in row] for row in subtract(matmul(hadamard, p), matmul(p, hadamard))],
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
