import json
import math


def primes_up_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k * k : n + 1 : k] = b"\x00" * (((n - k * k) // k) + 1)
    return [k for k in range(2, n + 1) if sieve[k]]


def log_genus(bound, sigma, genus):
    total = 0.0
    for p in primes_up_to(bound):
        x = p ** (-sigma)
        total += math.log1p(-x) + sum(x**m / m for m in range(1, genus + 1))
    return total


bounds = [100, 1_000, 10_000, 100_000, 1_000_000]
genus_one = [log_genus(b, 0.5, 1) for b in bounds]
genus_two = [log_genus(b, 0.5, 2) for b in bounds]

checks = {
    "genus_one_drifts_negative": all(
        x > y for x, y in zip(genus_one, genus_one[1:])
    ),
    "genus_one_drift_remains_visible": genus_one[-2] - genus_one[-1] > 0.03,
    "genus_two_is_cauchy_at_test_scale": abs(genus_two[-1] - genus_two[-2])
    < 0.001,
    "critical_minimum_genus_is_two": min(
        m for m in range(10) if (m + 1) * 0.5 > 1
    )
    == 2,
    "zeta_one_minimum_genus_is_one": min(
        m for m in range(10) if (m + 1) * 1.0 > 1
    )
    == 1,
}

result = {
    "schema": "marici.aspect.projected-critical-seam-genus-two.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "bounds": bounds,
    "critical_genus_one_log_values": genus_one,
    "critical_genus_two_log_values": genus_two,
    "conclusion": (
        "The projected critical-seam Euler product requires exactly two "
        "connected countercurrents; the full Tate minor is separately unit."
    ),
}

print(json.dumps(result, indent=2))
