"""Directed completed-zeta certificate for the outer log-response margin."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from math import factorial

from theta_inner_interval_certificate import I, PI_HI, PI_LO, PRECISION, scale
from xi_variance_elasticity_outer_certificate import log_power_integral
from xi_fourth_cumulant_outer_certificate import log_interval


EULER_LO = Decimal("0.577215664901532860606512090082402431042159335939923598805767234884867")
EULER_HI = Decimal("0.577215664901532860606512090082402431042159335939923598805767234884868")
SUM_TERMS = 768
PRIME_CUTOFF = 100


def log_i(value: I) -> I:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lo = value.lo.ln()
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        hi = value.hi.ln()
    return I(lo, hi)


def digamma(x: I) -> I:
    total = -I(EULER_LO, EULER_HI)
    for n in range(SUM_TERMS):
        total = total + I.point(1) / I.point(n + 1) - I.point(1) / (x + I.point(n))
    # f(t)=1/(t+1)-1/(t+x) is positive decreasing for x>1.
    n = I.point(SUM_TERMS)
    integral = log_i((n + x) / (n + I.point(1)))
    first = I.point(1) / (n + I.point(1)) - I.point(1) / (n + x)
    return total + integral + I(Decimal(0), first.hi)


def reciprocal_sum(x: I, power: int) -> I:
    total = I.point(0)
    for n in range(SUM_TERMS):
        total = total + (x + I.point(n)).power(power).reciprocal()
    start = x + I.point(SUM_TERMS)
    integral = start.power(power - 1).reciprocal() / I.point(power - 1)
    first = start.power(power).reciprocal()
    return total + integral + I(Decimal(0), first.hi)


def prime_base(number: int) -> int | None:
    for p in range(2, number + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        value = p
        while value < number:
            value *= p
        if value == number:
            return p
    return None


def zeta_log_derivative(s: I, order: int) -> I:
    magnitude = I.point(0)
    for n in range(2, PRIME_CUTOFF + 1):
        p = prime_base(n)
        if p is None:
            continue
        ln = log_interval(n)
        lp = log_interval(p)
        magnitude = magnitude + lp * ln.power(order - 1) * (-s * ln).exp()
    # Lambda(n)<=log(n), so the omitted magnitude is bounded by an all-integer tail.
    tail = log_power_integral(s, PRIME_CUTOFF, order)
    upper = magnitude.hi + tail.hi
    if order % 2:
        return I(-upper, -magnitude.lo)
    return I(magnitude.lo, upper)


def completed_jet(s: I) -> tuple[I, I, I]:
    y = s - I.point("0.5")
    x = s / I.point(2)
    log_pi = log_i(I(PI_LO, PI_HI))
    a = I.point(1) / s + I.point(1) / (s - I.point(1))
    a = a - log_pi / I.point(2) + digamma(x) / I.point(2)
    a = a + zeta_log_derivative(s, 1)
    variance = -I.point(1) / s.power(2) - I.point(1) / (s - I.point(1)).power(2)
    variance = variance + reciprocal_sum(x, 2) / I.point(4)
    variance = variance + zeta_log_derivative(s, 2)
    third = scale(I.point(1) / s.power(3) + I.point(1) / (s - I.point(1)).power(3), 2)
    third = third - reciprocal_sum(x, 3) / I.point(4)
    third = third + zeta_log_derivative(s, 3)
    return a, variance, third


def margin(s: I) -> I:
    y = s - I.point("0.5")
    a, variance, third = completed_jet(s)
    return y.power(2) * (variance.power(2) - a * third) - y * a * variance


def main() -> None:
    left = Decimal(8)
    right = Decimal(100)
    stack = [(left, right, 0)]
    minimum = None
    worst = None
    count = 0
    while stack:
        a, b, depth = stack.pop()
        enclosure = margin(I(a, b))
        count += 1
        if enclosure.lo <= 0:
            assert depth < 18, (a, b, enclosure)
            midpoint = (a + b) / 2
            stack.extend([(a, midpoint, depth + 1), (midpoint, b, depth + 1)])
            continue
        if minimum is None or enclosure.lo < minimum:
            minimum = enclosure.lo
            worst = (a, b, enclosure)
    print(f"evaluated_enclosures={count}")
    print(f"certified_lower_bound={minimum}")
    print(f"worst_cell={worst}")


if __name__ == "__main__":
    main()
