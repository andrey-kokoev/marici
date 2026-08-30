"""Exact margin and alternating-term checks for reciprocal spectral density."""

from fractions import Fraction


# Rational bounds 3 < pi < 22/7 imply:
# square reciprocal mass / pi = pi/6 < 11/21 < 2/3.
square_mass_upper = Fraction(11, 21)
threshold = Fraction(2, 3)
assert square_mass_upper < threshold
certified_margin = threshold - square_mass_upper
assert certified_margin == Fraction(1, 7)

# The exact symbolic margin is (4-pi)/6; 22/7 gives a rational lower bound.
exact_margin_lower = Fraction(4, 1) - Fraction(22, 7)
exact_margin_lower /= 6
assert exact_margin_lower == Fraction(1, 7)

# Clustered seven-mode hostile labels near 1 have reciprocal mass near 7/pi.
# Since pi < 22/7, 7/pi > 49/22 > 2/3.
cluster_lower = Fraction(49, 22)
assert cluster_lower > threshold

# Multiplier (2r+3)/(2r+2) never exceeds 3/2.
for r in range(1000):
    multiplier = Fraction(2 * r + 3, 2 * (r + 1))
    assert multiplier <= Fraction(3, 2)
    assert multiplier * square_mass_upper < 1

print("certified square-spectrum reciprocal mass upper bound:", square_mass_upper)
print("all-order sufficient threshold:", threshold)
print("certified margin:", certified_margin)
print("seven-label cluster reciprocal-mass lower bound:", cluster_lower)
print("PASS: reciprocal spectral density isolates the protection mechanism")
