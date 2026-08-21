"""Directed certificate that c5=K''''' is positive near the c4 crossing."""

from __future__ import annotations

from decimal import Decimal
from math import factorial

from theta_inner_interval_certificate import I, scale
from xi_fourth_cumulant_outer_certificate import log_interval


def prime_power_base(number: int) -> int | None:
    for prime in range(2, number + 1):
        if any(prime % divisor == 0 for divisor in range(2, int(prime**0.5) + 1)):
            continue
        power = prime
        while power < number:
            power *= prime
        if power == number:
            return prime
    return None


PRIME_POWER_BASE = {
    number: prime
    for number in range(2, 101)
    if (prime := prime_power_base(number)) is not None
}


def integer_log_tail(s: I, start: int, power: int) -> I:
    """Upper-bound sum_(n>=start) log(n)^power n^-s."""
    log_start = log_interval(start)
    first = log_start.power(power) * (-s * log_start).exp()
    base = (I.point(1) - s) * log_start
    integral_factor = I.point(0)
    for index in range(power + 1):
        coefficient = factorial(power) // factorial(power - index)
        term = scale(log_start.power(power - index), coefficient)
        term = term / (s - I.point(1)).power(index + 1)
        integral_factor = integral_factor + term
    return first + base.exp() * integral_factor


def fifth_cumulant_lower(s: I) -> I:
    result = scale((s - I.point(1)).power(5).reciprocal(), 24)

    gamma_upper = I.point(0)
    for n in range(1, 101):
        gamma_upper = gamma_upper + (s + I.point(2 * n)).power(5).reciprocal()
    gamma_start = s + I.point(202)
    gamma_upper = gamma_upper + gamma_start.power(5).reciprocal()
    gamma_upper = gamma_upper + scale(gamma_start.power(4).reciprocal(), "0.125")
    result = result - scale(gamma_upper, 24)

    for number, prime in PRIME_POWER_BASE.items():
        log_number = log_interval(number)
        log_prime = log_interval(prime)
        term = log_prime * log_number.power(4) * (-s * log_number).exp()
        result = result - term

    # Lambda(n)<=log(n), so the omitted prime-power tail is bounded by this
    # all-integer logarithmic Dirichlet tail.
    result = result - integer_log_tail(s, 101, 5)
    return result


def fourth_cumulant_upper(s: I) -> I:
    result = -scale((s - I.point(1)).power(4).reciprocal(), 6)
    gamma_upper = I.point(0)
    for n in range(1, 101):
        gamma_upper = gamma_upper + (s + I.point(2 * n)).power(4).reciprocal()
    gamma_start = s + I.point(202)
    gamma_upper = gamma_upper + gamma_start.power(4).reciprocal()
    gamma_upper = gamma_upper + gamma_start.power(3).reciprocal() / I.point(6)
    result = result + scale(gamma_upper, 6)

    for number, prime in PRIME_POWER_BASE.items():
        log_number = log_interval(number)
        log_prime = log_interval(prime)
        result = result + log_prime * log_number.power(3) * (-s * log_number).exp()
    result = result + integer_log_tail(s, 101, 4)
    return result


def main() -> None:
    # y in [7.235,7.24], hence s=y+1/2.
    left = Decimal("7.735")
    right = Decimal("7.74")
    cells = 512
    minimum = None
    worst = None
    for index in range(cells):
        cell_left = left + (right - left) * Decimal(index) / Decimal(cells)
        cell_right = left + (right - left) * Decimal(index + 1) / Decimal(cells)
        enclosure = fifth_cumulant_lower(I(cell_left, cell_right))
        if minimum is None or enclosure.lo < minimum:
            minimum = enclosure.lo
            worst = (index, cell_left, cell_right, enclosure)
    print(f"cells={cells}")
    print(f"certified_lower_bound={minimum}")
    print(f"worst_cell={worst}")
    assert minimum is not None and minimum > 0
    left_fourth = fourth_cumulant_upper(I.point(left))
    print(f"c4_at_y_7.235_enclosure={left_fourth}")
    assert left_fourth.hi < 0


if __name__ == "__main__":
    main()
