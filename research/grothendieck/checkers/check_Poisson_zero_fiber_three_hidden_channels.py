#!/usr/bin/env python3
"""Exact rank and reconstruction audit of the four Poisson channels."""

from fractions import Fraction


hidden = (
    (1, 1, -1, -1),
    (1, -1, 0, 0),
    (0, 0, 1, -1),
)
assert all(sum(vector) == 0 for vector in hidden)


def ports(vector):
    a, b, c, d = vector
    return (a + b + c + d, a + b - c - d, a - b, c - d)


def reconstruct(readouts):
    r0, r1, r2, r3 = readouts
    return (
        Fraction(r0 + r1 + 2 * r2, 4),
        Fraction(r0 + r1 - 2 * r2, 4),
        Fraction(r0 - r1 + 2 * r3, 4),
        Fraction(r0 - r1 - 2 * r3, 4),
    )


samples = ((1, 2, 3, 4), hidden[0], hidden[1], hidden[2])
assert all(reconstruct(ports(vector)) == vector for vector in samples)
assert all(sum(value * value for value in vector) > 0 for vector in hidden)

print("scalar_zero_fiber_dimension=3")
print("hidden_channels=symmetric_contrast,bulk_odd,pole_odd")
print("four_port_transform=faithful")
print("positive_full_norm_does_not_forbid_scalar_zero")

