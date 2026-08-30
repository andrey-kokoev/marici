"""Exact Cauchy-jet realization and cocycle law for the Li feature family."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, w = sp.symbols("s w")
    cauchy = 1 / (s - w)

    for n in range(1, 13):
        direct = sp.expand(1 - (1 - 1 / s) ** n)
        binomial = sum(
            (-1) ** (j + 1) * sp.binomial(n, j) / s**j
            for j in range(1, n + 1)
        )
        jet = sum(
            (-1) ** (j + 1)
            * sp.binomial(n, j)
            / sp.factorial(j - 1)
            * sp.diff(cauchy, w, j - 1).subs(w, 0)
            for j in range(1, n + 1)
        )
        assert sp.cancel(direct - binomial) == 0
        assert sp.cancel(direct - jet) == 0

    u = sp.symbols("u")
    m, n = sp.symbols("m n", integer=True, positive=True)
    feature_m = 1 - u**m
    feature_n = 1 - u**n
    feature_mn = 1 - u ** (m + n)
    cocycle_residual = sp.expand(feature_mn - (feature_m + u**m * feature_n))
    assert cocycle_residual == 0

    print("checked_orders=1..12")
    print("cauchy_jet_residuals_zero=True")
    print("feature_formula=1-(1-1/s)^n")
    print("feature_cocycle=V_(m+n)-V_m-u^m*V_n")
    print(f"feature_cocycle_residual={cocycle_residual}")
    print("positive_source_gram_constructed=False")


if __name__ == "__main__":
    main()
