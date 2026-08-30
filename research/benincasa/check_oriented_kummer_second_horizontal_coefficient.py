"""Second normal coefficient of the source-derived oriented g3 Kummer readout."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
E, sqrt_delta = sp.symbols("E sqrtDelta")


def main() -> None:
    substitution, _numerator, denominator = source.walls["g3"]
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)),
        t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    tangent = sp.Poly(sp.fraction(sp.together(tangent))[0], t, x, y, z).as_expr()

    tangent_E = sp.Poly(sp.expand(tangent.subs(z, E - x - y)), t)
    denominator_E = sp.expand(denominator.subs(z, E - x - y))
    leading, linear, constant = tangent_E.all_coeffs()
    discriminant = sp.factor(linear**2 - 4 * leading * constant)
    root_plus = (-linear + sqrt_delta) / (2 * leading)
    root_minus = (-linear - sqrt_delta) / (2 * leading)

    reciprocal_trace = sp.together(
        1 / denominator_E.subs(t, root_plus)
        + 1 / denominator_E.subs(t, root_minus)
    )
    reciprocal_trace = sp.factor(
        sp.cancel(reciprocal_trace).subs(sqrt_delta**2, discriminant)
    )
    rational = sp.factor(-E * reciprocal_trace)
    reduced_delta = sp.factor(discriminant / E)

    # Normalize by the nonzero special-fiber value.  This avoids selecting a
    # square-root branch while retaining the oriented Kummer normalization.
    r0 = sp.factor(rational.subs(E, 0))
    d0 = sp.factor(reduced_delta.subs(E, 0))
    # Expand rationally: if R/R0=1+a1 E+a2 E^2 and
    # Delta/Delta0=1+b1 E+b2 E^2, then multiply by
    # (Delta/Delta0)^(-1/2).  This avoids leaving cancellable radicals in
    # SymPy's expression tree.
    a1 = sp.factor(sp.diff(rational, E).subs(E, 0) / r0)
    a2 = sp.factor(sp.diff(rational, E, 2).subs(E, 0) / (2 * r0))
    b1 = sp.factor(sp.diff(reduced_delta, E).subs(E, 0) / d0)
    b2 = sp.factor(sp.diff(reduced_delta, E, 2).subs(E, 0) / (2 * d0))
    first = sp.factor(a1 - b1 / 2)
    second = sp.factor(a2 - b2 / 2 + 3 * b1**2 / 8 - a1 * b1 / 2)
    normalized = sp.factor(1 + first * E + second * E**2)
    numerator, denominator2 = map(sp.factor, sp.fraction(second))

    quartic = sp.factor(-16 * x**2 * y**2 - 8 * x * y * E**2
                        + 8 * (x + y) * E**3 - 5 * E**4)
    quartic0 = sp.factor(quartic.subs(E, 0))
    assert sp.gcd(sp.Poly(numerator, x, y), sp.Poly(quartic0, x, y)).total_degree() == 0

    result = {
        "schema": "marici.oriented-kummer-second-horizontal.v1",
        "normal_coordinate": "E=X1+X2+X3",
        "normalized_series_through_E2": str(sp.factor(normalized)),
        "relative_first_E_coefficient": str(first),
        "relative_second_E_coefficient": str(second),
        "second_coefficient_numerator": str(numerator),
        "second_coefficient_denominator": str(denominator2),
        "second_coefficient_poles": ["x", "y", "x+y"],
        "quartic_special_fiber_factor": str(quartic0),
        "quartic_pole": False,
        "readout_grade_two_nonzero": second != 0,
        "scope": (
            "source-derived oriented local scalar Kummer readout through second "
            "ordinary normal order; not the full localization connecting class"
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("oriented-kummer-second-horizontal.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
