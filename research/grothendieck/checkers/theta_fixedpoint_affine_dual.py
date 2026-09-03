"""First-derivative dual algebra over correlated affine Taylor forms."""
from dataclasses import dataclass
from fractions import Fraction as F
from theta_fixedpoint_affine import (
    Affine, affine, cosh_sqrt_affine, exp_negative_affine,
    negative_log1m_affine)
from theta_fixedpoint_interval import cosh_sqrt_derivative, FixedInterval, PI


@dataclass(frozen=True)
class AffineDual:
    value: Affine
    dq: Affine
    dy: Affine

    def __init__(self, value, dq=0, dy=0):
        object.__setattr__(self, "value", affine(value))
        object.__setattr__(self, "dq", affine(dq))
        object.__setattr__(self, "dy", affine(dy))

    def __add__(self, other):
        other = dual(other)
        return AffineDual(self.value + other.value,
                          self.dq + other.dq, self.dy + other.dy)

    __radd__ = __add__

    def __neg__(self):
        return AffineDual(-self.value, -self.dq, -self.dy)

    def __sub__(self, other):
        return self + (-dual(other))

    def __rsub__(self, other):
        return dual(other) - self

    def __mul__(self, other):
        other = dual(other)
        return AffineDual(self.value * other.value,
                          self.dq * other.value + self.value * other.dq,
                          self.dy * other.value + self.value * other.dy)

    __rmul__ = __mul__

    def reciprocal(self):
        inverse = self.value.reciprocal()
        square = self.value * self.value
        return AffineDual(inverse, -self.dq / square, -self.dy / square)

    def __truediv__(self, other):
        return self * dual(other).reciprocal()

    def __rtruediv__(self, other):
        return dual(other) / self


def dual(value):
    return value if isinstance(value, AffineDual) else AffineDual(value)


def cosh_sqrt_affine_dual(x):
    x = dual(x)
    value = cosh_sqrt_affine(x.value)
    derivative = Affine(cosh_sqrt_derivative(x.value.range()))
    return AffineDual(value, derivative * x.dq, derivative * x.dy)


def exp_negative_affine_dual(x):
    x = dual(x)
    value = exp_negative_affine(x.value)
    return AffineDual(value, -value * x.dq, -value * x.dy)


def negative_log1m_affine_dual(x):
    x = dual(x)
    value = negative_log1m_affine(x.value)
    derivative = (1 - x.value).reciprocal()
    return AffineDual(value, derivative * x.dq, derivative * x.dy)


def dominant_log_magnitude_affine_dual(q, y):
    q, y = dual(q), dual(y)
    amplitude = AffineDual(Affine(2 * PI)) / q
    cosine = cosh_sqrt_affine_dual(q * y)
    exponent = amplitude * (cosine - 1)
    denominator = (amplitude - 3) * (amplitude - 3)
    correction = 6 * amplitude * (cosine - 1) / denominator
    return exponent + negative_log1m_affine_dual(correction)


def cancellation_free_residual_affine_dual(q, y):
    q, y = dual(q), dual(y)
    m = dominant_log_magnitude_affine_dual(q, y)
    eta = dominant_log_magnitude_affine_dual(q, 4 * y) - 4 * m
    eta_range = eta.value.range()
    if eta_range.hi < 0:
        raise AssertionError("eta convexity contradicted")
    # Convexity supplies only the value clamp; derivative forms are retained.
    eta = AffineDual(Affine(FixedInterval(max(0, eta_range.lo), eta_range.hi)),
                     eta.dq, eta.dy)
    root = (1 - exp_negative_affine_dual(2 * m)) / y
    deficit = (exp_negative_affine_dual(4 * m)
               * (1 - exp_negative_affine_dual(eta)) / (y * y))
    return root * root - deficit


if __name__ == "__main__":
    q = AffineDual(Affine(F(2), aq=F(1, 10)), dq=1)
    y = AffineDual(Affine(F(3), ay=F(1, 20)), dy=1)
    product = q * y
    assert product.dq.range().lower_fraction() <= y.value.range().lower_fraction()
    assert product.dy.range().upper_fraction() >= q.value.range().upper_fraction()
    recovered = product / q
    assert recovered.value.range().lower_fraction() <= y.value.range().lower_fraction()
    assert recovered.value.range().upper_fraction() >= y.value.range().upper_fraction()
    x = AffineDual(Affine(F(1, 100), aq=F(1, 1000), ay=F(1, 2000)), dq=1, dy=1)
    cosine = cosh_sqrt_affine_dual(x)
    exponential = exp_negative_affine_dual(x)
    logarithm = negative_log1m_affine_dual(x)
    assert cosine.dq.range().lo > 0 and cosine.dy.range().lo > 0
    assert exponential.dq.range().hi < 0 and exponential.dy.range().hi < 0
    assert logarithm.dq.range().lo > 0 and logarithm.dy.range().lo > 0
    q0, q1 = F(819, 2048), F(8201, 20480)
    y0, y1 = F(59869, 1792000), F(3757, 112000)
    q_cell = AffineDual(Affine((q0 + q1)/2, aq=(q1-q0)/2), dq=1)
    y_cell = AffineDual(Affine((y0 + y1)/2, ay=(y1-y0)/2), dy=1)
    residual = cancellation_free_residual_affine_dual(q_cell, y_cell)
    dq_range, dy_range = residual.dq.range(), residual.dy.range()
    print("affine residual cell:", dq_range.lo, dy_range.hi)
    assert dq_range.lo > 0 and dy_range.hi < 0
    print("theta fixedpoint affine dual: PASS")
