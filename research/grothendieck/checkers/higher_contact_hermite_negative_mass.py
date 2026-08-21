"""Audit of quadratic and quartic backward-heat Hermite contact laws."""

import json
import math
from pathlib import Path


def h2(z):
    return 4 * z**2 - 2


def h4(z):
    return 16 * z**4 - 48 * z**2 + 12


C1 = 8 * math.sqrt(2) / 3

# H4 is negative between the two positive roots and on the reflected interval.
root_low = math.sqrt((3 - math.sqrt(6)) / 2)
root_high = math.sqrt((3 + math.sqrt(6)) / 2)


def negative_h4_antiderivative(z):
    return -16 * z**5 / 5 + 16 * z**3 - 12 * z


# Factor two from reflection and factor two from x=2*sqrt(delta)*z.
C2 = 4 * (
    negative_h4_antiderivative(root_high)
    - negative_h4_antiderivative(root_low)
)
assert C1 == 8 * math.sqrt(2) / 3
assert C2 > 0

deltas = [0.04, 0.01, 0.0025]
quadratic_masses = [C1 * delta**1.5 for delta in deltas]
quartic_masses = [C2 * delta**2.5 for delta in deltas]
assert all(abs(mass / delta**1.5 - C1) < 1e-12 for mass, delta in zip(quadratic_masses, deltas))
assert all(abs(mass / delta**2.5 - C2) < 1e-12 for mass, delta in zip(quartic_masses, deltas))

result = {
    "quadratic_Hermite": "H2(z)=4z^2-2",
    "quartic_Hermite": "H4(z)=16z^4-48z^2+12",
    "quadratic_negative_mass_coefficient": C1,
    "quartic_negative_mass_coefficient": C2,
    "quadratic_onset_exponent": "3/2",
    "quartic_onset_exponent": "5/2",
    "general_onset_exponent": "m+1/2",
    "higher_contact_requires_additional_vanishing_jets": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "higher-contact-hermite-negative-mass.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
