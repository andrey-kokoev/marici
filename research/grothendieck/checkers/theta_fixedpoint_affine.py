"""Two-variable fixedpoint affine Taylor forms with interval remainder."""
from dataclasses import dataclass
from fractions import Fraction as F
from theta_fixedpoint_interval import (
    FixedInterval, fixed, exp_negative, negative_log1m,
    cosh_sqrt, cosh_sqrt_derivative)
from theta_fixedpoint_jet import cosh_sqrt_second


def symmetric(x):
    x = fixed(x)
    radius = max(abs(x.lo), abs(x.hi))
    return FixedInterval(-radius, radius)


@dataclass(frozen=True)
class Affine:
    center: FixedInterval
    aq: FixedInterval
    ay: FixedInterval
    remainder: FixedInterval

    def __init__(self, center, aq=0, ay=0, remainder=0):
        object.__setattr__(self, "center", fixed(center))
        object.__setattr__(self, "aq", fixed(aq))
        object.__setattr__(self, "ay", fixed(ay))
        object.__setattr__(self, "remainder", fixed(remainder))

    def deviation(self):
        return symmetric(self.aq) + symmetric(self.ay) + self.remainder

    def range(self):
        return self.center + self.deviation()

    def __add__(self, other):
        other = affine(other)
        return Affine(self.center + other.center, self.aq + other.aq,
                      self.ay + other.ay,
                      self.remainder + other.remainder)

    __radd__ = __add__

    def __neg__(self):
        return Affine(-self.center, -self.aq, -self.ay, -self.remainder)

    def __sub__(self, other):
        return self + (-affine(other))

    def __rsub__(self, other):
        return affine(other) - self

    def __mul__(self, other):
        other = affine(other)
        c1, c2 = self.center, other.center
        remainder = (c1 * other.remainder + c2 * self.remainder
                     + self.deviation() * other.deviation())
        return Affine(c1 * c2,
                      c1 * other.aq + c2 * self.aq,
                      c1 * other.ay + c2 * self.ay,
                      remainder)

    __rmul__ = __mul__

    def reciprocal(self):
        domain = self.range()
        if domain.lo <= 0 <= domain.hi:
            raise ZeroDivisionError("affine range contains zero")
        value = self.center.reciprocal()
        first = -(value * value)
        inverse_domain = domain.reciprocal()
        second = 2 * inverse_domain * inverse_domain * inverse_domain
        return unary_taylor(self, value, first, symmetric(second))

    def __truediv__(self, other):
        return self * affine(other).reciprocal()

    def __rtruediv__(self, other):
        return affine(other) / self


def affine(value):
    return value if isinstance(value, Affine) else Affine(value)


def recondition(x):
    """Recenter while preserving the already-certified affine range."""
    x = affine(x)
    target = x.range()
    midpoint = (target.lo + target.hi) // 2
    center = FixedInterval(midpoint, midpoint)
    linear = symmetric(x.aq) + symmetric(x.ay)
    remainder = FixedInterval(target.lo - center.hi - linear.hi,
                              target.hi - center.lo - linear.lo)
    return Affine(center, x.aq, x.ay, remainder)


def unary_taylor(x, value, first, second_bound):
    x = affine(x)
    deviation = x.deviation()
    quadratic = symmetric(fixed(F(1, 2)) * second_bound * deviation * deviation)
    return Affine(value, first * x.aq, first * x.ay,
                  first * x.remainder + quadratic)


def cosh_sqrt_affine(x):
    x = affine(x)
    return unary_taylor(x, cosh_sqrt(x.center),
                        cosh_sqrt_derivative(x.center),
                        cosh_sqrt_second(x.range()))


def exp_negative_affine(x):
    x = affine(x)
    value = exp_negative(x.center)
    return unary_taylor(x, value, -value, exp_negative(x.range()))


def negative_log1m_affine(x):
    x = affine(x)
    value = negative_log1m(x.center)
    first = (1 - x.center).reciprocal()
    second = (1 - x.range()).reciprocal()
    return unary_taylor(x, value, first, second * second)


if __name__ == "__main__":
    q0, q1 = F(2), F(3)
    y0, y1 = F(4), F(5)
    q = Affine(F(5, 2), aq=F(1, 2))
    y = Affine(F(9, 2), ay=F(1, 2))
    product = q * y
    enclosure = product.range()
    assert enclosure.lower_fraction() <= q0 * y0
    assert enclosure.upper_fraction() >= q1 * y1
    # Shared-symbol cancellation survives exactly, unlike natural intervals.
    cancelled = q - q
    assert cancelled.range().lo == cancelled.range().hi == 0
    inverse_range = q.reciprocal().range()
    assert inverse_range.lower_fraction() <= F(1, 3)
    assert inverse_range.upper_fraction() >= F(1, 2)
    small = Affine(F(1, 100), aq=F(1, 1000), ay=F(1, 2000))
    cosine = cosh_sqrt_affine(small).range()
    exponential = exp_negative_affine(small).range()
    logarithm = negative_log1m_affine(small).range()
    assert cosine.lo > fixed(1).lo
    assert exponential.lo > 0 and exponential.hi < fixed(1).hi
    assert logarithm.lo > 0
    inflated = Affine(F(2), aq=F(1, 10), ay=F(1, 20),
                      remainder=FixedInterval.enclosing(F(-1, 5), F(1, 4)))
    before, after = inflated.range(), recondition(inflated).range()
    assert after.lo <= before.lo and after.hi >= before.hi
    assert after.hi - after.lo >= before.hi - before.lo
    print("theta fixedpoint affine Taylor core: PASS")
