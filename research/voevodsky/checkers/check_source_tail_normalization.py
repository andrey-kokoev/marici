from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    t = sp.symbols("t", positive=True, real=True)
    u = sp.symbols("u", real=True)
    gaussian_integral = sp.integrate(sp.exp(-t * u**2), (u, -sp.oo, sp.oo))
    gamma_constant = sp.simplify(-sp.log(sp.pi) * gaussian_integral / (4 * sp.pi))
    expected_gamma_constant = -sp.log(sp.pi) / (4 * sp.sqrt(sp.pi * t))
    assert sp.simplify(gamma_constant - expected_gamma_constant) == 0

    x = sp.symbols("x", real=True)
    inverse_gaussian = sp.integrate(sp.exp(-t * u**2) * sp.exp(sp.I * u * x), (u, -sp.oo, sp.oo)) / (2 * sp.pi)
    expected_inverse = sp.exp(-x**2 / (4 * t)) / (2 * sp.sqrt(sp.pi * t))
    assert sp.simplify(inverse_gaussian - expected_inverse) == 0

    result = {
        "schema":"marici.voevodsky.source-tail-normalization-check.v1",
        "status":"gamma_and_prime_tail_normalizations_frozen",
        "fourier_inverse":"(2*pi)^-1 integral h(u) exp(i*u*x) du",
        "gamma_multiplier":"[Re psi(1/4+i*u/2)-log(pi)]/(4*pi)",
        "gamma_scale":"1/(4*pi)",
        "prime_form":"-sum_(n>=2) Lambda(n)/sqrt(n) Re autocorrelation(log n)",
        "prime_absolute_constant":"sum_(log n<=2L) Lambda(n)/sqrt(n)",
        "gaussian_gamma_constant_verified":True,
        "gaussian_prime_transform_verified":True,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
