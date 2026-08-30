"""Diagnostic endpoint sweep for the primitive theta flux family.

This checker supports discovery only.  The moving-endpoint identities in the
associated note are exact; the sampled signs here are not interval proofs.
"""

from __future__ import annotations

import json
import math


PANELS = 24000
RIGHT = 6.0


def profile(u: float, c: float) -> float:
    x = c * math.exp(2.0 * u)
    exponent = 1.25 * math.log(x) + math.log(2.0 * x - 3.0) - x
    return 0.0 if exponent < -745.0 else math.exp(exponent)


def moments(c: float) -> dict[int, float]:
    step = RIGHT / PANELS
    totals = {k: 0.0 for k in range(3, 11)}
    for index in range(PANELS + 1):
        u = index * step
        weight = 1.0 if index in (0, PANELS) else (4.0 if index % 2 else 2.0)
        density = profile(u, c)
        for k in totals:
            totals[k] += weight * density * u**k
    return {k: value * step / 3.0 for k, value in totals.items()}


def sample(c: float) -> dict[str, float]:
    m = moments(c)
    omega = math.log(m[8] * m[4] / m[6] ** 2) - math.log(m[10] * m[6] / m[8] ** 2)
    endpoint_derivative = (
        -4.0 * m[3] / m[4]
        + 18.0 * m[5] / m[6]
        - 24.0 * m[7] / m[8]
        + 10.0 * m[9] / m[10]
    )
    return {
        "c": c,
        "a": 0.5 * math.log(c),
        "omega": omega,
        "d_omega_d_a": endpoint_derivative,
    }


def main() -> None:
    endpoints = [1.500001, 1.5001, 1.51, 1.6, 2.0, 3.0, math.pi, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0]
    samples = [sample(c) for c in endpoints]
    assert all(item["omega"] > 0.0 for item in samples)
    assert all(item["d_omega_d_a"] > 0.0 for item in samples)
    print(json.dumps({
        "status": "diagnostic Simpson sweep; exact identities are documented separately",
        "panels": PANELS,
        "samples": samples,
    }, indent=2))


if __name__ == "__main__":
    main()
