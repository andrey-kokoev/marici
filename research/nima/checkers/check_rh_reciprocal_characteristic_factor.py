"""Exact check of the reciprocal characteristic normal-factor identity."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    n = max(len(a), len(b))
    return trim(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    )


def scale(c, a):
    return trim(c * x for x in a)


def sub(a, b):
    return add(a, scale(Fraction(-1), b))


def mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def linear(c):
    return (Fraction(c), Fraction(1))


def evaluate(p, x):
    out = Fraction(0)
    for coefficient in reversed(p):
        out = out * x + coefficient
    return out


z = Fraction(3, 4)
assert z != Fraction(1, 2)
records = []

for rates in ([2], [2, 3], [2, 3, 5], [2, 3, 5, 7]):
    reservoir = (Fraction(1),)
    for rate in rates:
        reservoir = mul(reservoir, linear(rate))
    direct = mul(linear(z), reservoir)
    reciprocal = mul(linear(1 - z), reservoir)
    difference = sub(direct, reciprocal)
    expected = scale(2 * (z - Fraction(1, 2)), reservoir)
    assert difference == expected
    for rate in rates:
        assert evaluate(reservoir, -Fraction(rate)) == 0
        assert evaluate(direct, -Fraction(rate)) == 0
        assert evaluate(reciprocal, -Fraction(rate)) == 0
    records.append({
        "label_count": len(rates),
        "normal_factor_identity": True,
        "common_kernel_witnesses": len(rates),
        "off_seam": True,
    })

payload = {
    "schema": "marici.research.check.v1",
    "claim": "reciprocal characteristic difference equals the normal displacement times a noninvertible source reservoir factor",
    "normal_displacement": str(z - Fraction(1, 2)),
    "records": records,
    "verdict": "normal factor exposed but common source kernel prevents cancellation",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-reciprocal-characteristic-factor.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
