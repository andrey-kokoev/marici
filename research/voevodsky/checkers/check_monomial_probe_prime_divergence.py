from __future__ import annotations

import json
import math


def von_mangoldt(n: int) -> float:
    prime = None
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            if prime is not None:
                return 0.0
            prime = p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        if prime is not None:
            return 0.0
        prime = m
    return math.log(prime) if prime is not None else 0.0


def gaussian_cos_integral(a: float, b: float) -> float:
    return math.sqrt(math.pi / a) * math.exp(-(b * b) / (4 * a))


def rayleigh(N: int, d: int, t: float, h: float) -> float:
    a = t + 2 * d * h
    denominator = gaussian_cos_integral(a, 0.0) - gaussian_cos_integral(a + h, 0.0)
    total = 0.0
    for n in range(2, N + 1):
        weight = von_mangoldt(n) / math.sqrt(n)
        b = math.log(n)
        cosine_integral = gaussian_cos_integral(a, b) - gaussian_cos_integral(a + h, b)
        total -= weight * cosine_integral / denominator
    return total


def main() -> None:
    t, h, N = 1.0, 0.5, 300
    degrees = [0, 10, 100, 1000, 10000]
    values = [rayleigh(N, d, t, h) for d in degrees]
    at_zero = -sum(von_mangoldt(n) / math.sqrt(n) for n in range(2, N + 1))
    errors = [abs(value - at_zero) for value in values]
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    assert errors[-1] < 0.02 * abs(at_zero)

    result = {
        "schema":"marici.voevodsky.monomial-probe-prime-divergence-check.v1",
        "status":"analytic_core_detects_low_frequency_divergence",
        "cutoff":N,
        "degrees":degrees,
        "rayleigh_values":values,
        "prime_multiplier_at_zero":at_zero,
        "analytic_polynomial_core_uniform_lower_bound":False,
        "degree_restricted_cofinal_system_excluded":False,
        "joint_source_regularization_excluded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
