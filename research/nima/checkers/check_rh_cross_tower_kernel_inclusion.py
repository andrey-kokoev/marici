#!/usr/bin/env python3
"""Finite DPC for scalar-output nullity implying Ward-packet nullity."""

from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a, x):
    return tuple(sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a)))


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    # State coordinates: vacuum plus two Ward-visible directions.
    scalar_output = [[1, 1, 1]]
    ward = [[0, 1, 0], [0, 0, 1]]

    full_admissible = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    two_dimensional_admissible = [[1, 0], [0, 1], [0, 0]]
    one_dimensional_admissible = [[1], [0], [0]]

    l_full = matmul(scalar_output, full_admissible)
    w_full = matmul(ward, full_admissible)
    witness = (0, 1, -1)
    assert matvec(scalar_output, witness) == (0,)
    assert matvec(ward, witness) != (0, 0)
    assert rank(w_full) == 2 > rank(l_full)

    l_two = matmul(scalar_output, two_dimensional_admissible)
    w_two = matmul(ward, two_dimensional_admissible)
    assert rank(w_two) == 1 == rank(l_two)
    two_witness = (1, -1)
    assert matvec(l_two, two_witness) == (0,)
    assert matvec(w_two, two_witness) != (0, 0)

    l_one = matmul(scalar_output, one_dimensional_admissible)
    w_one = matmul(ward, one_dimensional_admissible)
    assert rank(l_one) == 1
    assert rank(w_one) == 0

    result = {
        "schema": "marici.rh-cross-tower-kernel-inclusion.v1",
        "full_state_hostile": {"state": witness, "scalar_output": 0, "ward_output": matvec(ward, witness)},
        "necessary_rank_condition": "rank(W restricted to A_s) <= rank(L restricted to A_s) <= 1",
        "rank_condition_not_sufficient": {
            "admissible_dimension": 2,
            "scalar_rank": rank(l_two),
            "ward_rank": rank(w_two),
            "kernel_inclusion_fails": True
        },
        "vacuum_line_fixture": {"scalar_rank": rank(l_one), "ward_rank": rank(w_one), "kernel_inclusion_holds": True},
        "decisive_gate": "ker(L_s) subset ker(W_s) on the source_admissible_solution_space",
        "required_mechanism": "source_green_identity_or_dynamic_observability_not_static_state_reconstruction"
    }
    out = Path(__file__).parents[1] / "results" / "rh-cross-tower-kernel-inclusion.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
