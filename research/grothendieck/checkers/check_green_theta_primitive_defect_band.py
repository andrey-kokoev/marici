from fractions import Fraction
from math import log, pi


def cubic(x):
    return 4 * x**3 - 28 * x**2 + 41 * x - 9


# Rational isolating intervals for all three roots.
intervals = [
    (Fraction(265, 1000), Fraction(267, 1000)),
    (Fraction(1670, 1000), Fraction(1671, 1000)),
    (Fraction(5063, 1000), Fraction(5064, 1000)),
]
for left, right in intervals:
    assert cubic(left) * cubic(right) < 0

# Only the final root meets the physical n=1 chart; n>=2 starts beyond it.
assert cubic(Fraction(314159, 100000)) < 0
assert 4 * pi > 5.064

root_upper = 5.064
u_upper = 0.5 * log(root_upper / pi)
assert 0.238 < u_upper < 0.240

print("green_moment_coefficients=-36,164,-112,16")
print("physical_cubic_roots=one")
print("negative_labels=primitive_n1_only")
print("primitive_defect_band_upper_u<0.240")

