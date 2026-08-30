"""Directed-decimal interval certificate for V'''' on the modular interval.

This deliberately uses only the Python standard library.  The omitted n>=51
theta tail is enclosed by +/-1e-1000 in each derivative sum; the elementary
Gaussian estimate justifying that allowance is recorded in the research note.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext


PRECISION = 70
PI_LO = Decimal("3.141592653589793238462643383279502884197169399375105820974944592307816")
PI_HI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592307817")
TAIL = Decimal("1e-1000")


def binary(left: Decimal, right: Decimal, operation, rounding):
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        return operation(left, right)


@dataclass(frozen=True)
class I:
    lo: Decimal
    hi: Decimal

    @staticmethod
    def point(value: int | str | Decimal) -> "I":
        number = Decimal(value)
        return I(number, number)

    def __add__(self, other: "I") -> "I":
        return I(
            binary(self.lo, other.lo, lambda x, y: x + y, ROUND_FLOOR),
            binary(self.hi, other.hi, lambda x, y: x + y, ROUND_CEILING),
        )

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def __sub__(self, other: "I") -> "I":
        return self + (-other)

    def __mul__(self, other: "I") -> "I":
        pairs = [(self.lo, other.lo), (self.lo, other.hi), (self.hi, other.lo), (self.hi, other.hi)]
        lower = [binary(x, y, lambda a, b: a * b, ROUND_FLOOR) for x, y in pairs]
        upper = [binary(x, y, lambda a, b: a * b, ROUND_CEILING) for x, y in pairs]
        return I(min(lower), max(upper))

    def reciprocal(self) -> "I":
        assert self.lo > 0 or self.hi < 0
        return I(
            binary(Decimal(1), self.hi, lambda x, y: x / y, ROUND_FLOOR),
            binary(Decimal(1), self.lo, lambda x, y: x / y, ROUND_CEILING),
        )

    def __truediv__(self, other: "I") -> "I":
        return self * other.reciprocal()

    def exp(self) -> "I":
        with localcontext() as context:
            context.prec = PRECISION
            context.rounding = ROUND_FLOOR
            lo = self.lo.exp()
        with localcontext() as context:
            context.prec = PRECISION
            context.rounding = ROUND_CEILING
            hi = self.hi.exp()
        return I(lo, hi)

    def power(self, exponent: int) -> "I":
        result = I.point(1)
        for _ in range(exponent):
            result = result * self
        return result


def scale(value: I, scalar: int | str) -> I:
    return value * I.point(scalar)


def derivative_sums(u: I) -> list[I]:
    pi = I(PI_LO, PI_HI)
    sums = [I.point(0) for _ in range(5)]
    for n in range(1, 51):
        a = scale((scale(u, 2)).exp() * pi, 2 * n * n)
        h = a - I.point(3)
        phi = scale(pi, 2 * n * n) * (scale(u, "2.5")).exp() * h * scale(-scale(a, "0.5"), 1).exp()
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
        sums = [total + phi * bell for total, bell in zip(sums, bells)]
    error = I(-TAIL, TAIL)
    return [total + error for total in sums]


def potential_fourth(u: I) -> I:
    sums = derivative_sums(u)
    ratios = [entry / sums[0] for entry in sums[1:]]
    r1, r2, r3, r4 = ratios
    log_fourth = r4 - scale(r3 * r1, 4) - scale(r2.power(2), 3) + scale(r2 * r1.power(2), 12) - scale(r1.power(4), 6)
    return -log_fourth


def main() -> None:
    endpoint = Decimal("0.046970170550847214")
    cells = 4096
    best_lo = None
    best_cell = None
    for index in range(cells):
        left = endpoint * Decimal(index) / Decimal(cells)
        right = endpoint * Decimal(index + 1) / Decimal(cells)
        enclosure = potential_fourth(I(left, right))
        if best_lo is None or enclosure.lo < best_lo:
            best_lo = enclosure.lo
            best_cell = (index, left, right, enclosure)
    assert best_lo is not None and best_lo > 0
    print(f"cells={cells}")
    print(f"certified_lower_bound={best_lo}")
    print(f"worst_cell={best_cell}")


if __name__ == "__main__":
    main()
