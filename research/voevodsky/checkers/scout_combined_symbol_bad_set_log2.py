from __future__ import annotations

import cmath
import json
import math


BERNOULLI_2K = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730]
EULER_GAMMA = 0.5772156649015329


def digamma(z: complex) -> complex:
    shift = 0j
    while abs(z) < 12:
        shift -= 1 / z
        z += 1
    value = cmath.log(z) - 1 / (2*z)
    for k, b in enumerate(BERNOULLI_2K, start=1):
        value -= b / (2*k*z**(2*k))
    return value + shift


def m_gamma(u: float) -> float:
    return (digamma(complex(0.25, u/2)).real - math.log(math.pi)) / (4*math.pi)


def root_for_level(level: float) -> float:
    lo, hi = 0.0, 50.0
    for _ in range(180):
        mid = (lo+hi)/2
        if m_gamma(math.exp(mid)) < level:
            lo = mid
        else:
            hi = mid
    return math.exp(hi)


def main() -> None:
    L = math.log(2)
    coefficients = [(math.log(2)/math.sqrt(2), math.log(2)),
                    (math.log(3)/math.sqrt(3), math.log(3)),
                    (math.log(2)/2, 2*math.log(2))]
    c_prime = sum(c for c, _ in coefficients)
    c_low = (EULER_GAMMA + math.pi/2 + 3*math.log(2) + math.log(math.pi))/(4*math.pi)
    c_minus = c_low + c_prime  # attained at u=0
    deltas = [0.05, 0.1, 0.2, 0.4, 0.8]
    samples = 300000
    phi = (math.sqrt(5)-1)/2
    rows = []
    for delta in deltas:
        cutoff = root_for_level(c_prime + delta)
        bad = 0
        for k in range(1, samples+1):
            u = cutoff * ((k*phi) % 1.0)
            symbol = m_gamma(u) - sum(c*math.cos(a*u) for c, a in coefficients)
            if symbol < delta:
                bad += 1
        fraction = bad/samples
        measure_estimate = 2*cutoff*fraction
        dimension_estimate = (L*measure_estimate/math.pi)*(delta+c_minus)/delta
        rows.append({"delta":delta,"absolute_cutoff":cutoff,"bad_fraction":fraction,
                     "bad_measure_estimate":measure_estimate,"dimension_estimate":dimension_estimate})
    best = min(rows, key=lambda row: row["dimension_estimate"])
    result = {"schema":"marici.voevodsky.combined-symbol-bad-set-log2-scout.v1",
              "status":"nonrigorous_quasimontecarlo_bad_set_scout","L":"log(2)",
              "samples_per_delta":samples,"C_minus_exact_formula":"C_low_gamma+C_prime",
              "C_minus":c_minus,"rows":rows,"best_delta":best["delta"],
              "best_dimension_estimate":best["dimension_estimate"],
              "directed_interval_certified":False,"trace_dimension_computationally_feasible":False,
              "rh_implication":False,"passed":True}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
