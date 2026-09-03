from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def main() -> None:
    primes = list(sp.primerange(2, 50))
    product = Fraction(1, 1)
    rows = []
    Q = 1
    phi = 1
    for p in primes:
        Q *= p
        phi *= p - 1
        product *= Fraction(p - 1, p)
        assert product == Fraction(phi, Q)
        rows.append({"p":p, "affinity_squared":f"{product.numerator}/{product.denominator}"})

    # Each new prime strictly decreases the Hellinger affinity.
    values = [float(sp.sqrt(sp.Rational(Fraction(row["affinity_squared"]).numerator,
                                                Fraction(row["affinity_squared"]).denominator)))
              for row in rows]
    assert all(values[i + 1] < values[i] for i in range(len(values) - 1))

    result = {
        "schema":"marici.voevodsky.finite-density-corona-coupling-check.v1",
        "status":"hellinger_product_verified",
        "prime_cutoff":primes[-1],
        "affinity":"sqrt(phi(Q)/Q)=product_(p|Q)sqrt(1-1/p)",
        "strictly_decreasing":True,
        "infinite_limit_zero":"uses divergence of sum_p 1/p",
        "naive_cross_coupling_survives":False,
        "renormalized_nonlocal_coupling_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
