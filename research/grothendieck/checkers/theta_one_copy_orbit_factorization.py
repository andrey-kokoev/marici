"""Phase-stable one-copy factorization of labelled theta orbit blocks."""
import cmath
import json
import math
from pathlib import Path

from theta_conditional_adjacent_block_falsifier import log_phi_label


def one_copy(label, a, b, steps, cutoff=4.0):
    """Return Z_n(a+ib), Z'_n(a+ib) from the folded half-line source."""
    width = cutoff / steps
    z = complex(a, b)
    z_real_terms = []
    z_imag_terms = []
    dz_real_terms = []
    dz_imag_terms = []
    for index in range(steps + 1):
        radius = index * width
        phi = math.exp(log_phi_label(label, radius))
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        value = 2 * phi * cmath.cosh(z * radius)
        derivative = 2 * radius * phi * cmath.sinh(z * radius)
        z_real_terms.append(coefficient * value.real)
        z_imag_terms.append(coefficient * value.imag)
        dz_real_terms.append(coefficient * derivative.real)
        dz_imag_terms.append(coefficient * derivative.imag)
    factor = width / 3
    transform = complex(math.fsum(z_real_terms) * factor, math.fsum(z_imag_terms) * factor)
    derivative = complex(math.fsum(dz_real_terms) * factor, math.fsum(dz_imag_terms) * factor)
    return transform, derivative


def ordered_orbit(n_data, m_data, alpha, beta):
    zn, dzn = n_data
    zm, dzm = m_data
    sum_moment = dzn * zm.conjugate() + zn * dzm.conjugate()
    difference_moment = dzn * zm.conjugate() - zn * dzm.conjugate()
    return beta * sum_moment.real + alpha * difference_moment.imag


def sample(a, b, steps, max_label=4):
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    data = {label: one_copy(label, a, b, steps) for label in range(1, max_label + 1)}
    orbit_values = []
    for n in range(1, max_label + 1):
        for m in range(n, max_label + 1):
            value = ordered_orbit(data[n], data[m], alpha, beta)
            if n != m:
                value += ordered_orbit(data[m], data[n], alpha, beta)
            orbit_values.append({"orbit": [n, m], "value": value})
    partial_values = []
    for cutoff_label in range(1, max_label + 1):
        partial_values.append(math.fsum(
            item["value"] for item in orbit_values
            if item["orbit"][0] <= cutoff_label and item["orbit"][1] <= cutoff_label
        ))
    return {"b": b, "steps": steps, "orbits": orbit_values, "partial_source_values": partial_values}


a = 1.0
frequencies = [24.0, 32.0, 40.0]
resolutions = [10000, 20000]
samples = [sample(a, b, steps) for b in frequencies for steps in resolutions]

result = {
    "a": a,
    "frequencies": frequencies,
    "simpson_resolutions": resolutions,
    "folded_radius_cutoff": 4.0,
    "factorization": "Z_n(z)=2 integral_0^inf phi_n(r) cosh(zr) dr",
    "samples": samples,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-one-copy-orbit-factorization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for item in samples:
        print(f"b={item['b']:.1f} steps={item['steps']} partials={item['partial_source_values']}")
        print(f"orbits={item['orbits']}")
