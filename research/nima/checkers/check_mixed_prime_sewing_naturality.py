import cmath
import math


def local_data(p: int, s: complex) -> tuple[complex, complex, complex]:
    logp = math.log(p)
    a = cmath.exp(-s * logp)
    b = cmath.exp((s - 1.0) * logp)
    e_plus = 1.0 / (1.0 - a)
    e_minus = 1.0 / (1.0 - b)
    gamma = (1.0 - a) / (1.0 - b)
    return e_plus, e_minus, gamma


def connection_data(p: int, s: complex) -> tuple[complex, complex, complex]:
    logp = math.log(p)
    a = cmath.exp(-s * logp)
    b = cmath.exp((s - 1.0) * logp)
    j_plus = -logp * a / (1.0 - a)
    j_minus = logp * b / (1.0 - b)
    j_gamma = logp * a / (1.0 - a) + logp * b / (1.0 - b)
    return j_plus, j_minus, j_gamma


for prime in (2, 3, 5, 7, 11):
    for sample in (0.5 + 0.7j, 0.75 + 1.1j, 1.25 + 0.4j):
        e_plus, e_minus, gamma = local_data(prime, sample)
        assert abs(e_minus - gamma * e_plus) < 1e-12
        j_plus, j_minus, j_gamma = connection_data(prime, sample)
        assert abs(j_minus - j_plus - j_gamma) < 1e-12

epsilon = 0.2


def hostile_completion_ratio(s: complex) -> complex:
    return 1.0 + epsilon * cmath.exp(s * s)


def hostile_completion_connection(s: complex) -> complex:
    numerator = 2.0 * epsilon * s * cmath.exp(s * s)
    return numerator / hostile_completion_ratio(s)


sample = 0.6 + 0.8j
assert abs(hostile_completion_connection(sample)) > 0.1

print("local reciprocal section and connection squares pass for five primes")
print("cutoff-dependent completion factor produces mixed residual:", hostile_completion_connection(sample))
