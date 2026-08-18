"""Exact two-denominator product-pole calibration at generic Kummer weight."""

from __future__ import annotations

import argparse
import json
from itertools import product

import sympy as sp

from physical_single_q_twisted_derham_calibration import (
    Q_POLYNOMIALS,
    add_value,
    shifted,
)
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


PAIRS = {
    "lower": ("g1", "g2"),
    "g1_G12": ("g1", "G12"),
    "g2_G12": ("g2", "G12"),
}
EXPECTED = {"lower": 9, "g1_G12": 18, "g2_G12": 18}


def filtered_dimension(
    q_polynomials,
    k_depth: int,
    q_depth: int,
    ambient_degree: int,
    cutoff_degree: int,
    gamma: int,
) -> int:
    column_degree = ambient_degree + 4
    low_monomials = monomials_at_most(cutoff_degree)
    low_labels = [
        (0, *q_levels, monomial)
        for q_levels in product(range(min(1, q_depth) + 1), repeat=2)
        for monomial in low_monomials
    ]
    low_set = set(low_labels)
    ambient_monomials = monomials_at_most(column_degree)
    ordered_columns = list(low_labels)
    for k_pole in range(k_depth + 1):
        for q_levels in product(range(q_depth + 1), repeat=2):
            ordered_columns.extend(
                label
                for monomial in ambient_monomials
                if (label := (k_pole, *q_levels, monomial)) not in low_set
            )
    columns = {label: index for index, label in enumerate(ordered_columns)}
    low_count = len(low_labels)
    pivots = {}

    q_derivative_terms = [
        tuple(
            [
                (exponent, int(coefficient) % PRIME)
                for exponent, coefficient in sp.Poly(
                    sp.diff(q_polynomial, variable), *VARS, modulus=PRIME
                ).terms()
            ]
            for variable in VARS
        )
        for q_polynomial in q_polynomials
    ]

    # Exact differentials on the full labelled product-pole lattice.
    for k_pole in range(k_depth):
        for q_levels in product(range(q_depth + 1), repeat=2):
            if any(level > 0 and level == q_depth for level in q_levels):
                continue
            for axis in range(3):
                for exponent in monomials_at_most(ambient_degree):
                    row = {}
                    if exponent[axis]:
                        derived = list(exponent)
                        derived[axis] -= 1
                        add_value(
                            row,
                            columns[(k_pole, *q_levels, tuple(derived))],
                            exponent[axis],
                        )
                    for derivative_exponent, coefficient in K_DERIVATIVE_TERMS[axis]:
                        add_value(
                            row,
                            columns[
                                (
                                    k_pole + 1,
                                    *q_levels,
                                    shifted(exponent, derivative_exponent),
                                )
                            ],
                            (gamma - k_pole) * coefficient,
                        )
                    for q_index, q_pole in enumerate(q_levels):
                        if not q_pole:
                            continue
                        raised = list(q_levels)
                        raised[q_index] += 1
                        for derivative_exponent, coefficient in q_derivative_terms[q_index][axis]:
                            add_value(
                                row,
                                columns[
                                    (
                                        k_pole,
                                        *raised,
                                        shifted(exponent, derivative_exponent),
                                    )
                                ],
                                -q_pole * coefficient,
                            )
                    add_pivot(row, pivots)

    # Cayley--Menger localization transitions.
    for k_pole in range(k_depth):
        for q_levels in product(range(q_depth + 1), repeat=2):
            for exponent in monomials_at_most(ambient_degree - 4):
                row = {columns[(k_pole, *q_levels, exponent)]: 1}
                monomial = c ** exponent[0] * a ** exponent[1] * b ** exponent[2]
                for term, value in polynomial_terms(-monomial * K):
                    add_value(row, columns[(k_pole + 1, *q_levels, term)], value)
                add_pivot(row, pivots)

    # Independent localization transitions for each labelled denominator.
    for q_index, q_polynomial in enumerate(q_polynomials):
        for k_pole in range(k_depth + 1):
            for q_levels in product(range(q_depth + 1), repeat=2):
                if q_levels[q_index] == q_depth:
                    continue
                raised = list(q_levels)
                raised[q_index] += 1
                for exponent in monomials_at_most(ambient_degree - 1):
                    row = {columns[(k_pole, *q_levels, exponent)]: 1}
                    monomial = c ** exponent[0] * a ** exponent[1] * b ** exponent[2]
                    for term, value in polynomial_terms(-monomial * q_polynomial):
                        add_value(
                            row,
                            columns[(k_pole, *raised, term)],
                            value,
                        )
                    add_pivot(row, pivots)

    killed_low = sum(pivot < low_count for pivot in pivots)
    return low_count - killed_low


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", choices=sorted(PAIRS), required=True)
    parser.add_argument("--k-depth", type=int, default=2)
    parser.add_argument("--q-depth", type=int, default=2)
    parser.add_argument("--ambient", type=int, default=10)
    parser.add_argument("--cutoff", type=int, default=5)
    parser.add_argument("--gamma", type=int, default=5)
    arguments = parser.parse_args()
    names = PAIRS[arguments.pair]
    dimension = filtered_dimension(
        tuple(Q_POLYNOMIALS[name] for name in names),
        arguments.k_depth,
        arguments.q_depth,
        arguments.ambient,
        arguments.cutoff,
        arguments.gamma % PRIME,
    )
    expected = EXPECTED[arguments.pair]
    print(
        json.dumps(
            {
                "schema": "marici.benincasa.physical_two_q_twisted_derham_calibration.v1",
                "prime": PRIME,
                "kinematics": [2, 3, 4],
                "pair": names,
                "gamma": arguments.gamma,
                "k_depth": arguments.k_depth,
                "q_depth_each": arguments.q_depth,
                "ambient_degree": arguments.ambient,
                "cutoff_degree": arguments.cutoff,
                "deletion_closed_binary_pole_image_dimension": dimension,
                "expected_deletion_closed_rank": expected,
                "calibration_passed": dimension == expected,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
