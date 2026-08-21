"""Directed modular/compact certificate for concavity of log a(exp x).

The polynomial margin is
    D = a (r-wq) = y^2 (a'^2-aa'') - y a a'.
Since a>0, D>=0 is equivalent to h''<=0 for h(x)=log a(exp x).
"""

from __future__ import annotations

from decimal import Decimal
from math import comb, factorial

from theta_inner_interval_certificate import I, PI_HI, PI_LO, scale
from theta_tilt_third_cumulant import raw_moment


ORDER_X = 40
SIMPSON_ERROR_NUMERATOR = Decimal("5e-12")


def absolute_upper(value: I) -> Decimal:
    return max(abs(value.lo), abs(value.hi))


def product(left: list[I], right: list[I], order: int) -> list[I]:
    return [
        sum(
            (scale(left[k] * right[n - k], comb(n, k)) for k in range(n + 1)),
            I.point(0),
        )
        for n in range(order + 1)
    ]


def subtract(left: list[I], right: list[I]) -> list[I]:
    return [a - b for a, b in zip(left, right)]


def cumulant_jet(b: list[I], y: I, maximum: int) -> list[I]:
    derivatives = []
    for order in range(maximum + 1):
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
    cumulants = [I.point(0) for _ in range(maximum + 1)]
    for order in range(1, maximum + 1):
        correction = sum(
            (
                scale(
                    cumulants[index] * raw[order - index],
                    comb(order - 1, index - 1),
                )
                for index in range(1, order)
            ),
            I.point(0),
        )
        cumulants[order] = raw[order] - correction
    return cumulants


def margin_jet(b: list[I], y: I, order: int = 2) -> list[I]:
    cumulants = cumulant_jet(b, y, order + 3)
    a = cumulants[1 : order + 2]
    variance = cumulants[2 : order + 3]
    third = cumulants[3 : order + 4]
    y_jet = [y, I.point(1)] + [I.point(0)] * (order - 1)
    y2_jet = product(y_jet, y_jet, order)
    variance2 = product(variance, variance, order)
    a_third = product(a, third, order)
    first = product(y2_jet, subtract(variance2, a_third), order)
    second = product(product(y_jet, a, order), variance, order)
    return subtract(first, second)


def polynomial_margin_series(b: list[I]) -> list[I]:
    # Ordinary power-series arithmetic, unlike product(), which handles jets.
    size = 2 * ORDER_X + 2
    def mul(left: list[I], right: list[I]) -> list[I]:
        return [
            sum((left[k] * right[n-k] for k in range(n + 1)), I.point(0))
            for n in range(size)
        ]
    def div(num: list[I], den: list[I]) -> list[I]:
        out = [I.point(0) for _ in range(size)]
        for n in range(size):
            correction = sum((den[k] * out[n-k] for k in range(1, n + 1)), I.point(0))
            out[n] = (num[n] - correction) / den[0]
        return out
    bx = [scale(b[n + 1], n + 1) if n < ORDER_X else I.point(0) for n in range(ORDER_X + 1)]
    log_derivative = div(bx + [I.point(0)] * (size-len(bx)), b + [I.point(0)] * (size-len(b)))
    a = [I.point(0) for _ in range(size)]
    for n, coefficient in enumerate(log_derivative):
        if 2*n+1 < size:
            a[2*n+1] = scale(coefficient, 2)
    ap = [scale(a[n+1], n+1) if n+1 < size else I.point(0) for n in range(size)]
    app = [scale(ap[n+1], n+1) if n+1 < size else I.point(0) for n in range(size)]
    core = subtract(mul(ap, ap), mul(a, app))
    return subtract([I.point(0), I.point(0)] + core[:-2], [I.point(0)] + mul(a, ap)[:-1])


def horner(coefficients: list[I], x: I) -> I:
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = coefficient + x * result
    return result


def main() -> None:
    scale_factor = (I.point(20) - I(PI_LO, PI_HI)).exp()
    b = []
    for n in range(ORDER_X + 1):
        center = I.point(Decimal(str(raw_moment(0.0, 2*n))) / Decimal(factorial(2*n))) * scale_factor
        rounding = max(abs(center.lo), abs(center.hi)) * Decimal("1e-14")
        error = SIMPSON_ERROR_NUMERATOR / Decimal(factorial(2*n)) + rounding
        b.append(center + I(-error, error))

    series = polynomial_margin_series(b)
    normalized = [series[index] for index in range(4, len(series), 2)]
    modular = horner(normalized, I(Decimal(0), Decimal("0.01")))
    print(f"modular_D_over_y4_0_to_0_1={modular}")

    stack = [(Decimal("0.1"), Decimal("7.5"), 0)]
    count = 0
    lower_min = None
    worst = None
    while stack:
        left, right, depth = stack.pop()
        midpoint = (left + right) / 2
        radius = (right - left) / 2
        point = margin_jet(b, I.point(midpoint), 1)
        second = margin_jet(b, I(left, right), 2)[2]
        lower = point[0].lo - radius * absolute_upper(point[1]) - radius*radius*absolute_upper(second)/2
        if lower <= 0:
            assert depth < 18, (left, right, point, second, lower)
            stack.extend([(left, midpoint, depth+1), (midpoint, right, depth+1)])
            continue
        count += 1
        if lower_min is None or lower < lower_min:
            lower_min = lower
            worst = (left, right, point, second)
    print(f"compact_taylor_cells={count}")
    print(f"compact_D_lower={lower_min}")
    print(f"compact_worst={worst}")
    print(f"certified_through_7_5={modular.lo > 0 and lower_min is not None and lower_min > 0}")


if __name__ == "__main__":
    main()
