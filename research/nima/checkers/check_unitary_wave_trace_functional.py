import cmath


eigenvalues = (-2.0, -0.5, 1.25, 3.0)
weights = (1.0, -0.3, 0.4, 0.2)
functional_norm = sum(abs(weight) for weight in weights)


def wave_trace(q: float) -> complex:
    return sum(
        weight * cmath.exp(1j * q * eigenvalue)
        for eigenvalue, weight in zip(eigenvalues, weights)
    )


for q in (-10.0, -2.0, 0.0, 1.5, 9.0):
    assert abs(wave_trace(q)) <= functional_norm + 1e-12


def hostile_trace(q: float) -> complex:
    return cmath.exp(0.2 * q) * cmath.exp(1.1j * q)


assert abs(hostile_trace(20.0)) > 10.0
assert abs(hostile_trace(-20.0)) < 0.1

positive_weights = (1.0, 0.5, 0.25, 0.125)


def positive_wave(q: float) -> complex:
    return sum(
        weight * cmath.exp(1j * q * eigenvalue)
        for eigenvalue, weight in zip(eigenvalues, positive_weights)
    )


times = (0.0, 0.7, 1.9)
for coefficients in ((1.0, -0.2j, 0.5), (0.3j, 1.0, -0.7)):
    quadratic = 0.0j
    for i, left in enumerate(coefficients):
        for j, right in enumerate(coefficients):
            quadratic += left.conjugate() * right * positive_wave(times[j] - times[i])
    assert quadratic.real >= -1e-12
    assert abs(quadratic.imag) < 1e-12

print("signed fixed functional retains bounded real-frequency support")
print("positive functional passes finite positive-type tests")
print("complex-frequency hostile violates the bounded functional estimate")
