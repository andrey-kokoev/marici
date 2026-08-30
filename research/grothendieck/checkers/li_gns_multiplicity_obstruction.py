"""Exact finite-atomic witness that scalar moment GNS records mass, not eigenspace multiplicity."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z", nonzero=True)
    multiplicity = 3
    max_degree = 5

    # Model A: one scalar atom with mass m.
    scalar_moments = [multiplicity * z**k for k in range(max_degree + 1)]

    # Model B: m identical one-dimensional copies, each with unit mass.
    repeated_moments = [sum(z**k for _ in range(multiplicity)) for k in range(max_degree + 1)]
    assert all(sp.simplify(a - b) == 0 for a, b in zip(scalar_moments, repeated_moments))

    # The scalar moment Gram has rank one irrespective of the positive mass.
    gram = sp.Matrix(
        max_degree + 1,
        max_degree + 1,
        lambda i, j: multiplicity * z**i * z ** (-j),
    )
    assert gram.rank() == 1

    scalar_operator = sp.Matrix([[z]])
    repeated_operator = sp.eye(multiplicity) * z
    assert scalar_operator.eigenvals()[z] == 1
    assert repeated_operator.eigenvals()[z] == multiplicity

    print(f"encoded_atomic_mass={multiplicity}")
    print("scalar_and_repeated_moments_equal=True")
    print("scalar_cyclic_gram_rank=1")
    print("scalar_operator_eigen_multiplicity=1")
    print(f"amplified_operator_eigen_multiplicity={multiplicity}")
    print("moments_do_not_force_operator_multiplicity=True")


if __name__ == "__main__":
    main()
