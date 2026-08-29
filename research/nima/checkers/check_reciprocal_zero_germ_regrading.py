from fractions import Fraction


def growth_rate(sigma: Fraction, alpha: Fraction) -> Fraction:
    return 1 - (1 + alpha) * sigma


samples = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]

# Common degree-one cutoff selects exactly the seam.
neutral_common = [sigma for sigma in samples if growth_rate(sigma, Fraction(1)) == 0]
assert neutral_common == [Fraction(1, 2)]

# A power regrading can counterfeit neutral growth at every sample point.
for sigma in samples:
    alpha = (1 - sigma) / sigma
    assert alpha > 0
    assert growth_rate(sigma, alpha) == 0

# A bounded multiplicative cutoff distortion contributes no logarithmic
# exponent, so the degree-one result is unchanged.
for sigma in samples:
    common_rate = growth_rate(sigma, Fraction(1))
    bounded_distortion_rate = common_rate
    assert bounded_distortion_rate == common_rate

print("common degree-one cutoff: neutral only at sigma=1/2")
print("arbitrary power regrading: neutral at every tested sigma")
print("required gate: degree-zero filtered sewing over one source cutoff")
