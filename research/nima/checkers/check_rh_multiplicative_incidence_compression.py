#!/usr/bin/env python3
"""Exact four-label audit of multiplicative incidence and scalar restriction."""

from fractions import Fraction
import json
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
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


def matvec(a, x):
    return tuple(sum(row[j] * x[j] for j in range(len(x))) for row in a)


def main():
    # Labels are 1, 2, 3, 6. Edges impose a_pn = q_p a_n.
    q2, q3 = Fraction(1, 2), Fraction(1, 3)
    incidence = [
        [-q2, 1, 0, 0],     # 1 -> 2
        [-q3, 0, 1, 0],     # 1 -> 3
        [0, -q3, 0, 1],     # 2 -> 6
        [0, 0, -q2, 1],     # 3 -> 6
    ]
    coherent = (1, q2, q3, q2 * q3)
    assert matvec(incidence, coherent) == (0, 0, 0, 0)
    assert rank(incidence) == 3

    scalar_coefficient = sum(coherent)
    assert scalar_coefficient == (1 + q2) * (1 + q3)
    assert scalar_coefficient != 0

    # Without cross-label incidence, aggregate cancellation remains visible.
    labelwise_witness = (0, 1, -1, 0)
    assert sum(labelwise_witness) == 0
    assert labelwise_witness != (0, 0, 0, 0)

    result = {
        "schema": "marici.rh-multiplicative-incidence-compression.v1",
        "labels": [1, 2, 3, 6],
        "incidence_rank": rank(incidence),
        "coherent_line_generator": [str(x) for x in coherent],
        "prime_square_commutes": True,
        "finite_scalar_restriction": str(scalar_coefficient),
        "finite_euler_factorization": "(1+q2)(1+q3)",
        "labelwise_scalar_cancellation_witness": labelwise_witness,
        "completion_warning": "on_the_coherent_line_kernel_inclusion_is_equivalent_to_nonvanishing_of_the_completed_boundary_coefficient",
        "required_extra_law": "independent_mixed_green_orientation"
    }
    out = Path(__file__).parents[1] / "results" / "rh-multiplicative-incidence-compression.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
