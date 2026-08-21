"""Diagnostic fourth-derivative bounds for normalized theta moments."""

from __future__ import annotations

import json
import math


def phi_derivatives(u: float) -> list[float]:
    totals = [0.0] * 5
    e2u = math.exp(2.0 * u)
    for n in range(1, 40):
        a = 2.0 * math.pi * n * n * e2u
        h = a - 3.0
        phi = 2.0 * math.pi * n * n * math.exp(2.5 * u) * h * math.exp(-0.5 * a)
        l1 = 2.5 + 2.0 * a / h - a
        l2 = -12.0 * a / h**2 - 2.0 * a
        l3 = -24.0 * a / h**2 + 48.0 * a * a / h**3 - 4.0 * a
        l4 = -48.0 * a / h**2 + 288.0 * a * a / h**3 - 288.0 * a**3 / h**4 - 8.0 * a
        bells = [
            1.0,
            l1,
            l2 + l1 * l1,
            l3 + 3.0 * l1 * l2 + l1**3,
            l4 + 4.0 * l1 * l3 + 3.0 * l2 * l2 + 6.0 * l1 * l1 * l2 + l1**4,
        ]
        totals = [total + phi * bell for total, bell in zip(totals, bells)]
        if n >= 6 and phi < 1e-300:
            break
    return totals


def falling(number: int, count: int) -> int:
    if number < count:
        return 0
    return math.prod(range(number - count + 1, number + 1))


def main() -> None:
    samples = 12000
    maxima = [0.0] * 41
    locations = [0.0] * 41
    for index in range(samples + 1):
        u = 6.0 * index / samples
        phi = phi_derivatives(u)
        for n in range(41):
            order = 2 * n
            value = 0.0
            for phi_order in range(5):
                power_order = 4 - phi_order
                if order < power_order:
                    continue
                power = 1.0 if order == power_order else u ** (order - power_order)
                value += (
                    math.comb(4, phi_order)
                    * phi[phi_order]
                    * falling(order, power_order)
                    * power
                    / math.factorial(order)
                )
            if abs(value) > maxima[n]:
                maxima[n] = abs(value)
                locations[n] = u

    panels = 12000
    step = 6.0 / panels
    errors = [6.0 * step**4 * maximum / 180.0 for maximum in maxima]
    worst = max(range(41), key=lambda n: errors[n])
    print(
        json.dumps(
            {
                "status": "diagnostic grid maxima; not directed interval bounds",
                "panels": panels,
                "worst_order": 2 * worst,
                "worst_location": locations[worst],
                "worst_fourth_derivative": maxima[worst],
                "worst_simpson_allowance": errors[worst],
                "selected": [
                    {
                        "order": 2 * n,
                        "maximum": maxima[n],
                        "location": locations[n],
                        "allowance": errors[n],
                    }
                    for n in (0, 1, 5, 10, 20, 30, 40)
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
