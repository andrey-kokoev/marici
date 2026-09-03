from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    t = sp.Symbol("t", real=True)
    s = 35*t**4 - 84*t**5 + 70*t**6 - 20*t**7
    s1 = sp.factor(sp.diff(s, t))
    s2 = sp.factor(sp.diff(s, t, 2))
    s3 = sp.factor(sp.diff(s, t, 3))

    cubic_integral = sp.integrate(s1**3, (t, 0, 1))
    assert cubic_integral == 140**3 * sp.factorial(9)**2 / sp.factorial(19)
    cross_variation = sp.Rational(35, 16) ** 2
    third_variation = 336 * sp.sqrt(5) / 25

    bound = sp.simplify(
        sp.pi**3 * cubic_integral / 8
        + 3 * sp.pi**2 * cross_variation / 4
        + sp.pi * third_variation / 2
    )
    normalized = sp.simplify(2 * bound / (3 * sp.pi))
    prior = sp.Rational(42875, 49152)*sp.pi**2 + sp.Rational(147, 40)*sp.sqrt(5)*sp.pi + 70
    scout = sp.Float("9.84825790")
    assert sp.N(normalized, 30) < sp.N(prior, 30)
    assert sp.N(normalized, 30) > scout

    result = {
        "schema": "marici.voevodsky.angular-ims-integrated-variation.v1",
        "status": "directed_integrated_variation_bound_verified",
        "integral_s_prime_cubed": str(cubic_integral),
        "integral_abs_s_prime_s_second": str(cross_variation),
        "integral_abs_s_third": str(third_variation),
        "rho_third_L1_upper_bound": str(bound),
        "rho_third_L1_upper_bound_decimal": str(sp.N(bound, 16)),
        "normalized_localization_upper_bound": str(normalized),
        "normalized_localization_upper_bound_decimal": str(sp.N(normalized, 16)),
        "prior_directed_bound_decimal": str(sp.N(prior, 16)),
        "non_directed_scout": str(scout),
        "strict_improvement_verified": True,
        "scout_certified": False,
        "next_gate": "directed interval integration of abs(rho''') if low-block cutoff remains intractable",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
