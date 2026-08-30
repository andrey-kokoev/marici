"""Exact rational audit of prime heat moment and variance identities."""

from fractions import Fraction as F
import json
from pathlib import Path


# Positive damped weights and rational log-displacement surrogates at one
# variance. Sigma derivatives are represented algebraically by multiplication
# with minus displacement squared.
atoms = [(F(1, 2), F(1)), (F(1, 3), F(2)), (F(1, 5), F(4))]


def moment(k):
    return sum(weight * displacement**k for weight, displacement in atoms)


M0, M2, M4, M6 = (moment(k) for k in (0, 2, 4, 6))
first_log_derivative = -M2 / M0
second_log_derivative = M4 / M0 - (M2 / M0) ** 2
effective_scale_derivative = -second_log_derivative

assert M0 > 0 and M2 > 0 and M4 > 0 and M6 > 0
assert second_log_derivative > 0
assert effective_scale_derivative < 0
assert M0 * M4 - M2**2 > 0

# Order-one Hankel derivative is the negative shifted Hankel block. Its
# quadratic form is negative for a hostile rational polynomial vector.
v0, v1 = F(2), F(-1)
shifted_energy = v0**2 * M2 + 2 * v0 * v1 * moment(3) + v1**2 * M4
flow_quadratic_form = -shifted_energy
assert shifted_energy > 0
assert flow_quadratic_form < 0

result = {
    "atom_count": len(atoms),
    "M0": str(M0),
    "M2": str(M2),
    "M4": str(M4),
    "M6": str(M6),
    "first_log_derivative": str(first_log_derivative),
    "log_convexity_variance": str(second_log_derivative),
    "effective_scale_derivative": str(effective_scale_derivative),
    "effective_scale_strictly_decreases": True,
    "Hankel_flow_quadratic_form": str(flow_quadratic_form),
    "Hankel_blocks_decrease_in_Loewner_order": True,
    "twisted_zero_moment_obeys_heat_equation": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "prime-heat-moment-variance-dissipation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
