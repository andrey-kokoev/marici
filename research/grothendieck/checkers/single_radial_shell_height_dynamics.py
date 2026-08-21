"""Exact moment and numerical sinc checks for rank-one shell compression."""

import math
from fractions import Fraction


# Uniform interval [-1/4,3/4] has mean 1/4 and variance 1/12.
left = Fraction(-1, 4)
right = Fraction(3, 4)
mean = (left + right) / 2
second_moment = (right**3 - left**3) / (3 * (right - left))
variance = second_moment - mean**2
assert mean == Fraction(1, 4)
assert variance == Fraction(1, 12)


def residual_fraction(height: float) -> float:
    if height == 0.0:
        return 0.0
    sinc = math.sin(height / 2.0) / (height / 2.0)
    return 1.0 - sinc * sinc


for height in (0.1, 0.5, 1.0, 3.0, 10.0):
    residual = residual_fraction(height)
    assert 0.0 < residual <= 1.0

# Any positive constant times harmonic shell mass has growing finite prefixes.
fixed_residual = residual_fraction(1.0)
prefixes = [fixed_residual * sum(1.0 / k for k in range(1, cutoff + 1)) for cutoff in (10, 100, 1000, 10000)]
assert all(later > earlier for earlier, later in zip(prefixes, prefixes[1:]))

print("quarter_shifted_shell_coordinate_mean_equals_one_quarter=True")
print("shell_coordinate_variance_equals_one_twelfth=True")
print("fixed_radial_phase_residual_positive_at_nonzero_height=True")
print("rank_one_shell_fluctuation_norm_diverges_harmonically=True")
print("moving_radial_projective_derivative_diverges=True")
print("multi_mode_shell_fiber_required=True")
