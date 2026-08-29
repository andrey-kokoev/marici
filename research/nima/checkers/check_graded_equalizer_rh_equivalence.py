from fractions import Fraction


def direct_grade(sigma: Fraction) -> Fraction:
    return 1 - sigma


def reciprocal_grade(sigma: Fraction) -> Fraction:
    return sigma


def enters_strict_equalizer(sigma: Fraction) -> bool:
    return direct_grade(sigma) == reciprocal_grade(sigma)


samples = [
    Fraction(1, 10),
    Fraction(1, 4),
    Fraction(1, 3),
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(3, 4),
    Fraction(9, 10),
]

admitted = [sigma for sigma in samples if enters_strict_equalizer(sigma)]
assert admitted == [Fraction(1, 2)]

for sigma in samples:
    assert enters_strict_equalizer(sigma) == (sigma == Fraction(1, 2))

print("strict graded equalizer membership iff sigma=1/2")
print("zero-locus factorization through equalizer is RH-equivalent")
print("missing gain: independent source constructor for diagonal factorization")
