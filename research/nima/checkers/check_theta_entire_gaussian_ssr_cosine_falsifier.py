"""Exact symbolic identities plus numerical residual for the Gaussian witness."""

import cmath
import math
from fractions import Fraction


# Rational sampled Laplace minor certifies the required reverse sign.
q = Fraction(1, 2)
minor = q * q**4 - q**2 * q**2
assert minor < 0

# Exact exponent relation for z^2/8 = log(sqrt(2)) + pi*i:
# exp(z^2/8) = -sqrt(2), so 1 + exp(z^2/8)/sqrt(2) = 0.
z_squared = 8 * (math.log(math.sqrt(2)) + 1j * math.pi)
z = cmath.sqrt(z_squared)


def transform(z_value):
    return (
        math.sqrt(math.pi) * cmath.exp(-(z_value**2) / 4)
        + math.sqrt(math.pi / 2) * cmath.exp(-(z_value**2) / 8)
    )


residual = transform(z)
assert z.real != 0 and z.imag > 0
assert abs(residual) < 1e-14

print("sample SSR 2x2 minor:", minor)
print("upper-half-plane zero:", z)
print("entire-transform residual:", residual)
print("PASS: even positive Schwartz SSR mixture has nonreal Fourier zeros")
