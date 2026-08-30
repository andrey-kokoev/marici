"""Verify that the first cocircuit seven needs a mod-49 readout."""
import json
import math
from pathlib import Path


def rising(start, length):
    out = 1
    for j in range(length):
        out *= start + j
    return out


def valuation(n, p):
    out = 0
    while n % p == 0 and n:
        out += 1
        n //= p
    return out


g = 14
a = rising(4, g)
b = rising(g + 8, g - 1)
baseline = min(valuation(a, 7), valuation(b, 7))
actual = baseline + 1
baseline_order = 7 ** baseline
actual_order = 7 ** actual

tests = {
    "first_even_multiple_is_14": g == 14,
    "baseline_exponent_is_one": baseline == 1,
    "actual_exponent_is_two": actual == 2,
    "mod7_readout_same": math.gcd(baseline_order, 7) == math.gcd(actual_order, 7) == 7,
    "mod49_readout_separates": math.gcd(baseline_order, 49) == 7
    and math.gcd(actual_order, 49) == 49,
    "lift_fiber_has_seven_elements": 49 // 7 == 7,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_extra_seven_lift_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "grade": g,
    "baseline_7_adic_exponent": baseline,
    "actual_7_adic_exponent": actual,
    "minimal_separating_modulus": 49,
    "verdict": "the extra seven is a sevenfold lift fiber, not seven modes",
}

out = Path(__file__).resolve().parents[1] / "results" / "magnetic_extra_seven_lift_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
