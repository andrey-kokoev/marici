#!/usr/bin/env python3
"""Freeze and exhaustively certify the five-rail component codes."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


QUBIT = [
    (1, 0, 0, 1, 0, 0, 1, 1, 0, 0),  # X Z Z X I
    (0, 1, 0, 0, 1, 0, 0, 1, 1, 0),  # I X Z Z X
    (1, 0, 1, 0, 0, 0, 0, 0, 1, 1),  # X I X Z Z
    (0, 1, 0, 1, 0, 1, 0, 0, 0, 1),  # Z X I X Z
]

# Deterministically found isotropic pure [[5,1,3]]_3 stabilizer.  Each row is
# (X exponents | Z exponents), with arithmetic in F_3.
QUTRIT = [
    (2, 1, 0, 1, 0, 1, 2, 1, 2, 2),
    (0, 1, 0, 1, 1, 1, 1, 2, 0, 0),
    (1, 1, 1, 0, 2, 2, 0, 0, 1, 0),
    (2, 1, 0, 0, 0, 1, 1, 0, 1, 1),
]


def symplectic(u, v, q):
    return sum(u[i] * v[5 + i] - u[5 + i] * v[i] for i in range(5)) % q


def weight(v):
    return sum(bool(v[i] or v[5 + i]) for i in range(5))


def rank(rows, q):
    matrix = [list(row) for row in rows]
    pivot_row = 0
    for column in range(10):
        pivot = next((i for i in range(pivot_row, len(matrix)) if matrix[i][column] % q), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = pow(matrix[pivot_row][column], -1, q)
        matrix[pivot_row] = [(x * scale) % q for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][column] % q:
                scale = matrix[i][column] % q
                matrix[i] = [
                    (matrix[i][j] - scale * matrix[pivot_row][j]) % q for j in range(10)
                ]
        pivot_row += 1
    return pivot_row


def span(rows, q):
    return {
        tuple(sum(coefficients[j] * rows[j][i] for j in range(4)) % q for i in range(10))
        for coefficients in itertools.product(range(q), repeat=4)
    }


def single_rail_errors(q):
    zero = (0,) * 10
    errors = []
    for rail in range(5):
        for x in range(q):
            for z in range(q):
                if x == z == 0:
                    continue
                error = list(zero)
                error[rail] = x
                error[5 + rail] = z
                errors.append(tuple(error))
    return errors


def certify(name, q, stabilizers):
    assert rank(stabilizers, q) == 4
    assert all(symplectic(a, b, q) == 0 for a in stabilizers for b in stabilizers)
    stabilizer_span = span(stabilizers, q)
    vectors = list(itertools.product(range(q), repeat=10))
    centralizer = [v for v in vectors if all(symplectic(v, s, q) == 0 for s in stabilizers)]
    logical = [v for v in centralizer if v not in stabilizer_span]
    distance = min(weight(v) for v in logical)
    stabilizer_minimum = min(weight(v) for v in stabilizer_span if any(v))
    assert distance == 3
    assert stabilizer_minimum >= 3
    assert len(centralizer) == q**6
    assert len(stabilizer_span) == q**4

    logical_x = min(logical, key=lambda v: (weight(v), v))
    logical_z = min(
        (v for v in logical if symplectic(logical_x, v, q) == 1),
        key=lambda v: (weight(v), v),
    )
    errors = single_rail_errors(q)
    syndrome_table = {
        tuple(symplectic(error, stabilizer, q) for stabilizer in stabilizers): error
        for error in errors
    }
    assert len(syndrome_table) == len(errors)
    assert (0, 0, 0, 0) not in syndrome_table

    return {
        "name": name,
        "field_order": q,
        "parameters": f"[[5,1,3]]_{q}",
        "stabilizer_generators": [list(v) for v in stabilizers],
        "stabilizer_rank": 4,
        "stabilizer_minimum_weight": stabilizer_minimum,
        "centralizer_size": len(centralizer),
        "distance": distance,
        "logical_x": list(logical_x),
        "logical_z": list(logical_z),
        "logical_pairing": symplectic(logical_x, logical_z, q),
        "single_rail_error_count": len(errors),
        "distinct_nonzero_syndromes": len(syndrome_table),
        "recovery_table": [
            {
                "syndrome": list(syndrome),
                "error": list(error),
                "correction": [(-entry) % q for entry in error],
            }
            for syndrome, error in sorted(syndrome_table.items())
        ],
        "code_dimension": q,
    }


def main():
    qubit = certify("five_qubit_perfect_code", 2, QUBIT)
    qutrit = certify("five_qutrit_stabilizer_code", 3, QUTRIT)
    result = {
        "schema": "marici.kitaev.s3-five-rail-code-freeze.v1",
        "component_codes": {"qubit": qubit, "qutrit": qutrit},
        "six_level_bus": {
            "rail_factorization": "C2 tensor C3 on each of five rails",
            "code": "[[5,1,3]]_2 tensor [[5,1,3]]_3",
            "physical_rail_dimension": 6,
            "logical_dimension": 6,
            "distance": 3,
            "stabilizer_generators": 8,
        },
        "eight_level_bus": {
            "rail_factorization": "C2 tensor C2 tensor C2 on each of five rails",
            "code": "three componentwise [[5,1,3]]_2 codes",
            "physical_rail_dimension": 8,
            "logical_dimension": 8,
            "distance": 3,
            "stabilizer_generators": 12,
        },
        "total_bus_rails_for_holonomy_relative_label": 15,
        "logical_basis_definition": "joint +1 stabilizer eigenspace, resolved by the listed logical-Z eigenvalues in each tensor factor",
        "verdict": "The previously abstract five-rail six- and eight-level buses now have explicit component stabilizers, logical Pauli pairs, unique single-rail syndromes, and exactly certified distance three.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-five-rail-code-freeze.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
