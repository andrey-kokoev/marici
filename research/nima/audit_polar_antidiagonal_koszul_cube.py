#!/usr/bin/env python3
"""Exact incidence matrices for the anti-diagonal E,P3,a,b Koszul cube."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


VARIABLES = ("E", "P3", "a", "b")


def subsets(k):
    return list(itertools.combinations(range(len(VARIABLES)), k))


def differential(k):
    source = subsets(k)
    target = subsets(k+1)
    target_pos = {s: i for i, s in enumerate(target)}
    matrix = [[Fraction(0) for _ in source] for _ in target]
    for j, s in enumerate(source):
        remaining = [i for i in range(len(VARIABLES)) if i not in s]
        for i in remaining:
            sign = -1 if sum(1 for x in s if x < i) % 2 else 1
            t = tuple(sorted(s+(i,)))
            matrix[target_pos[t]][j] = Fraction(sign)
    return matrix


def multiply(left, right):
    return [[sum(left[i][k]*right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def rank(matrix):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x/scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x-factor*y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    matrices = [differential(k) for k in range(4)]
    for k in range(3):
        product = multiply(matrices[k+1], matrices[k])
        assert all(value == 0 for row in product for value in row)
    ranks = [rank(matrix) for matrix in matrices]
    assert ranks == [1, 3, 3, 1]
    dimensions = [1, 4, 6, 4, 1]
    homology = [
        dimensions[k]-(ranks[k] if k < 4 else 0)-(ranks[k-1] if k > 0 else 0)
        for k in range(5)
    ]
    assert homology == [0, 0, 0, 0, 0]

    packet = {
        "variables": VARIABLES,
        "source_term": "M=2*E*P3*a*b",
        "complex_dimensions": dimensions,
        "differential_ranks": ranks,
        "d_squared_zero": True,
        "homology_dimensions": homology,
        "orientation_rule": "(-1)^(number of existing indices preceding inserted index)",
        "anti_diagonal_cube_exact": True,
        "remaining_column": "filtered diagonal C column",
    }
    out = Path(__file__).with_name("polar-antidiagonal-koszul-cube.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
