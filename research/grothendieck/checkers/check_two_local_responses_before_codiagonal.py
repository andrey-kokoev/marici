"""Exact Aspect-style test for two local responses versus one codiagonal port."""

from fractions import Fraction


checks = 0
for f in (Fraction(1, 3), Fraction(1), Fraction(7, 2)):
    for u in (Fraction(-4), Fraction(1, 5), Fraction(3)):
        v = -u  # completed scalar zero
        r_plus = -f * u
        r_minus = -f * v
        common = r_plus + r_minus
        relative = r_plus - r_minus

        assert u + v == 0
        assert common == 0
        assert relative == -2 * f * u
        assert relative != 0
        checks += 4

print(f"PASS {checks}/{checks}: codiagonal response erases the nonzero relative zero-state witness")

