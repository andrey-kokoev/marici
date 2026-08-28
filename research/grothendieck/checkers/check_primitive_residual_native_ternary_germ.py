"""Exact native-arity test for R(z,h,p) = -2*z*h*p."""

from fractions import Fraction


def residual(z: Fraction, h: Fraction, p: Fraction) -> Fraction:
    return -2 * z * h * p


checks = 0
samples = (Fraction(-3), Fraction(1, 2), Fraction(5))

# Every coordinate two-plane is blind.
for a in samples:
    for b in samples:
        assert residual(a, b, Fraction(0)) == 0
        assert residual(a, Fraction(0), b) == 0
        assert residual(Fraction(0), a, b) == 0
        checks += 3

# The alternating three-cube difference is the nonzero ternary coefficient.
for a in samples:
    for b in samples:
        for c in samples:
            cube = Fraction(0)
            for ez in (0, 1):
                for eh in (0, 1):
                    for ep in (0, 1):
                        sign = -1 if (3 - ez - eh - ep) % 2 else 1
                        cube += sign * residual(ez * a, eh * b, ep * c)
            assert cube == -2 * a * b * c
            assert cube != 0
            checks += 2

print(f"PASS {checks}/{checks}: all binary faces vanish while the ternary germ survives")

