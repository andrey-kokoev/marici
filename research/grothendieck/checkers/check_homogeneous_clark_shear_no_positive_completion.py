"""Exact dependency-free checks for the homogeneous Clark-shear no-go."""

from fractions import Fraction


def q(sign: int, a: Fraction, p: Fraction, tangent: Fraction) -> Fraction:
    return 2 * (tangent * tangent - (p + sign * a * tangent) ** 2)


checks = 0
for a in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(7, 3)):
    # Pure radial variation remains strictly negative on both sheets.
    assert q(1, a, Fraction(1), Fraction(0)) == -2
    assert q(-1, a, Fraction(1), Fraction(0)) == -2
    checks += 2

    # Equal-weight identity on a small exact grid.
    for p, tangent in (
        (Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(-1)),
        (Fraction(-3), Fraction(2)),
    ):
        lhs = q(1, a, p, tangent) + q(-1, a, p, tangent)
        rhs = 4 * ((1 - a * a) * tangent * tangent - p * p)
        assert lhs == rhs
        checks += 1

print(f"PASS {checks}/{checks}: homogeneous opposite shears retain a negative radial direction")

