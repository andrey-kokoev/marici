from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    t, h = sp.symbols("t h", real=True, positive=True)
    s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7
    rho1 = sp.sin(sp.pi * s / 2)
    rho2 = sp.cos(sp.pi * s / 2)
    assert sp.simplify(rho1**2 + rho2**2) == 1
    for order in range(1, 4):
        assert sp.diff(rho1, t, order).subs(t, 0) == 0
        assert sp.diff(rho1, t, order).subs(t, 1) == 0
        assert sp.diff(rho2, t, order).subs(t, 0) == 0
        assert sp.diff(rho2, t, order).subs(t, 1) == 0

    s1 = sp.Rational(35, 16)
    s2 = 84 * sp.sqrt(5) / 25
    s3 = sp.Integer(210)
    composition_bound = sp.simplify(
        sp.pi**3 * s1**3 / 8
        + 3 * sp.pi**2 * s1 * s2 / 4
        + sp.pi * s3 / 2
    )
    general_localization_bound = sp.simplify(2 * sp.pi * composition_bound / (3 * h**2))
    normalized_bound = sp.simplify(general_localization_bound.subs(h, sp.pi))

    scout = sp.Float("9.84825790")
    assert sp.N(normalized_bound, 20) > scout

    result = {
        "schema": "marici.voevodsky.angular-quadratic-ims-bound.v1",
        "status": "directed_angular_quadratic_bound_verified",
        "square_partition_identity": True,
        "endpoint_derivatives_through_order_three_vanish": True,
        "rho_third_derivative_L1_upper_bound": str(composition_bound),
        "rho_third_derivative_L1_upper_bound_decimal": str(sp.N(composition_bound, 16)),
        "general_two_window_two_transition_bound": str(general_localization_bound),
        "normalized_h_theta_pi_bound": str(normalized_bound),
        "normalized_h_theta_pi_bound_decimal": str(sp.N(normalized_bound, 16)),
        "non_directed_scout": str(scout),
        "scout_certified": False,
        "directed_bound_is_above_scout": True,
        "next_gate": "compare certified normalized bound against finite low-block margin",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
