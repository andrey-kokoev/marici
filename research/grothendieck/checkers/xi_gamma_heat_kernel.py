"""Digamma-integral audit for the archimedean squared-resolvent heat kernel."""

from __future__ import annotations

import mpmath as mp
import sympy as sp


def main() -> None:
    # Exact transform normalization used under the digamma integral.
    x, t, a = sp.symbols("x t a", positive=True)
    kernel = sp.exp(-a**2 / (4 * t)) / sp.sqrt(sp.pi * t)
    transform = sp.integrate(sp.exp(-x * t) * kernel, (t, 0, sp.oo))
    assert sp.simplify(transform - sp.exp(-a * sp.sqrt(x)) / sp.sqrt(x)) == 0

    # The apparent r=0 singularity in the completed integrand is removable.
    r, tau = sp.symbols("r tau", positive=True)
    numerator = sp.exp(-r) - sp.exp(-r / 4 - r**2 / (16 * tau))
    integrand = numerator / (1 - sp.exp(-r))
    endpoint_limit = sp.simplify(sp.limit(integrand, r, 0, dir="+"))
    assert endpoint_limit == -sp.Rational(3, 4)

    # High-precision reconnaissance of the standard digamma representation.
    mp.mp.dps = 60
    residuals = []
    for y in (mp.mpf("0.6"), mp.mpf("1.0"), mp.mpf("2.5"), mp.mpf("7.0")):
        z = y / 2 + mp.mpf("0.25")
        integral = mp.quad(
            lambda q: (mp.exp(-q) - mp.exp(-z * q)) / (1 - mp.exp(-q)),
            [0, 1, mp.inf],
        )
        residual = -mp.euler + integral - mp.digamma(z)
        residuals.append(residual)
        assert abs(residual) < mp.mpf("1e-50")

    print("sqrt_laplace_transform_residual=0")
    print("gamma_kernel_integrand_limit_at_0=-3/4")
    print("digamma_integral_samples=4")
    print("maximum_digamma_residual=" + mp.nstr(max(abs(v) for v in residuals), 12))
    print("gamma_heat_kernel_formula_verified=True")
    print("numeric_values_certified=False")


if __name__ == "__main__":
    main()
