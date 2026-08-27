import json
import math
from pathlib import Path


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


prime_powers = set()
for p in range(2, 101):
    if not is_prime(p):
        continue
    x = p
    while x <= 100:
        prime_powers.add(x)
        x *= p

samples = sorted(math.log(n) for n in prime_powers)
left, right = math.log(2), math.log(3)

checks = {
    "prime_power_set_is_finite_below_100": len(prime_powers) < 100,
    "log2_is_a_sample": left in samples,
    "log3_is_a_sample": right in samples,
    "open_log2_log3_gap_has_no_sample": not any(left < x < right for x in samples),
    "gap_has_positive_width": right - left > 0,
}

result = {
    "schema": "marici.grothendieck.prime-power-universal-quadrature-no-go.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness_gap": ["log(2)", "log(3)"],
    "witness": "Any nonzero nonnegative smooth bump supported strictly inside the gap has positive Lebesgue integral and zero value at every log-prime-power sample.",
}

out = Path(__file__).parents[1] / "results" / "prime_power_universal_quadrature_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
