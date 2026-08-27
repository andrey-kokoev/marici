#!/usr/bin/env python3
"""Solve the u=0 global source module with denominator v(v-2)."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix


EXE = ROOT / "research" / "benincasa" / "marici-gm" / "target" / "release" / "marked_relative_reduction_engine.exe"
OUTPUT = ROOT / "research" / "benincasa" / "results" / os.environ.get(
    "MARICI_GLOBAL_SOFT_RESULT", "global_two_soft_polynomial_module.json"
)
SOURCE_DEGREE = int(os.environ.get("MARICI_GLOBAL_SOFT_SOURCE_DEGREE", "16"))
NUMERATOR_DEGREE = int(os.environ.get("MARICI_GLOBAL_SOFT_NUMERATOR_DEGREE", "4"))


def export(v: int) -> dict:
    env = os.environ.copy()
    env.update(
        MARICI_EXACT_POINT_SOURCE_MODE="1",
        MARICI_EXACT_U="0",
        MARICI_EXACT_V=str(v),
        MARICI_EXACT_AXIS="v",
        MARICI_EXACT_MASTER="0",
        MARICI_EXACT_RAW_RESIDUES="1",
    )
    return json.loads(subprocess.run([str(EXE)], env=env, check=True, capture_output=True, text=True).stdout)


def inverse(matrix: list[list[int]], prime: int) -> list[list[int]]:
    n = len(matrix)
    augmented = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column] % prime)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = pow(augmented[column][column], -1, prime)
        augmented[column] = [(value * scale) % prime for value in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column] % prime:
                scale = augmented[row][column]
                augmented[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [row[n:] for row in augmented]


def rational_reconstruct(value: int, modulus: int) -> Fraction:
    bound = isqrt(modulus // 2)
    old_remainder, remainder = modulus, value
    old_denominator, denominator = 0, 1
    while abs(remainder) > bound:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_denominator, denominator = denominator, old_denominator - quotient * denominator
    if denominator < 0:
        remainder, denominator = -remainder, -denominator
    assert denominator and abs(denominator) <= bound
    assert (remainder - value * denominator) % modulus == 0
    return Fraction(remainder, denominator)


def main() -> None:
    points = list(range(1, SOURCE_DEGREE + 3))
    packets = [export(point) for point in points]
    prime = packets[0]["prime"]
    unknowns = packets[0]["unknowns"]
    assert unknowns == 372
    row_labels = sorted({tuple(row["monomial"]) for packet in packets for row in packet["rows"]})
    row_index = {label: index for index, label in enumerate(row_labels)}
    assert len(row_labels) == 132

    matrix_samples: dict[tuple[int, int], list[int]] = {}
    rhs_samples: dict[int, list[int]] = {}
    for sample, packet in enumerate(packets):
        rows = {tuple(row["monomial"]): row for row in packet["rows"]}
        for label, index in row_index.items():
            row = rows.get(label, {"entries": [], "rhs": "0"})
            entries = {int(column): int(value) % prime for column, value in row["entries"]}
            for column in range(unknowns):
                matrix_samples.setdefault((index, column), [0] * len(points))[sample] = entries.get(column, 0)
            rhs_samples.setdefault(index, [0] * len(points))[sample] = int(row["rhs"]) % prime

    size = SOURCE_DEGREE + 1
    interpolation_points = points[:size]
    vandermonde = [
        [pow(point, degree, prime) for degree in range(size)]
        for point in interpolation_points
    ]
    transform = inverse(vandermonde, prime)

    def coefficients(samples: list[int]) -> list[int]:
        return [
            sum(transform[degree][point] * samples[point] for point in range(size)) % prime
            for degree in range(size)
        ]

    matrix_coefficients = {key: coefficients(values) for key, values in matrix_samples.items()}
    rhs_coefficients = {key: coefficients(values) for key, values in rhs_samples.items()}
    held_out = points[-1]
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(matrix_coefficients[key])) % prime
        == values[-1]
        for key, values in matrix_samples.items()
    )
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(rhs_coefficients[key])) % prime
        == values[-1]
        for key, values in rhs_samples.items()
    )

    # M(v) N(v) = v(v-2) r(v), with every component of N allowed through
    # NUMERATOR_DEGREE except the target e6 numerator, constrained to degree zero.
    variable_columns = unknowns * (NUMERATOR_DEGREE + 1)
    augmented_column = variable_columns
    field = GF(prime)
    dod: dict[int, dict[int, object]] = {}
    max_equation_degree = max(
        SOURCE_DEGREE + NUMERATOR_DEGREE,
        SOURCE_DEGREE + 2,
    )
    for equation_degree in range(max_equation_degree + 1):
        for source_row in range(len(row_labels)):
            row: dict[int, object] = {}
            for numerator_degree in range(NUMERATOR_DEGREE + 1):
                matrix_degree = equation_degree - numerator_degree
                if not 0 <= matrix_degree <= SOURCE_DEGREE:
                    continue
                block = numerator_degree * unknowns
                for source_column in range(unknowns):
                    value = matrix_coefficients[(source_row, source_column)][matrix_degree]
                    if value:
                        row[block + source_column] = field(value)
            # v(v-2)r = v^2 r - 2v r.
            rhs = 0
            if 0 <= equation_degree - 2 <= SOURCE_DEGREE:
                rhs += rhs_coefficients[source_row][equation_degree - 2]
            if 0 <= equation_degree - 1 <= SOURCE_DEGREE:
                rhs -= 2 * rhs_coefficients[source_row][equation_degree - 1]
            rhs %= prime
            if rhs:
                row[augmented_column] = field(rhs)
            if row:
                dod[len(dod)] = row

    # No-infinity logarithmic condition for the target coordinate N_e6,q0:
    # all numerator coefficients above degree zero vanish.
    target_coordinate = 8
    for degree in range(1, NUMERATOR_DEGREE + 1):
        dod[len(dod)] = {degree * unknowns + target_coordinate: field.one}

    matrix = DomainMatrix.from_dod(
        dod,
        (len(dod), variable_columns + 1),
        field,
    )
    reduced, pivots = matrix.rref()
    inconsistent = augmented_column in pivots
    reduced_dod = reduced.to_dod()
    free = set(range(variable_columns)) - set(pivots)
    target = target_coordinate
    target_is_pivot = target in pivots
    target_row = reduced_dod.get(pivots.index(target), {}) if target_is_pivot else {}
    target_fixed = (
        not inconsistent
        and target_is_pivot
        and all(target_row.get(column, field.zero) == field.zero for column in free)
    )
    target_value = (
        int(target_row.get(augmented_column, field.zero)) % prime
        if target_fixed
        else None
    )

    output = {
        "schema": "marici.benincasa.global_two_soft_polynomial_module.v1",
        "prime": prime,
        "u": 0,
        "derivative_axis": "v",
        "denominator": "v*(v-2)",
        "numerator_degree": NUMERATOR_DEGREE,
        "target": "constant numerator of (B_v)_e6,q0",
        "target_high_coefficients_forced_zero": NUMERATOR_DEGREE,
        "source_degree": SOURCE_DEGREE,
        "held_out_polynomial_identity": True,
        "equations": len(dod),
        "variables": variable_columns,
        "rank": len(pivots),
        "consistent": not inconsistent,
        "target_is_pivot": target_is_pivot,
        "target_fixed": target_fixed,
        "target_mod_prime": target_value,
        "target_rational": str(rational_reconstruct(target_value, prime)) if target_value is not None else None,
        "candidate_target": "1/4",
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
