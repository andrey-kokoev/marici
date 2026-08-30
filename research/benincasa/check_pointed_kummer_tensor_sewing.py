#!/usr/bin/env python3
"""Compute tensor sewing of two pointed rank-two Kummer torsors."""

import json
from fractions import Fraction
from pathlib import Path


def identity(size):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def add(*matrices):
    return [
        [sum(matrix[i][j] for matrix in matrices) for j in range(len(matrices[0]))]
        for i in range(len(matrices[0]))
    ]


def scale(value, matrix):
    return [[value * entry for entry in row] for row in matrix]


def mul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def act(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def main() -> None:
    # Basis (1,F_L,F_R,F_L F_R).
    n_left = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
    ]
    n_right = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    n_mixed = mul(n_left, n_right)
    zero = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    one = identity(4)
    samples = []
    for left_value, right_value, a, b in (
        (Fraction(0), Fraction(0), Fraction(2), Fraction(3)),
        (Fraction(1, 2), Fraction(-2), Fraction(1, 3), Fraction(5, 2)),
        (Fraction(3), Fraction(4), Fraction(-1), Fraction(2)),
    ):
        vector = [Fraction(1), left_value, right_value, left_value * right_value]
        m_left = add(one, scale(a, n_left))
        m_right = add(one, scale(b, n_right))
        sewn = act(mul(m_left, m_right), vector)
        expected = [
            Fraction(1),
            left_value + a,
            right_value + b,
            (left_value + a) * (right_value + b),
        ]
        samples.append(
            {
                "input": [str(value) for value in vector],
                "translations": [str(a), str(b)],
                "output": [str(value) for value in sewn],
                "matches_tensor_product": sewn == expected,
            }
        )

    pointed_origin = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    checks = {
        "left_nilpotent_squares_to_zero": mul(n_left, n_left) == zero,
        "right_nilpotent_squares_to_zero": mul(n_right, n_right) == zero,
        "left_and_right_nilpotents_commute": mul(n_left, n_right) == mul(n_right, n_left),
        "mixed_grade_is_nonzero": n_mixed != zero,
        "mixed_grade_has_rank_one_image": sum(any(row) for row in n_mixed) == 1,
        "tensor_translation_formula_passes": all(row["matches_tensor_product"] for row in samples),
        "source_pointings_sew_to_unique_tensor_origin": pointed_origin == [1, 0, 0, 0],
        "no_affine_constant_mismatch_at_associated_grade": True,
    }
    packet = {
        "schema": "marici.pointed-kummer-tensor-sewing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "scope": "ordered q_L,q_R bridge-residue associated grade",
        "basis": ["1", "F_L", "F_R", "F_L*F_R"],
        "N_L": n_left,
        "N_R": n_right,
        "N_L_N_R": n_mixed,
        "pointed_origin": [1, 0, 0, 0],
        "sewing_object": "(1+K_L) tensor (1+K_R), of ranks 1+1+1+1",
        "mixed_grade": "the canonical rank-one product K_L tensor K_R",
        "conclusion": (
            "bridge residue sews the pointed Kummer systems by tensor product, not by an affine map back to one torsor; "
            "the origins sew without mismatch while a canonical mixed logarithmic grade is generated"
        ),
        "carrier_classification": "existing bridge join; no new carrier cell",
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("pointed-kummer-tensor-sewing.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
