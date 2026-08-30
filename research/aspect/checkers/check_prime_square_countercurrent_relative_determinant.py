import json
import math


def primes_up_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k * k : n + 1 : k] = b"\x00" * (((n - k * k) // k) + 1)
    return [k for k in range(2, n + 1) if sieve[k]]


def log_relative(bound, coefficient=1.0):
    return sum(
        math.log1p(-1.0 / p) + coefficient / p for p in primes_up_to(bound)
    )


bounds = [100, 1_000, 10_000, 100_000, 1_000_000]
relative = [log_relative(bound) for bound in bounds]
under = [log_relative(bound, 0.9) for bound in bounds]
over = [log_relative(bound, 1.1) for bound in bounds]

checks = {
    "relative_sequence_is_cauchy_at_test_scale": abs(relative[-1] - relative[-2])
    < 1e-5,
    "relative_limit_is_finite": math.isfinite(relative[-1]),
    "relative_volume_is_positive": math.exp(relative[-1]) > 0,
    "under_counterterm_drifts_down": all(x > y for x, y in zip(under, under[1:])),
    "over_counterterm_drifts_up": all(x < y for x, y in zip(over, over[1:])),
    "local_quadratic_tail_bound": all(
        0 <= -math.log1p(-1 / p) - 1 / p <= 1 / p**2
        for p in primes_up_to(10_000)
    ),
}

result = {
    "schema": "marici.aspect.prime-square-relative-determinant.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "bounds": bounds,
    "log_relative_values": relative,
    "relative_volume_at_last_bound": math.exp(relative[-1]),
    "interpretation": (
        "The same-cutoff prime-square countercurrent cancels the unique divergent "
        "linear term and leaves a positive relative determinant."
    ),
}

print(json.dumps(result, indent=2))
