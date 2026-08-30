"""Exact checks for reciprocal affine endpoint transversality."""

from fractions import Fraction


def norm2(z: tuple[Fraction, Fraction]) -> Fraction:
    return z[0] * z[0] + z[1] * z[1]


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


checks = 0
for f0 in (Fraction(1), Fraction(3, 2), Fraction(7)):
    for u in (
            (Fraction(0), Fraction(0)),
            (Fraction(2), Fraction(-1)),
            (Fraction(-3, 2), Fraction(4)),
    ):
        # Completed scalar nullity is U+V=0, hence V=-U.
        v = (-u[0], -u[1])
        y_u = add(u, (f0, Fraction(0)))
        y_v = add(v, (f0, Fraction(0)))
        lhs = norm2(y_u) + norm2(y_v)
        rhs = 2 * norm2(u) + 2 * f0 * f0
        assert lhs == rhs
        assert lhs > 0
        checks += 2

print(f"PASS {checks}/{checks}: reciprocal affine endpoint stays nonzero on the completed zero domain")
