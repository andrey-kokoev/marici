"""Hostile diagnostic sweep of three-height imaginary-axis Xi Pick minors."""

from __future__ import annotations

import itertools
import json
import math

from theta_tilt_third_cumulant import raw_moment, sample


def mean(y: float) -> float:
    return raw_moment(y, 1) / raw_moment(y, 0)


def determinant3(matrix: list[list[float]]) -> float:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def local_gate(y: float) -> dict[str, float]:
    data = sample(y)
    a = data["mean"]
    a_prime = data["variance"]
    a_second = data["third_cumulant"]
    q = a - y * a_prime
    r = -y * y * a_second
    margin = q * (3.0 * a - 2.0 * q) - a * r
    fourth_raw = raw_moment(y, 4) / raw_moment(y, 0)
    second_raw = a_prime + a * a
    third_raw = a_second + 3.0 * a * second_raw - 2.0 * a**3
    fourth_cumulant = (
        fourth_raw
        - 4.0 * a * third_raw
        - 3.0 * second_raw**2
        + 12.0 * a * a * second_raw
        - 6.0 * a**4
    )
    margin_derivative = 3.0 * q * (a_prime + y * a_second) + a * y * y * fourth_cumulant
    return {
        "y": y,
        "q": q,
        "r": r,
        "margin": margin,
        "margin_over_y6": margin / y**6,
        "fourth_cumulant": fourth_cumulant,
        "margin_derivative": margin_derivative,
    }


def main() -> None:
    heights = [
        0.01,
        0.02,
        0.05,
        0.1,
        0.2,
        0.5,
        1.0,
        2.0,
        5.0,
        10.0,
        20.0,
        50.0,
        100.0,
    ]
    means = {y: mean(y) for y in heights}
    rows = []
    for triple in itertools.combinations(heights, 3):
        matrix = [
            [(means[x] + means[y]) / (x + y) for y in triple]
            for x in triple
        ]
        determinant = determinant3(matrix)
        diagonal_product = math.prod(matrix[index][index] for index in range(3))
        rows.append((determinant / diagonal_product, determinant, triple))
    rows.sort()
    print(
        json.dumps(
            {
                "arithmetic": "IEEE-754 double; theta moments by 12000-panel Simpson",
                "triples": len(rows),
                "negative_normalized_determinants": sum(row[0] < -1e-10 for row in rows),
                "confluent_gate_samples": [
                    local_gate(y) for y in [0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
                ],
                "ten_smallest": [
                    {
                        "heights": triple,
                        "normalized_determinant": normalized,
                        "determinant": determinant,
                    }
                    for normalized, determinant, triple in rows[:10]
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
