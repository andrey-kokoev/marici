"""Exact inverse-Laplace transform of the Euler-product contribution to the squared xi resolvent."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x, t, a = sp.symbols("x t a", positive=True)
    gaussian_kernel = sp.exp(-a**2 / (4 * t)) / sp.sqrt(sp.pi * t)
    transform = sp.integrate(sp.exp(-x * t) * gaussian_kernel, (t, 0, sp.oo))
    expected = sp.exp(-a * sp.sqrt(x)) / sp.sqrt(x)
    assert sp.simplify(transform - expected) == 0

    coefficient = sp.symbols("q", positive=True)
    # For a prime power, a=log(n)>0 and q=Lambda(n)/sqrt(n).
    prime_kernel_atom = -coefficient * sp.exp(-a**2 / (4 * t)) / (
        2 * sp.sqrt(sp.pi * t)
    )
    transformed_atom = sp.integrate(
        sp.exp(-x * t) * prime_kernel_atom,
        (t, 0, sp.oo),
    )
    expected_prime_atom = -coefficient * sp.exp(-sp.sqrt(x) * a) / (2 * sp.sqrt(x))
    assert sp.simplify(transformed_atom - expected_prime_atom) == 0

    y = sp.symbols("y", positive=True)
    endpoint_resolvent = 1 / y
    endpoint_kernel = sp.exp(t / 4)
    endpoint_transform = sp.integrate(
        sp.exp(-(y + sp.Rational(1, 4)) * t) * endpoint_kernel,
        (t, 0, sp.oo),
    )
    assert sp.simplify(endpoint_transform - endpoint_resolvent) == 0

    print("sqrt_laplace_transform_residual=0")
    print("prime_heat_atom=-Lambda(n)/(2*sqrt(pi*t*n))*exp(-(log(n))^2/(4*t))")
    print("prime_heat_kernel_sign=nonpositive")
    print("endpoint_heat_kernel=exp(t/4)")
    print("pointwise_completion_coupling_required=True")


if __name__ == "__main__":
    main()
