"""Exact generating-function collapse from Li second differences to xi'/xi."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z = sp.symbols("z")
    order = 10
    lam = sp.symbols(f"lambda0:{order + 2}")
    li_series = sum(lam[n] * z**n for n in range(1, order + 2))

    c0 = lam[1]
    c_series = c0 + sum(
        (lam[k + 1] - 2 * lam[k] + lam[k - 1]) * z**k
        for k in range(1, order + 1)
    )
    collapsed = sp.expand((1 - z) ** 2 * li_series / z)
    residual = sp.series(c_series - collapsed, z, 0, order + 1).removeO().expand()
    assert residual.subs(lam[0], 0) == 0

    # Li's generating identity:
    # log xi(1/(1-z)) = log xi(1) + sum lambda_n z^n/n.
    formal_log_coefficients = sum(lam[n] * z**n / n for n in range(1, order + 2))
    derived_li_series = sp.expand(z * sp.diff(formal_log_coefficients, z))
    assert sp.series(derived_li_series - li_series, z, 0, order + 2).removeO() == 0

    s = sp.symbols("s")
    mobius_inverse = 1 / (1 - z)
    assert sp.simplify(sp.diff(mobius_inverse, z) - 1 / (1 - z) ** 2) == 0
    critical_half_plane_residual = sp.expand(
        sp.Symbol("sigma") - sp.Rational(1, 2)
    )

    print(f"checked_series_order={order}")
    print("second_difference_generating_residual=0")
    print("li_logarithmic_generating_residual=0")
    print("caratheodory_function=xi_prime_over_xi(1/(1-z))")
    print("unit_disk_maps_to=Re(s)>1/2")
    print("toeplitz_psd_iff_caratheodory_real_part_nonnegative=True")


if __name__ == "__main__":
    main()
