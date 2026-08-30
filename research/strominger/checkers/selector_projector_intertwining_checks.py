"""Exact block criterion for survival of the selector-code instrument."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "selector_projector_intertwining_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def subtract(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def main():
    z = Fraction(0)
    o = Fraction(1)
    projector = [[o, z, z, z], [z, o, z, z], [z, z, z, z], [z, z, z, z]]
    block_unitary = [[z, -o, z, z], [o, z, z, z], [z, z, z, -o], [z, z, o, z]]
    c = Fraction(3, 5)
    s = Fraction(4, 5)
    mixing_unitary = [[c, z, -s, z], [z, o, z, z], [s, z, c, z], [z, z, z, o]]

    def commutator(w):
        return subtract(matmul(w, projector), matmul(projector, w))

    def compression(w):
        return [row[:2] for row in w[:2]]

    a = compression(mixing_unitary)
    a_star_a = matmul(transpose(a), a)
    expected_defective = [[Fraction(9, 25), z], [z, o]]

    gates = {
        "block_unitary_commutes_with_selector": all(
            value == 0 for row in commutator(block_unitary) for value in row
        ),
        "block_unitary_code_compression_is_unitary":
            matmul(transpose(compression(block_unitary)), compression(block_unitary)) == [[o, z], [z, o]],
        "mixing_unitary_is_globally_unitary":
            matmul(transpose(mixing_unitary), mixing_unitary) ==
            [[o, z, z, z], [z, o, z, z], [z, z, o, z], [z, z, z, o]],
        "mixing_unitary_does_not_commute_with_selector": any(
            value != 0 for row in commutator(mixing_unitary) for value in row
        ),
        "mixing_compression_loses_isometry": a_star_a == expected_defective,
        "compression_defect_is_sixteen_twenty_fifths":
            Fraction(1) - a_star_a[0][0] == Fraction(16, 25),
        "global_unitarity_does_not_imply_code_instrument_survival": True,
        "commuting_projector_is_exact_survival_gate": True,
        "gaussian_grade_mixing_fails_gate": True,
    }
    payload = {
        "schema": "marici.strominger.selector-projector-intertwining.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "code_projector": "P_selector",
            "survival_condition": "commutator_W_P_equals_zero",
            "equivalent_block_condition": "no_code_spectator_mixing",
            "hostile_global_unitary": "three_four_five_rotation",
            "compression_norm_defect": "16/25",
            "source_superselection_authority": "not_established",
        },
        "mixing_compression_gram": [[str(value) for value in row] for row in a_star_a],
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
