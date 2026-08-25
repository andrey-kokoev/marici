"""Exact finite separation of spectral SSR from cosine-zero orientation."""

from fractions import Fraction


def det2(a, b, c, d):
    return a * d - b * c


# A rational surrogate q=1/2 for exp(-1).  The sampled Laplace matrix
# q^(u*lambda), u,lambda in {1,2}, has the required negative 2x2 sign.
q = Fraction(1, 2)
k11 = q ** (1 * 1)
k12 = q ** (1 * 2)
k21 = q ** (2 * 1)
k22 = q ** (2 * 2)
minor2 = det2(k11, k12, k21, k22)
assert minor2 < 0

# Cosine transform numerator for e^-u + e^-2u is 3(z^2+2).
# At z^2=-2 it vanishes, while both denominator factors remain nonzero.
z_squared = Fraction(-2)
numerator = 3 * (z_squared + 2)
denominator = (1 + z_squared) * (4 + z_squared)
assert numerator == 0
assert denominator != 0

print("sample Laplace-kernel 2x2 minor:", minor2)
print("cosine-transform numerator at z^2=-2:", numerator)
print("cosine-transform denominator at z^2=-2:", denominator)
print("nonreal zeros:", "+/- i*sqrt(2)")
print("PASS: spectral SSR-infinity does not orient cosine-transform zeros")
