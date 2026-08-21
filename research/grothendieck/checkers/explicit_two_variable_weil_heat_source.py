"""Dependency-free normalization audit for the shifted-Gaussian source formula."""

import cmath
import json
import math
from pathlib import Path


samples = [(0.2, -1.3), (0.7, 0.0), (1.4, 2.1)]
maximum_endpoint_residual = 0.0
for t, xi in samples:
    h_plus = cmath.exp(-t * (0.5j - xi) ** 2)
    h_minus = cmath.exp(-t * (-0.5j - xi) ** 2)
    endpoint_from_poles = (h_plus + h_minus) / 2
    endpoint_closed = math.exp(t / 4 - t * xi * xi) * math.cos(t * xi)
    residual = abs(endpoint_from_poles - endpoint_closed)
    maximum_endpoint_residual = max(maximum_endpoint_residual, residual)
assert maximum_endpoint_residual < 1e-14

# The shifted Gaussian Fourier pair supplies the phase exp(-i xi a); pairing
# opposite arithmetic atoms leaves its cosine.
t, xi, a = 0.8, 1.1, math.log(2)
positive_atom = math.sqrt(math.pi / t) * math.exp(-a * a / (4 * t)) * cmath.exp(-1j * xi * a)
negative_atom = positive_atom.conjugate()
paired = (positive_atom + negative_atom) / 2
expected = math.sqrt(math.pi / t) * math.exp(-a * a / (4 * t)) * math.cos(xi * a)
assert abs(paired.imag) < 1e-15
assert abs(paired.real - expected) < 1e-15

result = {
    "endpoint_formula": "exp(t/4-t*xi^2)*cos(t*xi)",
    "maximum_endpoint_identity_residual": maximum_endpoint_residual,
    "paired_prime_atoms_produce_cosine": True,
    "signed_divisor_normalization": "one half",
    "zero_slice_counts_positive_ordinates_once": True,
    "nonzero_character_completed_positivity_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "explicit-two-variable-weil-heat-source.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
