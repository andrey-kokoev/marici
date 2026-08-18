"""Calibrate one literal source-denominator pole at generic Kummer weight.

The pole lattice is indexed by (K pole, q pole).  It retains exact-form
components and localization transitions along both axes.  The low subspace
is the deletion closure of polynomial forms at q-pole levels zero and one.
"""

from __future__ import annotations

import argparse
import json
from itertools import product

import sympy as sp

from physical_top_twisted_derham_calibration import (
    K,
    K_DERIVATIVE_TERMS,
    PRIME,
    VARS,
    a,
    add_pivot,
    b,
    c,
    monomials_at_most,
    polynomial_terms,
)


Q_POLYNOMIALS = {
    "g1": c + b + 2,
    "g2": c + a + 3,
    "G12": c + 9,
}


def shifted(exponent, delta):
    return tuple(exponent[index] + delta[index] for index in range(3))


def add_value(row, column, value):
    next_value = (row.get(column, 0) + value) % PRIME
    if next_value:
        row[column] = next_value
    else:
        row.pop(column, None)


def filtered_dimension(
    q_polynomial,
    k_depth: int,
    q_depth: int,
    ambient_degree: int,
    cutoff_degree: int,
    gamma: int,
) -> int:
    column_degree = ambient_degree + 4
    low_monomials = monomials_at_most(cutoff_degree)
    low_labels = [
        (0, q_pole, monomial)
        for q_pole in range(min(1, q_depth) + 1)
        for monomial in low_monomials
    ]
    ambient_monomials = monomials_at_most(column_degree)
    low_set = set(low_labels)
    ordered_columns = list(low_labels)
    for k_pole in range(k_depth + 1):
        for q_pole in range(q_depth + 1):
            ordered_columns.extend(
                label
                for monomial in ambient_monomials
                if (label := (k_pole, q_pole, monomial)) not in low_set
            )
    columns = {label: index for index, label in enumerate(ordered_columns)}
    low_count = len(low_labels)
    pivots = {}

    q_derivative_terms = tuple(
        [
            (exponent, int(coefficient) % PRIME)
            for exponent, coefficient in sp.Poly(
                sp.diff(q_polynomial, variable), *VARS, modulus=PRIME
            ).terms()
        ]
        for variable in VARS
    )

    # Exact twisted differentials.  The final q-pole primitive level is
    # omitted when n>0 because its derivative exits the declared truncation.
    for k_pole in range(k_depth):
        for q_pole in range(q_depth + 1):
            if q_pole > 0 and q_pole == q_depth:
                continue
            for axis in range(3):
                for exponent in monomials_at_most(ambient_degree):
                    row = {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        add_value(
                            row,
                            columns[(k_pole, q_pole, tuple(derived))],
                            exponent[axis],
                        )
                    for derivative_exponent, coefficient in K_DERIVATIVE_TERMS[axis]:
                        add_value(
                            row,
                            columns[
                                (
                                    k_pole + 1,
                                    q_pole,
                                    shifted(exponent, derivative_exponent),
                                )
                            ],
                            (gamma - k_pole) * coefficient,
                        )
                    if q_pole:
                        for derivative_exponent, coefficient in q_derivative_terms[axis]:
                            add_value(
                                row,
                                columns[
                                    (
                                        k_pole,
                                        q_pole + 1,
                                        shifted(exponent, derivative_exponent),
                                    )
                                ],
                                -q_pole * coefficient,
                            )
                    add_pivot(row, pivots)

    # K-localization transitions.
    for k_pole in range(k_depth):
        for q_pole in range(q_depth + 1):
            for exponent in monomials_at_most(ambient_degree - 4):
                row = {columns[(k_pole, q_pole, exponent)]: 1}
                monomial = c ** exponent[0] * a ** exponent[1] * b ** exponent[2]
                for term, value in polynomial_terms(-monomial * K):
                    add_value(row, columns[(k_pole + 1, q_pole, term)], value)
                add_pivot(row, pivots)

    # q-localization transitions.
    for k_pole in range(k_depth + 1):
        for q_pole in range(q_depth):
            for exponent in monomials_at_most(ambient_degree - 1):
                row = {columns[(k_pole, q_pole, exponent)]: 1}
                monomial = c ** exponent[0] * a ** exponent[1] * b ** exponent[2]
                for term, value in polynomial_terms(-monomial * q_polynomial):
                    add_value(row, columns[(k_pole, q_pole + 1, term)], value)
                add_pivot(row, pivots)

    killed_low = sum(pivot < low_count for pivot in pivots)
    return low_count - killed_low


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", choices=sorted(Q_POLYNOMIALS), required=True)
    parser.add_argument("--k-depth", type=int, default=2)
    parser.add_argument("--q-depth", type=int, default=2)
    parser.add_argument("--ambient", type=int, default=12)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--gamma", type=int, default=5)
    arguments = parser.parse_args()
    dimension = filtered_dimension(
        Q_POLYNOMIALS[arguments.q],
        arguments.k_depth,
        arguments.q_depth,
        arguments.ambient,
        arguments.cutoff,
        arguments.gamma % PRIME,
    )
    expected = 16 if arguments.q == "G12" else 8
    print(
        json.dumps(
            {
                "schema": "marici.benincasa.physical_single_q_twisted_derham_calibration.v1",
                "prime": PRIME,
                "kinematics": [2, 3, 4],
                "q": arguments.q,
                "gamma": arguments.gamma,
                "k_depth": arguments.k_depth,
                "q_depth": arguments.q_depth,
                "ambient_degree": arguments.ambient,
                "cutoff_degree": arguments.cutoff,
                "deletion_closed_level_zero_one_image_dimension": dimension,
                "expected_deletion_closed_rank": expected,
                "calibration_passed": dimension == expected,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
