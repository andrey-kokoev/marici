"""Finite-field calibration for the physical d=3 twisted de Rham reducer.

This first gate treats the zero-denominator family only.  The twist is
K^(-1/2); unlike the deletion-cube critical count, no generic exponent is
inserted.  Pole levels are retained as separate blocks.  A polynomial
vector-field primitive at rational pole K^m maps to

    div(V) / K^m - (m+1/2) V(K) / K^(m+1).

The computation is a hostile test of whether specializing to d=3 before
reduction preserves the generic-dimensional polynomial master space.  A
generic weight reproduces rank 7, while gamma=-1/2 leaves a one-dimensional
image of the degree-five level-zero numerator space.
"""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from itertools import product

import sympy as sp


PRIME = int(os.environ.get("MARICI_FIELD_PRIME", "32003"))
c, a, b = sp.symbols("c a b")
VARS = (c, a, b)

K = sp.expand(
    4 * a**4
    + 3 * a**2 * b**2
    + 9 * b**4
    - 84 * a**2
    - 11 * c**2 * a**2
    - 99 * b**2
    - 21 * c**2 * b**2
    + 16 * c**4
    + 48 * c**2
    + 576
)
K_DERIVATIVES = tuple(sp.diff(K, variable) for variable in VARS)
K_DERIVATIVE_TERMS = tuple(
    [
        (exponent, int(coefficient) % PRIME)
        for exponent, coefficient in sp.Poly(derivative, *VARS, modulus=PRIME).terms()
    ]
    for derivative in K_DERIVATIVES
)


def monomials_at_most(degree: int) -> list[tuple[int, int, int]]:
    return [
        exponent
        for exponent in product(range(degree + 1), repeat=3)
        if sum(exponent) <= degree
    ]


def polynomial_terms(expression: sp.Expr):
    terms = sp.Poly(sp.expand(expression), *VARS, modulus=PRIME).terms()
    answer = []
    for exponent, coefficient in terms:
        value = int(coefficient) % PRIME
        if value:
            answer.append((exponent, value))
    return answer


def add_pivot(row: dict[int, int], pivots: dict[int, dict[int, int]]) -> None:
    while row:
        pivot = max(row)
        coefficient = row[pivot]
        if pivot not in pivots:
            inverse = pow(coefficient, PRIME - 2, PRIME)
            pivots[pivot] = {
                column: value * inverse % PRIME for column, value in row.items()
            }
            return
        existing = pivots[pivot]
        for column, value in existing.items():
            next_value = (row.get(column, 0) - coefficient * value) % PRIME
            if next_value:
                row[column] = next_value
            else:
                row.pop(column, None)


def filtered_dimension(
    common_pole: int,
    ambient_degree: int,
    cutoff_degree: int,
    gamma: int,
) -> int:
    # The gradient term raises polynomial degree by three.  Retain it in the
    # next pole block instead of clearing all levels to one denominator.
    column_degree = ambient_degree + 3
    low = monomials_at_most(cutoff_degree)
    ambient = monomials_at_most(column_degree)
    ordered_columns = [(0, monomial) for monomial in low]
    ordered_columns.extend(
        (0, monomial) for monomial in ambient if monomial not in set(low)
    )
    for pole in range(1, common_pole + 1):
        ordered_columns.extend((pole, monomial) for monomial in ambient)
    columns = {label: index for index, label in enumerate(ordered_columns)}
    low_count = len(low)
    pivots: dict[int, dict[int, int]] = {}

    for rational_pole in range(common_pole):
        logarithmic_weight = (gamma - rational_pole) % PRIME
        for axis, _variable in enumerate(VARS):
            for exponent in monomials_at_most(ambient_degree):
                row: dict[int, int] = {}
                if exponent[axis]:
                    derived = list(exponent)
                    derived[axis] -= 1
                    row[columns[(rational_pole, tuple(derived))]] = exponent[axis]
                for derivative_exponent, derivative_coefficient in K_DERIVATIVE_TERMS[axis]:
                    term = tuple(
                        exponent[index] + derivative_exponent[index] for index in range(3)
                    )
                    value = logarithmic_weight * derivative_coefficient % PRIME
                    column = columns[(rational_pole + 1, term)]
                    next_value = (row.get(column, 0) + value) % PRIME
                    if next_value:
                        row[column] = next_value
                    else:
                        row.pop(column, None)
                add_pivot(row, pivots)

        # The pole blocks are presentations of the same localization, not a
        # direct sum: P/K^m equals P*K/K^(m+1).
        transition_bound = ambient_degree - 4
        if transition_bound >= 0:
            for exponent in monomials_at_most(transition_bound):
                row = {columns[(rational_pole, exponent)]: 1}
                monomial = c ** exponent[0] * a ** exponent[1] * b ** exponent[2]
                for term, value in polynomial_terms(-monomial * K):
                    column = columns[(rational_pole + 1, term)]
                    next_value = (row.get(column, 0) + value) % PRIME
                    if next_value:
                        row[column] = next_value
                    else:
                        row.pop(column, None)
                add_pivot(row, pivots)

    killed_low = sum(pivot < low_count for pivot in pivots)
    return low_count - killed_low


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-pole", type=int, default=4)
    parser.add_argument("--max-ambient", type=int, default=18)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--gamma-numerator", type=int, default=-1)
    parser.add_argument("--gamma-denominator", type=int, default=2)
    arguments = parser.parse_args()
    gamma = (
        arguments.gamma_numerator
        * pow(arguments.gamma_denominator % PRIME, PRIME - 2, PRIME)
    ) % PRIME

    trace = []
    for common_pole in range(1, arguments.max_pole + 1):
        for ambient_degree in range(max(arguments.cutoff, 4 * common_pole), arguments.max_ambient + 1):
            dimension = filtered_dimension(
                common_pole, ambient_degree, arguments.cutoff, gamma
            )
            record = {
                "common_pole": common_pole,
                "ambient_degree": ambient_degree,
                "cutoff_degree": arguments.cutoff,
                "filtered_dimension": dimension,
            }
            trace.append(record)
            print(json.dumps(record, sort_keys=True), flush=True)

    print(
        json.dumps(
            {
                "schema": "marici.benincasa.physical_top_twisted_derham_calibration.v1",
                "prime": PRIME,
                "kinematics": [2, 3, 4],
                "twist_exponent": (
                    f"{arguments.gamma_numerator}/{arguments.gamma_denominator}"
                ),
                "generic_q_regulators_used": False,
                "published_generic_dimensional_rank": 7,
                "level_zero_image_dimension": trace[-1]["filtered_dimension"],
                "published_rank_reproduced": (
                    trace[-1]["filtered_dimension"] == 7
                ),
                "cutoff_degree": arguments.cutoff,
                "trace": trace,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
