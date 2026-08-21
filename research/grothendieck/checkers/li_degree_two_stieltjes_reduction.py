"""Exact reduction of the degree-two Li channels to three Stieltjes constants."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t = sp.symbols("t")
    gamma1, gamma2 = sp.symbols("gamma_1 gamma_2", real=True)
    gamma0 = sp.EulerGamma

    # t*zeta(1+t), through the order needed for lambda_1..lambda_3.
    zeta_regular = 1 + gamma0 * t - gamma1 * t**2 + gamma2 * t**3 / 2
    # Write the half-gamma Taylor coefficients explicitly. This avoids
    # relying on a CAS simplifier to normalize polygamma values at 1/2.
    half_gamma_series = (
        sp.loggamma(sp.Rational(1, 2))
        + (-sp.EulerGamma - 2 * sp.log(2)) * t / 2
        + sp.pi**2 * t**2 / 16
        - 7 * sp.zeta(3) * t**3 / 24
    )
    log_xi_series = (
        sp.log(1 + t)
        + sp.log(zeta_regular)
        - (1 + t) * sp.log(sp.pi) / 2
        + half_gamma_series
    ).series(t, 0, 4).removeO().expand()

    a = [sp.expand(log_xi_series).coeff(t, j) for j in range(4)]
    expected_a1 = 1 + gamma0 / 2 - sp.log(4 * sp.pi) / 2
    expected_a2 = -sp.Rational(1, 2) - gamma1 - gamma0**2 / 2 + sp.pi**2 / 16
    expected_a3 = (
        sp.Rational(1, 3)
        + gamma2 / 2
        + gamma0 * gamma1
        + gamma0**3 / 3
        - 7 * sp.zeta(3) / 24
    )
    assert sp.simplify(a[1] - expected_a1) == 0
    assert sp.simplify(a[2] - expected_a2) == 0
    assert sp.simplify(a[3] - expected_a3) == 0

    l1 = a[1]
    l2 = 2 * a[1] + 2 * a[2]
    l3 = 3 * a[1] + 6 * a[2] + 3 * a[3]
    odd_channel = sp.factor((l1 + 2 * l2 - l3) / 2)
    coupled = sp.factor((l1 * l3 + 2 * l1 * l2 - l1**2 - l2**2) / 2)

    # Universal expressions in the Taylor coefficients of log xi(1+t).
    A1, A2, A3 = sp.symbols("a_1 a_2 a_3")
    generic_l1 = A1
    generic_l2 = 2 * A1 + 2 * A2
    generic_l3 = 3 * A1 + 6 * A2 + 3 * A3
    generic_odd = sp.factor((generic_l1 + 2 * generic_l2 - generic_l3) / 2)
    generic_coupled = sp.factor(
        (generic_l1 * generic_l3 + 2 * generic_l1 * generic_l2 - generic_l1**2 - generic_l2**2) / 2
    )

    print("stieltjes_reduction_residual_zero=True")
    print(f"lambda_1={sp.sstr(l1)}")
    print(f"lambda_2={sp.sstr(sp.factor(l2))}")
    print(f"lambda_3={sp.sstr(sp.factor(l3))}")
    print(f"odd_channel_in_logxi_jets={generic_odd}")
    print(f"coupled_channel_in_logxi_jets={generic_coupled}")
    print(f"odd_channel_stieltjes_operation_count={sp.count_ops(odd_channel)}")
    print(f"coupled_channel_stieltjes_operation_count={sp.count_ops(coupled)}")


if __name__ == "__main__":
    main()
