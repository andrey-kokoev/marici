"""Trace-norm expansion of the oriented g3 Kummer residue difference."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
energy, square_root = sp.symbols("E sqrtDelta")


def main() -> None:
    substitution, numerator, denominator = source.walls["g3"]
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)),
        t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    tangent = sp.Poly(
        sp.fraction(sp.together(tangent))[0], t, x, y, z
    ).as_expr()

    tangent_e = sp.Poly(sp.expand(tangent.subs(z, energy - x - y)), t)
    denominator_e = sp.expand(denominator.subs(z, energy - x - y))
    leading, linear, constant = tangent_e.all_coeffs()
    discriminant = sp.factor(linear**2 - 4 * leading * constant)
    root_plus = (-linear + square_root) / (2 * leading)
    root_minus = (-linear - square_root) / (2 * leading)

    reciprocal_trace = sp.together(
        1 / denominator_e.subs(t, root_plus)
        + 1 / denominator_e.subs(t, root_minus)
    )
    reciprocal_trace = sp.factor(
        sp.cancel(reciprocal_trace).subs(square_root**2, discriminant)
    )

    # q*(rho_plus-rho_minus) = rational_part/sqrt(discriminant/E).
    rational_part = sp.factor(-energy * reciprocal_trace)
    reduced_discriminant = sp.factor(discriminant / energy)
    rational_0 = sp.factor(rational_part.subs(energy, 0))
    rational_1 = sp.factor(sp.diff(rational_part, energy).subs(energy, 0))
    delta_0 = sp.factor(reduced_discriminant.subs(energy, 0))
    delta_1 = sp.factor(sp.diff(reduced_discriminant, energy).subs(energy, 0))
    relative_first = sp.factor(
        rational_1 / rational_0 - delta_1 / (2 * delta_0)
    )

    expected = (4 * x**2 + 19 * x * y + 4 * y**2) / (4 * x * y * (x + y))
    assert sp.factor(relative_first - expected) == 0

    print(json.dumps({
        "schema": "marici.oriented-kummer-first-horizontal.v1",
        "reduced_discriminant": str(reduced_discriminant),
        "leading_rational_part": str(rational_0),
        "leading_reduced_discriminant": str(delta_0),
        "relative_first_E_coefficient": str(relative_first),
        "first_coefficient_poles": ["x", "y", "x+y"],
        "quartic_pole": False,
        "scope": "oriented local scalar pairing; not the full localization connecting class",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
