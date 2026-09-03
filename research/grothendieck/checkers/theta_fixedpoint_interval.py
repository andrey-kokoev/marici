"""Scaled-integer outward intervals for fast exact theta box checks."""
from dataclasses import dataclass
from fractions import Fraction as F

SCALE = 10**30


def ceil_div(n, d):
    return -((-n) // d)


def floor_fraction(x):
    x = F(x)
    return (x.numerator * SCALE) // x.denominator


def ceil_fraction(x):
    x = F(x)
    return ceil_div(x.numerator * SCALE, x.denominator)


@dataclass(frozen=True)
class FixedInterval:
    lo: int
    hi: int

    @classmethod
    def enclosing(cls, lo, hi=None):
        hi = lo if hi is None else hi
        return cls(floor_fraction(lo), ceil_fraction(hi))

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def __add__(self, other):
        other = fixed(other)
        return FixedInterval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return FixedInterval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-fixed(other))

    def __rsub__(self, other):
        return fixed(other) - self

    def __mul__(self, other):
        other = fixed(other)
        values = (self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi)
        return FixedInterval(min(values) // SCALE,
                             ceil_div(max(values), SCALE))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        if self.hi < 0:
            return -(-self).reciprocal()
        square = SCALE * SCALE
        return FixedInterval(square // self.hi,
                             ceil_div(square, self.lo))

    def __truediv__(self, other):
        return self * fixed(other).reciprocal()

    def __rtruediv__(self, other):
        return fixed(other) / self

    def lower_fraction(self):
        return F(self.lo, SCALE)

    def upper_fraction(self):
        return F(self.hi, SCALE)


def fixed(value):
    return value if isinstance(value, FixedInterval) else FixedInterval.enclosing(value)


@dataclass(frozen=True)
class FixedDual:
    value: FixedInterval
    dq: FixedInterval
    dy: FixedInterval

    def __init__(self, value, dq=0, dy=0):
        object.__setattr__(self, "value", fixed(value))
        object.__setattr__(self, "dq", fixed(dq))
        object.__setattr__(self, "dy", fixed(dy))

    def __add__(self, other):
        other = fixed_dual(other)
        return FixedDual(self.value + other.value, self.dq + other.dq,
                         self.dy + other.dy)

    __radd__ = __add__

    def __neg__(self):
        return FixedDual(-self.value, -self.dq, -self.dy)

    def __sub__(self, other):
        return self + (-fixed_dual(other))

    def __rsub__(self, other):
        return fixed_dual(other) - self

    def __mul__(self, other):
        other = fixed_dual(other)
        return FixedDual(self.value * other.value,
                         self.dq * other.value + self.value * other.dq,
                         self.dy * other.value + self.value * other.dy)

    __rmul__ = __mul__

    def reciprocal(self):
        square = self.value * self.value
        return FixedDual(self.value.reciprocal(),
                         -self.dq / square, -self.dy / square)

    def __truediv__(self, other):
        return self * fixed_dual(other).reciprocal()

    def __rtruediv__(self, other):
        return fixed_dual(other) / self


def fixed_dual(value):
    return value if isinstance(value, FixedDual) else FixedDual(value)


def cosh_sqrt(x, terms=10):
    """Outward enclosure of cosh(sqrt(x)), 0 <= x <= 1/16."""
    x = fixed(x)
    # 1/15 safely contains the proved x<=1/16 domain plus rounding halo.
    if x.lo < 0 or x.hi > fixed(F(1, 15)).hi:
        raise ValueError("cosh_sqrt domain")
    total = term = fixed(1)
    for n in range(1, terms + 1):
        term = term * x / ((2 * n) * (2 * n - 1))
        total += term
    next_term = term * x / ((2 * terms + 2) * (2 * terms + 1))
    ratio = x / ((2 * terms + 3) * (2 * terms + 4))
    tail = next_term / (1 - ratio)
    return FixedInterval(total.lo, total.hi + tail.hi)


def cosh_sqrt_derivative(x, terms=10):
    x = fixed(x)
    if x.lo < 0 or x.hi > fixed(F(1, 15)).hi:
        raise ValueError("cosh_sqrt_derivative domain")
    total = term = fixed(F(1, 2))
    for n in range(2, terms + 1):
        term = term * x / ((2 * n) * (2 * n - 1)) * F(n, n - 1)
        total += term
    next_term = (term * x / ((2 * terms + 2) * (2 * terms + 1))
                 * F(terms + 1, terms))
    ratio = x / ((2 * terms + 3) * (2 * terms + 4))
    tail = next_term / (1 - ratio)
    return FixedInterval(total.lo, total.hi + tail.hi)


def cosh_sqrt_dual(x, terms=10):
    x = fixed_dual(x)
    value = cosh_sqrt(x.value, terms)
    derivative = cosh_sqrt_derivative(x.value, terms)
    return FixedDual(value, derivative * x.dq, derivative * x.dy)


def exp_negative(x, terms=18):
    """Outward fixedpoint enclosure of exp(-x), 0 <= x <= 1/2."""
    x = fixed(x)
    if x.lo < 0 or x.hi > fixed(F(1, 2)).hi:
        raise ValueError("exp_negative domain")
    total = term = fixed(1)
    for n in range(1, terms + 1):
        term = term * x / n
        total += term
    next_term = term * x / (terms + 1)
    tail = next_term / (1 - x / (terms + 2))
    exp_positive = FixedInterval(total.lo, total.hi + tail.hi)
    return exp_positive.reciprocal()


def exp_negative_dual(x, terms=18):
    x = fixed_dual(x)
    value = exp_negative(x.value, terms)
    return FixedDual(value, -value * x.dq, -value * x.dy)


def negative_log1m(x, terms=8):
    """Outward fixedpoint enclosure of -log(1-x), 0 <= x <= 1/25."""
    x = fixed(x)
    if x.lo < 0 or x.hi > fixed(F(1, 25)).hi:
        raise ValueError("negative_log1m domain")
    total = term = x
    for n in range(2, terms + 1):
        term = term * x
        total += term / n
    next_term = term * x / (terms + 1)
    tail = next_term / (1 - x)
    return FixedInterval(total.lo, total.hi + tail.hi)


def negative_log1m_dual(x, terms=8):
    x = fixed_dual(x)
    value = negative_log1m(x.value, terms)
    derivative = (1 - x.value).reciprocal()
    return FixedDual(value, derivative * x.dq, derivative * x.dy)


def one_minus_exp_negative_dual(x, terms=18):
    return 1 - exp_negative_dual(x, terms)


PI = FixedInterval.enclosing(F(3141592653589793238, 10**18),
                             F(3141592653589793239, 10**18))


def dominant_log_magnitude(q, y):
    q, y = fixed_dual(q), fixed_dual(y)
    amplitude = FixedDual(2 * PI) / q
    cosine = cosh_sqrt_dual(q * y)
    exponent = amplitude * (cosine - 1)
    denominator = (amplitude - 3) * (amplitude - 3)
    correction = 6 * amplitude * (cosine - 1) / denominator
    return exponent + negative_log1m_dual(correction)


def scaled_derivative_numerators(q, y):
    """Return y^2 D_q and y^3 D_y without small-y division."""
    q, y = fixed_dual(q), fixed_dual(y)
    m = dominant_log_magnitude(q, y)
    m4 = dominant_log_magnitude(q, 4 * y)
    eta = m4 - 4 * m
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    ev = FixedInterval(max(0, eta.value.lo), eta.value.hi)
    e2, e4, ee = exp_negative(2*m.value), exp_negative(4*m.value), exp_negative(ev)
    u, c = 1-e2, 1-ee
    nq = 4*u*e2*m.dq + e4*(4*m.dq*c - ee*eta.dq)
    ny = (4*y.value*u*e2*m.dy - 2*u*u
          + y.value*e4*(4*m.dy*c - ee*eta.dy) + 2*e4*c)
    return nq, ny


def symbolic_residual_derivatives(q, y):
    """Differentiate final stable formula after eliminating repeated dual use."""
    q, y = fixed_dual(q), fixed_dual(y)
    m = dominant_log_magnitude(q, y)
    m4 = dominant_log_magnitude(q, 4 * y)
    eta = m4 - 4 * m
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    eta_value = FixedInterval(max(0, eta.value.lo), eta.value.hi)
    e2, e4, ee = exp_negative(2 * m.value), exp_negative(4 * m.value), exp_negative(eta_value)
    u, c = 1 - e2, 1 - ee
    a = u / y.value
    value = a * a - e4 * c / (y.value * y.value)
    def derivative(mz, m4z, explicit_y):
        az = 2 * e2 * mz / y.value
        if explicit_y:
            az -= u / (y.value * y.value)
        etaz = m4z - 4 * mz
        numerator_z = e4 * (-4 * mz * c + ee * etaz)
        result = 2 * a * az - numerator_z / (y.value * y.value)
        if explicit_y:
            result += 2 * e4 * c / (y.value * y.value * y.value)
        return result
    return FixedDual(value, derivative(m.dq, m4.dq, False),
                     derivative(m.dy, m4.dy, True))


def cancellation_free_residual_quotient(q, y):
    q, y = fixed_dual(q), fixed_dual(y)
    m = dominant_log_magnitude(q, y)
    m4 = dominant_log_magnitude(q, 4 * y)
    eta = m4 - 4 * m
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    eta = FixedDual(FixedInterval(max(0, eta.value.lo), eta.value.hi),
                    eta.dq, eta.dy)
    root = one_minus_exp_negative_dual(2 * m) / y
    deficit = (exp_negative_dual(4 * m)
               * one_minus_exp_negative_dual(eta) / (y * y))
    return root * root - deficit


if __name__ == "__main__":
    a = FixedInterval.enclosing(F(-1, 3), F(2, 7))
    b = FixedInterval.enclosing(F(3, 11), F(5, 13))
    product = a * b
    exact = (F(-5, 39), F(10, 91))
    assert product.lower_fraction() <= exact[0]
    assert product.upper_fraction() >= exact[1]
    quotient = b / FixedInterval.enclosing(F(7, 5), F(3, 2))
    assert quotient.lower_fraction() <= F(2, 11)
    assert quotient.upper_fraction() >= F(25, 91)
    q = FixedDual(FixedInterval.enclosing(F(3, 10), F(31, 100)), dq=1)
    y = FixedDual(FixedInterval.enclosing(F(1, 1000), F(11, 10000)), dy=1)
    product_dual = q * y
    assert product_dual.dq.lower_fraction() <= y.value.lower_fraction()
    assert product_dual.dy.lower_fraction() <= q.value.lower_fraction()
    recovered = product_dual / q
    assert recovered.value.lower_fraction() <= y.value.lower_fraction()
    assert recovered.value.upper_fraction() >= y.value.upper_fraction()
    cosine = cosh_sqrt_dual(product_dual)
    assert cosine.dq.lo > 0 and cosine.dy.lo > 0
    exponential = exp_negative_dual(product_dual)
    assert exponential.dq.hi < 0 and exponential.dy.hi < 0
    b = FixedDual(FixedInterval.enclosing(F(1, 1000), F(1, 500)), dq=1, dy=1)
    logarithm = negative_log1m_dual(b)
    assert logarithm.dq.lo > SCALE and logarithm.dy.lo > SCALE
    corner_q = FixedDual(FixedInterval.enclosing(F(3, 10), F(30001, 100000)), dq=1)
    corner_y = FixedDual(FixedInterval.enclosing(F(3570, 100000), F(1, 28)), dy=1)
    stable = cancellation_free_residual_quotient(corner_q, corner_y)
    weak_q = FixedDual(FixedInterval.enclosing(F(819, 2048), F(8201, 20480)), dq=1)
    weak_y = FixedDual(FixedInterval.enclosing(F(59869, 1792000), F(3757, 112000)), dy=1)
    symbolic = symbolic_residual_derivatives(weak_q, weak_y)
    nq, ny = scaled_derivative_numerators(weak_q, weak_y)
    print("scaled weak numerators:", float(nq.lower_fraction()),
          float(ny.upper_fraction()))
    assert nq.lo > 0 and ny.hi < 0
    print("symbolic weak cell:", float(symbolic.dq.lower_fraction()),
          float(symbolic.dy.upper_fraction()))
    assert symbolic.dq.lo > 0 and symbolic.dy.hi < 0
    print("fixedpoint stable corner:", float(stable.dq.lower_fraction()),
          float(stable.dy.upper_fraction()))
    assert stable.dq.lo > 0 and stable.dy.hi < 0
    try:
        FixedInterval(1, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("deliberate reversed interval accepted")
    print("theta fixedpoint interval core: PASS")
