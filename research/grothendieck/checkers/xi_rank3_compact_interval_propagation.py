"""Propagate certified moment quadrature intervals through the compact Xi jet."""

from __future__ import annotations

from decimal import Decimal
from math import factorial

from theta_inner_interval_certificate import I, PI_HI, PI_LO, scale
from theta_tilt_third_cumulant import raw_moment


ORDER_X = 40
SIMPSON_ERROR_NUMERATOR = Decimal("5e-12")


def add(*series: list[I]) -> list[I]:
    return [sum((item[index] for item in series), I.point(0)) for index in range(len(series[0]))]


def series_scale(series: list[I], scalar: int) -> list[I]:
    return [scale(value, scalar) for value in series]


def shift(series: list[I], amount: int = 1) -> list[I]:
    return [I.point(0)] * amount + series[: len(series) - amount]


def derivative(series: list[I]) -> list[I]:
    return [scale(series[index + 1], index + 1) if index + 1 < len(series) else I.point(0) for index in range(len(series))]


def multiply(left: list[I], right: list[I]) -> list[I]:
    return [
        sum((left[j] * right[index - j] for j in range(index + 1)), I.point(0))
        for index in range(len(left))
    ]


def divide(numerator: list[I], denominator: list[I]) -> list[I]:
    quotient = [I.point(0) for _ in numerator]
    for degree in range(len(numerator)):
        correction = sum(
            (denominator[j] * quotient[degree - j] for j in range(1, degree + 1)),
            I.point(0),
        )
        quotient[degree] = (numerator[degree] - correction) / denominator[0]
    return quotient


def horner(coefficients: list[I], x: I) -> I:
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = coefficient + x * result
    return result


def absolute_upper(value: I) -> Decimal:
    return max(abs(value.lo), abs(value.hi))


def direct_margin_jet(b: list[I], y: I) -> tuple[I, I, I]:
    derivatives = []
    for order in range(7):
        total = I.point(0)
        for n, coefficient in enumerate(b):
            degree = 2 * n
            if degree < order:
                continue
            falling = factorial(degree) // factorial(degree - order)
            power = I.point(1) if degree == order else y.power(degree - order)
            total = total + scale(coefficient * power, falling)
        derivatives.append(total)
    raw = [I.point(1)] + [value / derivatives[0] for value in derivatives[1:]]
    cumulants = [I.point(0) for _ in range(7)]
    for order in range(1, 7):
        correction = sum(
            (
                scale(cumulants[index] * raw[order - index], factorial(order - 1) // factorial(index - 1) // factorial(order - index))
                for index in range(1, order)
            ),
            I.point(0),
        )
        cumulants[order] = raw[order] - correction
    a, variance, third, fourth, fifth, sixth = cumulants[1:]
    q = a - y * variance
    first = scale(q * (variance + y * third), 3) + a * y.power(2) * fourth
    second = scale((-y * third) * (variance + y * third), 3)
    second = second + scale(q * (scale(third, 2) + y * fourth), 3)
    second = second + variance * y.power(2) * fourth
    second = second + a * (scale(y * fourth, 2) + y.power(2) * fifth)
    q_prime = -y * third
    q_second = -(third + y * fourth)
    a_combo = variance + y * third
    b_combo = scale(third, 2) + y * fourth
    third_derivative = scale(
        q_second * a_combo + scale(q_prime * b_combo, 2) + q * (scale(fourth, 3) + y * fifth),
        3,
    )
    third_derivative = third_derivative + third * y.power(2) * fourth
    third_derivative = third_derivative + scale(y * variance * fourth, 2)
    third_derivative = third_derivative + variance * y.power(2) * fifth
    third_derivative = third_derivative + variance * (scale(y * fourth, 2) + y.power(2) * fifth)
    third_derivative = third_derivative + a * (
        scale(fourth, 2) + scale(y * fifth, 4) + y.power(2) * sixth
    )
    return first, second, third_derivative


def main() -> None:
    # raw_moment at y=0 uses one common stabilizing scale.  Recover it here.
    # The scan maximum is attained at u=0: log_scale=20-pi.
    scale_factor = (I.point(20) - I(PI_LO, PI_HI)).exp()
    b: list[I] = []
    for n in range(ORDER_X + 1):
        scaled_center = Decimal(str(raw_moment(0.0, 2 * n))) / Decimal(factorial(2 * n))
        center = I.point(scaled_center) * scale_factor
        rounding = max(abs(center.lo), abs(center.hi)) * Decimal("1e-14")
        error = SIMPSON_ERROR_NUMERATOR / Decimal(factorial(2 * n)) + rounding
        b.append(center + I(-error, error))

    b_x = [scale(b[n + 1], n + 1) if n < ORDER_X else I.point(0) for n in range(ORDER_X + 1)]
    b_at_1 = sum(b, I.point(0)) / b[0]
    b_at_2 = sum((scale(value, 2 ** (2 * n)) for n, value in enumerate(b)), I.point(0)) / b[0]
    print(f"B_1_over_B_0_truncated={b_at_1}")
    print(f"B_2_over_B_0_truncated={b_at_2}")
    log_derivative = divide(b_x, b)
    order_y = 2 * ORDER_X + 1
    a = [I.point(0) for _ in range(order_y + 1)]
    for n, coefficient in enumerate(log_derivative):
        if 2 * n + 1 <= order_y:
            a[2 * n + 1] = scale(coefficient, 2)
    a_prime = derivative(a)
    a_second = derivative(a_prime)
    a_third = derivative(a_second)
    q = add(a, series_scale(shift(a_prime), -1))
    s_prime = add(
        series_scale(multiply(q, add(a_prime, shift(a_second))), 3),
        multiply(a, shift(a_third, 2)),
    )
    normalized = [s_prime[index] for index in range(5, len(s_prime), 2)]

    endpoint = horner(normalized, I.point("56.25"))
    modular_interval = horner(normalized, I(Decimal(0), Decimal("0.01")))
    derivative_coefficients = [scale(normalized[index], index) for index in range(1, len(normalized))]
    derivative_max = None
    derivative_worst = None
    cells = 1024
    for index in range(cells):
        left = Decimal("56.25") * Decimal(index) / Decimal(cells)
        right = Decimal("56.25") * Decimal(index + 1) / Decimal(cells)
        enclosure = horner(derivative_coefficients, I(left, right))
        if derivative_max is None or enclosure.hi > derivative_max:
            derivative_max = enclosure.hi
            derivative_worst = (left, right, enclosure)
    print(f"endpoint_enclosure={endpoint}")
    print(f"modular_normalized_enclosure_0_to_0_1={modular_interval}")
    print(f"derivative_upper={derivative_max}")
    print(f"derivative_worst_cell={derivative_worst}")
    certified = endpoint.lo > 0 and derivative_max is not None and derivative_max < 0
    print(f"certified={certified}")
    print("status=naive coefficient intervals lose source correlations; use direct B-jet cells")

    print(f"direct_B_jet_at_7_5={direct_margin_jet(b, I.point('7.5'))[0]}")

    base_cells = 64
    start = Decimal("0.1")
    stop = Decimal("7.5")
    stack = [
        (
            start + (stop - start) * Decimal(index) / Decimal(base_cells),
            start + (stop - start) * Decimal(index + 1) / Decimal(base_cells),
            0,
        )
        for index in range(base_cells)
    ]
    certified_count = 0
    certified_lower = None
    worst = None
    while stack:
        left, right, depth = stack.pop()
        midpoint = (left + right) / Decimal(2)
        radius = (right - left) / Decimal(2)
        point_first, point_second, _ = direct_margin_jet(b, I.point(midpoint))
        cell_third = direct_margin_jet(b, I(left, right))[2]
        lower = (
            point_first.lo
            - radius * absolute_upper(point_second)
            - radius * radius * absolute_upper(cell_third) / Decimal(2)
        )
        if lower <= 0:
            assert depth < 14, (left, right, point_first, point_second, cell_third)
            stack.extend([(left, midpoint, depth + 1), (midpoint, right, depth + 1)])
            continue
        certified_count += 1
        if certified_lower is None or lower < certified_lower:
            certified_lower = lower
            worst = (left, right, point_first, point_second, cell_third)
    print(f"taylor_certified_cells={certified_count}")
    print(f"taylor_certified_lower={certified_lower}")
    print(f"taylor_worst={worst}")


if __name__ == "__main__":
    main()
