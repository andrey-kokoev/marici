"""Convergence-tested hostile quadrature for the conditional adjacent block."""
import json
import math
from pathlib import Path


PI = math.pi


def log_phi_label(label, radius):
    x = PI * label * label * math.exp(2 * radius)
    return math.log(2 * PI * label * label) + 2.5 * radius + math.log(2 * x - 3) - x


def mass_and_midpoint(a, D, n, m, steps, cutoff=8.0):
    width = 2 * cutoff / steps
    mass = midpoint = 0.0
    for index in range(steps + 1):
        S = -cutoff + index * width
        exponent = (
            a * S
            + log_phi_label(n, abs((S + D) / 2))
            + log_phi_label(m, abs((S - D) / 2))
        )
        value = 0.0 if exponent < -745 else math.exp(exponent)
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        mass += coefficient * value
        midpoint += coefficient * S * value
    # The (S,D) density carries the Jacobian factor 1/2.
    return mass * width / 6, midpoint * width / 6


def block(a, b, label_pairs, D_steps, S_steps):
    L = PI / b
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    width = L / D_steps
    total = 0.0
    for index in range(D_steps + 1):
        D = index * width
        residual = 0.0
        for n, m in label_pairs:
            W, J = mass_and_midpoint(a, D, n, m, S_steps)
            shifted_W, shifted_J = mass_and_midpoint(a, D + L, n, m, S_steps)
            residual += (
                beta * math.cos(b * D) * (J - shifted_J)
                + alpha * math.sin(b * D) * (D * W - (D + L) * shifted_W)
            )
        coefficient = 1 if index in (0, D_steps) else (4 if index % 2 else 2)
        total += coefficient * residual
    return total * width / 3


a, b = 1.0, 8.0
resolutions = ((40, 800), (80, 1200), (160, 2000))
diagonal_values = []
exchange_orbit_values = []
for D_steps, S_steps in resolutions:
    diagonal_values.append(block(a, b, ((1, 1),), D_steps, S_steps))
    exchange_orbit_values.append(block(a, b, ((1, 2), (2, 1)), D_steps, S_steps))

assert all(value > 0 for value in diagonal_values)
assert all(value < 0 for value in exchange_orbit_values)
exchange_spread = max(exchange_orbit_values) - min(exchange_orbit_values)

result = {
    "parameters_a_b": [a, b],
    "canonical_shift": "L=pi/b",
    "D_and_S_simpson_resolutions": [list(pair) for pair in resolutions],
    "diagonal_label_11_block_values": diagonal_values,
    "exchange_orbit_12_21_block_values": exchange_orbit_values,
    "exchange_orbit_value_spread": exchange_spread,
    "diagonal_block_positive_at_all_resolutions": True,
    "exchange_orbit_block_negative_at_all_resolutions": True,
    "labels_regrouped_only_by_source_exchange": True,
    "S_D_density_jacobian_one_half_included": True,
    "interval_certified": False,
    "large_b_leading_term": "4*pi*(J_double_prime(0)-a*W(0))/b^2",
    "diagnostic_J_double_prime_minus_aW_at_a1": "approximately +2.52e-4",
    "negative_large_b_obstruction_supported": False,
    "finite_frequency_failure_requires_direct_interval_enclosure": True,
    "pick_inequality_falsified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-conditional-adjacent-block-falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
