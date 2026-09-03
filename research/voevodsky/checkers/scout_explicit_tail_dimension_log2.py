from __future__ import annotations

import cmath
import json
import math


BERNOULLI_2K = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730]


def digamma_asymptotic(z: complex) -> complex:
    value = cmath.log(z) - 1 / (2 * z)
    for k, bernoulli in enumerate(BERNOULLI_2K, start=1):
        value -= bernoulli / (2 * k * z ** (2 * k))
    return value


def main() -> None:
    L = math.log(2)
    c_prime = math.log(2) / math.sqrt(2) + math.log(3) / math.sqrt(3) + math.log(2) / 2
    c_low = (0.5772156649015329 + math.pi / 2 + 3 * math.log(2) + math.log(math.pi)) / (4 * math.pi)

    def m_gamma_from_log(log_R: float) -> float:
        R = math.exp(log_R)
        z = complex(0.25, R / 2)
        return (digamma_asymptotic(z).real - math.log(math.pi)) / (4 * math.pi)

    def dimension_bound(log_R: float) -> float:
        R = math.exp(log_R)
        m_R = m_gamma_from_log(log_R)
        if m_R <= c_prime:
            return math.inf
        return (2 * L * R / math.pi) * (m_R + c_low) / (m_R - c_prime)

    lo, hi = 1.0, 40.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if m_gamma_from_log(mid) <= c_prime:
            lo = mid
        else:
            hi = mid
    threshold_log_R = hi

    lo, hi = threshold_log_R + 1e-8, threshold_log_R + 10
    phi = (1 + math.sqrt(5)) / 2
    for _ in range(250):
        x1 = hi - (hi - lo) / phi
        x2 = lo + (hi - lo) / phi
        if dimension_bound(x1) < dimension_bound(x2):
            hi = x2
        else:
            lo = x1
    optimum_log_R = (lo + hi) / 2
    R = math.exp(optimum_log_R)
    m_R = m_gamma_from_log(optimum_log_R)
    bound = dimension_bound(optimum_log_R)
    M = math.floor(bound)
    assert M + 1 > bound
    delta_lower = m_R - c_prime - (m_R + c_low) * (2 * L * R) / (math.pi * (M + 1))
    assert delta_lower > 0

    result = {
        "schema":"marici.voevodsky.explicit-tail-dimension-log2-scout.v1",
        "status":"nonrigorous_float_asymptotic_tail_dimension_scout",
        "L":"log(2)",
        "included_prime_powers":[2,3,4],
        "C_prime":format(c_prime, ".16g"),
        "C_low_gamma":format(c_low, ".16g"),
        "positivity_threshold_R":format(math.exp(threshold_log_R), ".16g"),
        "optimized_R":format(R, ".16g"),
        "m_R_gamma":format(m_R, ".16g"),
        "dimension_bound":format(bound, ".16g"),
        "sufficient_M":M,
        "delta_lower":format(delta_lower, ".16g"),
        "digamma_method":"six_term_asymptotic_at_large_imaginary_argument",
        "directed_interval_certified":False,
        "finite_schur_matrix_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
