"""Second-order scaled-interval jets for centered theta enclosures."""
from dataclasses import dataclass
from fractions import Fraction as F
from theta_fixedpoint_interval import (
    FixedInterval, fixed, cosh_sqrt, cosh_sqrt_derivative,
    exp_negative, negative_log1m, PI)


@dataclass(frozen=True)
class FixedJet:
    value: FixedInterval
    dq: FixedInterval
    dy: FixedInterval
    dqq: FixedInterval
    dqy: FixedInterval
    dyy: FixedInterval

    def __init__(self, value, dq=0, dy=0, dqq=0, dqy=0, dyy=0):
        for name, item in (("value", value), ("dq", dq), ("dy", dy),
                           ("dqq", dqq), ("dqy", dqy), ("dyy", dyy)):
            object.__setattr__(self, name, fixed(item))

    def __add__(self, other):
        other = jet(other)
        return FixedJet(*(getattr(self, k) + getattr(other, k)
                          for k in ("value", "dq", "dy", "dqq", "dqy", "dyy")))

    __radd__ = __add__

    def __neg__(self):
        return FixedJet(*(-getattr(self, k)
                          for k in ("value", "dq", "dy", "dqq", "dqy", "dyy")))

    def __sub__(self, other):
        return self + (-jet(other))

    def __rsub__(self, other):
        return jet(other) - self

    def __mul__(self, other):
        other = jet(other)
        a, b = self, other
        return FixedJet(
            a.value * b.value,
            a.dq * b.value + a.value * b.dq,
            a.dy * b.value + a.value * b.dy,
            a.dqq * b.value + 2 * a.dq * b.dq + a.value * b.dqq,
            a.dqy * b.value + a.dq * b.dy + a.dy * b.dq + a.value * b.dqy,
            a.dyy * b.value + 2 * a.dy * b.dy + a.value * b.dyy)

    __rmul__ = __mul__

    def reciprocal(self):
        inverse = self.value.reciprocal()
        first = -(inverse * inverse)
        second = 2 * inverse * inverse * inverse
        return unary_compose(self, inverse, first, second)

    def __truediv__(self, other):
        return self * jet(other).reciprocal()

    def __rtruediv__(self, other):
        return jet(other) / self


def jet(x):
    return x if isinstance(x, FixedJet) else FixedJet(x)


def unary_compose(x, value, first, second):
    """Jet of f(x), given interval enclosures of f, f', and f''."""
    x = jet(x)
    return FixedJet(value,
                    first * x.dq,
                    first * x.dy,
                    second * x.dq * x.dq + first * x.dqq,
                    second * x.dq * x.dy + first * x.dqy,
                    second * x.dy * x.dy + first * x.dyy)


def cosh_sqrt_second(x, terms=10):
    x = fixed(x)
    total = term = fixed(F(1, 12))
    for n in range(2, terms):
        term = term * x * F(n + 1, n - 1) / ((2*n + 2) * (2*n + 1))
        total += term
    next_term = term * x * F(terms + 1, terms - 1) / ((2*terms + 2) * (2*terms + 1))
    ratio = x / ((2*terms + 3) * (2*terms + 4)) * F(terms + 2, terms)
    tail = next_term / (1 - ratio)
    return FixedInterval(total.lo, total.hi + tail.hi)


def cosh_sqrt_jet(x):
    x = jet(x)
    return unary_compose(x, cosh_sqrt(x.value),
                         cosh_sqrt_derivative(x.value),
                         cosh_sqrt_second(x.value))


def exp_negative_jet(x):
    x = jet(x)
    value = exp_negative(x.value)
    return unary_compose(x, value, -value, value)


def negative_log1m_jet(x):
    x = jet(x)
    value = negative_log1m(x.value)
    first = (1 - x.value).reciprocal()
    return unary_compose(x, value, first, first * first)


def dominant_log_magnitude_jet(q, y):
    q, y = jet(q), jet(y)
    amplitude = FixedJet(2 * PI) / q
    cosine = cosh_sqrt_jet(q * y)
    exponent = amplitude * (cosine - 1)
    denominator = (amplitude - 3) * (amplitude - 3)
    correction = 6 * amplitude * (cosine - 1) / denominator
    return exponent + negative_log1m_jet(correction)


def scaled_nq_jet(q, y):
    """Jet carrying Nq and its first q,y derivatives."""
    q, y = jet(q), jet(y)
    m = dominant_log_magnitude_jet(q, y)
    eta = dominant_log_magnitude_jet(q, 4*y) - 4*m
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    eta = FixedJet(FixedInterval(max(0,eta.value.lo),eta.value.hi),
                   eta.dq,eta.dy,eta.dqq,eta.dqy,eta.dyy)
    e2,e4,ee=exp_negative_jet(2*m),exp_negative_jet(4*m),exp_negative_jet(eta)
    u,c=1-e2,1-ee
    mq=FixedJet(m.dq,dq=m.dqq,dy=m.dqy)
    etaq=FixedJet(eta.dq,dq=eta.dqq,dy=eta.dqy)
    return 4*u*e2*mq + e4*(4*mq*c-ee*etaq)


def cancellation_free_residual_jet(q, y):
    q, y = jet(q), jet(y)
    m = dominant_log_magnitude_jet(q, y)
    eta = dominant_log_magnitude_jet(q, 4 * y) - 4 * m
    if eta.value.hi < 0:
        raise AssertionError("eta convexity contradicted")
    eta = FixedJet(FixedInterval(max(0, eta.value.lo), eta.value.hi),
                   eta.dq, eta.dy, eta.dqq, eta.dqy, eta.dyy)
    root = (1 - exp_negative_jet(2 * m)) / y
    deficit = exp_negative_jet(4 * m) * (1 - exp_negative_jet(eta)) / (y * y)
    return root * root - deficit


def magnitude(interval):
    return max(abs(interval.lo), abs(interval.hi))


if __name__ == "__main__":
    q = FixedJet(FixedInterval.enclosing(2, 3), dq=1)
    y = FixedJet(FixedInterval.enclosing(4, 5), dy=1)
    product = q * y
    assert product.dqy.lo <= fixed(1).lo <= product.dqy.hi
    assert product.dqq.lo == product.dqq.hi == 0
    recovered = product / q
    assert recovered.value.lo <= y.value.lo and recovered.value.hi >= y.value.hi
    assert recovered.dy.lo <= fixed(1).lo <= recovered.dy.hi
    x = FixedJet(FixedInterval.enclosing(F(1, 100), F(1, 80)), dq=1, dy=1)
    c = cosh_sqrt_jet(x)
    assert c.dqq.lo > 0 and c.dqy.lo > 0 and c.dyy.lo > 0
    e = exp_negative_jet(x)
    assert e.dq.hi < 0 and e.dqq.lo > 0
    l = negative_log1m_jet(x)
    assert l.dq.lo > 0 and l.dqq.lo > 0
    q0, q1 = F(819, 2048), F(8201, 20480)
    y0, y1 = F(59869, 1792000), F(3757, 112000)
    qc, yc = (q0 + q1) / 2, (y0 + y1) / 2
    center = cancellation_free_residual_jet(FixedJet(qc, dq=1), FixedJet(yc, dy=1))
    box = cancellation_free_residual_jet(
        FixedJet(FixedInterval.enclosing(q0, q1), dq=1),
        FixedJet(FixedInterval.enclosing(y0, y1), dy=1))
    rq, ry = fixed((q1 - q0) / 2), fixed((y1 - y0) / 2)
    dq_cost = fixed(magnitude(box.dqq)) * rq + fixed(magnitude(box.dqy)) * ry
    dy_cost = fixed(magnitude(box.dqy)) * rq + fixed(magnitude(box.dyy)) * ry
    centered_dq_lower = center.dq.lo - dq_cost.hi
    centered_dy_upper = center.dy.hi + dy_cost.hi
    print("centered weak cell:", centered_dq_lower, centered_dy_upper)
    # Deliberate dependency witness: natural Hessian extension is too wide.
    assert not (centered_dq_lower > 0 and centered_dy_upper < 0)
    print("theta fixedpoint second-order jet: PASS (natural Hessian rejected)")
