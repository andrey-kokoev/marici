#!/usr/bin/env python3
"""Exact rank and quotient census for the frozen supported T7 cospan."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(len(a[0]))]
        r += 1
    return r


def main():
    root = Path(__file__).resolve().parents[3]
    # Rows (e2,e3,e4,e5,e6,v0); columns
    # (Theta101,Theta110,Theta111,g101,g110,g111) at x=2,y=3.
    matrix = [
        [0, -180, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 3],
        [180, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 2],
        [0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0],
    ]
    logarithmic = [row[:3] for row in matrix]
    cut_nearby = [row[3:] for row in matrix]
    annihilator = [1, 0, -1, 0, 0, 180]
    column_relation = [0, 0, -2, -1, -1, 2]
    assert rank(logarithmic) == 3
    assert rank(cut_nearby) == 3
    assert rank(matrix) == 5
    assert all(sum(annihilator[i] * matrix[i][j] for i in range(6)) == 0
               for j in range(6))
    assert all(sum(matrix[i][j] * column_relation[j] for j in range(6)) == 0
               for i in range(6))
    result = {
        "schema": "marici.nima.t7_supported_cospan_quotient.v1",
        "passed": True,
        "generic_fiber": {"x": 2, "y": 3},
        "ambient_basis": ["e1", "e2", "e3", "e4", "e5", "e6", "v_alg"],
        "supported_block_basis": ["e2", "e3", "e4", "e5", "e6", "v_alg"],
        "logarithmic_image_rank": 3,
        "cut_nearby_image_rank": 3,
        "combined_supported_image_rank": 5,
        "t7_quotient_dimension": 2,
        "first_missing_direction": "e1",
        "second_quotient_detecting_covector": "e2-e4+180*v_alg",
        "unique_column_relation": "2*g111-Theta101-Theta110-2*Theta111=0",
        "interpretation": "the declared logarithmic and Cut-nearby supported cospan misses exactly two T7 directions; one is e1 and the other is the intrinsic quotient of the six-dimensional supported block",
        "scope": "exact generic fiber in the frozen independently normalized representatives; the coefficient 180 is frame-dependent while the quotient line and dimensions are invariant",
    }
    path = root / "research/nima/results/t7-supported-cospan-quotient.json"
    payload = path.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "quotient_dimension": 2,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
