import cmath
import math


epsilon = 0.5


def h(z: complex) -> complex:
    return 1.0 + epsilon * cmath.exp(z * z)


axis_errors = [abs(h(1j * y) - 1.0) for y in (1.0, 2.0, 4.0, 8.0)]
assert all(a > b for a, b in zip(axis_errors, axis_errors[1:]))
assert axis_errors[-1] < 1e-20

w = math.log(1.0 / epsilon) + 1j * math.pi
root = cmath.sqrt(w)
assert abs(root.imag) > 0.1
assert abs(h(root)) < 1e-12

transition_before = 3.0 - 2.0j
d_minus = 2.0 + 1.0j
d_plus = transition_before * d_minus
sample = 0.4 + 0.7j
transition_after = (h(sample) * d_plus) / (h(sample) * d_minus)
assert abs(transition_after - transition_before) < 1e-12

print("axial errors:", axis_errors)
print("off-axis root:", root)
print("root residual:", abs(h(root)))
print("transition residual:", abs(transition_after - transition_before))
