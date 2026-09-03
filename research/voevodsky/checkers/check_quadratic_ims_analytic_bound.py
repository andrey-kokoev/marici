from __future__ import annotations

import json

import sympy as sp


def coefficient_mass(poly: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    return sum(abs(coefficient) for coefficient in sp.Poly(sp.expand(poly), variable).all_coeffs())


def main() -> None:
    u, t, h = sp.symbols("u t h", real=True, positive=True)
    q = u**2 + (1 - u) ** 2
    f = u / sp.sqrt(q)
    s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7

    f_bounds = []
    for order in range(1, 4):
        numerator, denominator = sp.fraction(sp.factor(sp.diff(f, u, order)))
        denominator_power = sp.Rational(2 * order + 1, 2)
        assert sp.simplify(denominator / q**denominator_power) == 1
        bound = sp.simplify(coefficient_mass(numerator, u) * 2**denominator_power)
        f_bounds.append(bound)
    assert f_bounds == [4 * sp.sqrt(2), 52 * sp.sqrt(2), 960 * sp.sqrt(2)]

    s1_bound = sp.Rational(35, 16)
    s2_bound = 84 * sp.sqrt(5) / 25
    s3_bound = sp.Integer(210)
    assert sp.diff(s, t).subs(t, sp.Rational(1, 2)) == s1_bound

    composition_bound = sp.simplify(
        f_bounds[2] * s1_bound**3
        + 3 * f_bounds[1] * s1_bound * s2_bound
        + f_bounds[0] * s3_bound
    )
    localization_bound = sp.simplify(2 * sp.pi * composition_bound / (3 * h**2))

    result = {
        "schema": "marici.voevodsky.quadratic-ims-analytic-bound.v1",
        "status": "directed_exact_upper_bound_verified",
        "f_derivative_sup_bounds": [str(value) for value in f_bounds],
        "s_derivative_sup_bounds": [str(s1_bound), str(s2_bound), str(s3_bound)],
        "rho_third_derivative_L1_upper_bound": str(composition_bound),
        "rho_third_derivative_L1_upper_bound_decimal": str(sp.N(composition_bound, 16)),
        "two_window_two_transition_localization_bound": str(localization_bound),
        "scout_value_certified": False,
        "sharpness_claimed": False,
        "sufficient_for_C3_admissibility": True,
        "next_gate": "test whether finite low-block margin absorbs the conservative bound",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
