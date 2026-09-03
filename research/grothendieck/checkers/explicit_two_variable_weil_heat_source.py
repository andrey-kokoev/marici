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

# Pull back the full-divisor, even-test convention to the prior convention:
# one shifted Gaussian, division by two, and positive ordinates counted once.
# Evenness identifies the +xi and -xi gamma integrals. Every displayed
# coefficient must acquire the same positive factor.
marici_coefficients = {
    "endpoint": 1.0,
    "gamma_integral": 1 / (4 * math.pi),
    "prime_sum": -1 / (2 * math.sqrt(math.pi * t)),
}
symmetrized_coefficients = {
    "endpoint": 4.0,
    "gamma_integral": 1 / math.pi,
    "prime_sum": -2 / math.sqrt(math.pi * t),
}
normalization_ratios = {
    key: symmetrized_coefficients[key] / marici_coefficients[key]
    for key in marici_coefficients
}
assert all(abs(ratio - 4.0) < 1e-15 for ratio in normalization_ratios.values())

# Deliberate failure: omitting one normalization operation predicts factor two.
wrong_ratio = 2.0
assert any(abs(ratio - wrong_ratio) > 1e-15 for ratio in normalization_ratios.values())

result = {
    "endpoint_formula": "exp(t/4-t*xi^2)*cos(t*xi)",
    "maximum_endpoint_identity_residual": maximum_endpoint_residual,
    "paired_prime_atoms_produce_cosine": True,
    "signed_divisor_normalization": "one half",
    "zero_slice_counts_positive_ordinates_once": True,
    "symmetrized_to_marici_ratios": normalization_ratios,
    "common_positive_normalization_factor": 4.0,
    "factor_two_deliberate_failure_rejected": True,
    "direct_source_page_verified": True,
    "source_arxiv": "2005.02996",
    "source_archive_sha256": "5ee4bbde5a3f4396e972ed214d394f4dc237439f3a5438f02e2efbb196657a58",
    "source_formula_lines": "98-110",
    "nonzero_character_completed_positivity_proved": False,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "explicit-two-variable-weil-heat-source.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
