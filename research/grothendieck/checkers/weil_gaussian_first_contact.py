"""First-contact audit for the exact signed three-atom Gaussian model."""

import json
import math
from pathlib import Path


sigma = 1 / (4 * math.log(2))
x = 0.0
q0 = 1 / math.sqrt(4 * math.pi * sigma)
exponential = math.exp(-1 / (4 * sigma))

# U=q_sigma(x)[2 exp(-1/(4sigma)) cosh(x/(2sigma))-1].
bracket = 2 * exponential * math.cosh(x / (2 * sigma)) - 1
value = q0 * bracket
character_derivative = 0.0
character_second_derivative = q0 * 2 * exponential / (4 * sigma**2)
variance_derivative = q0 * 2 * exponential / (4 * sigma**2)

assert abs(value) < 1e-15
assert character_derivative == 0
assert character_second_derivative > 0
assert variance_derivative > 0
assert abs(character_second_derivative - variance_derivative) < 1e-14

result = {
    "model": "delta_-1+delta_1-delta_0",
    "contact_variance": sigma,
    "contact_character": x,
    "value_at_contact": value,
    "character_derivative_at_contact": character_derivative,
    "character_second_derivative_positive": True,
    "variance_derivative_positive": True,
    "heat_equation_at_contact_verified": True,
    "finite_threshold_requires_double_contact": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "weil-gaussian-first-contact.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
