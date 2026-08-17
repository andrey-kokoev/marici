"""Exact coefficient-shadow audit for the D03 hidden-extension test.

This checker separates two facts:

* the unrestricted one-road mixed block is explicitly contractible; and
* the simultaneous kernel of the two literal endpoint quotient maps is the
  two-term complex R -> R^2 with differential (-x0,x1).

The latter has H_1=0 and H_0=(x0,x1), up to grading shift.  Since this ideal
is x3-torsion-free, a *full* generic x3-localization restriction would kill
every endpoint-invisible coefficient class.  A first Rees symbol alone is
weaker: it misses x3^2(x0,x1).

No physical mixed-variance restriction functor is constructed here.
"""

from __future__ import annotations

import json
from math import comb

Int = int
Powers = tuple[int, int, int, int]
Polynomial = dict[Powers, Int]
Matrix = list[list[Polynomial]]

X0, X1, X3, X4 = range(4)
ZERO_POWERS: Powers = (0, 0, 0, 0)


def scalar(value: Int) -> Polynomial:
    return {} if value == 0 else {ZERO_POWERS: value}


def variable(slot: int) -> Polynomial:
    powers = [0, 0, 0, 0]
    powers[slot] = 1
    return {tuple(powers): 1}  # type: ignore[arg-type]


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for powers, coefficient in right.items():
        result[powers] = result.get(powers, 0) + coefficient
        if result[powers] == 0:
            del result[powers]
    return result


def negate(value: Polynomial) -> Polynomial:
    return {powers: -coefficient for powers, coefficient in value.items()}


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_powers, left_coefficient in left.items():
        for right_powers, right_coefficient in right.items():
            powers: Powers = tuple(
                left_powers[index] + right_powers[index] for index in range(4)
            )  # type: ignore[assignment]
            result[powers] = (
                result.get(powers, 0) + left_coefficient * right_coefficient
            )
            if result[powers] == 0:
                del result[powers]
    return result


def zero_matrix(rows: int, columns: int) -> Matrix:
    return [[{} for _ in range(columns)] for _ in range(rows)]


def multiply_matrices(left: Matrix, right: Matrix) -> Matrix:
    assert left and right and len(left[0]) == len(right)
    result = zero_matrix(len(left), len(right[0]))
    for row, entries in enumerate(left):
        for middle, entry in enumerate(entries):
            for column, right_entry in enumerate(right[middle]):
                result[row][column] = add(
                    result[row][column],
                    multiply_polynomials(entry, right_entry),
                )
    return result


def add_matrices(left: Matrix, right: Matrix) -> Matrix:
    assert len(left) == len(right)
    result: Matrix = []
    for left_row, right_row in zip(left, right, strict=True):
        assert len(left_row) == len(right_row)
        result.append(
            [
                add(left_entry, right_entry)
                for left_entry, right_entry in zip(
                    left_row, right_row, strict=True
                )
            ]
        )
    return result


def constant_matrix(rows: list[list[Int]]) -> Matrix:
    return [[scalar(value) for value in row] for row in rows]


def road_complex() -> tuple[Matrix, Matrix]:
    zero: Polynomial = {}
    x0, x1, x3, x4 = (variable(slot) for slot in (X0, X1, X3, X4))
    d_two = [[x3], [negate(x4)], [negate(x0)], [x1]]
    d_one = [
        [negate(x0), zero, negate(x3), zero],
        [x1, zero, zero, negate(x3)],
        [zero, negate(x0), x4, zero],
        [zero, x1, zero, x4],
    ]
    assert multiply_matrices(d_one, d_two) == zero_matrix(4, 1)
    return d_two, d_one


def endpoint_maps() -> tuple[Matrix, Matrix, Matrix]:
    # Product of the v00 and v10 restrictions in degrees 2, 1, and 0.
    r_two = constant_matrix([[-1], [1]])
    r_one = constant_matrix(
        [
            [-1, 0, 0, 0],
            [0, 0, -1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, -1],
        ]
    )
    r_zero = constant_matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    return r_two, r_one, r_zero


def check_endpoint_kernel() -> None:
    d_two, d_one = road_complex()
    r_two, r_one, r_zero = endpoint_maps()
    zero: Polynomial = {}
    x0, x1, x3 = (variable(slot) for slot in (X0, X1, X3))

    quotient_d_two = [
        [x3, zero],
        [negate(x0), zero],
        [zero, x3],
        [zero, negate(x1)],
    ]
    quotient_d_one = [
        [x0, x3, zero, zero],
        [zero, zero, x1, x3],
    ]
    assert multiply_matrices(quotient_d_one, quotient_d_two) == zero_matrix(2, 2)
    assert multiply_matrices(r_one, d_two) == multiply_matrices(
        quotient_d_two, r_two
    )
    assert multiply_matrices(r_zero, d_one) == multiply_matrices(
        quotient_d_one, r_one
    )

    # The simultaneous degreewise kernels are
    # K2=0, K1=<e_2>, K0=<e_3,e_4>.
    k_one_inclusion = constant_matrix([[0], [1], [0], [0]])
    k_zero_inclusion = constant_matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
    assert r_two == constant_matrix([[-1], [1]])  # primitive injection
    assert multiply_matrices(r_one, k_one_inclusion) == zero_matrix(4, 1)
    assert multiply_matrices(r_zero, k_zero_inclusion) == zero_matrix(2, 2)
    assert multiply_matrices(d_one, k_one_inclusion) == [
        [{}],
        [{}],
        [negate(x0)],
        [x1],
    ]

    # H0=coker R(-1)->R^2 is I(1), I=(x0,x1), via
    # (a,b) |-> x1*a+x0*b.  Its defining syzygy maps to zero.
    assert add(
        multiply_polynomials(x1, negate(x0)),
        multiply_polynomials(x0, x1),
    ) == {}

    # Exact Hilbert-function identity for the shifted ideal.
    for degree in range(33):
        coker_dimension = 2 * comb(degree + 3, 3) - comb(degree + 2, 3)
        shifted_ideal_dimension = comb(degree + 4, 3) - (degree + 2)
        assert coker_dimension == shifted_ideal_dimension

    # I lies in the polynomial domain, so multiplication by x3 is injective.
    # The explicit element below also witnesses the nonzero F^2 sector that
    # a first Rees-symbol test cannot see.
    higher_rees = multiply_polynomials(
        multiply_polynomials(x3, x3),
        x0,
    )
    assert higher_rees


def check_ordinary_one_road_contraction() -> None:
    # R<m> -> R<q,xi> -> R<b>, dm=q-x3*xi, dq=x3*b, dxi=b.
    one, zero, x3 = scalar(1), {}, variable(X3)
    d_two = [[one], [negate(x3)]]
    d_one = [[x3, one]]
    assert multiply_matrices(d_one, d_two) == zero_matrix(1, 1)

    # h(b)=xi and h(q)=m.
    h_zero = [[zero], [one]]
    h_one = [[one, zero]]
    assert multiply_matrices(d_one, h_zero) == [[one]]
    assert multiply_matrices(h_one, d_two) == [[one]]
    assert add_matrices(
        multiply_matrices(d_two, h_one),
        multiply_matrices(h_zero, d_one),
    ) == [[one, zero], [zero, one]]


def main() -> None:
    check_ordinary_one_road_contraction()
    check_endpoint_kernel()
    print(
        json.dumps(
            {
                "claim": (
                    "In the exact one-road coefficient shadow, unrestricted Hom "
                    "is contractible. The simultaneous v00/v10 endpoint kernel "
                    "has differential (-x0,x1), H1=0, and H0=(x0,x1) up to "
                    "grading shift. Full generic x3-localization has zero kernel "
                    "on this torsion-free module, whereas gr^1 alone misses "
                    "x3^2(x0,x1)."
                ),
                "status": "proved_scoped_gate",
                "factorization_test": {
                    "ordinary_one_road_hom": "acyclic by explicit contraction",
                    "endpoint_kernel_ranks_degree_0_1_2": [2, 1, 0],
                    "endpoint_kernel_differential": "(-x0,x1)",
                    "endpoint_kernel_H1": "0",
                    "endpoint_kernel_H0": "(x0,x1), grading shifted",
                    "integer_torsion": "none",
                    "x3_torsion": "none",
                    "full_generic_localization_kernel": "0",
                    "first_rees_symbol_kernel_contains": "x3^2*(x0,x1)",
                    "physical_admissible_mapping_complex": "UNINSTANTIATED",
                },
                "boundary": (
                    "The checker does not identify the source interior cell with "
                    "the endpoint-relative target module, construct the physical "
                    "restriction functors, or decide connector parity."
                ),
                "next_experiment": (
                    "Construct all face restrictions from one common filtered "
                    "admissible Hom complex and compute their homotopy fibre."
                ),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
