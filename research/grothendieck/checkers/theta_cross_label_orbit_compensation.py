"""Diagnostic decomposition of the theta block by source exchange orbit."""
import json
import math
from pathlib import Path

from theta_conditional_adjacent_block_falsifier import log_phi_label, mass_and_midpoint


def orbit_block(a, b, labels, band_count=6, d_steps_per_band=80, s_steps=1200):
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    steps = band_count * d_steps_per_band
    upper = band_count * math.pi / b
    width = upper / steps
    total = 0.0
    for index in range(steps + 1):
        d = index * width
        value = 0.0
        for n, m in labels:
            mass, midpoint = mass_and_midpoint(a, d, n, m, s_steps)
            value += beta * math.cos(b * d) * midpoint
            value += alpha * d * math.sin(b * d) * mass
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        total += coefficient * value
    return total * width / 3


def diagonal_signed_and_absolute(a, b, band_count=6, d_steps_per_band=80, s_steps=1200):
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    steps = band_count * d_steps_per_band
    width = (band_count * math.pi / b) / steps
    signed = absolute = 0.0
    cutoff = 8.0
    s_width = 2 * cutoff / s_steps
    for index in range(steps + 1):
        d = index * width
        mass, midpoint = mass_and_midpoint(a, d, 1, 1, s_steps)
        value = beta * math.cos(b * d) * midpoint + alpha * d * math.sin(b * d) * mass
        d_coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        signed += d_coefficient * value
        absolute_at_d = 0.0
        for s_index in range(s_steps + 1):
            s = -cutoff + s_index * s_width
            exponent = (
                a * s
                + log_phi_label(1, abs((s + d) / 2))
                + log_phi_label(1, abs((s - d) / 2))
            )
            density = 0.0 if exponent < -745 else math.exp(exponent)
            kernel = beta * s * math.cos(b * d) + alpha * d * math.sin(b * d)
            s_coefficient = 1 if s_index in (0, s_steps) else (4 if s_index % 2 else 2)
            absolute_at_d += s_coefficient * density * abs(kernel)
        # The (S,D) density contains the Jacobian 1/2.
        absolute_at_d *= s_width / 6
        absolute += d_coefficient * absolute_at_d
    return signed * width / 3, absolute * width / 3


a, b = 1.0, 11.0
max_label = 4
orbits = []
for n in range(1, max_label + 1):
    for m in range(n, max_label + 1):
        labels = [(n, m)] if n == m else [(n, m), (m, n)]
        value = orbit_block(a, b, labels)
        orbits.append({"orbit": labels, "value": value})

orbits_by_source_order = sorted(orbits, key=lambda item: item["orbit"][0])
positive_total = sum(item["value"] for item in orbits if item["value"] > 0)
negative_total = sum(item["value"] for item in orbits if item["value"] < 0)
total = positive_total + negative_total
diagonal_signed, diagonal_absolute = diagonal_signed_and_absolute(a, b)
tail_ratio_at_zero = sum(
    math.exp(log_phi_label(label, 0.0) - log_phi_label(1, 0.0))
    for label in range(2, 20)
)
density_perturbation_factor = 2 * tail_ratio_at_zero + tail_ratio_at_zero**2
perturbation_budget = density_perturbation_factor * diagonal_absolute

result = {
    "parameters_a_b": [a, b],
    "integration_domain": "0 <= d <= 6*pi/b",
    "max_source_label": max_label,
    "exchange_orbits": orbits_by_source_order,
    "positive_orbit_sum": positive_total,
    "negative_orbit_sum": negative_total,
    "truncated_total": total,
    "truncated_total_positive": total > 0,
    "diagonal_11_signed": diagonal_signed,
    "diagonal_11_absolute_d_kernel_norm": diagonal_absolute,
    "higher_label_to_label1_ratio_at_radius_zero_n2_to_19": tail_ratio_at_zero,
    "product_density_perturbation_factor": density_perturbation_factor,
    "conditional_perturbation_budget": perturbation_budget,
    "signed_margin_exceeds_conditional_budget": diagonal_signed > perturbation_budget,
    "tail_ratio_supremum_at_zero_proved": False,
    "interval_certified": False,
    "labels_preserved": True,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-cross-label-orbit-compensation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for item in orbits_by_source_order:
        print(f"orbit={item['orbit']} value={item['value']:.16e}")
    print(f"positive_orbit_sum={positive_total:.16e}")
    print(f"negative_orbit_sum={negative_total:.16e}")
    print(f"truncated_total={total:.16e}")
    print(f"diagonal_absolute={diagonal_absolute:.16e}")
    print(f"tail_ratio_at_zero={tail_ratio_at_zero:.16e}")
    print(f"conditional_perturbation_budget={perturbation_budget:.16e}")
