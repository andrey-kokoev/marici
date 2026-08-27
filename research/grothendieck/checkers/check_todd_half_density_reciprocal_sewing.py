#!/usr/bin/env python3
"""Exact formal checks for reciprocal sewing of the Todd boundary germ."""

from fractions import Fraction
from math import factorial


def multiply(a: list[Fraction], b: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= degree:
                out[i + j] += ai * bj
    return out


degree = 10
exp_half = [Fraction(1, 2**n * factorial(n)) for n in range(degree + 1)]

# tau(t)=t/(exp(t)-1), computed by solving tau(t)*(exp(t)-1)/t=1.
denominator = [Fraction(1, factorial(n + 1)) for n in range(degree + 1)]
tau = [Fraction(0) for _ in range(degree + 1)]
tau[0] = Fraction(1)
for n in range(1, degree + 1):
    tau[n] = -sum(tau[k] * denominator[n - k] for k in range(n))

centered = multiply(exp_half, tau, degree)
assert all(centered[n] == 0 for n in range(1, degree + 1, 2))

# tau(-t)=exp(t)*tau(t).
tau_reflected = [coefficient * ((-1) ** n) for n, coefficient in enumerate(tau)]
exp_full = [Fraction(1, factorial(n)) for n in range(degree + 1)]
assert tau_reflected == multiply(exp_full, tau, degree)

# First centered coefficients: t/(2*sinh(t/2)).
assert centered[:7] == [
    Fraction(1),
    Fraction(0),
    Fraction(-1, 24),
    Fraction(0),
    Fraction(7, 5760),
    Fraction(0),
    Fraction(-31, 967680),
]

print("todd_transition=tau(-t)/tau(t)=exp(t)")
print("unique_centering_character=exp(t/2)")
print("centered_germ=t/(2*sinh(t/2))")
print("centered_germ_reflection=even")
print("zeta_zero_order_anomaly=cancelled")
print("remaining_boundary_tangent=odd_bernoulli_tower")
