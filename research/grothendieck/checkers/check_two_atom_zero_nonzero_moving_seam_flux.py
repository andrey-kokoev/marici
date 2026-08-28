"""Exact two-atom falsifier for scalar-zero implies moving-seam-flux zero."""

from fractions import Fraction


checks = 0
for a, b in (
    (Fraction(1), Fraction(2)),
    (Fraction(2), Fraction(5)),
    (Fraction(3), Fraction(1)),
    (Fraction(7, 3), Fraction(4, 5)),
):
    w = -a / b
    scalar = a + b * w
    odd_flux = a * b * (w - 1 / w)

    assert scalar == 0
    assert odd_flux == b * b - a * a
    assert odd_flux != 0
    assert abs(w) != 1
    checks += 4

# Balanced weights are the exact seam degeneration.
a = b = Fraction(3)
w = -a / b
assert a + b * w == 0
assert a * b * (w - 1 / w) == 0
assert abs(w) == 1
checks += 3

print(f"PASS {checks}/{checks}: unequal positive two-atom cancellation has nonzero oriented flux")

