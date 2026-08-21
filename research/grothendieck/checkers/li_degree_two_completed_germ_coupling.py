"""Exact polarization and high-precision reconnaissance of degree-two completion coupling."""

from __future__ import annotations

import mpmath as mp
import sympy as sp


def q(vector):
    a1, a2, a3 = vector
    return a1**2 + a1 * a2 + sp.Rational(3, 2) * a1 * a3 - 2 * a2**2


def bilinear(left, right):
    return sp.expand(q(tuple(left[i] + right[i] for i in range(3))) - q(left) - q(right))


def q_numeric(vector):
    a1, a2, a3 = vector
    return a1**2 + a1 * a2 + mp.mpf("1.5") * a1 * a3 - 2 * a2**2


def main() -> None:
    e = sp.symbols("e1:4")
    g = sp.symbols("g1:4")
    p = sp.symbols("p1:4")
    total = tuple(e[i] + g[i] + p[i] for i in range(3))
    exact_residual = sp.expand(
        q(total)
        - q(e)
        - q(g)
        - q(p)
        - bilinear(e, g)
        - bilinear(e, p)
        - bilinear(g, p)
    )
    assert exact_residual == 0

    mp.mp.dps = 80
    eg = mp.euler
    gamma1 = mp.stieltjes(1)
    gamma2 = mp.stieltjes(2)
    endpoint = (mp.mpf(1), mp.mpf("-0.5"), mp.mpf(1) / 3)
    archimedean = (
        -mp.log(mp.pi) / 2 - eg / 2 - mp.log(2),
        mp.pi**2 / 16,
        -7 * mp.zeta(3) / 24,
    )
    prime = (
        eg,
        -gamma1 - eg**2 / 2,
        gamma2 / 2 + eg * gamma1 + eg**3 / 3,
    )

    def cross(left, right):
        combined = tuple(left[i] + right[i] for i in range(3))
        return q_numeric(combined) - q_numeric(left) - q_numeric(right)

    pieces = {
        "endpoint_self": q_numeric(endpoint),
        "archimedean_self": q_numeric(archimedean),
        "prime_self": q_numeric(prime),
        "endpoint_archimedean_cross": cross(endpoint, archimedean),
        "endpoint_prime_cross": cross(endpoint, prime),
        "archimedean_prime_cross": cross(archimedean, prime),
    }
    coupled_total = sum(pieces.values())

    def odd(vector):
        a1, a2, a3 = vector
        return a1 - a2 - mp.mpf("1.5") * a3

    print("exact_polarization_residual=0")
    for name, value in pieces.items():
        print(f"{name}={mp.nstr(value, 30)}")
    print(f"coupled_total={mp.nstr(coupled_total, 30)}")
    print(f"odd_endpoint={mp.nstr(odd(endpoint), 30)}")
    print(f"odd_archimedean={mp.nstr(odd(archimedean), 30)}")
    print(f"odd_prime={mp.nstr(odd(prime), 30)}")
    print(f"odd_total={mp.nstr(odd(endpoint)+odd(archimedean)+odd(prime), 30)}")
    print("numeric_values_certified=False")


if __name__ == "__main__":
    main()
