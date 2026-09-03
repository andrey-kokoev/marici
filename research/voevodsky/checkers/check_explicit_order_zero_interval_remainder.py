from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    u = sp.Symbol("u", nonnegative=True)
    ratio_squared = sp.factor((1 + u) ** 2 / (sp.Rational(1, 16) + u**2 / 4))
    derivative_numerator = sp.factor(sp.together(sp.diff(ratio_squared, u))).as_numer_denom()[0]
    critical_points = sp.solve(derivative_numerator, u)
    assert critical_points == [sp.Rational(1, 4)]
    maximum_squared = sp.simplify(ratio_squared.subs(u, critical_points[0]))
    assert maximum_squared == 20

    C0 = sp.pi + 4 + sp.log(20) / 2
    C_prime = sp.Integer(2)
    L = sp.Integer(1)
    cutoffs = [2**power for power in range(10, 17)]
    reserves = [sp.log(1 + sp.pi * (M + 1) / (2 * L)) - C0 - C_prime for M in cutoffs]
    positive_cutoffs = [M for M, reserve in zip(cutoffs, reserves) if reserve > 0]
    assert positive_cutoffs[0] == 32768
    assert reserves[cutoffs.index(16384)] < 0

    result = {
        "schema": "marici.voevodsky.explicit-order-zero-interval-remainder.v1",
        "status": "principal_order_zero_remainder_budget_verified",
        "digamma_minus_log_bound": "4",
        "ratio_maximizer": "1/4",
        "ratio_maximum_squared": "20",
        "standard_log_comparison_bound": "log(20)/2",
        "carleman_boundary_norm": "pi",
        "principal_order_zero_constant": str(C0),
        "relative_log_coefficient_eta": "0",
        "synthetic_C_local": "0",
        "synthetic_C_prime": "2",
        "checked_power_of_two_cutoffs": cutoffs,
        "exact_tail_reserves": [str(value) for value in reserves],
        "first_positive_checked_cutoff": positive_cutoffs[0],
        "localization_commutator_constant_materialized": False,
        "finite_low_block_positive_pivot_materialized": False,
        "next_gate": "interval-enclosed finite low-block ground eigenvalue and localization constant",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
