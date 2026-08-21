"""Coarse directed enclosure of fourth derivatives of normalized theta moments."""

from __future__ import annotations

from decimal import Decimal
from math import comb, factorial

from theta_inner_interval_certificate import I, PI_HI, PI_LO, scale


def absolute_upper(value: I) -> Decimal:
    return max(abs(value.lo), abs(value.hi))


def phi_derivatives(u: I) -> list[I]:
    totals = [I.point(0) for _ in range(5)]
    pi = I(PI_LO, PI_HI)
    e2u = scale(u, 2).exp()
    for n in range(1, 11):
        a = scale(pi * e2u, 2 * n * n)
        h = a - I.point(3)
        phi = scale(pi, 2 * n * n) * scale(u, "2.5").exp() * h * (-scale(a, "0.5")).exp()
        l1 = I.point("2.5") + scale(a / h, 2) - a
        l2 = -scale(a / h.power(2), 12) - scale(a, 2)
        l3 = -scale(a / h.power(2), 24) + scale(a.power(2) / h.power(3), 48) - scale(a, 4)
        l4 = (
            -scale(a / h.power(2), 48)
            + scale(a.power(2) / h.power(3), 288)
            - scale(a.power(3) / h.power(4), 288)
            - scale(a, 8)
        )
        bells = [
            I.point(1),
            l1,
            l2 + l1.power(2),
            l3 + scale(l1 * l2, 3) + l1.power(3),
            l4 + scale(l1 * l3, 4) + scale(l2.power(2), 3) + scale(l1.power(2) * l2, 6) + l1.power(4),
        ]
        totals = [total + phi * bell for total, bell in zip(totals, bells)]
    # For n>=11, a>=242*pi>760.  Even after four derivatives and u^80,
    # the geometric Gaussian tail is below this symmetric allowance.
    tail = I(Decimal("-1e-100"), Decimal("1e-100"))
    return [total + tail for total in totals]


def falling(number: int, count: int) -> int:
    if number < count:
        return 0
    return factorial(number) // factorial(number - count)


def main() -> None:
    cells = 1024
    endpoint = Decimal(6)
    maxima = [Decimal(0) for _ in range(41)]
    locations = [None for _ in range(41)]
    for index in range(cells):
        left = endpoint * Decimal(index) / Decimal(cells)
        right = endpoint * Decimal(index + 1) / Decimal(cells)
        u = I(left, right)
        phi = phi_derivatives(u)
        for n in range(41):
            order = 2 * n
            value = I.point(0)
            for phi_order in range(5):
                power_order = 4 - phi_order
                if order < power_order:
                    continue
                power = I.point(1) if order == power_order else u.power(order - power_order)
                coefficient = comb(4, phi_order) * falling(order, power_order)
                value = value + scale(phi[phi_order] * power, coefficient) / I.point(factorial(order))
            upper = absolute_upper(value)
            if upper > maxima[n]:
                maxima[n] = upper
                locations[n] = (left, right)
    worst = max(range(41), key=lambda n: maxima[n])
    print(f"cells={cells}")
    print(f"worst_order={2 * worst}")
    print(f"worst_cell={locations[worst]}")
    print(f"certified_fourth_derivative_upper={maxima[worst]}")
    print(f"simpson_allowance_12000={Decimal(6) / Decimal(180) * (Decimal(6) / Decimal(12000))**4 * maxima[worst]}")
    allowances = [
        Decimal(6) / Decimal(180) * (Decimal(6) / Decimal(12000))**4 * maximum
        for maximum in maxima
    ]
    print(f"order_specific_allowances={[str(value) for value in allowances]}")
    assert maxima[worst] < Decimal("1e6")


if __name__ == "__main__":
    main()
