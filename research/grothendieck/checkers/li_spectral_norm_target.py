"""Exact Li pair-norm identity and its off-critical circularity residual."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    sigma, gamma = sp.symbols("sigma gamma", real=True)
    rho = sigma + sp.I * gamma
    u = sp.cancel((rho - 1) / rho)
    modulus_residual = sp.factor(sp.simplify(u * sp.conjugate(u) - 1))

    theta = sp.symbols("theta", real=True)
    n = sp.symbols("n", integer=True, positive=True)
    unit = sp.exp(sp.I * theta)
    paired_li = 2 - unit**n - unit ** (-n)
    squared_feature = sp.expand((1 - unit**n) * (1 - unit ** (-n)))
    norm_residual = sp.simplify(paired_li - squared_feature)

    expected_modulus_residual = sp.factor((1 - 2 * sigma) / (sigma**2 + gamma**2))
    assert sp.simplify(modulus_residual - expected_modulus_residual) == 0
    assert norm_residual == 0
    assert modulus_residual.subs(sigma, sp.Rational(1, 2)) == 0

    print(f"u_modulus_squared_minus_one={modulus_residual}")
    print("unit_modulus_iff_sigma_one_half=True")
    print(f"paired_li_minus_squared_feature={norm_residual}")
    print("conditional_pair_identity=2-u^n-u^(-n)=|1-u^n|^2")
    print("source_side_norm_constructed=False")


if __name__ == "__main__":
    main()
