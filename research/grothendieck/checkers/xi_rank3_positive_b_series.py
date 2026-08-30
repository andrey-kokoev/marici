"""Stable positive-B series computation of the compact rank-three margin."""

from __future__ import annotations

import json
import math

from theta_tilt_third_cumulant import raw_moment


ORDER_X = 40


def derivative(series: list[float]) -> list[float]:
    return [(i + 1) * series[i + 1] if i + 1 < len(series) else 0.0 for i in range(len(series))]


def shift(series: list[float], amount: int = 1) -> list[float]:
    return [0.0] * amount + series[: len(series) - amount]


def add(*series: list[float]) -> list[float]:
    return [sum(item[i] for item in series) for i in range(len(series[0]))]


def scale(series: list[float], scalar: float) -> list[float]:
    return [scalar * value for value in series]


def multiply(left: list[float], right: list[float]) -> list[float]:
    return [sum(left[j] * right[i - j] for j in range(i + 1)) for i in range(len(left))]


def divide(numerator: list[float], denominator: list[float]) -> list[float]:
    quotient = [0.0] * len(numerator)
    for degree in range(len(numerator)):
        quotient[degree] = (
            numerator[degree]
            - sum(denominator[j] * quotient[degree - j] for j in range(1, degree + 1))
        ) / denominator[0]
    return quotient


def compute(intervals: int) -> dict[str, object]:
    normalizer = raw_moment(0.0, 0, intervals)
    b = [
        raw_moment(0.0, 2 * n, intervals) / normalizer / math.factorial(2 * n)
        for n in range(ORDER_X + 1)
    ]
    b_x = [(n + 1) * b[n + 1] if n < ORDER_X else 0.0 for n in range(ORDER_X + 1)]
    logarithmic_x_derivative = divide(b_x, b)

    order_y = 2 * ORDER_X + 1
    a = [0.0] * (order_y + 1)
    for n, coefficient in enumerate(logarithmic_x_derivative):
        if 2 * n + 1 <= order_y:
            a[2 * n + 1] = 2.0 * coefficient
    a_prime = derivative(a)
    a_second = derivative(a_prime)
    a_third = derivative(a_second)
    q = add(a, scale(shift(a_prime), -1.0))
    s_prime = add(
        scale(multiply(q, add(a_prime, shift(a_second))), 3.0),
        multiply(a, shift(a_third, 2)),
    )
    coefficients = [s_prime[index] for index in range(5, len(s_prime), 2)]

    samples: list[dict[str, float]] = []
    for y in (7.2, 7.5):
        terms = [coefficient * y ** (2 * index) for index, coefficient in enumerate(coefficients)]
        samples.append(
            {
                "y": y,
                "S_prime_over_y5": sum(terms),
                "last_term": terms[-1],
                "last_term_absolute_ratio": abs(terms[-1] / terms[-2]),
            }
        )
    derivative_coefficients = [
        index * coefficient for index, coefficient in enumerate(coefficients)
    ][1:]
    derivative_rows = []
    for index in range(10001):
        x = 56.25 * index / 10000.0
        derivative_rows.append(
            sum(coefficient * x**degree for degree, coefficient in enumerate(derivative_coefficients))
        )
    return {
        "samples": samples,
        "polynomial_derivative_min": min(derivative_rows),
        "polynomial_derivative_max": max(derivative_rows),
    }


def main() -> None:
    refinements = [
        {"simpson_intervals": intervals, **compute(intervals)}
        for intervals in (3000, 6000, 12000)
    ]
    print(json.dumps({"order_x": ORDER_X, "refinements": refinements}, indent=2))


if __name__ == "__main__":
    main()
