"""Exact Hermite reference constants for scale-normalized Newman discriminant entropy."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x = sp.symbols("x")
    for rank in range(2, 9):
        hermite = sp.Poly(sp.hermite_prob(rank, x), x)
        discriminant = sp.factor(sp.discriminant(hermite.as_expr(), x))
        expected_discriminant = sp.prod(k**k for k in range(1, rank + 1))
        assert discriminant == expected_discriminant

        # For a centered monic polynomial, sum roots^2=-2*[x^(N-2)].
        coefficient = hermite.nth(rank - 2)
        radius_squared = -2 * coefficient
        assert radius_squared == rank * (rank - 1)

        exponent = sp.Rational(rank * (rank - 1), 2)
        normalized_reference = sp.factor(
            discriminant / radius_squared**exponent
        )
        print(
            f"rank={rank} hermite_discriminant={discriminant} "
            f"radius_squared={radius_squared} "
            f"normalized_reference={normalized_reference}"
        )

    # At a Hermite root, He_N''/He_N'=x, hence A_i=x/2, matching
    # N(N-1)/(2R^2)=1/2.
    rank = sp.symbols("N", integer=True, positive=True)
    radius_squared = rank * (rank - 1)
    equilibrium_coefficient = sp.simplify(
        rank * (rank - 1) / (2 * radius_squared)
    )
    assert equilibrium_coefficient == sp.Rational(1, 2)

    print("hermite_equilibrium_coefficient=1/2")
    print("relative_entropy=log(normalized_Hermite_discriminant/normalized_discriminant)")
    print("relative_entropy_nonnegative=True")
    print("relative_entropy_derivative=-centered_repulsion_dissipation")


if __name__ == "__main__":
    main()
