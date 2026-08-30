"""Cancellation-free second-variation model for the full unit-slope chart."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class J:
    value: float
    first: float
    second: float

    def __add__(self, other: J | float) -> J:
        other = other if isinstance(other, J) else J(other, 0.0, 0.0)
        return J(self.value+other.value, self.first+other.first, self.second+other.second)

    __radd__ = __add__

    def __neg__(self) -> J:
        return J(-self.value, -self.first, -self.second)

    def __sub__(self, other: J | float) -> J:
        return self + (-other if isinstance(other, J) else -other)

    def __rsub__(self, other: float) -> J:
        return J(other, 0.0, 0.0) - self

    def __mul__(self, other: J | float) -> J:
        other = other if isinstance(other, J) else J(other, 0.0, 0.0)
        return J(
            self.value*other.value,
            self.first*other.value+self.value*other.first,
            self.second*other.value+2.0*self.first*other.first+self.value*other.second,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> J:
        result = J(1.0, 0.0, 0.0)
        for _ in range(exponent):
            result = result*self
        return result


def limiting_margin(k: float, holding: float) -> float:
    rapidity_gap = 0.5*math.log1p(k)
    x = (rapidity_gap+holding)/2.0
    t0 = math.tanh(x)
    s0 = 1.0-t0*t0
    p = J(1.0, -1.0, 0.0)
    q = J(1.0, -(1.0+k), 0.0)
    t = J(t0, s0*k/8.0, 0.0)
    r = J(t0, -s0*(holding/2.0+k/8.0), 0.0)
    n = (
        t**4 + t**2*p*q - t*(p+q)*r
        + (1.0-2.0*t**2-t**2*p*q)*r**2 + t*(p+q)*r**3
    )
    assert abs(n.value) < 1e-12 and abs(n.first) < 1e-10
    return n.second/2.0


def closed_limiting_margin(k: float, holding: float) -> float:
    t = math.tanh((0.5*math.log1p(k)+holding)/2.0)
    s = 1.0-t*t
    diagonal = t*t*s-holding*t*s*s+(1.0+3.0*t*t)*holding*holding*s*s/4.0
    linear = (
        t*s*(t*t+2.0*t-1.0)/2.0
        +holding*s*s*(1.0-2.0*t+3.0*t*t)/4.0
    )
    quadratic = -(1.0-t)**3*(1.0+t)**2*(3.0*t-1.0)/16.0
    return diagonal+k*linear+k*k*quadratic


def derivative(k: float, holding: float, step: float = 1e-5) -> float:
    return (limiting_margin(k, holding+step)-limiting_margin(k, holding-step))/(2.0*step)


def critical(k: float) -> tuple[float, float]:
    left, right = 1e-6, 8.0
    for _ in range(70):
        midpoint = (left+right)/2.0
        if derivative(k, midpoint) > 0.0:
            left = midpoint
        else:
            right = midpoint
    holding = (left+right)/2.0
    step = 2e-4
    second = (
        limiting_margin(k, holding+step)-2.0*limiting_margin(k, holding)
        +limiting_margin(k, holding-step)
    )/(step*step)
    return holding, -second


def main() -> None:
    for k in (0.0, 0.001, 0.01, 0.1, 0.3, 1.0, 3.0, 10.0, 100.0):
        assert abs(limiting_margin(k, 1.25)-closed_limiting_margin(k, 1.25)) < 1e-11
        print(k, critical(k))


if __name__ == "__main__":
    main()
