"""Dependency-free exact interval primitives for the dominant theta checker."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __init__(self, lo, hi=None):
        object.__setattr__(self, "lo", F(lo))
        object.__setattr__(self, "hi", F(lo if hi is None else hi))
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def __add__(self, other):
        other = interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-interval(other))

    def __rsub__(self, other):
        return interval(other) - self

    def __mul__(self, other):
        other = interval(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * interval(other).reciprocal()

    def __rtruediv__(self, other):
        return interval(other) / self


@dataclass(frozen=True)
class Dual:
    value: Interval
    dq: Interval
    dy: Interval

    def __init__(self, value, dq=0, dy=0):
        object.__setattr__(self, "value", interval(value))
        object.__setattr__(self, "dq", interval(dq))
        object.__setattr__(self, "dy", interval(dy))

    def __add__(self, other):
        other = dual(other)
        return Dual(self.value + other.value, self.dq + other.dq,
                    self.dy + other.dy)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.dq, -self.dy)

    def __sub__(self, other):
        return self + (-dual(other))

    def __rsub__(self, other):
        return dual(other) - self

    def __mul__(self, other):
        other = dual(other)
        return Dual(self.value * other.value,
                    self.dq * other.value + self.value * other.dq,
                    self.dy * other.value + self.value * other.dy)

    __rmul__ = __mul__

    def reciprocal(self):
        inverse = self.value.reciprocal()
        square = self.value * self.value
        return Dual(inverse, -self.dq / square, -self.dy / square)

    def __truediv__(self, other):
        return self * dual(other).reciprocal()

    def __rtruediv__(self, other):
        return dual(other) / self


def interval(value):
    return value if isinstance(value, Interval) else Interval(value)


def dual(value):
    return value if isinstance(value, Dual) else Dual(value)


def cosh_sqrt(x: Interval, terms=10):
    """Enclose cosh(sqrt(x)) for 0 <= x <= 1/16 (including 4*q*y)."""
    x = interval(x)
    if x.lo < 0 or x.hi > F(1, 16):
        raise ValueError("cosh_sqrt domain")
    total = term = Interval(1)
    for n in range(1, terms + 1):
        term = term * x / ((2 * n) * (2 * n - 1))
        total += term
    next_hi = term.hi * x.hi / ((2 * terms + 2) * (2 * terms + 1))
    ratio = x.hi / ((2 * terms + 3) * (2 * terms + 4))
    return Interval(total.lo, total.hi + next_hi / (1 - ratio))


def cosh_sqrt_derivative(x: Interval, terms=10):
    """Enclose d/dx cosh(sqrt(x)) on 0 <= x <= 1/16."""
    x = interval(x)
    if x.lo < 0 or x.hi > F(1, 16):
        raise ValueError("cosh_sqrt_derivative domain")
    total = term = Interval(F(1, 2))
    for n in range(2, terms + 1):
        term = term * x / ((2 * n) * (2 * n - 1)) * n / (n - 1)
        total += term
    next_hi = (term.hi * x.hi / ((2 * terms + 2) * (2 * terms + 1))
               * F(terms + 1, terms))
    ratio = x.hi / ((2 * terms + 3) * (2 * terms + 4))
    return Interval(total.lo, total.hi + next_hi / (1 - ratio))


def cosh_sqrt_dual(x: Dual, terms=10):
    x = dual(x)
    value = cosh_sqrt(x.value, terms)
    derivative = cosh_sqrt_derivative(x.value, terms)
    return Dual(value, derivative * x.dq, derivative * x.dy)


def exp_negative(x: Interval, terms=18):
    """Enclose exp(-x) for 0 <= x <= 1/2 (including the doubled argument)."""
    x = interval(x)
    if x.lo < 0 or x.hi > F(1, 2):
        raise ValueError("exp_negative domain")
    total = term = Interval(1)
    for n in range(1, terms + 1):
        term = term * x / n
        total += term
    next_hi = term.hi * x.hi / (terms + 1)
    tail = next_hi / (1 - x.hi / (terms + 2))
    exp_pos = Interval(total.lo, total.hi + tail)
    return exp_pos.reciprocal()


def exp_negative_dual(x: Dual, terms=18):
    x = dual(x)
    value = exp_negative(x.value, terms)
    return Dual(value, -value * x.dq, -value * x.dy)


def negative_log1m(x: Interval, terms=8):
    """Enclose -log(1-x) for 0 <= x <= 1/25, including doubled y."""
    x = interval(x)
    if x.lo < 0 or x.hi > F(1, 25):
        raise ValueError("negative_log1m domain")
    total = term = x
    for n in range(2, terms + 1):
        term = term * x
        total += term / n
    tail = term.hi * x.hi / ((terms + 1) * (1 - x.hi))
    return Interval(total.lo, total.hi + tail)


def negative_log1m_dual(x: Dual, terms=8):
    x = dual(x)
    value = negative_log1m(x.value, terms)
    derivative = (1 - x.value).reciprocal()
    return Dual(value, derivative * x.dq, derivative * x.dy)


def one_minus_exp_negative_dual(x: Dual, terms=18):
    """Enclose 1-exp(-x), preserving derivatives, for 0 <= x <= 1/2."""
    return 1 - exp_negative_dual(x, terms)


PI = Interval(F(3141592653589793238, 10**18),
              F(3141592653589793239, 10**18))


def dominant_kernel(q: Dual, y: Dual):
    """Normalized (1,1) kernel on the physical inner domain."""
    q, y = dual(q), dual(y)
    amplitude = dual(2 * PI) / q
    cosine = cosh_sqrt_dual(q * y)
    exponential = exp_negative_dual(amplitude * (cosine - 1))
    numerator = amplitude * amplitude - 6 * amplitude * cosine + 9
    denominator = (amplitude - 3) * (amplitude - 3)
    return exponential * numerator / denominator


def dominant_residual_quotient(q: Dual, y: Dual):
    """Direct positive-y quotient; callers must keep y away from zero."""
    q, y = dual(q), dual(y)
    kernel = dominant_kernel(q, y)
    doubled = dominant_kernel(q, 4 * y)
    return (1 + doubled - 2 * kernel * kernel) / (y * y)


def dominant_log_magnitude(q: Dual, y: Dual):
    """Return m=-log(G) without first enclosing G."""
    q, y = dual(q), dual(y)
    amplitude = dual(2 * PI) / q
    cosine = cosh_sqrt_dual(q * y)
    exponent = amplitude * (cosine - 1)
    denominator = (amplitude - 3) * (amplitude - 3)
    correction = 6 * amplitude * (cosine - 1) / denominator
    return exponent + negative_log1m_dual(correction)


def cancellation_free_residual_quotient(q: Dual, y: Dual):
    q, y = dual(q), dual(y)
    m = dominant_log_magnitude(q, y)
    m4 = dominant_log_magnitude(q, 4 * y)
    eta = m4 - 4 * m
    # Proven in research/grothendieck/theta-eta-convexity-lemma.md:
    # m is convex with m(0)=0, so eta=m(4y)-4m(y)>=0. Dependency may widen
    # the computed value below zero; intersect only that value enclosure and
    # retain the independently propagated derivative intervals exactly.
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    eta = Dual(Interval(max(F(0), eta.value.lo), eta.value.hi),
               eta.dq, eta.dy)
    square_root = one_minus_exp_negative_dual(2 * m) / y
    deficit = (exp_negative_dual(4 * m)
               * one_minus_exp_negative_dual(eta) / (y * y))
    return square_root * square_root - deficit


if __name__ == "__main__":
    c = cosh_sqrt(Interval(0, F(1, 64)))
    e = exp_negative(Interval(0, F(1, 4)))
    assert c.lo <= 1 <= c.hi
    assert e.lo < 1 <= e.hi
    q = Dual(Interval(F(3, 10), F(31, 100)), dq=1)
    y = Dual(Interval(F(1, 1000), F(11, 10000)), dy=1)
    product = q * y
    assert product.dq.lo == y.value.lo and product.dy.lo == q.value.lo
    quotient = product / q
    assert quotient.value.lo <= y.value.lo <= quotient.value.hi
    c_dual = cosh_sqrt_dual(product)
    assert c_dual.dq.lo > 0 and c_dual.dy.lo > 0
    e_dual = exp_negative_dual(product)
    assert e_dual.dq.hi < 0 and e_dual.dy.hi < 0
    b = Dual(Interval(F(1, 1000), F(1, 500)), dq=1, dy=1)
    log_dual = negative_log1m_dual(b)
    assert log_dual.dq.lo > 1 and log_dual.dy.lo > 1
    one_minus = one_minus_exp_negative_dual(product)
    assert one_minus.dq.lo > 0 and one_minus.dy.lo > 0
    corner_q = Dual(Interval(F(3, 10), F(30001, 100000)), dq=1)
    corner_y = Dual(Interval(F(3570, 100000), F(1, 28)), dy=1)
    corner = dominant_residual_quotient(corner_q, corner_y)
    direct_corner_signs = corner.dq.lo > 0 and corner.dy.hi < 0
    print("direct corner signs:", direct_corner_signs,
          float(corner.dq.lo), float(corner.dy.hi))
    # Direct subtraction is deliberately expected to fail this sign test;
    # the theorem checker must use the cancellation-free log/expm1 form.
    assert not direct_corner_signs
    stable_corner = cancellation_free_residual_quotient(corner_q, corner_y)
    print("stable corner:", float(stable_corner.dq.lo),
          float(stable_corner.dy.hi))
    assert stable_corner.dq.lo > 0 and stable_corner.dy.hi < 0
    # Deliberate-failure witness: reversing an interval must be rejected.
    try:
        Interval(1, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("deliberate failure did not trigger")
    print("theta dominant exact interval primitives: PASS")
