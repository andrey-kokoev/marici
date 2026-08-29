import cmath
import math


step = 0.01
count = 20000
delta = 0.3


def flux(t: float) -> complex:
    return (1.0 + 0.2j) * math.exp(0.12 * t) * cmath.exp(1.7j * t)


laplace = 0.0j
weighted_energy = 0.0
weight_norm = 0.0
for index in range(count):
    t = (index + 0.5) * step
    value = flux(t)
    laplace += value * cmath.exp(-(delta + 0.8j) * t) * step
    weighted_energy += abs(value * math.exp(-delta * t / 2.0)) ** 2 * step
    weight_norm += math.exp(-delta * t) * step

bound = math.sqrt(weighted_energy * weight_norm)
assert abs(laplace) <= bound * (1.0 + 1e-12)

exact_weight_norm = 1.0 / delta
assert abs(weight_norm - exact_weight_norm) < 0.01

print("discrete Laplace magnitude:", abs(laplace))
print("Cauchy-Schwarz bound:", bound)
print("weight norm approaches 1/delta:", weight_norm)
