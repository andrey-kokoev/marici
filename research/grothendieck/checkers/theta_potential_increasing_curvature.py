"""Diagnostic sweep of V''' for the full Riemann theta potential V=-log Phi."""

from __future__ import annotations

import json
import math


def potential_derivatives(u: float) -> tuple[float, float]:
    records = []
    for n in range(1, 40):
        n2 = float(n * n)
        a = 2.0 * math.pi * n2 * math.exp(2.0 * u)
        h = a - 3.0
        log_term = math.log(2.0 * math.pi * n2) + 2.5 * u + math.log(h) - 0.5 * a
        first = 2.5 + 2.0 * a / h - a
        second = -12.0 * a / (h * h) - 2.0 * a
        third = -24.0 * a / (h * h) + 48.0 * a * a / (h**3) - 4.0 * a
        fourth = (
            -48.0 * a / (h * h)
            + 288.0 * a * a / (h**3)
            - 288.0 * a**3 / (h**4)
            - 8.0 * a
        )
        records.append((log_term, first, second, third, fourth))
        if n >= 5 and log_term < records[0][0] - 50.0:
            break

    maximum = max(record[0] for record in records)
    weights = [math.exp(record[0] - maximum) for record in records]
    normalizer = sum(weights)
    phi_1 = sum(weight * record[1] for weight, record in zip(weights, records)) / normalizer
    phi_2 = sum(
        weight * (record[2] + record[1] ** 2)
        for weight, record in zip(weights, records)
    ) / normalizer
    phi_3 = sum(
        weight * (record[3] + 3.0 * record[1] * record[2] + record[1] ** 3)
        for weight, record in zip(weights, records)
    ) / normalizer
    phi_4 = sum(
        weight
        * (
            record[4]
            + 4.0 * record[1] * record[3]
            + 3.0 * record[2] ** 2
            + 6.0 * record[1] ** 2 * record[2]
            + record[1] ** 4
        )
        for weight, record in zip(weights, records)
    ) / normalizer
    log_phi_third = phi_3 - 3.0 * phi_2 * phi_1 + 2.0 * phi_1**3
    log_phi_fourth = (
        phi_4
        - 4.0 * phi_3 * phi_1
        - 3.0 * phi_2**2
        + 12.0 * phi_2 * phi_1**2
        - 6.0 * phi_1**4
    )
    return -log_phi_third, -log_phi_fourth


def potential_third(u: float) -> float:
    return potential_derivatives(u)[0]


def main() -> None:
    # Dense near the modular fixed point, then extend into the dominant-term tail.
    points = [index / 10000.0 for index in range(0, 10001)]
    points.extend(1.0 + index / 1000.0 for index in range(1, 4001))
    rows = [(u, potential_third(u)) for u in points]
    minimum = min(rows, key=lambda row: row[1])
    negative = [row for row in rows if row[0] > 0.0 and row[1] < -1e-10]
    selected = [0.0, 0.0001, 0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0]
    inner_endpoint = 0.046970170550847214
    inner_rows = [
        (inner_endpoint * index / 10000.0, potential_derivatives(inner_endpoint * index / 10000.0)[1])
        for index in range(10001)
    ]
    inner_minimum = min(inner_rows, key=lambda row: row[1])
    print(
        json.dumps(
            {
                "grid_points": len(rows),
                "minimum": {"u": minimum[0], "V_third": minimum[1]},
                "negative_count_below_tolerance": len(negative),
                "inner_V_fourth_minimum": {
                    "u": inner_minimum[0],
                    "V_fourth": inner_minimum[1],
                },
                "samples": [
                    {
                        "u": u,
                        "V_third": potential_derivatives(u)[0],
                        "V_fourth": potential_derivatives(u)[1],
                    }
                    for u in selected
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
