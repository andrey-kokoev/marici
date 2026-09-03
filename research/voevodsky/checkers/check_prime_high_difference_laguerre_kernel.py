from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    u, a = sp.symbols("u a", positive=True, real=True)
    z = a / u
    atom = u ** -sp.Rational(1, 2) * sp.exp(-z)

    for q in range(0, 8):
        derivative = sp.diff(atom, u, q)
        laguerre_form = ((-1) ** q * sp.factorial(q)
                         * u ** (-q - sp.Rational(1, 2))
                         * sp.exp(-z)
                         * sp.assoc_laguerre(q, -sp.Rational(1, 2), z))
        assert sp.simplify(derivative - laguerre_form) == 0

    # For odd q, the large-z leading sign of L_q^(-1/2) is negative.
    x = sp.symbols("x", positive=True, real=True)
    for q in [1, 3, 5, 7]:
        polynomial = sp.Poly(sp.assoc_laguerre(q, -sp.Rational(1, 2), x), x)
        assert polynomial.LC() == -sp.Rational(1, sp.factorial(q))

    result = {
        "schema":"marici.voevodsky.prime-high-difference-laguerre-kernel-check.v1",
        "status":"exact_derivative_kernel_verified",
        "derivative_orders_checked":"0..7",
        "identity":"d^q[u^-1/2 exp(-a/u)]/du^q=(-1)^q q! u^(-q-1/2) exp(-a/u)L_q^(-1/2)(a/u)",
        "odd_large_argument_laguerre_sign":"negative",
        "global_prime_sign":False,
        "rank_uniform_bound":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
