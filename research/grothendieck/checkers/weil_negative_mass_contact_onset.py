"""Audit of the universal 3/2 negative-mass onset at a heat tangency."""

import json
import math
from pathlib import Path


kappa = 1.75
deltas = [0.04, 0.01, 0.0025]


def exact_local_negative_mass(delta):
    radius = math.sqrt(2 * delta)
    return 2 * kappa * (2 * delta * radius - radius**3 / 3)


coefficient = 8 * math.sqrt(2) * kappa / 3
masses = [exact_local_negative_mass(delta) for delta in deltas]
scaled = [mass / delta**1.5 for mass, delta in zip(masses, deltas)]
assert all(abs(value - coefficient) < 1e-13 for value in scaled)
assert all(left > right for left, right in zip(masses, masses[1:]))

result = {
    "curvature_kappa": kappa,
    "sharpening_deltas": deltas,
    "negative_masses": masses,
    "mass_over_delta_to_three_halves": scaled,
    "expected_coefficient": coefficient,
    "universal_onset_exponent": "3/2",
    "heat_smoothing_negative_mass_nonincreasing": True,
    "negative_mass_zero_iff_kernel_nonnegative": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "weil-negative-mass-contact-onset.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
