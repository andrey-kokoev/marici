#!/usr/bin/env python3
"""Classify the integral rank-nine cusp extension left by Entries 289/1151."""

from itertools import product
import hashlib
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def classify_row(b1, b2, s1):
    # C-I = [[0,2],[0,0]].  B -> B-S(C-I) sends (b1,b2) to
    # (b1,b2-2*s1); the second splitting column is irrelevant.
    return b1, b2 - 2 * s1


def main():
    c_minus_i = [[0, 2], [0, 0]]

    # For N=[[0,B],[0,C-I]], N^2 has upper-right block B(C-I).
    # Rowwise this is (0,2*b1), hence N^2=0 iff b1=0.
    square_zero_rows = []
    for b1, b2 in product(range(-3, 4), repeat=2):
        b_times_n = matmul([[b1, b2]], c_minus_i)[0]
        if b_times_n == [0, 0]:
            square_zero_rows.append([b1, b2])
        assert (b_times_n == [0, 0]) == (b1 == 0)

    # Exhaustively verify on a bounded window that integral splitting changes
    # preserve b2 mod 2, and that equal parities admit an integral change.
    for b2, target in product(range(-8, 9), repeat=2):
        same_orbit = (b2 - target) % 2 == 0
        if same_orbit:
            s1 = (b2 - target) // 2
            assert classify_row(0, b2, s1) == (0, target)
        else:
            assert all(classify_row(0, b2, s1)[1] != target for s1 in range(-12, 13))

    result = {
        "schema": "marici.nima.integral_rank9_cusp_extension_class.v1",
        "input": {
            "kernel_rank": 7,
            "kernel_monodromy": "I_7",
            "elliptic_monodromy": [[1, 2], [0, 1]],
            "full_nilpotent_square_zero": True,
        },
        "derivation": {
            "block_form": "N=[[0,B],[0,C-I]]",
            "square_zero_condition": "B(C-I)=0 forces the first column of B to vanish",
            "splitting_change": "B -> B-S(C-I); the second column changes by an even kernel vector",
        },
        "classification": {
            "ambient_integral_extension_class": "second column of B modulo 2",
            "ambient_group": "(Z/2)^7",
            "ambient_number_of_classes": 128,
            "source_supported_kernel_basis": ["e6", "v_alg"],
            "source_supported_group": "(Z/2)^2",
            "source_supported_number_of_classes": 4,
            "rational_class": "zero: every class is removed after inverting 2",
            "required_source_datum": "two parity bits along (e6,v_alg) in the primitive integral kernel",
        },
        "bounded_verification": {
            "b1_b2_window": [-3, 3],
            "orbit_window": [-8, 8],
            "passed": True,
        },
    }

    out = Path(__file__).parents[1] / "results" / "integral-rank9-cusp-extension-class.json"
    payload = out.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
