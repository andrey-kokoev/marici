"""Exact PNT-density saddle integral for the large-time prime heat kernel."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    t, u = sp.symbols("t u", positive=True)
    saddle_integral = sp.integrate(
        sp.exp(u / 2 - u**2 / (4 * t)),
        (u, 0, sp.oo),
    )
    expected_integral = sp.sqrt(sp.pi * t) * sp.exp(t / 4) * (
        1 + sp.erf(sp.sqrt(t) / 2)
    )
    assert sp.simplify(saddle_integral - expected_integral) == 0

    continuum_prime = sp.simplify(-saddle_integral / (2 * sp.sqrt(sp.pi * t)))
    expected_prime = -sp.exp(t / 4) * (1 + sp.erf(sp.sqrt(t) / 2)) / 2
    assert sp.simplify(continuum_prime - expected_prime) == 0

    endpoint_remainder = sp.simplify(sp.exp(t / 4) + continuum_prime)
    expected_remainder = sp.exp(t / 4) * sp.erfc(sp.sqrt(t) / 2) / 2
    assert sp.simplify(
        endpoint_remainder - expected_remainder.rewrite(sp.erf)
    ) == 0

    scaled_limit = sp.limit(endpoint_remainder * sp.sqrt(sp.pi * t), t, sp.oo)
    assert scaled_limit == 1

    print("pnt_saddle_log_n=t")
    print("continuum_prime=-exp(t/4)*(1+erf(sqrt(t)/2))/2")
    print("endpoint_plus_continuum_prime=exp(t/4)*erfc(sqrt(t)/2)/2")
    print("large_time_remainder_asymptotic=1/sqrt(pi*t)")
    print("ordinary_pnt_scale_reaches_spectral_heat_scale=False")


if __name__ == "__main__":
    main()
