"""Directed interval certificate that the Xi fourth cumulant is positive for y>=7.24."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext

from theta_inner_interval_certificate import I, PRECISION, scale


PRIME_POWER_BASE = {
    2: 2,
    3: 3,
    4: 2,
    5: 5,
    7: 7,
    8: 2,
    9: 3,
    11: 11,
    13: 13,
    16: 2,
    17: 17,
    19: 19,
}


def log_interval(integer: int) -> I:
    value = Decimal(integer)
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = value.ln()
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = value.ln()
    return I(lower, upper)


def lower_bound(s: I) -> I:
    total = I.point(0)
    for n in range(1, 21):
        total = total + scale((s + I.point(2 * n)).power(4).reciprocal(), 6)

    tail_start = s + I.point(42)
    total = total + tail_start.power(3).reciprocal()
    total = total + scale(tail_start.power(4).reciprocal(), 3)
    total = total - scale((s - I.point(1)).power(4).reciprocal(), 6)

    for number, prime in PRIME_POWER_BASE.items():
        log_number = log_interval(number)
        log_prime = log_interval(prime)
        prime_term = log_prime * log_number.power(3) * (-s * log_number).exp()
        total = total + prime_term
    return total


def main() -> None:
    left = Decimal("7.74")
    right = Decimal("13")
    cells = 4096
    minimum = None
    worst = None
    evaluated = 0
    for index in range(cells):
        cell_left = left + (right - left) * Decimal(index) / Decimal(cells)
        cell_right = left + (right - left) * Decimal(index + 1) / Decimal(cells)
        stack = [(cell_left, cell_right, 0)]
        while stack:
            sub_left, sub_right, depth = stack.pop()
            enclosure = lower_bound(I(sub_left, sub_right))
            evaluated += 1
            if enclosure.lo <= 0:
                assert depth < 20, (sub_left, sub_right, enclosure)
                midpoint = (sub_left + sub_right) / Decimal(2)
                stack.append((midpoint, sub_right, depth + 1))
                stack.append((sub_left, midpoint, depth + 1))
                continue
            if minimum is None or enclosure.lo < minimum:
                minimum = enclosure.lo
                worst = (index, sub_left, sub_right, enclosure)
    print(f"cells={cells}")
    print(f"evaluated_enclosures={evaluated}")
    print(f"certified_lower_bound={minimum}")
    print(f"worst_cell={worst}")
    print("coarse_continuation=s>=13: (s-1)^4 > 6(s+2)^3")
    assert minimum is not None and minimum > 0


if __name__ == "__main__":
    main()
