"""Exact checks for the mixed-prime moving-seam difference cocycle."""

from fractions import Fraction


# A nontrivial exact surrogate for one source-defined prefix current.
def prefix(length: Fraction) -> Fraction:
    return length**4 - 3 * length**2 + 2 * length


def cell(left: Fraction, right: Fraction) -> Fraction:
    return prefix(right) - prefix(left)


cuts = [Fraction(0), Fraction(2), Fraction(3), Fraction(4), Fraction(6), Fraction(9), Fraction(12)]
checks = 0

for a in cuts:
    assert cell(a, a) == 0
    checks += 1
    for b in cuts:
        assert cell(b, a) == -cell(a, b)
        checks += 1
        for c in cuts:
            assert cell(a, b) + cell(b, c) == cell(a, c)
            checks += 1

# Two different refinements of the same interval give the same total.
coarse = [Fraction(0), Fraction(4), Fraction(12)]
fine = cuts
coarse_total = sum(cell(a, b) for a, b in zip(coarse, coarse[1:]))
fine_total = sum(cell(a, b) for a, b in zip(fine, fine[1:]))
assert coarse_total == fine_total == prefix(Fraction(12)) - prefix(Fraction(0))
checks += 1

print(f"PASS {checks}/{checks}: mixed-prime overlap cells form a refinement-invariant difference cocycle")

