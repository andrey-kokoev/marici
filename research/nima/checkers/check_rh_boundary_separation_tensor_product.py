#!/usr/bin/env python3
"""Finite rank audit for Fourier-character times arithmetic-probe separation."""

import json
from pathlib import Path


def rank(matrix, eps=1e-12):
    a = [list(map(complex, row)) for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if abs(a[i][c]) > eps), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(rows):
            if i != r and abs(a[i][c]) > eps:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def kron_rows(a, b):
    rows = []
    for ar in a:
        for br in b:
            rows.append([x * y for x in ar for y in br])
    return rows


def main():
    fourier_rows = [
        [1, 1, 0, 0],
        [1, -1, 0, 0],
        [0, 0, 1, 1j],
        [0, 0, 1, -1j],
    ]
    arithmetic_cylinders = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    one_mellin_row = [[1, 2, 3]]

    full = kron_rows(fourier_rows, arithmetic_cylinders)
    scalar_arithmetic = kron_rows(fourier_rows, one_mellin_row)
    one_total_scalar = [[1] * 12]

    assert rank(fourier_rows) == 4
    assert rank(arithmetic_cylinders) == 3
    assert rank(full) == 12
    assert rank(scalar_arithmetic) == 4
    assert rank(one_total_scalar) == 1

    result = {
        "schema": "marici.rh-boundary-separation-tensor-product.v1",
        "fixture_label_count": 3,
        "combined_boundary_dimension": 12,
        "fourier_character_rank": 4,
        "arithmetic_cylinder_rank": 3,
        "tensor_probe_rank": 12,
        "four_characters_with_one_arithmetic_scalar_rank": 4,
        "one_total_scalar_rank": 1,
        "residual_dimension_after_four_scalar_character_rows": 8,
        "rank_factorization": "rank(character_family) times rank(arithmetic_family)",
        "completion_gate": "natural_continuous_arithmetic_probe_family_inside_each_character_sector"
    }
    out = Path(__file__).parents[1] / "results" / "rh-boundary-separation-tensor-product.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
