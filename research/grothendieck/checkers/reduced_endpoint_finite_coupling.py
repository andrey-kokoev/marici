"""Dependency-free numerical audit of the exact reduced endpoint constant."""

import json
import math
from pathlib import Path


# Euler's constant to more precision than needed for the robust sign check.
euler_gamma = 0.5772156649015328606
elementary_zeta_finite = 1 + euler_gamma
gamma_finite = -euler_gamma / 2 - math.log(2)
pi_normalization = -math.log(math.pi) / 2
completed = elementary_zeta_finite + gamma_finite + pi_normalization
closed = 1 + euler_gamma / 2 - math.log(2 * math.sqrt(math.pi))

assert abs(completed - closed) < 1e-15
assert completed > 0.02
assert completed < 0.03

result = {
    "elementary_plus_zeta_finite": elementary_zeta_finite,
    "gamma_finite": gamma_finite,
    "pi_normalization": pi_normalization,
    "completed_finite_coupling": completed,
    "closed_formula": "1+EulerGamma/2-log(2*sqrt(pi))",
    "positive": True,
    "counterterm_freedom": False,
    "conditional_spectral_sum": "sum_gamma m_gamma/(gamma^2+1/4)",
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "reduced-endpoint-finite-coupling.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
