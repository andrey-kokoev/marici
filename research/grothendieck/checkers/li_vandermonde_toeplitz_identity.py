"""Exact finite-atomic regression for the Toeplitz--Vandermonde identity."""

from __future__ import annotations

import itertools
import math

import sympy as sp


def main() -> None:
    atoms = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
    weights = (sp.Integer(2), sp.Integer(3), sp.Integer(5), sp.Integer(7))

    for rank in range(1, 5):
        moment = lambda k: sp.simplify(
            sum(weight * atom ** (-k) for atom, weight in zip(atoms, weights))
        )
        toeplitz = sp.Matrix(rank, rank, lambda i, j: moment(i - j))

        # For an atomic measure, the 1/N! ordered integral reduces to one
        # contribution per N-element subset.
        vandermonde_sum = sp.Integer(0)
        for indices in itertools.combinations(range(len(atoms)), rank):
            product_weight = sp.prod(weights[i] for i in indices)
            vandermonde_square = sp.prod(
                (atoms[j] - atoms[i]) * (sp.conjugate(atoms[j]) - sp.conjugate(atoms[i]))
                for i, j in itertools.combinations(indices, 2)
            )
            vandermonde_sum += product_weight * vandermonde_square

        residual = sp.simplify(toeplitz.det() - vandermonde_sum)
        assert residual == 0
        print(f"rank={rank} determinant={toeplitz.det()} residual={residual}")

    print("all_exact_residuals_zero=True")
    print("support_cardinality=4")
    print("strict_through_rank_4=True")


if __name__ == "__main__":
    main()
