#!/usr/bin/env python3
"""Numerical hostile check for the conditional first-Adams oriented margin.

This is not a proof: it tests the conservative lower bound
    det(G_res) >= det(Gram(W_L, W_2L))
against kappa_p^2/4, using only the ordinary window Gram.
"""

from __future__ import annotations

import json
import math


def window(t: float, q: float) -> float:
    # H(q)=int_q^infty exp(-pi*s^2) ds = erfc(sqrt(pi)*q)/2.
    root_pi = math.sqrt(math.pi)
    return 0.5 * (
        math.erfc(root_pi * (q + t)) - math.erfc(root_pi * (q - t))
    )


def simpson(f, a: float, b: float, n: int = 24000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4.0 * sum(f(a + h * j) for j in range(1, n, 2))
    total += 2.0 * sum(f(a + h * j) for j in range(2, n, 2))
    return total * h / 3.0


def R(x: float) -> float:
    alpha = math.sqrt(math.pi / 2.0)
    return 0.5 * x * math.erf(alpha * x) + math.exp(-0.5 * math.pi * x * x) / (
        math.pi * math.sqrt(2.0)
    )


def ordinary_window_determinant_closed(p: int) -> float:
    L = math.log(p)
    a = 2.0 * (R(2.0 * L) - R(0.0))
    d = 2.0 * (R(4.0 * L) - R(0.0))
    r = 2.0 * (R(3.0 * L) - R(L))
    return a * d - r * r


def ordinary_window_determinant_quadrature(p: int) -> float:
    L = math.log(p)
    radius = 2.0 * L + 8.0
    w1 = lambda q: window(L, q)
    w2 = lambda q: window(2.0 * L, q)
    a = simpson(lambda q: w1(q) ** 2, -radius, radius)
    d = simpson(lambda q: w2(q) ** 2, -radius, radius)
    r = simpson(lambda q: w1(q) * w2(q), -radius, radius)
    return a * d - r * r


def phi_prime(u: float) -> float:
    # Phi'_n(u) = -exp(u/2-x) * x * (8*x^2-30*x+15).
    total = 0.0
    eu = math.exp(2.0 * u)
    prefactor = math.exp(0.5 * u)
    for n in range(1, 1000):
        x = math.pi * n * n * eu
        term = -prefactor * math.exp(-x) * x * (8.0 * x * x - 30.0 * x + 15.0)
        total += term
        if n > 2 and abs(term) < 1e-300:
            break
    return total


def kappa(p: int) -> float:
    L = math.log(p)
    total = 0.0
    for k in range(1, 1000):
        term = p ** (-0.5 * k) * phi_prime(k * L)
        total += term
        if k > 2 and abs(term) < 1e-300:
            break
    return 2.0 * L * total


def primes_through(limit: int) -> tuple[int, ...]:
    values = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, math.isqrt(n) + 1)):
            values.append(n)
    return tuple(values)


def main() -> None:
    primes = primes_through(1000)
    quadrature_hostiles = {2, 3, 5, 7, 11, 17, 29, 53, 101, 997}
    rows = []
    for p in primes:
        det0 = ordinary_window_determinant_closed(p)
        quadrature_agrees = None
        if p in quadrature_hostiles:
            det_quad = ordinary_window_determinant_quadrature(p)
            assert abs(det0 - det_quad) <= 2e-10 * max(1.0, det0)
            quadrature_agrees = True
        kap = kappa(p)
        odd_cost = 0.25 * kap * kap
        rows.append(
            {
                "p": p,
                "ordinary_window_determinant_lower_bound": det0,
                "closed_formula_agrees_with_quadrature": quadrature_agrees,
                "kappa": kap,
                "oriented_cost": odd_cost,
                "lower_bound_minus_cost": det0 - odd_cost,
                "passes_conservative_margin": det0 > odd_cost,
            }
        )
    assert all(row["passes_conservative_margin"] for row in rows)
    print(json.dumps({
        "schema": "marici.nima.rh_first_adams_oriented_margin_numeric.v1",
        "scope": "numeric_hostile_not_proof",
        "uses_conservative_bound_M_phi_ignored": True,
        "prime_limit": 1000,
        "prime_count": len(primes),
        "quadrature_hostiles": sorted(quadrature_hostiles),
        "rows": rows,
        "verdict": "all_primes_through_1000_pass_conservative_oriented_margin",
    }, indent=2))


if __name__ == "__main__":
    main()
