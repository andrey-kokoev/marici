"""Compute the modular cumulant series for the normalized rank-three margin."""

from __future__ import annotations

import json
import math

from theta_tilt_third_cumulant import raw_moment


ORDER = 32


def determinant(matrix: list[list[float]]) -> float:
    work = [row[:] for row in matrix]
    result = 1.0
    for column in range(len(work)):
        pivot = max(range(column, len(work)), key=lambda row: abs(work[row][column]))
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            factor = work[row][column] / pivot_value
            for index in range(column + 1, len(work)):
                work[row][index] -= factor * work[column][index]
    return result


def hankel_determinants(sequence: list[float]) -> dict[str, float]:
    output = {}
    for shift in (0, 1):
        for size in range(2, 5):
            output[f"shift_{shift}_size_{size}"] = determinant(
                [[sequence[row + column + shift] for column in range(size)] for row in range(size)]
            )
    return output


def multiply(left: list[float], right: list[float]) -> list[float]:
    return [
        sum(left[index] * right[degree - index] for index in range(degree + 1))
        for degree in range(len(left))
    ]


def add(*series: list[float]) -> list[float]:
    return [sum(item[index] for item in series) for index in range(len(series[0]))]


def scale(series: list[float], scalar: float) -> list[float]:
    return [scalar * value for value in series]


def shift(series: list[float], amount: int = 1) -> list[float]:
    return [0.0] * amount + series[: len(series) - amount]


def derivative(series: list[float]) -> list[float]:
    return [
        (index + 1) * series[index + 1] if index + 1 < len(series) else 0.0
        for index in range(len(series))
    ]


def main() -> None:
    normalizer = raw_moment(0.0, 0)
    moments = [raw_moment(0.0, n) / normalizer for n in range(ORDER + 1)]
    cumulants = [0.0] * (ORDER + 1)
    for n in range(1, ORDER + 1):
        cumulants[n] = moments[n] - sum(
            math.comb(n - 1, j - 1) * cumulants[j] * moments[n - j]
            for j in range(1, n)
        )

    a = [
        cumulants[n + 1] / math.factorial(n) if n + 1 <= ORDER else 0.0
        for n in range(ORDER)
    ]
    a_prime = derivative(a)
    a_second = derivative(a_prime)
    a_third = derivative(a_second)
    q = add(a, scale(shift(a_prime), -1.0))
    margin_derivative = add(
        scale(multiply(q, add(a_prime, shift(a_second))), 3.0),
        multiply(a, shift(a_third, 2)),
    )
    normalized = [margin_derivative[index] for index in range(5, len(a), 2)]
    positive_moments = [(-1.0) ** index * value for index, value in enumerate(normalized)]
    stieltjes_hankel_2 = positive_moments[0] * positive_moments[2] - positive_moments[1] ** 2
    laplace_moments = [math.factorial(index) * value for index, value in enumerate(positive_moments)]
    laplace_hankel_2 = laplace_moments[0] * laplace_moments[2] - laplace_moments[1] ** 2
    print(
        json.dumps(
            {
                "even_cumulants": {
                    str(n): cumulants[n] for n in range(2, ORDER + 1, 2)
                },
                "S_prime_over_y5_coefficients_in_y2": normalized,
                "alternating_through_computed_order": all(
                    (-1.0) ** index * coefficient > 0.0
                    for index, coefficient in enumerate(normalized)
                ),
                "stieltjes_coefficient_hankel_2": stieltjes_hankel_2,
                "stieltjes_strengthening_falsified": stieltjes_hankel_2 < 0.0,
                "laplace_derivative_hankel_2": laplace_hankel_2,
                "complete_monotonicity_survives_first_hankel": laplace_hankel_2 >= 0.0,
                "stieltjes_hankel_determinants": hankel_determinants(positive_moments),
                "laplace_hankel_determinants": hankel_determinants(laplace_moments),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
