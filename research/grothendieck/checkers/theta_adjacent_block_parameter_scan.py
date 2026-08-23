"""Locate a high-margin hostile point for the exchange-orbit block."""
import json
import math
from pathlib import Path

from theta_conditional_adjacent_block_falsifier import block, mass_and_midpoint


a = 1.0
b_values = [4.0 + index / 2 for index in range(25)]
values = [block(a, b, ((1, 2), (2, 1)), 80, 1200) for b in b_values]
minimum_index = min(range(len(values)), key=values.__getitem__)


def cumulative_block(a_value, b_value, band_count, d_steps_per_band=80, s_steps=1200):
    """Integrate the original labelled H(d) over [0, band_count*pi/b]."""
    radius_squared = a_value * a_value + b_value * b_value
    alpha = 2 * a_value - a_value / (2 * radius_squared)
    beta = 2 * b_value + b_value / (2 * radius_squared)
    steps = band_count * d_steps_per_band
    upper = band_count * math.pi / b_value
    width = upper / steps
    total = 0.0
    for index in range(steps + 1):
        d = index * width
        integrand = 0.0
        for labels in ((1, 2), (2, 1)):
            mass, midpoint = mass_and_midpoint(a_value, d, *labels, s_steps)
            integrand += beta * math.cos(b_value * d) * midpoint
            integrand += alpha * d * math.sin(b_value * d) * mass
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        total += coefficient * integrand
    return total * width / 3


hostile_b = b_values[minimum_index]
cumulative_band_counts = list(range(1, 11))
cumulative_values = [cumulative_block(a, hostile_b, count) for count in cumulative_band_counts]

result = {
    "a": a,
    "b_values": b_values,
    "exchange_orbit_block_values": values,
    "most_negative_b": b_values[minimum_index],
    "most_negative_value": values[minimum_index],
    "cumulative_scan_b": hostile_b,
    "cumulative_band_counts_pi_over_b": cumulative_band_counts,
    "cumulative_exchange_orbit_values": cumulative_values,
    "interval_certified": False,
    "purpose": "choose a high-margin point before directed enclosure",
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-adjacent-block-parameter-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for b_value, value in zip(b_values, values):
        print(f"b={b_value:.1f} block={value:.16e}")
    print(f"most_negative_b={result['most_negative_b']}")
    print(f"most_negative_value={result['most_negative_value']:.16e}")
    for count, value in zip(cumulative_band_counts, cumulative_values):
        print(f"cumulative_bands={count} block={value:.16e}")
