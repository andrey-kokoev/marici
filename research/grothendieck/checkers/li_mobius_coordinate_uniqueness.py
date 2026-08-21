"""Exact uniqueness of the normalized Möbius coordinate intertwining reflection and inversion."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s = sp.symbols("s")
    a, b, c, d = sp.symbols("a b c d")
    mobius = (a * s + b) / (c * s + d)

    # Pole at 0 forces d=0; value 1 at infinity forces a=c != 0.
    normalized = sp.cancel(mobius.subs({d: 0, c: a}))
    reflected = sp.cancel(normalized.subs(s, 1 - s))
    inverse = sp.cancel(1 / normalized)
    numerator = sp.Poly(sp.together(reflected - inverse).as_numer_denom()[0], s)
    coefficients = [sp.factor(coefficient) for coefficient in numerator.all_coeffs()]
    assert coefficients == [-b * (a + b)]
    # The branch b=0 makes u identically one: its Möbius determinant -a*b
    # vanishes. Nonconstancy therefore leaves only a+b=0.
    solution = {b: -a}

    unique = sp.cancel(normalized.subs(solution))
    assert sp.simplify(unique - (s - 1) / s) == 0
    assert sp.simplify(unique.subs(s, 1 - s) - 1 / unique) == 0
    assert sp.simplify(unique.subs(s, sp.Rational(1, 2)) + 1) == 0

    print("normalizations=pole_at_0,value_1_at_infinity")
    print("intertwining_solution=b=-a")
    print("unique_coordinate=(s-1)/s")
    print("reflection_center_maps_to=-1")
    print("uniqueness_residual=0")


if __name__ == "__main__":
    main()
