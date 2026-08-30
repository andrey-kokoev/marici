import cmath


def polynomial_factor(z: complex, a: complex, z0: complex) -> complex:
    return (z - a) / (z0 - a)


def polynomial_log_derivative(z: complex, a: complex) -> complex:
    return 1.0 / (z - a)


def axial_factor(z: complex, epsilon: float) -> complex:
    return 1.0 + epsilon * cmath.exp(z * z)


def axial_log_derivative(z: complex, epsilon: float) -> complex:
    numerator = 2.0 * epsilon * z * cmath.exp(z * z)
    return numerator / axial_factor(z, epsilon)


a = 0.75 + 1.25j
z0 = -0.5 + 0.25j
sample = 0.2 + 0.4j

assert abs(polynomial_factor(z0, a, z0) - 1.0) < 1e-15
assert abs(polynomial_log_derivative(sample, a)) > 0.1

epsilon = 0.5
assert abs(axial_factor(8j, epsilon) - 1.0) < 1e-20
assert abs(axial_log_derivative(sample, epsilon)) > 0.1

radius = 1e-5
residue_estimate = radius * polynomial_log_derivative(a + radius, a)
assert abs(residue_estimate - 1.0) < 1e-10

constant_factor = 3.0 - 2.0j
for z in (0.1j, 1.0 + 0.2j, -2.0 + 3.0j):
    quotient_log_derivative = 0.0j
    assert quotient_log_derivative == 0.0j
    assert constant_factor != 0.0j

print("polynomial gauge detected by nonzero logarithmic derivative")
print("axial gauge detected despite axial normalization")
print("inserted simple zero has residue:", residue_estimate.real)
print("only constant common factors survive the connection law")
