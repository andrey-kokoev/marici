import cmath
import math


def h(v: float) -> float:
    return (4 * v - 2.25) * math.exp(v) + 16 * v - 4.25


def h_prime(v: float) -> float:
    return math.exp(v) * (4 * v + 1.75) + 16


assert h(0) == -6.5
for k in range(1001):
    assert h_prime(k / 100) > 0
assert h(1) > 0

z_squared = 4 * math.log(2) - 8j * math.pi
z = cmath.sqrt(z_squared)
transform = cmath.exp(-z * z / 4) + (1 / math.sqrt(2)) * cmath.exp(-z * z / 8)

assert abs(transform) < 1e-12
assert abs(z.real) > 1
assert abs(z.imag) > 1

print("source=positive_even_strictly_decreasing")
print("green_curvature_sign_changes=exactly_one")
print("transform_zero=off_both_axes")
print("missing_force=labelled_Poisson_coherence")

