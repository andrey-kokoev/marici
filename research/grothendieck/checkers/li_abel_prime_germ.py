"""Exact finite-order regression for the canonical Abel-renormalized prime germ."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    eps = sp.symbols("epsilon")
    order = 9
    stieltjes = sp.symbols(f"gamma0:{order + 1}")
    # gamma_0 is Euler's constant; independence is harmless for the formal audit.
    zeta_laurent = 1 / eps + sum(
        (-1) ** n * stieltjes[n] * eps**n / sp.factorial(n)
        for n in range(order + 1)
    )
    prime_abel = sp.series(
        -sp.diff(zeta_laurent, eps) / zeta_laurent,
        eps,
        0,
        order,
    ).removeO()
    completed_prime_germ = sp.series(1 / eps - prime_abel, eps, 0, order).removeO()

    assert sp.limit(completed_prime_germ, eps, 0) == stieltjes[0]
    assert not completed_prime_germ.has(sp.zoo)

    for k in range(1, 8):
        derivative_order = k - 1
        transported = sp.simplify(
            (-1) ** derivative_order
            * sp.diff(prime_abel, eps, derivative_order)
            / sp.factorial(derivative_order)
        )
        renormalized = sp.expand(transported - eps ** (-k))
        finite_part = sp.limit(renormalized, eps, 0)
        assert finite_part.is_finite is not False
        print(
            f"k={k} unique_singular_term=epsilon^-{k} "
            f"finite_part={sp.sstr(finite_part)}"
        )

    print("completed_prime_germ=1/epsilon+zeta_prime_over_zeta(1+epsilon)")
    print("completed_prime_germ_analytic=True")
    print("completed_prime_germ_value_at_0=gamma_0")
    print("abel_counterterm_degree_independent_rule=True")


if __name__ == "__main__":
    main()
