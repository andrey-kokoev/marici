#!/usr/bin/env python3
"""Exact Fourier-character audit for the five-cell boundary quotient."""

import itertools
import json
from pathlib import Path


def matmul_row(row, matrix):
    return tuple(sum(row[k] * matrix[k][j] for k in range(len(row))) for j in range(len(matrix[0])))


def scale(value, row):
    return tuple(value * x for x in row)


def determinant(matrix):
    total = 0j
    n = len(matrix)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = (-1 if inversions % 2 else 1)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += term
    return total


def encode(z):
    return {"real": int(z.real), "imag": int(z.imag)}


def main():
    # Boundary basis: constant, delta, centered tail K, principal-value V.
    # Columns encode F(1)=delta, F(delta)=1, F(K)=V, F(V)=-K.
    fourier = (
        (0, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 0, -1),
        (0, 0, 1, 0),
    )
    characters = (
        (1, (1, 1, 0, 0)),
        (-1, (1, -1, 0, 0)),
        (1j, (0, 0, 1, 1j)),
        (-1j, (0, 0, 1, -1j)),
    )
    for eigenvalue, covector in characters:
        assert matmul_row(covector, fourier) == scale(eigenvalue, covector)

    character_matrix = tuple(row for _, row in characters)
    det = determinant(character_matrix)
    assert det != 0

    # One scalar character supplies one row on a four-dimensional quotient.
    scalar_residual_dimension = 3
    assert scalar_residual_dimension == len(character_matrix) - 1

    result = {
        "schema": "marici.rh-five-cell-observer-characters.v1",
        "boundary_basis": ["constant", "delta", "centered_tail", "principal_value"],
        "fourier_characters": ["1", "-1", "i", "-i"],
        "character_covectors": [[encode(complex(x)) for x in row] for row in character_matrix],
        "character_matrix_determinant": encode(det),
        "full_character_family_rank": 4,
        "single_scalar_character_rank": 1,
        "single_scalar_residual_dimension": scalar_residual_dimension,
        "required_preprojection_type": "fourier_representation_valued_observer",
        "scalarization_stage": "after_boundary_descent"
    }
    out = Path(__file__).parents[1] / "results" / "rh-five-cell-observer-characters.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
