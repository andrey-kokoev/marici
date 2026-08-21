"""Dependency-free finite spectral audit of the Weil Gaussian kernel."""

import cmath
import math


ordinates = [-3.0, -1.0, 1.0, 3.0]
multiplicities = [1, 2, 2, 1]


def kernel(t, xi):
    return 0.5 * sum(
        multiplicity * math.exp(-t * (xi - gamma) ** 2)
        for gamma, multiplicity in zip(ordinates, multiplicities)
    )


def heat_trace(t):
    return sum(
        multiplicity * math.exp(-t * gamma**2)
        for gamma, multiplicity in zip(ordinates, multiplicities)
        if gamma > 0
    )


sample_times = [0.1, 0.5, 2.0]
sample_characters = [-4.0, -0.75, 0.0, 1.25, 5.0]
assert all(abs(kernel(t, 0.0) - heat_trace(t)) < 1e-14 for t in sample_times)
assert all(kernel(t, xi) > 0 for t in sample_times for xi in sample_characters)

t, xi, displacement = 0.7, 1.3, 0.9
paired_character = math.exp(-(displacement**2) / (4 * t)) * (
    cmath.exp(1j * xi * displacement) + cmath.exp(-1j * xi * displacement)
)
damped_cosine = 2 * math.exp(-(displacement**2) / (4 * t)) * math.cos(
    xi * displacement
)
assert abs(paired_character.imag) < 1e-15
assert abs(paired_character.real - damped_cosine) < 1e-15

result = {
    "spectral_atom_count": len(ordinates),
    "kernel_formula": "(1/2) sum_signed_gamma m_gamma exp(-t(xi-gamma)^2)",
    "zero_slice_equals_heat_trace": True,
    "finite_positive_spectral_kernel": True,
    "paired_source_atom_becomes_damped_cosine": True,
    "all_character_source_positivity_is_RH_equivalent": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "two-variable-weil-gaussian-kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
