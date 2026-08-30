#!/usr/bin/env python3
"""Exact rank/cocycle audit for the exterior-observer extension DPC."""

from fractions import Fraction
import json
from pathlib import Path


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
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def main():
    # B = H + W, with a three-dimensional retained boundary quotient W.
    quotient_dimension = 3

    scalar_only = [[1, 1, 1]]
    partial_source_law = [[1, 0, 0], [0, 1, 0]]
    separating_source_law = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    assert rank(scalar_only) == 1
    assert quotient_dimension - rank(scalar_only) == 2
    assert rank(partial_source_law) == 2
    assert quotient_dimension - rank(partial_source_law) == 1
    assert rank(separating_source_law) == quotient_dimension

    # Three path extensions differ only on W*.  Their differences telescope.
    beta_p = (1, 0, 2)
    beta_q = (0, 1, 2)
    beta_r = (3, 1, -1)
    delta_pq = sub(beta_q, beta_p)
    delta_qr = sub(beta_r, beta_q)
    delta_pr = sub(beta_r, beta_p)
    assert add(delta_pq, delta_qr) == delta_pr
    assert delta_pr != (0, 0, 0)

    # Inconsistency: the same retained wall is required to have values 0 and 1.
    inconsistent_coefficients = [[1, 0, 0], [1, 0, 0]]
    inconsistent_augmented = [[1, 0, 0, 0], [1, 0, 0, 1]]
    assert rank(inconsistent_augmented) > rank(inconsistent_coefficients)

    result = {
        "schema": "marici.rh-boundary-observer-torsor-dpc.v1",
        "boundary_quotient_dimension_in_fixture": quotient_dimension,
        "scalar_continuation_residual_dimension": quotient_dimension - rank(scalar_only),
        "partial_source_law_residual_dimension": quotient_dimension - rank(partial_source_law),
        "separating_source_law_residual_dimension": quotient_dimension - rank(separating_source_law),
        "path_difference_cocycle": {
            "delta_pq": delta_pq,
            "delta_qr": delta_qr,
            "delta_pr": delta_pr,
            "telescopes": True,
            "nonzero": True
        },
        "verdicts": ["unique_descent", "residual_boundary_torsor", "inconsistent_boundary_laws"],
        "inconsistency_detected_by_augmented_rank": True,
        "rh_implication": "none_without_a_separate_green_orientation_theorem"
    }
    out = Path(__file__).parents[1] / "results" / "rh-boundary-observer-torsor-dpc.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
