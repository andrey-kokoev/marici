"""Exact weight identities for the conditional Li Cayley-domain audit."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    gamma = sp.symbols("gamma", real=True)
    rho = sp.Rational(1, 2) + sp.I * gamma
    u = sp.simplify(1 - 1 / rho)
    weight = sp.simplify((1 - u) * sp.conjugate(1 - u))
    expected_weight = 1 / (gamma**2 + sp.Rational(1, 4))
    assert sp.simplify(weight - expected_weight) == 0

    cayley = sp.simplify((1 + u) / (2 * sp.I * (1 - u)))
    assert sp.simplify(cayley - gamma) == 0

    domain_summand = sp.factor(gamma**2 * weight)
    assert sp.limit(domain_summand, gamma, sp.oo) == 1
    resolvent_summand = sp.simplify(weight / (gamma**2 + 1))
    assert sp.limit(resolvent_summand * gamma**4, gamma, sp.oo) == 1

    print("increment_weight=1/(gamma^2+1/4)")
    print("cayley_value=gamma")
    print("cyclic_H2_summand_limit=1")
    print("weighted_resolvent_summand_asymptotic=gamma^-4")
    print("cyclic_vector_in_H_domain_for_infinite_unbounded_divisor=False")


if __name__ == "__main__":
    main()
