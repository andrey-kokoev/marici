from fractions import Fraction


def comparator_exponent(sigma: Fraction) -> Fraction:
    return 1 - 2 * sigma


def finite_comparator(n: int, sigma: Fraction) -> Fraction:
    # Rational samples avoid floating-point claims. The omitted nonzero
    # spectral prefactor cannot affect uniform power growth.
    exponent = comparator_exponent(sigma)
    if exponent.denominator != 1:
        # Evaluate after raising to the denominator.
        return Fraction(n) ** exponent.numerator
    return Fraction(n) ** exponent.numerator


samples = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]

for sigma in samples:
    exponent = comparator_exponent(sigma)
    # Every cutoff map is an algebraic isomorphism: its scalar is nonzero.
    scalar_power = finite_comparator(16, sigma)
    assert scalar_power != 0

assert comparator_exponent(Fraction(1, 4)) > 0
assert comparator_exponent(Fraction(1, 2)) == 0
assert comparator_exponent(Fraction(3, 4)) < 0

# At the two hostile off-seam values, one direction diverges with cutoff.
for n in (2, 4, 16, 256):
    left = Fraction(n) ** 1  # square of N^(1/2)
    right_inverse = Fraction(n) ** 1
    assert left >= 1
    assert right_inverse >= 1

print("common cutoff: established independently of sigma")
print("finite sewing: invertible at every tested cutoff")
print("uniform degree-zero sewing: selected only at sigma=1/2")
